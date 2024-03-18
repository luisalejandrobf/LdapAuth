from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SUBTREE
import getpass

# Define LDAP server information
ldap_server = 'javedir.javeriana.edu.co' # Servidor produccion: javedir.javeriana.edu.co
ldap_port = 389
bind_dn = 'uid=soter,ou=pseudoAccounts,o=javeriana.edu.co,o=edu' # Verificar bind DN
bind_password = 's1meXhwdJiEj10A'
group_dn = 'cn=ingenieriasistemas.todos,ou=groups,o=javeriana.edu.co,o=edu'

# Establish connection with LDAP server
server = Server(ldap_server, port=ldap_port, get_info=ALL)
conn = Connection(server, user=bind_dn, password=bind_password, authentication=SIMPLE, auto_bind=True)

# Request username and password via console
username = input("Enter the username of the user: ")
password = input("Enter the user's password: ")

# Try to authenticate the user
user_dn = f'uid={username},ou=people,o=javeriana.edu.co,o=edu'
try:
    conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
    print(f"Authentication successful for user {username}")

    # Check group membership
    conn.search(search_base=group_dn,
                search_filter=f'(&(objectClass=groupOfNames)(member={user_dn}))',
                search_scope=SUBTREE,
                attributes=['cn'])

    if len(conn.entries) > 0:
        print(f"{username} is a member of the group {conn.entries[0].cn}")
    else:
        print(f"{username} is not a member of the group {group_dn}")

except Exception as e:
    print(f"Authentication error for user {username}: {e}")

# Close the connection
conn.unbind()
