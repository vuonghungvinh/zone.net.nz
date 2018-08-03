# coding=utf-8

"""
ISO 3166-1 country names and codes.

The format of all three lists is a tuple of 2-tuples for ease of use with
Django model field choices.  All lists are ordered by country name.  Country
names are Unicode, encoded using utf-8.

For fast conversion from key to country name create a dictionary as follows::

    >>> m = dict(iso_3166.ALPHA_2)
    >>> len(m)
    249
    >>> m['NZ']
    u'New Zealand'

List details:

ALPHA_2
    Two-letter country codes which are the most widely used
    of the three, and used most prominently for the Internet's country code
    top-level domains (with a few exceptions).

ALPHA_3
    Three-letter country codes which allow a better visual association
    between the codes and the country names than the alpha-2 codes.

NUMERIC
    Three-digit country codes which are identical to those developed and
    maintained by the United Nations Statistics Division, with the advantage
    of script (writing system) independence, and hence useful for people or
    systems using non-Latin scripts.

"""


ALPHA_2 = (
    ("AF", u"Afghanistan"),
    ("AX", u"Åland Islands"),
    ("AL", u"Albania"),
    ("DZ", u"Algeria"),
    ("AS", u"American Samoa"),
    ("AD", u"Andorra"),
    ("AO", u"Angola"),
    ("AI", u"Anguilla"),
    ("AQ", u"Antarctica"),
    ("AG", u"Antigua and Barbuda"),
    ("AR", u"Argentina"),
    ("AM", u"Armenia"),
    ("AW", u"Aruba"),
    ("AU", u"Australia"),
    ("AT", u"Austria"),
    ("AZ", u"Azerbaijan"),
    ("BS", u"Bahamas"),
    ("BH", u"Bahrain"),
    ("BD", u"Bangladesh"),
    ("BB", u"Barbados"),
    ("BY", u"Belarus"),
    ("BE", u"Belgium"),
    ("BZ", u"Belize"),
    ("BJ", u"Benin"),
    ("BM", u"Bermuda"),
    ("BT", u"Bhutan"),
    ("BO", u"Bolivia, Plurinational State of"),
    ("BQ", u"Bonaire, Sint Eustatius and Saba"),
    ("BA", u"Bosnia and Herzegovina"),
    ("BW", u"Botswana"),
    ("BV", u"Bouvet Island"),
    ("BR", u"Brazil"),
    ("IO", u"British Indian Ocean Territory"),
    ("BN", u"Brunei Darussalam"),
    ("BG", u"Bulgaria"),
    ("BF", u"Burkina Faso"),
    ("BI", u"Burundi"),
    ("KH", u"Cambodia"),
    ("CM", u"Cameroon"),
    ("CA", u"Canada"),
    ("CV", u"Cape Verde"),
    ("KY", u"Cayman Islands"),
    ("CF", u"Central African Republic"),
    ("TD", u"Chad"),
    ("CL", u"Chile"),
    ("CN", u"China"),
    ("CX", u"Christmas Island"),
    ("CC", u"Cocos (Keeling) Islands"),
    ("CO", u"Colombia"),
    ("KM", u"Comoros"),
    ("CG", u"Congo"),
    ("CD", u"Congo, The Democratic Republic of the"),
    ("CK", u"Cook Islands"),
    ("CR", u"Costa Rica"),
    ("CI", u"Côte d'Ivoire"),
    ("HR", u"Croatia"),
    ("CU", u"Cuba"),
    ("CW", u"Curaçao"),
    ("CY", u"Cyprus"),
    ("CZ", u"Czech Republic"),
    ("DK", u"Denmark"),
    ("DJ", u"Djibouti"),
    ("DM", u"Dominica"),
    ("DO", u"Dominican Republic"),
    ("EC", u"Ecuador"),
    ("EG", u"Egypt"),
    ("SV", u"El Salvador"),
    ("GQ", u"Equatorial Guinea"),
    ("ER", u"Eritrea"),
    ("EE", u"Estonia"),
    ("ET", u"Ethiopia"),
    ("FK", u"Falkland Islands (Malvinas)"),
    ("FO", u"Faroe Islands"),
    ("FJ", u"Fiji"),
    ("FI", u"Finland"),
    ("FR", u"France"),
    ("GF", u"French Guiana"),
    ("PF", u"French Polynesia"),
    ("TF", u"French Southern Territories"),
    ("GA", u"Gabon"),
    ("GM", u"Gambia"),
    ("GE", u"Georgia"),
    ("DE", u"Germany"),
    ("GH", u"Ghana"),
    ("GI", u"Gibraltar"),
    ("GR", u"Greece"),
    ("GL", u"Greenland"),
    ("GD", u"Grenada"),
    ("GP", u"Guadeloupe"),
    ("GU", u"Guam"),
    ("GT", u"Guatemala"),
    ("GG", u"Guernsey"),
    ("GN", u"Guinea"),
    ("GW", u"Guinea-Bissau"),
    ("GY", u"Guyana"),
    ("HT", u"Haiti"),
    ("HM", u"Heard Island and McDonald Islands"),
    ("VA", u"Holy See (Vatican City State)"),
    ("HN", u"Honduras"),
    ("HK", u"Hong Kong"),
    ("HU", u"Hungary"),
    ("IS", u"Iceland"),
    ("IN", u"India"),
    ("ID", u"Indonesia"),
    ("IR", u"Iran, Islamic Republic of"),
    ("IQ", u"Iraq"),
    ("IE", u"Ireland"),
    ("IM", u"Isle of Man"),
    ("IL", u"Israel"),
    ("IT", u"Italy"),
    ("JM", u"Jamaica"),
    ("JP", u"Japan"),
    ("JE", u"Jersey"),
    ("JO", u"Jordan"),
    ("KZ", u"Kazakhstan"),
    ("KE", u"Kenya"),
    ("KI", u"Kiribati"),
    ("KP", u"Korea, Democratic People's Republic of"),
    ("KR", u"Korea, Republic of"),
    ("KW", u"Kuwait"),
    ("KG", u"Kyrgyzstan"),
    ("LA", u"Lao People's Democratic Republic"),
    ("LV", u"Latvia"),
    ("LB", u"Lebanon"),
    ("LS", u"Lesotho"),
    ("LR", u"Liberia"),
    ("LY", u"Libya"),
    ("LI", u"Liechtenstein"),
    ("LT", u"Lithuania"),
    ("LU", u"Luxembourg"),
    ("MO", u"Macao"),
    ("MK", u"Macedonia, The Former Yugoslav Republic of"),
    ("MG", u"Madagascar"),
    ("MW", u"Malawi"),
    ("MY", u"Malaysia"),
    ("MV", u"Maldives"),
    ("ML", u"Mali"),
    ("MT", u"Malta"),
    ("MH", u"Marshall Islands"),
    ("MQ", u"Martinique"),
    ("MR", u"Mauritania"),
    ("MU", u"Mauritius"),
    ("YT", u"Mayotte"),
    ("MX", u"Mexico"),
    ("FM", u"Micronesia, Federated States of"),
    ("MD", u"Moldova, Republic of"),
    ("MC", u"Monaco"),
    ("MN", u"Mongolia"),
    ("ME", u"Montenegro"),
    ("MS", u"Montserrat"),
    ("MA", u"Morocco"),
    ("MZ", u"Mozambique"),
    ("MM", u"Myanmar"),
    ("NA", u"Namibia"),
    ("NR", u"Nauru"),
    ("NP", u"Nepal"),
    ("NL", u"Netherlands"),
    ("NC", u"New Caledonia"),
    ("NZ", u"New Zealand"),
    ("NI", u"Nicaragua"),
    ("NE", u"Niger"),
    ("NG", u"Nigeria"),
    ("NU", u"Niue"),
    ("NF", u"Norfolk Island"),
    ("MP", u"Northern Mariana Islands"),
    ("NO", u"Norway"),
    ("OM", u"Oman"),
    ("PK", u"Pakistan"),
    ("PW", u"Palau"),
    ("PS", u"Palestinian Territory, Occupied"),
    ("PA", u"Panama"),
    ("PG", u"Papua New Guinea"),
    ("PY", u"Paraguay"),
    ("PE", u"Peru"),
    ("PH", u"Philippines"),
    ("PN", u"Pitcairn"),
    ("PL", u"Poland"),
    ("PT", u"Portugal"),
    ("PR", u"Puerto Rico"),
    ("QA", u"Qatar"),
    ("RE", u"Réunion"),
    ("RO", u"Romania"),
    ("RU", u"Russian Federation"),
    ("RW", u"Rwanda"),
    ("BL", u"Saint Barthélemy"),
    ("SH", u"Saint Helena, Ascension and Tristan da Cunha"),
    ("KN", u"Saint Kitts and Nevis"),
    ("LC", u"Saint Lucia"),
    ("MF", u"Saint Martin (French Part)"),
    ("PM", u"Saint Pierre and Miquelon"),
    ("VC", u"Saint Vincent and the Grenadines"),
    ("WS", u"Samoa"),
    ("SM", u"San Marino"),
    ("ST", u"Sao Tome and Principe"),
    ("SA", u"Saudi Arabia"),
    ("SN", u"Senegal"),
    ("RS", u"Serbia"),
    ("SC", u"Seychelles"),
    ("SL", u"Sierra Leone"),
    ("SG", u"Singapore"),
    ("SX", u"Sint Maarten (Dutch Part)"),
    ("SK", u"Slovakia"),
    ("SI", u"Slovenia"),
    ("SB", u"Solomon Islands"),
    ("SO", u"Somalia"),
    ("ZA", u"South Africa"),
    ("GS", u"South Georgia and the South Sandwich Islands"),
    ("SS", u"South Sudan"),
    ("ES", u"Spain"),
    ("LK", u"Sri Lanka"),
    ("SD", u"Sudan"),
    ("SR", u"Suriname"),
    ("SJ", u"Svalbard and Jan Mayen"),
    ("SZ", u"Swaziland"),
    ("SE", u"Sweden"),
    ("CH", u"Switzerland"),
    ("SY", u"Syrian Arab Republic"),
    ("TW", u"Taiwan, Province of China"),
    ("TJ", u"Tajikistan"),
    ("TZ", u"Tanzania, United Republic of"),
    ("TH", u"Thailand"),
    ("TL", u"Timor-Leste"),
    ("TG", u"Togo"),
    ("TK", u"Tokelau"),
    ("TO", u"Tonga"),
    ("TT", u"Trinidad and Tobago"),
    ("TN", u"Tunisia"),
    ("TR", u"Turkey"),
    ("TM", u"Turkmenistan"),
    ("TC", u"Turks and Caicos Islands"),
    ("TV", u"Tuvalu"),
    ("UG", u"Uganda"),
    ("UA", u"Ukraine"),
    ("AE", u"United Arab Emirates"),
    ("GB", u"United Kingdom"),
    ("US", u"United States"),
    ("UM", u"United States Minor Outlying Islands"),
    ("UY", u"Uruguay"),
    ("UZ", u"Uzbekistan"),
    ("VU", u"Vanuatu"),
    ("VE", u"Venezuela, Bolivarian Republic of"),
    ("VN", u"Viet Nam"),
    ("VG", u"Virgin Islands, British"),
    ("VI", u"Virgin Islands, U.S."),
    ("WF", u"Wallis and Futuna"),
    ("EH", u"Western Sahara"),
    ("YE", u"Yemen"),
    ("ZM", u"Zambia"),
    ("ZW", u"Zimbabwe"),
)

ALPHA_3 = (
    ("AFG", u"Afghanistan"),
    ("ALA", u"Åland Islands"),
    ("ALB", u"Albania"),
    ("DZA", u"Algeria"),
    ("ASM", u"American Samoa"),
    ("AND", u"Andorra"),
    ("AGO", u"Angola"),
    ("AIA", u"Anguilla"),
    ("ATA", u"Antarctica"),
    ("ATG", u"Antigua and Barbuda"),
    ("ARG", u"Argentina"),
    ("ARM", u"Armenia"),
    ("ABW", u"Aruba"),
    ("AUS", u"Australia"),
    ("AUT", u"Austria"),
    ("AZE", u"Azerbaijan"),
    ("BHS", u"Bahamas"),
    ("BHR", u"Bahrain"),
    ("BGD", u"Bangladesh"),
    ("BRB", u"Barbados"),
    ("BLR", u"Belarus"),
    ("BEL", u"Belgium"),
    ("BLZ", u"Belize"),
    ("BEN", u"Benin"),
    ("BMU", u"Bermuda"),
    ("BTN", u"Bhutan"),
    ("BOL", u"Bolivia, Plurinational State of"),
    ("BES", u"Bonaire, Sint Eustatius and Saba"),
    ("BIH", u"Bosnia and Herzegovina"),
    ("BWA", u"Botswana"),
    ("BVT", u"Bouvet Island"),
    ("BRA", u"Brazil"),
    ("IOT", u"British Indian Ocean Territory"),
    ("BRN", u"Brunei Darussalam"),
    ("BGR", u"Bulgaria"),
    ("BFA", u"Burkina Faso"),
    ("BDI", u"Burundi"),
    ("KHM", u"Cambodia"),
    ("CMR", u"Cameroon"),
    ("CAN", u"Canada"),
    ("CPV", u"Cape Verde"),
    ("CYM", u"Cayman Islands"),
    ("CAF", u"Central African Republic"),
    ("TCD", u"Chad"),
    ("CHL", u"Chile"),
    ("CHN", u"China"),
    ("CXR", u"Christmas Island"),
    ("CCK", u"Cocos (Keeling) Islands"),
    ("COL", u"Colombia"),
    ("COM", u"Comoros"),
    ("COG", u"Congo"),
    ("COD", u"Congo, The Democratic Republic of the"),
    ("COK", u"Cook Islands"),
    ("CRI", u"Costa Rica"),
    ("CIV", u"Côte d'Ivoire"),
    ("HRV", u"Croatia"),
    ("CUB", u"Cuba"),
    ("CUW", u"Curaçao"),
    ("CYP", u"Cyprus"),
    ("CZE", u"Czech Republic"),
    ("DNK", u"Denmark"),
    ("DJI", u"Djibouti"),
    ("DMA", u"Dominica"),
    ("DOM", u"Dominican Republic"),
    ("ECU", u"Ecuador"),
    ("EGY", u"Egypt"),
    ("SLV", u"El Salvador"),
    ("GNQ", u"Equatorial Guinea"),
    ("ERI", u"Eritrea"),
    ("EST", u"Estonia"),
    ("ETH", u"Ethiopia"),
    ("FLK", u"Falkland Islands (Malvinas)"),
    ("FRO", u"Faroe Islands"),
    ("FJI", u"Fiji"),
    ("FIN", u"Finland"),
    ("FRA", u"France"),
    ("GUF", u"French Guiana"),
    ("PYF", u"French Polynesia"),
    ("ATF", u"French Southern Territories"),
    ("GAB", u"Gabon"),
    ("GMB", u"Gambia"),
    ("GEO", u"Georgia"),
    ("DEU", u"Germany"),
    ("GHA", u"Ghana"),
    ("GIB", u"Gibraltar"),
    ("GRC", u"Greece"),
    ("GRL", u"Greenland"),
    ("GRD", u"Grenada"),
    ("GLP", u"Guadeloupe"),
    ("GUM", u"Guam"),
    ("GTM", u"Guatemala"),
    ("GGY", u"Guernsey"),
    ("GIN", u"Guinea"),
    ("GNB", u"Guinea-Bissau"),
    ("GUY", u"Guyana"),
    ("HTI", u"Haiti"),
    ("HMD", u"Heard Island and McDonald Islands"),
    ("VAT", u"Holy See (Vatican City State)"),
    ("HND", u"Honduras"),
    ("HKG", u"Hong Kong"),
    ("HUN", u"Hungary"),
    ("ISL", u"Iceland"),
    ("IND", u"India"),
    ("IDN", u"Indonesia"),
    ("IRN", u"Iran, Islamic Republic of"),
    ("IRQ", u"Iraq"),
    ("IRL", u"Ireland"),
    ("IMN", u"Isle of Man"),
    ("ISR", u"Israel"),
    ("ITA", u"Italy"),
    ("JAM", u"Jamaica"),
    ("JPN", u"Japan"),
    ("JEY", u"Jersey"),
    ("JOR", u"Jordan"),
    ("KAZ", u"Kazakhstan"),
    ("KEN", u"Kenya"),
    ("KIR", u"Kiribati"),
    ("PRK", u"Korea, Democratic People's Republic of"),
    ("KOR", u"Korea, Republic of"),
    ("KWT", u"Kuwait"),
    ("KGZ", u"Kyrgyzstan"),
    ("LAO", u"Lao People's Democratic Republic"),
    ("LVA", u"Latvia"),
    ("LBN", u"Lebanon"),
    ("LSO", u"Lesotho"),
    ("LBR", u"Liberia"),
    ("LBY", u"Libya"),
    ("LIE", u"Liechtenstein"),
    ("LTU", u"Lithuania"),
    ("LUX", u"Luxembourg"),
    ("MAC", u"Macao"),
    ("MKD", u"Macedonia, The Former Yugoslav Republic of"),
    ("MDG", u"Madagascar"),
    ("MWI", u"Malawi"),
    ("MYS", u"Malaysia"),
    ("MDV", u"Maldives"),
    ("MLI", u"Mali"),
    ("MLT", u"Malta"),
    ("MHL", u"Marshall Islands"),
    ("MTQ", u"Martinique"),
    ("MRT", u"Mauritania"),
    ("MUS", u"Mauritius"),
    ("MYT", u"Mayotte"),
    ("MEX", u"Mexico"),
    ("FSM", u"Micronesia, Federated States of"),
    ("MDA", u"Moldova, Republic of"),
    ("MCO", u"Monaco"),
    ("MNG", u"Mongolia"),
    ("MNE", u"Montenegro"),
    ("MSR", u"Montserrat"),
    ("MAR", u"Morocco"),
    ("MOZ", u"Mozambique"),
    ("MMR", u"Myanmar"),
    ("NAM", u"Namibia"),
    ("NRU", u"Nauru"),
    ("NPL", u"Nepal"),
    ("NLD", u"Netherlands"),
    ("NCL", u"New Caledonia"),
    ("NZL", u"New Zealand"),
    ("NIC", u"Nicaragua"),
    ("NER", u"Niger"),
    ("NGA", u"Nigeria"),
    ("NIU", u"Niue"),
    ("NFK", u"Norfolk Island"),
    ("MNP", u"Northern Mariana Islands"),
    ("NOR", u"Norway"),
    ("OMN", u"Oman"),
    ("PAK", u"Pakistan"),
    ("PLW", u"Palau"),
    ("PSE", u"Palestinian Territory, Occupied"),
    ("PAN", u"Panama"),
    ("PNG", u"Papua New Guinea"),
    ("PRY", u"Paraguay"),
    ("PER", u"Peru"),
    ("PHL", u"Philippines"),
    ("PCN", u"Pitcairn"),
    ("POL", u"Poland"),
    ("PRT", u"Portugal"),
    ("PRI", u"Puerto Rico"),
    ("QAT", u"Qatar"),
    ("REU", u"Réunion"),
    ("ROU", u"Romania"),
    ("RUS", u"Russian Federation"),
    ("RWA", u"Rwanda"),
    ("BLM", u"Saint Barthélemy"),
    ("SHN", u"Saint Helena, Ascension and Tristan da Cunha"),
    ("KNA", u"Saint Kitts and Nevis"),
    ("LCA", u"Saint Lucia"),
    ("MAF", u"Saint Martin (French Part)"),
    ("SPM", u"Saint Pierre and Miquelon"),
    ("VCT", u"Saint Vincent and the Grenadines"),
    ("WSM", u"Samoa"),
    ("SMR", u"San Marino"),
    ("STP", u"Sao Tome and Principe"),
    ("SAU", u"Saudi Arabia"),
    ("SEN", u"Senegal"),
    ("SRB", u"Serbia"),
    ("SYC", u"Seychelles"),
    ("SLE", u"Sierra Leone"),
    ("SGP", u"Singapore"),
    ("SXM", u"Sint Maarten (Dutch Part)"),
    ("SVK", u"Slovakia"),
    ("SVN", u"Slovenia"),
    ("SLB", u"Solomon Islands"),
    ("SOM", u"Somalia"),
    ("ZAF", u"South Africa"),
    ("SGS", u"South Georgia and the South Sandwich Islands"),
    ("SSD", u"South Sudan"),
    ("ESP", u"Spain"),
    ("LKA", u"Sri Lanka"),
    ("SDN", u"Sudan"),
    ("SUR", u"Suriname"),
    ("SJM", u"Svalbard and Jan Mayen"),
    ("SWZ", u"Swaziland"),
    ("SWE", u"Sweden"),
    ("CHE", u"Switzerland"),
    ("SYR", u"Syrian Arab Republic"),
    ("TWN", u"Taiwan, Province of China"),
    ("TJK", u"Tajikistan"),
    ("TZA", u"Tanzania, United Republic of"),
    ("THA", u"Thailand"),
    ("TLS", u"Timor-Leste"),
    ("TGO", u"Togo"),
    ("TKL", u"Tokelau"),
    ("TON", u"Tonga"),
    ("TTO", u"Trinidad and Tobago"),
    ("TUN", u"Tunisia"),
    ("TUR", u"Turkey"),
    ("TKM", u"Turkmenistan"),
    ("TCA", u"Turks and Caicos Islands"),
    ("TUV", u"Tuvalu"),
    ("UGA", u"Uganda"),
    ("UKR", u"Ukraine"),
    ("ARE", u"United Arab Emirates"),
    ("GBR", u"United Kingdom"),
    ("USA", u"United States"),
    ("UMI", u"United States Minor Outlying Islands"),
    ("URY", u"Uruguay"),
    ("UZB", u"Uzbekistan"),
    ("VUT", u"Vanuatu"),
    ("VEN", u"Venezuela, Bolivarian Republic of"),
    ("VNM", u"Viet Nam"),
    ("VGB", u"Virgin Islands, British"),
    ("VIR", u"Virgin Islands, U.S."),
    ("WLF", u"Wallis and Futuna"),
    ("ESH", u"Western Sahara"),
    ("YEM", u"Yemen"),
    ("ZMB", u"Zambia"),
    ("ZWE", u"Zimbabwe"),
)


NUMERIC = (
    (4,   u"Afghanistan"),
    (248, u"Åland Islands"),
    (8,   u"Albania"),
    (2,   u"Algeria"),
    (6,   u"American Samoa"),
    (20,  u"Andorra"),
    (24,  u"Angola"),
    (660, u"Anguilla"),
    (10,  u"Antarctica"),
    (28,  u"Antigua and Barbuda"),
    (32,  u"Argentina"),
    (51,  u"Armenia"),
    (533, u"Aruba"),
    (36,  u"Australia"),
    (40,  u"Austria"),
    (31,  u"Azerbaijan"),
    (44,  u"Bahamas"),
    (48,  u"Bahrain"),
    (50,  u"Bangladesh"),
    (52,  u"Barbados"),
    (112, u"Belarus"),
    (56,  u"Belgium"),
    (84,  u"Belize"),
    (204, u"Benin"),
    (60,  u"Bermuda"),
    (64,  u"Bhutan"),
    (68,  u"Bolivia, Plurinational State of"),
    (535, u"Bonaire, Sint Eustatius and Saba"),
    (70,  u"Bosnia and Herzegovina"),
    (72,  u"Botswana"),
    (74,  u"Bouvet Island"),
    (76,  u"Brazil"),
    (86,  u"British Indian Ocean Territory"),
    (96,  u"Brunei Darussalam"),
    (100, u"Bulgaria"),
    (854, u"Burkina Faso"),
    (108, u"Burundi"),
    (116, u"Cambodia"),
    (120, u"Cameroon"),
    (124, u"Canada"),
    (132, u"Cape Verde"),
    (136, u"Cayman Islands"),
    (140, u"Central African Republic"),
    (148, u"Chad"),
    (152, u"Chile"),
    (156, u"China"),
    (162, u"Christmas Island"),
    (166, u"Cocos (Keeling) Islands"),
    (170, u"Colombia"),
    (174, u"Comoros"),
    (178, u"Congo"),
    (180, u"Congo, The Democratic Republic of the"),
    (184, u"Cook Islands"),
    (188, u"Costa Rica"),
    (384, u"Côte d'Ivoire"),
    (191, u"Croatia"),
    (192, u"Cuba"),
    (531, u"Curaçao"),
    (196, u"Cyprus"),
    (203, u"Czech Republic"),
    (208, u"Denmark"),
    (262, u"Djibouti"),
    (212, u"Dominica"),
    (214, u"Dominican Republic"),
    (218, u"Ecuador"),
    (818, u"Egypt"),
    (222, u"El Salvador"),
    (226, u"Equatorial Guinea"),
    (232, u"Eritrea"),
    (233, u"Estonia"),
    (231, u"Ethiopia"),
    (238, u"Falkland Islands (Malvinas)"),
    (234, u"Faroe Islands"),
    (242, u"Fiji"),
    (246, u"Finland"),
    (250, u"France"),
    (254, u"French Guiana"),
    (258, u"French Polynesia"),
    (260, u"French Southern Territories"),
    (266, u"Gabon"),
    (270, u"Gambia"),
    (268, u"Georgia"),
    (276, u"Germany"),
    (288, u"Ghana"),
    (292, u"Gibraltar"),
    (300, u"Greece"),
    (304, u"Greenland"),
    (308, u"Grenada"),
    (312, u"Guadeloupe"),
    (316, u"Guam"),
    (320, u"Guatemala"),
    (831, u"Guernsey"),
    (324, u"Guinea"),
    (624, u"Guinea-Bissau"),
    (328, u"Guyana"),
    (332, u"Haiti"),
    (334, u"Heard Island and McDonald Islands"),
    (336, u"Holy See (Vatican City State)"),
    (340, u"Honduras"),
    (344, u"Hong Kong"),
    (348, u"Hungary"),
    (352, u"Iceland"),
    (356, u"India"),
    (360, u"Indonesia"),
    (364, u"Iran, Islamic Republic of"),
    (368, u"Iraq"),
    (372, u"Ireland"),
    (833, u"Isle of Man"),
    (376, u"Israel"),
    (380, u"Italy"),
    (388, u"Jamaica"),
    (392, u"Japan"),
    (832, u"Jersey"),
    (400, u"Jordan"),
    (398, u"Kazakhstan"),
    (404, u"Kenya"),
    (296, u"Kiribati"),
    (408, u"Korea, Democratic People's Republic of"),
    (410, u"Korea, Republic of"),
    (414, u"Kuwait"),
    (417, u"Kyrgyzstan"),
    (418, u"Lao People's Democratic Republic"),
    (428, u"Latvia"),
    (422, u"Lebanon"),
    (426, u"Lesotho"),
    (430, u"Liberia"),
    (434, u"Libya"),
    (438, u"Liechtenstein"),
    (440, u"Lithuania"),
    (442, u"Luxembourg"),
    (446, u"Macao"),
    (807, u"Macedonia, The Former Yugoslav Republic of"),
    (450, u"Madagascar"),
    (454, u"Malawi"),
    (458, u"Malaysia"),
    (462, u"Maldives"),
    (466, u"Mali"),
    (470, u"Malta"),
    (584, u"Marshall Islands"),
    (474, u"Martinique"),
    (478, u"Mauritania"),
    (480, u"Mauritius"),
    (175, u"Mayotte"),
    (484, u"Mexico"),
    (583, u"Micronesia, Federated States of"),
    (498, u"Moldova, Republic of"),
    (492, u"Monaco"),
    (496, u"Mongolia"),
    (499, u"Montenegro"),
    (500, u"Montserrat"),
    (504, u"Morocco"),
    (508, u"Mozambique"),
    (104, u"Myanmar"),
    (516, u"Namibia"),
    (520, u"Nauru"),
    (524, u"Nepal"),
    (528, u"Netherlands"),
    (540, u"New Caledonia"),
    (554, u"New Zealand"),
    (558, u"Nicaragua"),
    (562, u"Niger"),
    (566, u"Nigeria"),
    (570, u"Niue"),
    (574, u"Norfolk Island"),
    (580, u"Northern Mariana Islands"),
    (578, u"Norway"),
    (512, u"Oman"),
    (586, u"Pakistan"),
    (585, u"Palau"),
    (275, u"Palestinian Territory, Occupied"),
    (591, u"Panama"),
    (598, u"Papua New Guinea"),
    (600, u"Paraguay"),
    (604, u"Peru"),
    (608, u"Philippines"),
    (612, u"Pitcairn"),
    (616, u"Poland"),
    (620, u"Portugal"),
    (630, u"Puerto Rico"),
    (634, u"Qatar"),
    (638, u"Réunion"),
    (642, u"Romania"),
    (643, u"Russian Federation"),
    (646, u"Rwanda"),
    (652, u"Saint Barthélemy"),
    (654, u"Saint Helena, Ascension and Tristan da Cunha"),
    (659, u"Saint Kitts and Nevis"),
    (662, u"Saint Lucia"),
    (663, u"Saint Martin (French Part)"),
    (666, u"Saint Pierre and Miquelon"),
    (670, u"Saint Vincent and the Grenadines"),
    (882, u"Samoa"),
    (674, u"San Marino"),
    (678, u"Sao Tome and Principe"),
    (682, u"Saudi Arabia"),
    (686, u"Senegal"),
    (688, u"Serbia"),
    (690, u"Seychelles"),
    (694, u"Sierra Leone"),
    (702, u"Singapore"),
    (534, u"Sint Maarten (Dutch Part)"),
    (703, u"Slovakia"),
    (705, u"Slovenia"),
    (90,  u"Solomon Islands"),
    (706, u"Somalia"),
    (710, u"South Africa"),
    (239, u"South Georgia and the South Sandwich Islands"),
    (728, u"South Sudan"),
    (724, u"Spain"),
    (144, u"Sri Lanka"),
    (736, u"Sudan"),
    (740, u"Suriname"),
    (744, u"Svalbard and Jan Mayen"),
    (748, u"Swaziland"),
    (752, u"Sweden"),
    (756, u"Switzerland"),
    (760, u"Syrian Arab Republic"),
    (158, u"Taiwan, Province of China"),
    (762, u"Tajikistan"),
    (834, u"Tanzania, United Republic of"),
    (764, u"Thailand"),
    (626, u"Timor-Leste"),
    (768, u"Togo"),
    (772, u"Tokelau"),
    (776, u"Tonga"),
    (780, u"Trinidad and Tobago"),
    (788, u"Tunisia"),
    (792, u"Turkey"),
    (795, u"Turkmenistan"),
    (796, u"Turks and Caicos Islands"),
    (798, u"Tuvalu"),
    (800, u"Uganda"),
    (804, u"Ukraine"),
    (784, u"United Arab Emirates"),
    (826, u"United Kingdom"),
    (840, u"United States"),
    (581, u"United States Minor Outlying Islands"),
    (858, u"Uruguay"),
    (860, u"Uzbekistan"),
    (548, u"Vanuatu"),
    (862, u"Venezuela, Bolivarian Republic of"),
    (704, u"Viet Nam"),
    (92,  u"Virgin Islands, British"),
    (850, u"Virgin Islands, U.S."),
    (876, u"Wallis and Futuna"),
    (732, u"Western Sahara"),
    (887, u"Yemen"),
    (894, u"Zambia"),
    (716, u"Zimbabwe"),
)