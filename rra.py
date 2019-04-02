# Python 3 Please.



from faker import Faker
import uuid
import time
import random
import requests


# The referral data for our Ring credit.

try:
	referrerId = int(input('what is your referrerId? '))
except ValueError:
	 print('Not a valid referrerID. Please use numbers.')
		quit()

inviteCode = input('what is your invite code? ')
referrerLink = input('what is your referrerLink? ')

# Set up our fake account information.
for x in range(int(input("how much: "))):
	class FakePerson(object):
		def __init__(self):
			self.fake = Faker()
			self.hardwareId = str(uuid.uuid4()).upper()

			self.first_name = self.fake.first_name()
			self.last_name = self.fake.last_name()

		@property
		def email(self):
			return '{}{}@{}'.format(self.first_name(), random.randint(100, 1000), '@gmail.com')
	
		@property
		def password(self):
			return self.fake.password(length = random.randint(8, 10), special_chars = False)
	
		@property
		def hardwareId(self):
			return str(uuid.uuid4()).upper()
	



	# init the fake person

	Fake = FakePerson()

	# TODO: All the timestamp/timezone formatting.
	
	offset = '{}{:02}{:02}'.format('-' if time.altzone > 0 else '+', abs(time.altzone) / 3600, abs(time.altzone / 60) % 60)
	
	timestamp = time.strftime('%Y-%m-%dT%H:%M') + offset
	#print 'Timestamp: {}\n'.format(timestamp)

	register = {
		'device':{
			'metadata':{
				 "app_brand" : "neighborhoods",
                 "scale" : 2,
                 "retina" : "true",
                 "build_profile" : "store_production",
                 "app_installation_date" : "2019-01-21 08:02:41 +0000",
                 "app_version" : "v1.2.0 (9))",
                 "api_version" : "9",
                 "device_name" : "iPhone 6S",
                 "language" : "en",
                 "resolution" : "375x667",
                 "device_model" : "iPhone",
                 "ios_version" : "10.2",
				'app_installation_date':timestamp,
				"language" : "en",
				'build_profile':'store_production',
				'app_version':'v1.1.0 (1))',
				'device_model':'iPhone'
			},
			'hardware_id':Fake.hardwareId,
			'app_brand':'neighborhoods',
			'os':'ios'
		},
		'profile':{
			'email':Fake.email,
			'last_name':Fake.last_name,
			'metadata':{
				'user_flow':'nh',
				'country':'US',
				'terms_of_service':timestamp,
				'data_storage_terms':timestamp
			},
			'first_name':Fake.first_name,
			'password_confirmation':Fake.password,
			'password':Fake.password,
			'phone_number':''
		}
	}

	# Create an account.



	response = requests.post('https://api.ring.com/clients_api/profile', headers = {'app_brand':'neighborhoods', 'X-API-LANG':'en'}, params = register)
	#print '{}\n'.format(response.content)

	# Get an oauth token for our account.
	response = requests.post('https://oauth.ring.com/oauth/token', headers = {'app_brand':'neighborhoods'}, params = {'grant_type':'password', 'client_id':'ring_official_ios', 'username':Fake.email, 'password':Fake..password, 'scope':'client'})
	#print '{}\n'.format(response.content)
	response = response.json()
	authorization = '{} {}'.format(response['token_type'], response['access_token'])

	# Tell Ring who referred us.
	referral = {
		'params':{
			'params':{
				'+referrer':'https://google.com/',
				'+is_first_session':True,
				'~creation_source':0,
				'referrer_id':referrerId,
				'+match_guaranteed':False,
				'~referring_link':referrerLink,
				# Logged ID was 562828469625838233. This may be some identifier from install. I don't know and don't care.
				'~id':str(random.randint(100000000000000000, 999999999999999999)),
				'$identity_id':referrerId,
				'+clicked_branch_link':True,
				'$ios_passive_deepview':'ring_video_doorbell_deepview_qlxb',
				'+click_timestamp':int(round(time.time() - 5)),
				'$one_time_use':False,
				'invite_code':inviteCode,
				'~feature':'referral'
			},
			'hardware_id':Fake.hardwareId,
			'referrer_id':referrerId,
			'invite_code':inviteCode
		},
		'hardware_id':Fake.hardwareId,
		'referrer_id':referrerId,
		'invite_code':inviteCode
	}


	headers = {
		'app_brand': 'neighborhoods',
		'X-API-LANG': 'en',
		'Authorization': authorization
	}

	response = requests.post('https://alerts.ring.com/api/end_users/referral', headers=headers, json=referral)
	print(response.content)
