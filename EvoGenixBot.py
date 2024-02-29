from gc import callbacks
from itertools import count
import random
import html
import json
import logging
import traceback
from typing import Dict
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot, InputMediaPhoto, InputMediaDocument, InputMediaVideo, InputMediaAudio, constants, InlineKeyboardButton, InlineKeyboardMarkup, ChatMember
from telegram.ext import ApplicationHandlerStop, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler, CallbackQueryHandler, TypeHandler

import os
import re
import requests

from config import *

TOKEN = '6879523943:AAFM5-CTjM4DDpJaUfkQDSf5UPv7oOL4Fu0' #real

bot = Bot(token=TOKEN)
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

bot_name = 'بات'

#private Q&A group
#main_group_id = -1001850055659 #test
#main_group_id = -1001827444680 #real

#channels id
data_channel_id = -1002140283775
file_channel_id = -1002129105890

#main channel id
channel_id = "@evogenix"
join_link = "https://t.me/+JVn2iRiwhQpmZGVk"

#convestation returns
q_option,q_choose,q_text,not_joined,joined,q_continue,q_c_done = range(7)

#text
help_txt = "راهنمایی"
quiz_text = "کوییز"
azmoon_txt = "منابع حل سوال"
home_return_txt = "برگشت"
azm_step_1_txt = "مرحله یک"
azm_step_2_txt = "مرحله دو"
azm_talaha_txt = "آزمون طلاها"
azm_ibo_txt = "IBO"
reference_book_txt = "کتاب ها"
book_and_manual_txt = "رفرنس های حل سوال"
other_country_exams_txt = "سوالات المپیاد داخلی سایر کشور ها و دیگر مسابقات"
requests_txt = "درخواست"
requests_discription = "سلام این بخش برای اینکه اگه درخواست یا پیشنهادی داری با ما مطرح کنی\nبعد از اینکه درخواست رو نوشتی دکمه ی 'بفرست' رو بزن اگر هم که درخواستی نداری دکمه 'لغو' رو بزن"
welcome_text = '''به EvoGenix خوش اومدی'''
help_message = '''🤖 EvoGenix Bot!

🌱اینجا هرفایلی که لازم داشته باشی رو میتونی گیر بیاری

🧬 @EvoGenix
🤖@EvoGenixBot
📎@EvoGenixSupport'''


pls_join = "لطفا برای استفاده از ربات در چنل عضو شوید"
join_button = [[InlineKeyboardButton("عضویت در چنل",url=join_link)]]

question_resource_slection_txt = "یکی از گزینه ها رو انتخاب کنید"

books_subject = [[InlineKeyboardButton("زیست شناسی عمومی",callback_data="bgb")]]

azm_talaha_buttons = []
for k in range(1,len(talaha_data_dict)-1,2):
    azm_talaha_buttons.append([InlineKeyboardButton("دوره "+str(list(talaha_data_dict.keys())[k]),callback_data="aztl"+str(list(talaha_data_dict.keys())[k])),
                               InlineKeyboardButton("دوره "+str(list(talaha_data_dict.keys())[k-1]),callback_data="aztl"+str(list(talaha_data_dict.keys())[k-1]))])
azm_talaha_buttons.append([InlineKeyboardButton("دوره 23 و 24",callback_data="aztl"+str(list(talaha_data_dict.keys())[-1]))])
azm_talaha_buttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

other_country_buttons = []
for k in other_country_list:
    other_country_buttons.append([InlineKeyboardButton(k,callback_data=other_country_list[k])])
other_country_buttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

subjects_books_button_list = dict()
for s in subjects_books_list:
    subjects_books_button_list[s] = list()
    for b in subjects_books_list[s]:
        subjects_books_button_list[s].append([InlineKeyboardButton(b,callback_data="lb"+str(books_message_id_dict[b]))])
    subjects_books_button_list[s].append([InlineKeyboardButton("برگشت",callback_data="rtrnbks")])

for i in range(len(question_subject_keyboard)-2):
    _mini_ = list()
    for j in question_subject_keyboard[i]:
        _mini_.append(InlineKeyboardButton(j,callback_data=book_subject_callback[j]))
    books_subject.append(_mini_)
books_subject.append([InlineKeyboardButton("آزمایشگاه",callback_data="bla"),InlineKeyboardButton("بیوانفورماتیک",callback_data="bin")])
books_subject.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

question_books_and_manual_buttons = []

for k in question_books_and_manual_list:
    question_books_and_manual_buttons.append([InlineKeyboardButton(k,callback_data="lb"+str(books_message_id_dict[k]))])
question_books_and_manual_buttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

start_keyboard = [[azmoon_txt,reference_book_txt],
                  [help_txt]]

question_resource_option = [[azm_step_2_txt,azm_step_1_txt],
                            [book_and_manual_txt,azm_ibo_txt],
                            [other_country_exams_txt,azm_talaha_txt],
                            [home_return_txt]]

m1_inlinebuttons = []
for i in range(1,28,2):
    m1_inlinebuttons.append([InlineKeyboardButton("دوره "+str(i),callback_data="M1_"+str(i)),InlineKeyboardButton("دوره "+str(i+1),callback_data="M1_"+str(i+1))])
m1_inlinebuttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

m2_inlinebuttons = [[InlineKeyboardButton("دوره 1",callback_data="M2_1"),InlineKeyboardButton("دوره 3",callback_data="M2_3")]]
for i in range(4,27,2):
    m2_inlinebuttons.append([InlineKeyboardButton("دوره "+str(i),callback_data="M2_"+str(i)),InlineKeyboardButton("دوره "+str(i+1),callback_data="M2_"+str(i+1))])
m2_inlinebuttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

ibo_inlinebuttons = [[InlineKeyboardButton("1990",callback_data="IBO_1990"),InlineKeyboardButton("1991",callback_data="IBO_1991")]]
for i in range(1993,2019,2):
    ibo_inlinebuttons.append([InlineKeyboardButton(str(i),callback_data="IBO_"+str(i)),InlineKeyboardButton(str(i+1),callback_data="IBO_"+str(i+1))])
ibo_inlinebuttons.append([InlineKeyboardButton("2020",callback_data="IBO_2020")])
ibo_inlinebuttons.append([InlineKeyboardButton("برگشت",callback_data="rtnqzhome")])

async def user_data(user_id, bot):
    #ChatGPT optimized
    channel_id = "@EvoGenix"
    user = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    user_data = user.user
    username = f'@{user_data.username}' if user_data.username else None
    text = (f'telegram id: {user_data.id}\n'
            f'first name: {user_data.first_name}\n'
            f'last name: {user_data.last_name}\n'
            f'username: {username}\n'
            f'<a href="tg://user?id={user_id}">Profile</a>')
    return text

async def subscribing_check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  
    _channel_id = "@EvoGenix" #real
    _owner_ = await bot.get_chat_member(chat_id=_channel_id, user_id=owener_id)
    
    _user_id = ""
    if update.message is not None:
        _user_id = update.message.chat.id
        
    elif update.callback_query is not None:
        _user_id = update.callback_query.message.chat.id
    else:
        return not_joined
    
    if int(_user_id)>0 and _user_id not in [owener_id,bussiness_id]:
        _chat_member = await bot.get_chat_member(chat_id=_channel_id, user_id=_user_id)
        can_use_list = [ChatMember.ADMINISTRATOR,
                        ChatMember.MEMBER,
                        ChatMember.OWNER]

        can_not_use_list = [ChatMember.BANNED,
                            ChatMember.LEFT,
                            ChatMember.RESTRICTED]

        if _chat_member.status in can_use_list:
            return joined
        elif _chat_member.status in can_not_use_list:
            if update.message is not None:
                await update.message.reply_html(text=pls_join,reply_markup=InlineKeyboardMarkup(join_button))
            elif update.callback_query is not None:
                await update.callback_query.message.reply_html(text=pls_join,reply_markup=InlineKeyboardMarkup(join_button))
            raise ApplicationHandlerStop()
    else:
        return joined

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #Chat GPT optimized
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_msg = f"سلام {user.mention_html()} {welcome_text}"
    await update.message.reply_html(welcome_msg, reply_markup=ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True, resize_keyboard=True))
    await bot.send_message(chat_id=data_channel_id, text=await user_data(user_id=update.message.chat.id, bot=bot), parse_mode=constants.ParseMode.HTML)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(help_message)

async def return_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #Chat GPT optimized
    await bot.send_message(
        chat_id=update.message.chat.id,
        text=f'خب برگشتیم!',
        reply_markup=ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )

    user_data = context.user_data
    keys_to_delete = ["q_subject", "q_user_id", "q_messages"]
    for key in keys_to_delete:
        if key in user_data:
            del user_data[key]

    user_data.clear()
    return ConversationHandler.END

async def question_resource_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text=question_resource_slection_txt,reply_markup=ReplyKeyboardMarkup(
            question_resource_option, one_time_keyboard=True,resize_keyboard=True))

async def m1_list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="یکی از دوره ها رو برای مرحله یک انتخاب کنید",reply_markup=InlineKeyboardMarkup(m1_inlinebuttons))

async def m2_list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="یکی از دوره ها رو برای مرحله دو انتخاب کنید",reply_markup=InlineKeyboardMarkup(m2_inlinebuttons))

async def ibo_list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="یکی از سال ها رو انتخاب کن",reply_markup=InlineKeyboardMarkup(ibo_inlinebuttons))

async def m1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _dore = int(update.callback_query.data.replace("M1_",""))
    await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=irBO_step_one[_dore]["q"])
    await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=irBO_step_one[_dore]["a"])

async def m2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _dore = int(update.callback_query.data.replace("M2_",""))
    if irBo_step_two[_dore]["q"] is not None:
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=irBo_step_two[_dore]["q"])
    if irBo_step_two[_dore]["a"] is not None:
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=irBo_step_two[_dore]["a"])

async def ibo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _dore = int(update.callback_query.data.replace("IBO_",""))
    await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=IBO_data_dict[_dore])

async def books_subject_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="لطفا یکی از موضوع ها رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(books_subject))

async def books_name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    subject = inv_book_subject_callback[update.callback_query.data]
    books_buttons = subjects_books_button_list[subject]
    await update.callback_query.message.edit_text(text="لطفا یکی از کتاب های زیر رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(books_buttons))

async def return_book_subject(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.callback_query.message.edit_text(text="لطفا یکی از موضوع ها رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(books_subject))

async def send_book_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.callback_query.data[:2] == "lb":
        _message_id = update.callback_query.data[2:]
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=_message_id)
    elif update.callback_query.data[:3] == "ch_":
        _message_id = update.callback_query.data[3:]
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=channel_id,message_id=_message_id)
 
async def other_countries_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="لطفا یکی از گزینه ها رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(other_country_buttons))

async def other_counteries_send_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    country = update.callback_query.data[2:]
    await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=other_country_message_id[country])

async def talaha_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="لطفا یکی از گزینه ها رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(azm_talaha_buttons))

async def talaha_send_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _dore = int(update.callback_query.data.replace("aztl",""))
    if talaha_data_dict[_dore]["q"] is not None:
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=talaha_data_dict[_dore]["q"])
    if talaha_data_dict[_dore]["a"] is not None:
        await bot.copy_message(chat_id=update.callback_query.message.chat.id,from_chat_id=file_channel_id,message_id=talaha_data_dict[_dore]["a"])
        
async def question_books_and_manual_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(text="لطفا یکی از گزینه ها رو انتخاب کنید",reply_markup=InlineKeyboardMarkup(question_books_and_manual_buttons))

async def id_to_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.chat.id in [owener_id,bussiness_id]:
        the_id = update.message.text.replace("$id ","")
        user_data_text = await user_data(user_id=the_id,bot=bot)
        await bot.send_message(chat_id = update.message.chat.id,text=user_data_text,parse_mode=constants.ParseMode.HTML)

async def call_me_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _answers_ = ['جانم','بله','جان','چی شده']
    if update.message.text in [bot_name,bot_name+" جون"]:
        _answer_ = ['جوونم این همه مرام',"سلام به همه داش مشتی ها"]
        await update.message.reply_html(text=random.choice(_answer_),reply_to_message_id=update.message.message_id)
    else:
        if update.message["from"]["id"] not in [owener_id,bussiness_id,sheyda_id]:
            await update.message.reply_html(text=random.choice(_answers_),reply_to_message_id=update.message.message_id)
        elif update.message["from"]["id"] in [owener_id,bussiness_id,sheyda_id]:
            await update.message.reply_html(text=random.choice(['جانم','جان']),reply_to_message_id=update.message.message_id)
            if update.message["from"]["id"] == sheyda_id:
                await update.message.forward(chat_id=owener_id)

async def i_am_tired(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _answers_ = ['خسته نباشی عزیزم','فدای خستگی هات بشم','منم خسته ام🥺','بیا بغلم🥲']
    await update.message.reply_html(text=random.choice(_answers_),reply_to_message_id=update.message.message_id)

async def i_am_sad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _answers_ = ['تو ناراحت باشی دلم منم میگیره🥲',"چی حالت رو بهتر میکنه","بیا بغلم",'من دوست دارم ناراحت نباش','قربونتون برم مننن 🥹\nنبینم ناراحت باشیا','وقتی منو داری برا چی ناراحتی؟']
    await update.message.reply_html(text=random.choice(_answers_),reply_to_message_id=update.message.message_id)

async def how_are_you(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    _answers_ = ['تو خوبی؟\nتا وقتی تو خوب باشی منم خوبم',"خوبم مرسی که پرسیدی",'خوبم تو حالت خوبه؟']
    if update.message["from"]["id"] not in [sheyda_id,owener_id,bussiness_id]:
        await update.message.reply_html(text=random.choice(_answers_),reply_to_message_id=update.message.message_id)
    elif update.message["from"]["id"] in [sheyda_id,owener_id,bussiness_id]:
        await update.message.reply_html(text='تو خوبی؟\nتا وقتی تو خوب باشی منم خوبم',reply_to_message_id=update.message.message_id)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    # Finally, send the message
    await context.bot.send_message(
        chat_id=bussiness_id, text=message, parse_mode=constants.ParseMode.HTML
    )
    
def main() -> None:
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TOKEN).build()

    #subscribe checking
    application.add_handler(TypeHandler(Update, callback=subscribing_check))
    
    application.add_handler(CommandHandler(command="start", callback=start,filters=filters.ChatType.PRIVATE),group=1)
    application.add_handler(CommandHandler(command="help", callback=help_command,filters=filters.ChatType.PRIVATE),group=1)
    
    #help
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & ~filters.UpdateType.EDITED_MESSAGE & filters.Regex(r'^'+help_txt+r'$'),help_command),group=1)
    #owner command id
    application.add_handler(MessageHandler(filters.Regex(r'\$id \d+') & filters.Chat([owener_id,bussiness_id]),id_to_profile),group=1)
    #handle question resource requests
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+azmoon_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,question_resource_handler),group=1)
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & ~filters.COMMAND & ~filters.UpdateType.EDITED_MESSAGE & filters.Regex(r'^'+home_return_txt+r'$'),return_to_main),group=1)
    #handle the M1 files and requests
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+azm_step_1_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,m1_list_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=m1_handler,pattern="M1_"),group=1)
    #handle the M2 files and requests
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+azm_step_2_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,m2_list_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=m2_handler,pattern="M2_"),group=1)
    #handle the IBO files and requests
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+azm_ibo_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,ibo_list_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=ibo_handler,pattern="IBO_"),group=1)
    #handle the Other countries file
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+other_country_exams_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,other_countries_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=other_counteries_send_handler,pattern="oc"),group=1)
    #handle the azmoon talaha file
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+azm_talaha_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,talaha_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=talaha_send_handler,pattern="aztl"),group=1)
    #handle the question books and manuals file
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+book_and_manual_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,question_books_and_manual_handler),group=1)
    #Book subject handler
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.Regex(r'^'+reference_book_txt+r'$') & ~filters.UpdateType.EDITED_MESSAGE & ~filters.COMMAND,books_subject_handler),group=1)
    application.add_handler(CallbackQueryHandler(callback=books_name_handler,pattern="b"),group=1)
    application.add_handler(CallbackQueryHandler(callback=send_book_handler,pattern="lb"),group=1)
    application.add_handler(CallbackQueryHandler(callback=return_book_subject,pattern="rtrnbks"),group=1)
    #admins
    application.add_handler(MessageHandler((filters.User(user_id=bot_admins) | filters.Chat(bot_admins)) & (filters.Regex(r'^ربات$')|filters.Regex(r'^بات$')|filters.Regex(f'^{bot_name}$')|filters.Regex(f'^{bot_name} جون$')),call_me_bot),group=1)
    application.add_handler(MessageHandler((filters.User(user_id=bot_admins) | filters.Chat(bot_admins)) & (filters.Regex(r'^خیلی خسته ام$')|filters.Regex(r'^خستمه$')|filters.Regex(r'^خستم$')|filters.Regex(r'^خسته ام$')|filters.Regex(r'^خیلی خستم$')),i_am_tired),group=1)
    #i_am_sad
    application.add_handler(MessageHandler((filters.User(user_id=bot_admins) | filters.Chat(bot_admins)) & (filters.Regex(r'^ناراحتم$')|filters.Regex(r'^خیلی ناراحتم$')),i_am_sad),group=1)
    application.add_handler(MessageHandler((filters.User(user_id=bot_admins) | filters.Chat(bot_admins)) & (filters.Regex(r'^ربات خوبی$')|filters.Regex(r'^بات خوبی$')|filters.Regex(r'^بات چطوری$')|filters.Regex(r'^ربات چطوری$')|filters.Regex(r'^ربات حالت چطوره$')|filters.Regex(r'^بات حالت چطوره$')),how_are_you),group=1)
    
    #erro handler 
    application.add_error_handler(error_handler) #real
    #~filters.UpdateType.EDITED_MESSAGE & 
    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    # PORT = int(os.environ.get('PORT', '8443'))
    # #add handlers
    # application.run_webhook(
    #     listen="0.0.0.0",
    #     port=PORT,
    #     url_path=TOKEN,
    #     webhook_url="https://.herokuapp.com/" + TOKEN
    # )

if __name__ == "__main__":
    main()
