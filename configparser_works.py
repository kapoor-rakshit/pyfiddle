
# REFRENCE : https://docs.python.org/3/library/configparser.html
# Essentially, configuration file consists of sections [], each of which contains keys with values.
# configparser classes can read and write .ini, .cfg and other such files

import configparser

config = configparser.ConfigParser()


#  Write to config file
#  DEFAULT (case-sensitive, uppercase) section which provides default values for all other sections
#  sections are (case-sensitive)
#  keys in sections are (case-insensitive) and stored in lowercase
#1
config['DEFAULT'] = {'Home' : 'Amritsar (Sifti da ghar)',
					 'School' : 'DAV Public School, Lawrence road',
					 'College' : 'NIT Jalandhar'}

#2
config['tesTvals_SECTION_1'] = {}
config['tesTvals_SECTION_1']['Val1'] = '2019'

#3
config['testvals_SECTION_2'] = {}
section2 = config['testvals_SECTION_2']
section2['Val2'] = 'Balle Balle'
section2['VAL3'] = 'Bhangre pao'
section2['HOME'] = 'Ambarsar'

with open('testconfig.cfg', 'w+') as configfile:
	config.write(configfile)



#  Read from config file
#
config.read('testconfig.cfg')                                # Read config file

print(config.sections())                                     # Sections

print('testvals_SECTION_2' in config)                        # Check for existence of section
print('VAL5' in config['testvals_SECTION_2'])                # Check for existence of key in section

print(config.get('testvals_SECTION_2', 'val5', fallback='Providing fallback value'))   # if key not exist in section, provide a fallback

print(config['testvals_SECTION_2']['home'])                  # Value of Section's key, LOCAL key preferred over DEFAULT

readSECTION2 = config['testvals_SECTION_2']
print(readSECTION2['VAL2'])

print(readSECTION2['college'], readSECTION2['School'])       # Keys not present in section but exist in DEFAULT, also becomes part of each section

for k in readSECTION2:
	print(k,":",readSECTION2[k])

