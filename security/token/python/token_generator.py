"""

This construction allows you to demo code using a preset example
you can use this code directly with:

    from token_generator import sign_url

For general use,
Example URL:
/path/to/protect?stime=20081201060100&etime=20151201060100

Where stime= is the start time, and etime is the end time
(both following yyyymmddHHMMSS format)

Please *note*: for SS authentication, the `stime' and `etime'
arguments in the query string are mandatory as part of the
resource specifier.

Tokens optionally support the use of 'ip' parameter, e.g.:
/path/to/protect?stime=20081201060100&etime=20151201060100&ip=10.0.0.5

"""

import hashlib
import hmac
import argparse

parser = argparse.ArgumentParser(prog="token_generator.py",
    description='''A sample token authentication app for Python''')
parser.add_argument('-u', '--url', nargs=1,
    help='URL to parse (path only)', required=True)
parser.add_argument('-k', '--key', nargs=1,
    help='PSK from the portal', required=True)
params = parser.parse_args()

__all__ = ["generate_token", "sign_url"]


def generate_token(resource, secret_key):
    """ Generate the token based on the resource (URL) and the secret key
    taken from the portal. This is based on the first 20 characters of the
    sha1sum of the secret key and the URL
    """
    hmac_builder = hmac.new(secret_key, resource, hashlib.sha1)
    print hmac_builder.hexdigest()
    return "0%s" % (hmac_builder.hexdigest()[:20])

def sign_url(url, secret):
    """ Return the signed URL with the token added as a new queryString argument
    ("encoded").
    """
    token = generate_token(url, secret)
    return url + "&encoded=" + token

signedUrl = sign_url(params.url[0], params.key[0])
print signedUrl
