def get_status(bigip, url):
    payload = {}
    payload['state'] = 'user-up'
    payload['session'] = 'user-enabled'
    change_node_status = bigip.put(url, json.dumps(payload)).json()
    time.sleep(5)
    node_status = bigip.get(url).json()
    return node_status


def get_token(bigip, url, creds):
    payload = {}
    payload['username'] = creds[0]
    payload['password'] = creds[1]
    payload['loginProviderName'] = 'tmos'

    token = bigip.post(url, json.dumps(payload)).json()['token']['token']
    return token


if __name__ == "__main__":
    import requests, json, argparse, getpass, sys, time
    #import os, requests, json, argparse, getpass
    requests.packages.urllib3.disable_warnings()

    parser = argparse.ArgumentParser(description='[F5-IP] [F5-UserName] [F5-Password] [F5-PoolName] [F5-MemberName] [F5-MemberPort]')

    parser.add_argument("host" )
    parser.add_argument("username")
#parser.add_argument("password")
    parser.add_argument("poolname")
    parser.add_argument("membername")
    parser.add_argument("memberport")
    args = vars(parser.parse_args())

    hostname = args['host']
    username = args['username']
    password = 'tutorAbc123'
    poolname = args['poolname']
    membername = args['membername']
    memberport = args['memberport']


    url_base = 'https://%s/mgmt' %hostname
    url_auth = '%s/shared/authn/login' %url_base
    url_pool = '%s/tm/ltm/pool/%s/members/~Common~%s:%s' % (url_base, poolname, membername, memberport)
    #print '\nURL_Pool: %s\n' %url_pool

    b = requests.session()
    b.headers.update({'Content-Type':'application/json'})
    b.auth = (username, password)
    b.verify = False
    token = get_token(b, url_auth, (username, password))


    b.auth = None
    b.headers.update({'X-F5-Auth-Token': token})

    response = get_status(b, url_pool)
#print '\nnode_status: %s\n' %response

    str1 = '%s' %response
    str2 = "monitor-enabled"
    str3 = "user-disabled"
if str1.find(str2) > 0:
    print str1
else:
    print str1
    sys.exit(-1)

