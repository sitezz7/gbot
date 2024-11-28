import os
import uuid
import aiohttp
import argparse
from datetime import datetime, timezone
from colorama import *
import random
from aiohttp_socks import ProxyConnector

green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
magenta = Fore.LIGHTMAGENTA_EX
white = Fore.LIGHTWHITE_EX
black = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL
yellow = Fore.LIGHTYELLOW_EX


class Grass:
    def __init__(self, userid, proxy):
        self.userid = userid
        self.proxy = proxy
        self.ses = None
        self.connection_duration = (60 * 60 * 3) + 20  # Set connection duration to 3 hours (10800 seconds)

    def log(self, msg):
        now = datetime.now(tz=timezone.utc).isoformat(" ").split(".")[0]
        print(f"{black}[{now}] {reset}{msg}{reset}")

    @staticmethod
    async def ipinfo(proxy=None):
        async with aiohttp.ClientSession() as client:
            result = await client.get("https://api.ipify.org/", proxy=proxy)
            return await result.text()

    async def start(self):
        max_retry = 10
        retry = 1
        proxy = self.proxy
        if proxy is None:
            proxy = await Grass.ipinfo()
        browser_id = uuid.uuid5(uuid.NAMESPACE_URL, proxy)
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        headers = {
            "Host": "proxy2.wynd.network:4650",
            "Connection": "Upgrade",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": useragent,
            "Upgrade": "websocket",
            "Origin": "chrome-extension://lkbnfiajjmbhnfledhphioinpickokdi",
            "Sec-WebSocket-Version": "13",
            "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        }
        while True:
            try:
                if retry >= max_retry:
                    self.log(f"{yellow}Max retry reached, skipping this proxy!")
                    await self.ses.close()
                    return
                
                self.log(f"{self.userid} is starting to connect to the server...")
                connector = ProxyConnector.from_url(proxy)
                self.ses = aiohttp.ClientSession(connector=connector)
                async with self.ses.ws_connect(
                    "wss://proxy2.wynd.network:4650/",
                    headers=headers,
                    timeout=1000,
                    autoclose=False,
                ) as wss:
                    res = await wss.receive_json()
                    auth_id = res.get("id")
                    if auth_id is None:
                        self.log(f"{red}Auth ID is None")
                        return None
                    auth_data = {
                        "id": auth_id,
                        "origin_action": "AUTH",
                        "result": {
                            "browser_id": browser_id.__str__(),
                            "user_id": self.userid,
                            "user_agent": useragent,
                            "timestamp": int(datetime.now().timestamp()),
                            "device_type": "extension",
                            "version": "4.26.2",
                            "extension_id": "lkbnfiajjmbhnfledhphioinpickokdi",
                        },
                    }
                    await wss.send_json(auth_data)
                    self.log(f"{green}Successfully connected {white}to the server!")
                    retry = 1
                    connection_start_time = datetime.now()
                    while True:
                        if (datetime.now() - connection_start_time).total_seconds() >= self.connection_duration:
                            self.log(f"{yellow}Connection has lasted {self.connection_duration/3600} hours, preparing to reconnect...")
                            break
                        
                        ping_data = {
                            "id": uuid.uuid4().__str__(),
                            "version": "1.0.0",
                            "action": "PING",
                            "data": {},
                        }
                        await wss.send_json(ping_data)
                        self.log(f"{white}Sent {green}ping {white}to the server!")
                        pong_data = {"id": "F3X", "origin_action": "PONG"}
                        await wss.send_json(pong_data)
                        self.log(f"{white}Sent {magenta}pong {white}to the server!")
                        await countdown(120)
            except KeyboardInterrupt:
                await self.ses.close()
                exit()
            except Exception as e:
                self.log(f"{red}Error: {white}{e}")
                retry += 1
                if retry >= max_retry:
                    self.log(f"{yellow}Max retry reached, skipping this proxy!")
                    await self.ses.close()
                    return
                continue


async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"Waiting for {hour}:{minute}:{seconds} ", flush=True, end="\r")
        await asyncio.sleep(1)


async def main():
    arg = argparse.ArgumentParser()
    arg.add_argument(
        "--proxy", "-P", default="proxies.txt", help="Custom proxy input file"
    )
    args = arg.parse_args()
    os.system("cls" if os.name == "nt" else "clear")

    print(
        f"""
    {red}Grass Script Season 2 Stable Infinite Multi-open script developed by [Zhixian Says] and open-sourced for free use.
    {red}Continuously updated Web3 projects, welcome to follow.
    {white}GitHub: {green}github.com/zx-meet
    {white}WeChat: {green}caba_9527
    {green}Good luck!!!
          """
    )

    userid = open("userid.txt", "r").read()
    if len(userid) <= 0:
        print(f"{red}Error: {white}Please input your user ID first!")
        exit()
    if not os.path.exists(args.proxy):
        print(f"{red}{args.proxy} not found, please ensure {args.proxy} is available!")
        exit()
    proxies = open(args.proxy, "r").read().splitlines()
    if len(proxies) <= 0:
        proxies = [None]
    
    # Create task list with delays and logging
    tasks = []
    total_proxies = len(proxies)
    
    for index, proxy in enumerate(proxies, 1):
        # Add a random delay of 2-10 seconds for each proxy
        delay = random.uniform(2, 10)
        tasks.append(asyncio.create_task(Grass(userid, proxy).start()))
        print(f"{green}Task {index}/{total_proxies} for the proxy created{reset}")

        if index != total_proxies:
            print(f"{white}Waiting for {green}{delay:.2f} seconds{white} before starting the next proxy task")
            await asyncio.sleep(delay)
        
    print(f"{magenta}All proxy tasks created, starting execution...{reset}")
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        import asyncio
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()
