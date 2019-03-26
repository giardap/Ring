# Ring Referral Abuser

This was a project made by me to easily spoof referrals to your ring account and make fraudulent purchases.

## Disclaimer

This has been submitted and fixed by Ring along wiht their referral system being shut down.

## Getting Started

To use this you need to find your referrerId, inviteCode, and referrerLink.
to find these you will need to use a network tracker such as Charles Proxy or Burp suite and grab the request when clicking your referrering link.
What you need to do is simple as this

Create a ring account in the neighbors app.
Head over to the referral section
Copy the link and and paste into wherever you can trace the response
Once you examine the response you will find something that looks like this.
```{
  "session_id" : "615809008687086307",
  "identity" : "youremail@here.com",
  "data" : "{"referrer_id":16372942,"~creation_source":0,"+click_timestamp":1548058666,"$identity_id":13311921,"$ios_passive_deepview":"ring_video_doorbell_deepview_qlxb","~feature":"referral","+match_guaranteed":true,"+clicked_branch_link":true,"$one_time_use":false,"~id":"615809209824759391","+is_first_session":true,"~referring_link":"https://download.ring.com/nSuwYXw/%22,/%22invite_code/%22:/%22dc175e8bce/%22%7D",
  "device_fingerprint_id" : "615809008687086307",
    "identity_id" : "615809008687086307",
  "link" : "https://download.ring.com/a/key_live_fiAFgsbsLJpNm7gHksC6BgcfwxcJI44h?%24identity_id=615809008687086307"
}
```
From there you will now have all the necessary parts to make this 
### Prerequisites

Before you use this you must need:

```
Python 2.7 on any operating system.
Pip
```

## Getting Started

To use this Just simply run
```
pip install requirements.txt
python ringkill.py
```
and enter valid credentials (referreeId, inviteCode, and referringLink)

## Disclaimer

This has been submitted and fixed by Ring along with their referral system being shut down.
