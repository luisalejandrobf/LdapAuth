from ldap3 import Server, Connection, SIMPLE, SYNC, ALL

# Define LDAP server information
ldap_server = 'ldap.forumsys.com'
ldap_port = 389
bind_dn = 'cn=read-only-admin,dc=example,dc=com'
bind_password = 'password'

# Establish connection with LDAP server
server = Server(ldap_server, port=ldap_port, get_info=ALL)
conn = Connection(server, user=bind_dn, password=bind_password, authentication=SIMPLE, auto_bind=True)

# Request username and password via console
username = input("Enter the username of the user: ")
password = input("Enter the user's password: ")

# Try to authenticate the user
user_dn = f'uid={username},dc=example,dc=com'
try:
    conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
    print(f"Authentication successful for user {username}")
except Exception as e:
    print(f"Authentication error for user {username}: {e}")

# Close the connection
conn.unbind()


'''
https://www.forumsys.com/2022/05/10/online-ldap-test-server/

LDAP Server Information (read-only access): Server: ldap.forumsys.com   Port: 389 Bind DN: cn=read-only-admin,dc=example,dc=com Bind Password: password

You may also bind to individual Users (uid) or the two Groups (ou) that include: 


All user passwords are password. 


ou=mathematicians,dc=example,dc=com
riemann
gauss
euler
euclid

ou=scientists,dc=example,dc=com
einstein
newton
galieleo
tesla
'''
