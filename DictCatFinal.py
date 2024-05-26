#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dictionary on various numerical value for discrete features
dictMarital = {
    1: 'single',
    2: 'married',
    3: 'widower',
    4: 'divorced',
    5: 'facto union',
    6: 'legally separated'
}

dictAppMode = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

dictAppOrder = {
    0: 'first choice',
    1: 'second choice',
    2: 'third choice',
    3: 'fourth choice',
    4: 'fifth choice',
    5: 'sixth choice',
    6: 'seventh choice',
    7: 'eighth choice',
    8: 'ninth choice',
    9: 'last choice'
}

dictCourse = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}

dictAtt = {
    1: 'daytime',
    0: 'evening'
}

dictQualification = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd Year Complementary High School Course",
    14: "10th Year of Schooling",
    15: "10th year of schooling - not completed",
    18: "General Commerce Course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-Professional Course",
    25: "Complementary High School Course - Not Concluded",
    26: "7th Year of Schooling",
    27: "2nd Cycle of the General High School Course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th Year of Schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't Read or Write",
    36: "Can Read Without Having a 4th Year of Schooling",
    37: "Basic Education 1st Cycle (4th/5th Year) or Equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological Specialization Course",
    40: "Higher Education - Degree (1st Cycle)",
    41: "Specialized Higher Studies Course",
    42: "Professional Higher Technical Course",
    43: "Higher Education - Master (2nd Cycle)",
    44: "Higher Education - Doctorate (3rd Cycle)"
}

dictNac = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
}

dictOcu = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative Staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(blank)",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces Personnel",
    112: "Directors of Administrative and Commercial Services",
    114: "Hotel, Catering, Trade and Other Services Directors",
    121: "Specialists in the Physical Sciences, Mathematics, Engineering and Related Techniques",
    122: "Health Professionals",
    123: "Teachers",
    124: "Specialists in Finance, Accounting, Administrative Organization, Public and Commercial Relations",
    125: "Specialists in information and communication technologies (ICT)",
    131: "Intermediate Level Science and Engineering Technicians and Professions",
    132: "Technicians and Professionals, of Intermediate Level of Health",
    134: "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services",
    135: "Information and Communication Technology Technicians",
    141: "Office Workers, Secretaries in General and Data Processing Operators",
    143: "Data, Accounting, Statistical, Financial Services and Registry-Related Operators",
    144: "Other Administrative Support Staff",
    151: "Personal Service Workers",
    152: "Sellers",
    153: "Personal Care Workers and the Like",
    154: "Protection and Security Services Personnel",
    161: "Market-Oriented Farmers and Skilled Agricultural and Animal Production Workers",
    163: "Farmers, Livestock Keepers, Fishermen, Hunters and Gatherers, Subsistence",
    171: "Skilled Construction Workers and the Like, Except Electricians",
    172: "Skilled Workers in Metallurgy, Metalworking and Similar",
    173: "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    174: "Skilled Workers in Electricity and Electronics",
    175: "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts",
    181: "Fixed Plant and Machine Operators",
    182: "Assembly Workers",
    183: "Vehicle Drivers and Mobile Equipment Operators",
    191: "cleaning workers",
    192: "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry",
    193: "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport",
    194: "Meal Preparation Assistants",
    195: "Street Vendors (Except Food) and Street Service Providers"
}

dictYN = {
    0: "No",
    1: "Yes"
}

dictGender = {
    0: "Female",
    1: "Male"
}

dictQualificationMapper = {
    0: [35, 36],
    1: [37],
    2: [11, 26, 29, 30, 38],
    3: [1, 6, 9, 10, 12, 14, 15, 19, 27],
    4: [13, 20, 22, 25, 31, 33, 39],
    5: [2, 3, 40, 41, 42],
    6: [4, 18, 43],
    7: [5, 44],
    8: [34]
}

dictQualificationNew = {
    0: "Non",
    1: "Primary",
    2: "Lower Secondary",
    3: "Upper Secondary",
    4: "Technical",
    5: "Bachelor",
    6: "Master",
    7: "Doctoral",
    8: "Unknown"
}

dictNacMapper = {
    0: [2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109],
    1: [1]
}

dictNacNew = {
    0: "Other",
    1: "Portugese"
}

dictOcuMapper = {
    0: [1, 112, 114],
    1: [2, 121, 122, 123, 124, 125],
    2: [3, 131, 132, 134, 135],
    3: [4, 141, 143, 144],
    4: [5, 151, 152, 153, 154],
    5: [6, 161, 163],
    6: [7, 171, 172, 173, 174, 175],
    7: [8, 181, 182,183],
    8: [9, 192, 193, 191, 194, 195],
    9: [10, 101, 102, 103],
    10: [0,90,99]
}

dictOcuNew = {
    0: "Managers",
    1: "Professionals",
    2: "Technicians and associate professionals",
    3: "Clerical support workers",
    4: "Service and sales workers",
    5: "Skilled agricultural, forestry and fishery workers",
    6: "Craft and related trades workers",
    7: "Plant and machine operators, and assemblers",
    8: "Unskilled worker",
    9: "Armed forces occupations",
    10: "Other"
}