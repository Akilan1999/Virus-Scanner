'''

 An example script showing how to access the ThreatCrowd API in python

'''


import requests, json
import argparse

'''
result =  requests.get("http://www.threatcrowd.org/searchApi/v2/email/report/", params = {"email": "william19770319@yahoo.com"})
print result.text

j = json.loads(result.text)
print j['domains'][0]
'''

parser= argparse.ArgumentParser()
parser.add_argument('input', type = str, help = "Argument")
arg = parser.parse_args()

print (requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": arg.input}).text)
"""
print (requests.get("http://www.threatcrowd.org/searchApi/v2/ip/report/", {"ip": "188.40.75.132"}).text)

print (requests.get("http://www.threatcrowd.org/searchApi/v2/antivirus/report/", {"antivirus" :"plugx"}).text)
"""

'''

Example Responses:

{"response_code":"1","domains":["aoldaily.com","aunewsonline.com","cnndaily.com","usnewssite.com"],"references":[],"permalink":"https:\/\/www.threatcrowd.org\/email.php?email=william19770319@yahoo.com"}

aoldaily.com

{"response_code":"1","resolutions":[{"last_resolved":"2015-10-09","ip_address":"-"},{"last_resolved":"2014-04-01","ip_address":"0.0.0.0"},{"last_resolved":"2013-09-03","ip_address":"50.116.42.33"},{"last_resolved":"2013-09-20","ip_address":"50.63.202.70"},{"last_resolved":"0000-00-00","ip_address":"66.228.48.134"},{"last_resolved":"2015-05-12","ip_address":"69.195.129.70"},{"last_resolved":"2014-12-13","ip_address":"69.195.129.72"},{"last_resolved":"2013-12-02","ip_address":"81.166.122.234"}],"hashes":[],"emails":["domains@virustracker.info","william19770319@yahoo.com"],"references":["http:\/\/blog.shadowserver.org\/2013\/02\/","http:\/\/sto-strategy.com\/s\/Appendix-D-Digital-FQDNs.pdf"],"permalink":"https:\/\/www.threatcrowd.org\/domain.php?domain=aoldaily.com"}

{"response_code":"1","resolutions":[{"last_resolved":"2015-02-17","domain":"tvgate.rocks"},{"last_resolved":"2015-02-17","domain":"nice-mobiles.com"},{"last_resolved":"2015-02-17","domain":"nauss-lab.com"},{"last_resolved":"2015-02-17","domain":"iwork-sys.com"},{"last_resolved":"2015-02-17","domain":"linkedim.in"},{"last_resolved":"2015-02-17","domain":"fpupdate.info"},{"last_resolved":"2015-02-17","domain":"ineltdriver.com"},{"last_resolved":"2015-02-17","domain":"flushupdate.com"},{"last_resolved":"2015-02-17","domain":"flushupate.com"},{"last_resolved":"2015-02-17","domain":"ahmedfaiez.info"},{"last_resolved":"2014-02-14","domain":"advtravel.info"},{"last_resolved":"2014-05-27","domain":"nartu.de"},{"last_resolved":"2015-02-19","domain":"www.fpupdate.info"},{"last_resolved":"2014-03-22","domain":"advtravel.info\r"},{"last_resolved":"2014-06-08","domain":"ahmedfaiez.info\r"},{"last_resolved":"2014-08-22","domain":"flushupate.com\r"},{"last_resolved":"2014-11-07","domain":"ineltdriver.com\r"},{"last_resolved":"2015-09-21","domain":"gbartu.de"},{"last_resolved":"2015-09-28","domain":"vartu.de"},{"last_resolved":"2015-10-10","domain":"ns1.atyafhosting.info"},{"last_resolved":"2015-10-10","domain":"NS2.ATYAFHOSTING.INFO"}],"hashes":["003f0ed24b5f70ddc7c6e80f9c4dac73","027fc90c13f6d87e1f68d25b0d0ec4a7","088420b7e56c73d3d495230d42e0cb95","1e52a293838464e4cd6c1c6d94a55793","2219f3941603262dc3478c60df3b02f6","238b48338c14c8ea87ff7ccab4544252","2607abe604832363514eb58c33a682fc","2986d9af413cd09d9ffdb40040e5c180","2b3baed817a79109824d3a8a94f6c317","2bce2ccd484a063e5e432a6f651782d9","4377b17d7984838993b998c4bab97925","4907a68a3ff0f010ed74214f957746c0","63c480b1cc601b02b4acb30309b007e6","686779709226c6727bd9ebc4b1ff21b1","6b4248a01a26ff07a85b5316702a2f5f","7075c9a874ab5b0c27942714394f3885","73c46bacc471db08a6c0e31caef3f9e8","74d8b882efae9fea1787f1558589fecb","76f74b24480bc1a42998c9440ddc2fad","7ac102b740b299824e34394f334b5508","7ed79032a1ad8535242428e69507ca0a","8a9b52ff90bbd585907694e68551b991","8bbad466f2257e05f66ece621ccf2056","9469ff12c582cf7943582dd28a1920cc","a0b76ea08917a9dd785a0a1a6ae6eebe","a4a390f90be49b2bb51194d0844fed7f","a59399c7608d140dc9cb5dffcb46f1d9","aefea9d795624da16d878dc9bb81bf87","b08a67892d2198aeb2826b398f8c6c74","bd54d70d473d45b75cc8bf1fbe6fa022","d048a6a8377a865f07cbc2429ffaa3e7","dff746868a1559de9d25037e73c06c52","e1d2543aba350a83c968872fbe957d85","f3d6bb7addc88ad45f79c5199f8db2e0","f78fcd4eaf3d9cd95116b6e6212ad327","fa6fbd1dd2d58885772bd0b37633d5d7"],"references":[""],"permalink":"https:\/\/www.threatcrowd.org\/ip.php?ip=188.40.75.132"}

{"response_code":"1","hashes":["321c1d36c16833477ada58ccfa012c6e","ec83d8379140396c8a18368af9d18421","38e0e7d95ef07f6ae514b1c883884c9b","c3f8b1ce2f9dc658e4a9ff198aabeb52","37aacb043222f814ef5013ab2bd6d820","9c6c697f4fbe5cc3c5c8900cbb390ed1","261a336ac5f9ffd6b6f6629d71c694d7","27d74947440dfcc91cb48dd2caa97375","56e11c88636ae745bc5b494a3ed10c21","4c1ad55784314eaa686e7f356b176e44","93cc00543b369a24c4db031b0411c65a","1e728ba8947b8913807562ff7f010a1f","2b88f6504fd54bbc454031f255a97cdf","169288437888fe819abeb0499e58ec22","f8a370de9233d27fed89ce7a7f7a03d1","6622918d92a44e67175f7aeb3fcb5a05","a5f60f1fa6e80fdbe82eff51c1245460","9962800c103eee89d140de26c3ee20e6","69b7c08a2e149ceb4f6ff9bd61f14290","b5697ceba684362b82a8f4cbcf3ab201","7c6722e3d52a578a080ac35de81c2e8e","2782c6cca0fad33d896feef4ec92f24b","dc78d92d10b486db9b610920959107e1","1c87f3704911d94d89fcf4f4c05c1897","1abbd53263fffaa8d97ccc67f5b3dea1","876f24c4102a4e911ab77ee328643dd2","5aa8efccaf6955e6949977a96c2cb0c2","64590646ab74325ee2ad480ef5a18307","642b12cdda124e1f70b548d126600f98","d9ab2b14e9b2f1d78c117fdb1bf0601e","637c9cd17fc8f42910d536b46ed3b445","2743b6bece1c5b6c30747da080c26673","3745095be9859492fc9975c66192310d","be2fd18964ad1e550d4c5f33bb6d0766","27b2ef2fa1c46239b7da08e61533d3c9","cc7b091b94c4f0641b180417b017fec2","405386b0fd12bc0defc9e4e4f4d2ad05","1ed0137d6b78f00f2ed3945d84d626aa","0bf5e206b4058887633ad8a3e7e0bdea","ef9d8cd06de03bd5f07b01c1cce9761f","c2fd460d5734dac2baf533576804c85e","fa816236701d93b09ea9e883b449fa33","62898b77bd9e8e286d6bc760f3e28981","4f92b6c9c55142ee562e8237ce1436a2","917a31528c38e0cec2a3e10210235625","01b16dff4a49a1f368c547e3a7bed9ce","dc9207ad7e0d1678e96c89ac1bf19354","22201573c8831f01293c611f8d851bf1","46869e9c38f8b6a9517b41d7378399b9","c557b6dc0edab783781fd9312f6886c3"],"references":[],"permalink":"https:\/\/www.threatcrowd.org\/listMalware.php?antivirus=plugx"}


''' 