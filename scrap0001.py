# Status Code Check
import bs4
import requests
from colorama import Fore

sites2 = ['google.com/']
#Status Code Check
Status_Code_Check = input(Fore.WHITE + "Would you like to perform a status code check against these subdomains? ")
if Status_Code_Check == "Y" or Status_Code_Check == "y":
    print (Fore.GREEN + "\nChecking subdomains...\n")
    for x in sites2:
        try:
            long_url = 'https://' + x + "/"
            r = requests.get(long_url, timeout=15, allow_redirects=True, verify=False)
            if r.status_code == 200:
                html = bs4.BeautifulSoup(r.text, features="lxml")
                print (Fore.GREEN + x + ' ' + str(r.status_code) + ' ' + html.title.text)
            else:
                print (Fore.PURPLE + x + ' ' + str(r.status_code))
        except:
            print (Fore.RED + 'https://' + x + "/" + ' FAILED')
            continue
    print (Fore.WHITE + "\nSubdomain HTTP status code check has completed.")
elif Status_Code_Check == "N" or Status_Code_Check == "n":
    print("\\n" + Fore.RED + "Status code check not performed. Terminating program.")
else:
    print("\n" + Fore.RED + "Invalid entry, terminating program.")