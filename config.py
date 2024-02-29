owener_id = 1255875612
bussiness_id = 1882341674
mohsen_id = 417735934
arman_id = 614114940
fatemeh_id = 633922746
yehaneh_id = 173307158
fallah_id = 815666122
anita_id = 711964031
nima_rasti_id = 1185610497
mammad_id = 473311022
#admins id 
bot_admins = [owener_id,bussiness_id,mohsen_id,
              arman_id,fatemeh_id,yehaneh_id,
              fallah_id,anita_id,nima_rasti_id,
              mammad_id]

home_return_txt = "برگشت"

question_subject_keyboard = [["بیوشیمی","سلولی"],
                    ["مولکولی","ژنتیک کلاسیک"],
                    ["تکامل و فیلوژنتیک","سیستماتیک گیاهی"],
                    ["سیستماتیک جانوری","آناتومی گیاهی"],
                    ["فیزیولوژی گیاهی","فیزیولوژی جانوری"],
                    ["فیزیولوژی انسانی","اکولوژی"],
                    ["رفتار شناسی","آمار و ریاضیات زیستی"],
                    ["مشاوره","غیره"],
                    [home_return_txt]]


irBO_step_one = {
    1: {'q': 3, 'a': 2},
    2: {'q': 5, 'a': 4},
    3: {'q': 7, 'a': 6},
    4: {'q': 9, 'a': 8},
    5: {'q': 11, 'a': 10}, 
    6: {'q': 13, 'a': 12}, 
    7: {'q': 15, 'a': 14}, 
    8: {'q': 17, 'a': 16}, 
    9: {'q': 19, 'a': 18}, 
    10: {'q': 21, 'a': 20}, 
    11: {'q': 23, 'a': 22}, 
    12: {'q': 25, 'a': 24}, 
    13: {'q': 28, 'a': 26}, 
    14: {'q': 30, 'a': 29}, 
    15: {'q': 32, 'a': 31}, 
    16: {'q': 34, 'a': 33}, 
    17: {'q': 36, 'a': 35}, 
    18: {'q': 38, 'a': 37}, 
    19: {'q': 40, 'a': 39}, 
    20: {'q': 42, 'a': 41}, 
    21: {'q': 44, 'a': 43}, 
    22: {'q': 46, 'a': 45}, 
    23: {'q': 48, 'a': 47}, 
    24: {'q': 50, 'a': 49}, 
    25: {'q': 52, 'a': 51}, 
    26: {'q': 118, 'a': 117},
    27: {'q': 119, 'a': 120}
    }


# for i in range(1,26):
#      if i == 2:
#          continue
#      if(irBo_step_two[i]['a']):
#          irBo_step_two[i]['a'] = irBo_step_two[i]['a'] + 16
#      irBo_step_two[i]['q'] = irBo_step_two[i]['q'] + 16

irBo_step_two = {
    1: {'q': 53, 'a': None},
    3: {'q': 54, 'a': None},
    4: {'q': 55, 'a': None},
    5: {'q': 56, 'a': None},
    6: {'q': 57, 'a': None},
    7: {'q': 58, 'a': None},
    8: {'q': 59, 'a': None},
    9: {'q': 60, 'a': None},
    10: {'q': 61, 'a': None},
    11: {'q': 62, 'a': None},
    12: {'q': 63, 'a': None},
    13: {'q': 64, 'a': None},
    14: {'q': 65, 'a': None},
    15: {'q': 66, 'a': None},
    16: {'q': 68, 'a': 67},
    17: {'q': 70, 'a': 69},
    18: {'q': 72, 'a': 71},
    19: {'q': 74, 'a': 73},
    20: {'q': 76, 'a': 75},
    21: {'q': 78, 'a': 77},
    22: {'q': 80, 'a': 79},
    23: {'q': 82, 'a': 81},
    24: {'q': 84, 'a': 83},
    25: {'q': 86, 'a': 85},
    26: {'q': 122, 'a': 121},
    199: {'q': 126, 'a': 127}
}
# 87
IBO_data_dict = {
    1990: 87,
    1991: 88,
    1993: 89,
    1994: 90,
    1995: 91,
    1996: 92,
    1997: 93,
    1998: 94,
    1999: 95,
    2000: 96,
    2001: 97,
    2002: 98,
    2003: 99,
    2004: 100,
    2005: 101,
    2006: 102,
    2007: 103,
    2008: 104,
    2009: 105,
    2010: 106,
    2011: 107,
    2012: 108,
    2013: 109,
    2014: 110,
    2015: 111,
    2016: 112,
    2017: 113,
    2018: 114,
    2019: 115,
    2020: 116
    }
#--------------------------
talaha_data_dict = {
    7: {'q': 287, 'a': None}, 
    10: {'q': 288, 'a': None}, 
    11: {'q': 289, 'a': 290}, 
    12: {'q': 291, 'a': 292}, 
    13: {'q': 293, 'a': 294}, 
    14: {'q': 295, 'a': None}, 
    15: {'q': 296, 'a': 297}, 
    16: {'q': 298, 'a': 299}, 
    17: {'q': 300, 'a': 301}, 
    18: {'q': 302, 'a': 303}, 
    19: {'q': 304, 'a': None}, 
    20: {'q': 305, 'a': None}, 
    21: {'q': 306, 'a': 307}, 
    22: {'q': 308, 'a': 309}, 
    24: {'q': 310, 'a': 311}
}

book_subject_callback = {
    "زیست شناسی عمومی":"bgb",
    "بیوشیمی":"bch",
    "سلولی":"bce",
    "مولکولی":"bmo",
    "ژنتیک کلاسیک":"bcg",
    "تکامل و فیلوژنتیک":"bep",
    "سیستماتیک گیاهی":"bps",
    "سیستماتیک جانوری":"bas",
    "آناتومی گیاهی":"bpa",
    "فیزیولوژی گیاهی":"bpp",
    "فیزیولوژی جانوری":"bap",
    "فیزیولوژی انسانی":"bhp",
    "اکولوژی":"bec",
    "رفتار شناسی":"bbe",
    "آمار و ریاضیات زیستی":"bma",
    "آزمایشگاه":"bla",
    "بیوانفورماتیک":"bin"
}

inv_book_subject_callback = {v: k for k, v in book_subject_callback.items()}

subjects_books_list = {
    "زیست شناسی عمومی":["Campbell Biology","Solomon Biology","Life Biology","Raven Biology"],
    "بیوشیمی":["Lehninger","Lehninger answer","Stryer","Voet","Harper","Enzyme Kinetic","Grisham","Grisham Answer","Biochemical Calculations"],
    "سلولی":["Lodish", "Lewins", "The Cell", "Essential cell biology","The problem book of the cell","جواب های امیری"],
    "مولکولی":["Watson", "Weaver", "Genes XI"],
    "ژنتیک کلاسیک":["Griffiths", "Griffiths answer", "Kowles", "Stansfield", "Wellnitz","جواب های شاهنظر"],
    "تکامل و فیلوژنتیک":["Bergstrom","Futuyama","Herron","Phylogenetic Handbook"],
    "سیستماتیک گیاهی":["Plant Systematics 2nd edition","Plant Systematics 3rd edition"],
    "سیستماتیک جانوری":["Hickman","Brusca","Kardong","جانورشناسی مقایسه ای"],
    "آناتومی گیاهی":["Raven Plants","Crang","Stern","Rost","Esaus","Microscope Pic","Color Atlas of Plant Structure","The Plant Stem"],
    "فیزیولوژی گیاهی":["Taiz and Zieger"],
    "فیزیولوژی جانوری":["Moyes", "Eckert","Hill"],
    "فیزیولوژی انسانی":["Guyton","Junqueira","Ganong","Saladin","Langman","Kandel","Case and problems","Berne and Levy","Boron & Boulpaep","Color Atlas of Physiology","Problem-Based Physiology",
                        "Problem-Based Physiology Fluid, Electrolyte & Acid-Base","Problem-Based Physiology Neurophysiology, Gastrointestinal & Endocrine Systems",
                        "Problem-Based Physiology Cardio, Respiratory & Renal Systems"],
    "اکولوژی":["Krebs","Primer","Rockwood","Elements of ecology","Molles"],
    "رفتار شناسی":["Krebs and Davies","Dugantin","Aubrey manning"],
    "آمار و ریاضیات زیستی":["Calculus for Biology and Medicine","Daniel", "Bernard", "Jerrold", "Sylvia"],
    "آزمایشگاه":["Biology Lab Manual","Photographic Atlas"],
    "بیوانفورماتیک":["Jin Xiong","Bioinformatics and Functional Genomics","Biological Sequence Analysis","Understanding Bioinformatics"]
}

books_message_id_dict = {
    'Campbell Biology': 312,
    'Campbell Biology Test Bank': 313,
    'GRE Biology Test': 314,
    'Solomon Biology': 315,
    'Life Biology': 316,
    'Raven Biology': 317, 
    'Lehninger': 318, 
    'Lehninger answer': 319, 
    'Stryer': 320, 
    'Voet': 321, 
    'Harper': 322, 
    'Enzyme Kinetic': 323, 
    'Grisham': 324, 
    'Grisham Answer': 325, 
    'Biochemical Calculations': 326, 
    'Lodish': 327, 
    'Lewins': 328, 
    'The Cell': 329, 
    'Essential cell biology': 330, 
    'The problem book of the cell': 331, 
    'جواب های امیری': 332, 
    'جواب های شاهنظر': 333, 
    'Watson': 334, 
    'Weaver': 335, 
    'Genes XI': 336, 
    'Griffiths': 337, 
    'Griffiths answer': 338, 
    'Kowles': 339, 
    'Stansfield': 340, 
    'Wellnitz': 341, 
    'Bergstrom': 342, 
    'Futuyama': 343, 
    'Herron': 344, 
    'Phylogenetic Handbook': 345, 
    'Plant Systematics 2nd edition': 346, 
    'Plant Systematics 3rd edition': 347, 
    'Hickman': 348, 
    'Brusca': 349, 
    'Kardong': 350, 
    'جانورشناسی مقایسه ای': 351, 
    'Raven Plants': 352, 
    'Crang': 353, 
    'Stern': 354, 
    'Rost': 355, 
    'Esaus': 356, 
    'Microscope Pic': 357, 
    'Color Atlas of Plant Structure': 358, 
    'Taiz and Zieger': 359, 
    'Moyes': 360, 
    'Eckert': 361, 
    'Hill': 362, 
    'Guyton': 363, 
    'Junqueira': 364, 
    'Ganong': 365, 
    'Saladin': 366, 
    'Langman': 367, 
    'Kandel': 368, 
    'Case and problems': 369, 
    'Berne and Levy': 370, 
    'Krebs': 371, 
    'Primer': 372, 
    'Rockwood': 373, 
    'Dugantin': 374, 
    'Elements of ecology': 375, 
    'Molles': 376, 
    'Krebs and Davies': 377, 
    'Aubrey manning': 378, 
    'Calculus for Biology and Medicine': 379, 
    'Daniel': 380, 
    'Bernard': 381, 
    'Jerrold': 382, 
    'Sylvia': 383, 
    'Biology Lab Manual': 384, 
    'Photographic Atlas': 385, 
    'Problem-Based Physiology Fluid, Electrolyte & Acid-Base': 386, 
    'Problem-Based Physiology Neurophysiology, Gastrointestinal & Endocrine Systems': 387, 
    'Problem-Based Physiology Cardio, Respiratory & Renal Systems': 388, 
    'Problem-Based Physiology':389, 
    'Color Atlas of Physiology': 390, 
    'Thieme Test Physiology': 391, 
    'Jin Xiong': 392, 
    'Bioinformatics and Functional Genomics': 393, 
    'Biological Sequence Analysis': 394, 
    'Understanding Bioinformatics': 395, 
    'Boron & Boulpaep': 396,
    'The Plant Stem': 398}

question_books_and_manual_list = [
    "Campbell Biology Test Bank",
    "GRE Biology Test",
    "The problem book of the cell",
    "Lehninger answer",
    "جواب های شاهنظر",
    "جواب های امیری",
    "Biochemical Calculations",
    "Grisham Answer",
    "Griffiths answer",
    "Case and problems",
    "Problem-Based Physiology",
    "Problem-Based Physiology Fluid, Electrolyte & Acid-Base",
    "Problem-Based Physiology Neurophysiology, Gastrointestinal & Endocrine Systems",
    "Problem-Based Physiology Cardio, Respiratory & Renal Systems",
    "Thieme Test Physiology"
    ]

other_country_list = {
    "المپیاد داخلی استرالیا":"ocasoe",
    "المپیاد کانادا":"ocbiocomp",
    "کانتست هنگ کنک":"ochoko",
    "المپیاد داخلی هند":"ocinbo",
    "مسابقات مندل":"ocmbio",
    "المپیاد داخلی نیوزلند":"ocnzibo",
    "مرحله اوپن آمریکا":"ocusaboo",
    "مرحله نیمه نهایی آمریکا":"ocusabos",
    "آزمون 1.99":"M2_199"
}

other_country_message_id = {
    "asoe":400,
    "biocomp":401,
    "hoko":402,
    "inbo":403,
    "mbio":404,
    "nzibo":405,
    "usaboo":406,
    "usabos":399,
}