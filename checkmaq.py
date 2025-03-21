import argparse
import ldap3
import sys

def main():
    parser = argparse.ArgumentParser(description="Check ms-DS-MachineAccountQuota for a domain.")

    parser.add_argument('-u', '--username', required=True, help='Username (without domain)')
    parser.add_argument('-p', '--password', required=True, help='Password')
    parser.add_argument('-d', '--domain', required=True, help='Domain (e.g., acme.local)')
    parser.add_argument('-dn', '--distinguished-name', required=True, help='Target Distinguished Name (e.g., DC=acme,DC=local)')

    args = parser.parse_args()

    user = f"{args.domain}\\{args.username}"
    server = ldap3.Server(args.domain)

    try:
        connection = ldap3.Connection(server=server, user=user, password=args.password, authentication=ldap3.NTLM)
        if not connection.bind():
            print("[!] Failed to bind to LDAP server.")
            print(connection.result)
            sys.exit(1)

        connection.search(args.distinguished_name, "(objectClass=*)", attributes=['ms-DS-MachineAccountQuota'])
        if connection.entries:
            print("[+] ms-DS-MachineAccountQuota:", connection.entries[0]['ms-DS-MachineAccountQuota'])
        else:
            print("[-] No entries found.")

    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
