import hashlib
import hmac
import argparse

parser = argparse.ArgumentParser(prog="token_tools.py",
    description='''A sample token authentication app for Python''')
parser.add_argument('-u', '--url', nargs=1,
    help='URL to parse (path only)', required=True)
parser.add_argument('-k', '--key', nargs=1,
    help='PSK from the portal', required=True)
params = parser.parse_args()

__all__ = ["generate_token", "sign_url"]


def generate_token(resource,secret_key):
    hmac_builder = hmac.new(secret_key, resource, hashlib.sha1)
    return "0%s" % (hmac_builder.hexdigest()[:20])

def sign_url(url,secret):
    token=generate_token(url,secret)
    return url + "&encoded=" + token
# Example URL:
# /path/to/protect?stime=20081201060100&etime=20151201060100
# Where stime= is the start time, and etime is the end time
# both following the format yyyymmddHHMMSS 
# 
# Tokens optionally support the use of 'ip'

#url = sign_url('insert url here','insert key from portal here')

url = sign_url(params.url[0], params.key[0])
print url
