import platform
import shutil
from colorama import Fore
import requests
import random
from faker import Faker
import time
from modules.__LOG__ import log
from concurrent.futures import ThreadPoolExecutor
import os
from threading import Lock

lock = Lock()  # Create a lock for thread-safe file writing

def __LOGO__():
    logo = """
                         █████╗  ██╗  ██╗ ███╗   ███╗ ███████╗ ██████╗      ███████╗ ███╗   ██╗
                        ██╔══██╗ ██║  ██║ ████╗ ████║ ██╔════╝ ██╔══██╗     ██╔════╝ ████╗  ██║
                        ███████║ ███████║ ██╔████╔██║ █████╗   ██║  ██║     ███████╗ ██╔██╗ ██║
                        ██╔══██║ ██╔══██║ ██║╚██╔╝██║ ██╔══╝   ██║  ██║     ╚════██║ ██║╚██╗██║
                        ██║  ██║ ██║  ██║ ██║ ╚═╝ ██║ ███████╗ ██████╔╝     ███████║ ██║ ╚████║
                        ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚══════╝ ╚═════╝      ╚══════╝ ╚═╝  ╚═══╝
                                                                                   
        [+] https://discord.gg/Q2a3ER7JEx
        [+] Welcome to the Discord Nitro Tool!  
        [+] Ahmed Sn
    """

    width = shutil.get_terminal_size().columns
    lines = logo.split('\n')
    banner = '\n'.join(line.center(width) for line in lines)
    print(Fore.CYAN + banner)

def __NAME__():
    return (Faker().first_name() + Faker().last_name()).lower()

def __CLS__():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def __PROXY__():
    # Set up your proxy here
    proxy = "http://chaudbes-cypher:12828$/@193.827.237.82:3028"
    return {
        "http": proxy,
        "https": proxy
    }

def __UUID__():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://www.chess.com/friends?name=csolver.xyz",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }
    r = requests.get(f"https://www.chess.com/member/{__NAME__()}", headers=headers)
    try:
        uuid = r.text.split('data-user-uuid="')[1].split('"')[0]
        log.info(f"Genning Promo --> {uuid[:15]}...")
        return uuid
    except:
        return None

def __GEN__():
    while True:
        proxies = __PROXY__()
        st = time.time()
        
        uuid = __UUID__()
        if uuid is None:
            continue

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.chess.com",
            "priority": "u=1, i",
            "referer": "https://www.chess.com/play/computer/discord-wumpus?utm_source=partnership&utm_medium=article&utm_campaign=discord2024_bot",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        }
        
        jData = {
            "userUuid": uuid,
            "campaignId": "4daf403e-66eb-11ef-96ab-ad0a069940ce",
        }
        
        try:
            r = requests.post(
                "https://www.chess.com/rpc/chesscom.partnership_offer_codes.v1.PartnershipOfferCodesService/RetrieveOfferCode",
                headers=headers,
                json=jData,
                proxies=proxies,  # Pass the proxies here
                timeout=10  # Optional timeout to handle slow responses
            )
            code = r.json()["codeValue"]
            promo = f'https://promos.discord.gg/{code}'
            log.success(f"Got Promo --> {promo}", round(time.time()-st, 2))
            
            with lock:
                with open('./output/promos.txt', 'a') as f:
                    f.write(f'{promo}\n')
        except Exception as e:
            log.error(f"Error during promo generation: {e}")

def __MAIN__():
    __CLS__()
    __LOGO__()

    # Input validation for number of promos
    while True:
        try:
            promos = int(log.input(f"Promos --> "))
            if promos <= 0:
                print("Please enter a positive integer.")
                continue
            break  # Break the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Run the generator for the specified number of promos
    for _ in range(promos):
        with ThreadPoolExecutor(max_workers=promos) as exc:
            exc.submit(__GEN__)

if __name__ == '__main__':
    __MAIN__()
