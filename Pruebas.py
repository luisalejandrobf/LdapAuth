from ldap3 import Server, Connection, ALL, NTLM
ldap_server = 'javedir.javeriana.edu.co'
ldap_port = 636
server = Server(ldap_server, port=ldap_port, use_ssl=True, get_info=ALL)
conn = Connection(server, user="cn=soter,dc=javeriana.edu.co,dc=edu", password='aKcrK%0;8D42W"*', auto_bind=True)
conn.extend.standard.who_am_i()
server.info
