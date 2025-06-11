import requests
import time
from colorama import init, Fore, Style
import pyfiglet
import os

init(autoreset=True)

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    ascii_banner = pyfiglet.figlet_format("Pixelith")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "💡 IP / Domain Bilgi Aracı - By Salih\n")

def bilgi_goster(data):
    print(Fore.GREEN + "[✓] IP Adresi     : " + Fore.WHITE + str(data.get("ip")))
    print(Fore.GREEN + "[✓] Hostname      : " + Fore.WHITE + str(data.get("hostname", "-")))
    print(Fore.GREEN + "[✓] Ülke          : " + Fore.WHITE + f"{data.get('country')} ({data.get('country_code')})")
    print(Fore.GREEN + "[✓] Şehir         : " + Fore.WHITE + str(data.get("city")))
    print(Fore.GREEN + "[✓] Kıta          : " + Fore.WHITE + str(data.get("continent")))
    print(Fore.GREEN + "[✓] Zaman Dilimi  : " + Fore.WHITE + str(data.get("timezone", {}).get("id")))
    print(Fore.GREEN + "[✓] Koordinatlar  : " + Fore.WHITE + f"{data.get('latitude')}, {data.get('longitude')}")
    print(Fore.GREEN + "[✓] ISP           : " + Fore.WHITE + str(data.get("connection", {}).get("isp")))
    print(Fore.GREEN + "[✓] VPN / Proxy   : " + Fore.WHITE + str(data.get("security", {}).get("vpn")))

def sorgula(adres):
    print(Fore.CYAN + f"\n[*] '{adres}' için sorgulama başlatılıyor...\n")
    time.sleep(1)
    try:
        response = requests.get(f"https://ipwho.is/{adres}")
        data = response.json()

        if not data.get("success", False):
            print(Fore.RED + f"[!] Hata: {data.get('message', 'Bilinmeyen hata')}")
            return

        bilgi_goster(data)
    except Exception as e:
        print(Fore.RED + f"[!] Hata oluştu: {e}")

if __name__ == "__main__":
    while True:
        temizle()
        banner()
        hedef = input(Fore.YELLOW + "🎯 IP, domain veya özel adres girin (örnek: 8.8.8.8, google.com): " + Fore.CYAN)
        if hedef.strip() == "":
            print(Fore.RED + "[!] Lütfen geçerli bir giriş yapın!")
            time.sleep(1)
            continue
        sorgula(hedef)
        input(Fore.YELLOW + "\nDevam etmek için ENTER'a basın...")
