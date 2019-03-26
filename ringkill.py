#!/usr/bin/env python2.7

from faker import Faker
import uuid, time, random, requests

# The referral data for our Ring credit.
referrerId = 7743547
inviteCode = '52d7ee1e2b'
referrerLink = 'https://download.ring.com/epSnOFbp5P'

# Set up our fake account information.
for x in range(input("how much: ")):
	fake = Faker()
	email = '{}{}@{}'.format(fake.user_name(), random.randint(100, 1000), fake.free_email_domain())
	hardwareId = str(uuid.uuid4()).upper()
	password = fake.password(length = random.randint(8, 10), special_chars = False)

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
                 "ios_version" : "10.2"
				'app_installation_date':time.strftime('%Y-%m-%d %H:%M:%S +0000', time.gmtime(time.time() - 300)),
				'language':'en',
				'build_profile':'store_production',
				'app_version':'v1.1.0 (1))',
				'device_model':'iPhone'
			},
			'hardware_id':hardwareId,
			'app_brand':'neighborhoods',
			'os':'ios'
		},
		'profile':{
			'email':email,
			'last_name':fake.last_name(),
			'metadata':{
				'user_flow':'nh',
				'country':'US',
				'terms_of_service':timestamp,
				'data_storage_terms':timestamp
			},
			'first_name':fake.first_name(),
			'password_confirmation':password,
			'password':password,
			'phone_number':''
		}
	}

	# Create an account.
	response = requests.post('https://api.ring.com/clients_api/profile', headers = {'app_brand':'neighborhoods', 'X-API-LANG':'en'}, json = register)
	#print '{}\n'.format(response.content)

	# Get an oauth token for our account.
	response = requests.post('https://oauth.ring.com/oauth/token', headers = {'app_brand':'neighborhoods'}, json = {'grant_type':'password', 'client_id':'ring_official_ios', 'username':email, 'password':password, 'scope':'client'})
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
			'hardware_id':hardwareId,
			'referrer_id':referrerId,
			'invite_code':inviteCode
		},
		'hardware_id':hardwareId,
		'referrer_id':referrerId,
		'invite_code':inviteCode
	}

	response = requests.post('https://alerts.ring.com/api/end_users/referral', headers = {'app_brand':'neighborhoods', 'X-API-LANG':'en', 'Authorization':authorization}, json = referral)
	print response.content
