[![License](https://img.shields.io/badge/License-GNU-blue.svg?style=flat-square)](https://github.com/giardap/Ring/blob/master/License.md) ![OS](https://img.shields.io/badge/Tested%20On-Linux%20|%20OSX%20|%20Windows%20|%20Android-yellowgreen.svg?style=flat-square) [![Python2.7](https://img.shields.io/badge/Python-2.7-green.svg?style=flat-square)](https://github.com/giardap/Ring/tree/python2.7) [![Python3](https://img.shields.io/badge/Python-3-green.svg?style=flat-square)](https://github.com/giardap/Ring)

# Ring Referral Abuser

This was a project made by me to easily spoof referrals to your ring account and make fraudulent purchases.

## Getting Started

To use this you need to find your referrerId, inviteCode, and referrerLink.
to find these you will need to use a network tracker such as Charles Proxy or Burp suite and grab the request when clicking your referrering link.
What you need to do is simple as this.

Step 1. Create a ring account in the neighbors app.

Step 2. Head over to the referral section.

Step 3. Copy the link and and paste into wherever you can trace the response.

Step 4. Once you examine the response you will find something that looks like this:

```{
  "session_id" : "615809008687086307",
  "identity" : "youremail@here.com",
  "data" : "{"referrer_id":16372942,"~creation_source":0,"+click_timestamp":1548058666,"$identity_id":13311921,"$ios_passive_deepview":"ring_video_doorbell_deepview_qlxb","~feature":"referral","+match_guaranteed":true,"+clicked_branch_link":true,"$one_time_use":false,"~id":"615809209824759391","+is_first_session":true,"~referring_link":"https://download.ring.com/nSuwYXw/%22,/%22invite_code/%22:/%22dc175e8bce/%22%7D",
  "device_fingerprint_id" : "615809008687086307",
    "identity_id" : "615809008687086307",
  "link" : "https://download.ring.com/a/key_live_fiAFgsbsLJpNm7gHksC6BgcfwxcJI44h?%24identity_id=615809008687086307"
}
```
From there you will now have all the necessary parts to make this work.

Step 5. Profit???

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
and enter valid credentials (referrerId, inviteCode, and referringLink)

## Authors

* **Padraig Marks** - *Initial work* - [Ring Exploit](https://hackerone.com/padraig)
* **Mustafa (exofeel)** - *Port to Py3* - [Mustafas work](https://github.com/exofeel)

## Disclaimer

This has been submitted and fixed by Ring along with their referral system being shut down.
