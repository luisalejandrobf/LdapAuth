from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SUBTREE

# Define LDAP server information
ldap_server = 'javedir.javeriana.edu.co'
ldap_port = 389
bind_dn = 'uid=soter,ou=pseudoAccounts,o=javeriana.edu.co,o=edu'
bind_password = 's1meXhwdJiEj10A'
group_dn = 'cn=ingenieriasistemas.todos,ou=groups,o=javeriana.edu.co,o=edu'

# Establish connection with LDAP server
server = Server(ldap_server, port=ldap_port, get_info=ALL)
conn = Connection(server, user=bind_dn, password=bind_password, authentication=SIMPLE, auto_bind=True)

# Search for all members of the specified group
conn.search(search_base=group_dn,
            search_filter='(objectClass=*)',
            search_scope=SUBTREE,
            attributes=['*'])

if len(conn.entries) > 0:
    print("Members of the group:")
    for entry in conn.entries:
        print(entry)
else:
    print(f"No members found for the group {group_dn}")

# Close the connection
conn.unbind()
