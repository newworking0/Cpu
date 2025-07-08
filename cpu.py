import telebot
import os
import time
import random
import threading
import platform
import psutil
import datetime

# Bot Token
token = "7535476931:AAH1Q-tszGw87O463Izb73F17pt7YGTzOAM"
bot = telebot.TeleBot(token)

APPROVED_USERS_FILE = "approved_users.txt"
approved_users = []
admins = [7774742430]
owner_id = 7774742430
stop_gali = False

CHANNEL_LINK = "https://t.me/+LfpQeLWVdZUwNjE1"
GROUP_LINK = "https://t.me/+H-oeF5PYBjM3Y2U1"
OWNER_LINK = "https://t.me/REVENGEKING199"

start_time = time.time()

def load_approved_users():
    users = []
    if os.path.exists(APPROVED_USERS_FILE):
        with open(APPROVED_USERS_FILE, "r") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 2:
                    users.append({'id': int(data[0]), 'username': data[1]})
    return users

def save_approved_users():
    with open(APPROVED_USERS_FILE, "w") as f:
        for user in approved_users:
            f.write(f"{user['id']},{user['username']}\n")

approved_users = load_approved_users()

galis = [
    "TARI MAA KI XHUT",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨",
    "Teri maa ki chut me solar panel laga dunga",
    "Tere baap ka lund flipkart pe sale pe daal dunga"
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑮𝑨𝑨𝑵𝑫 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑼𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀??𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑪𝑯𝑨𝑪𝑯𝑰 𝑲A LAND",
]

@bot.message_handler(commands=["ping"])
def ping(message):
    try:
        current_time = time.time()
        uptime = str(datetime.timedelta(seconds=int(current_time - start_time)))

        cpu_percent = "N/A"
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        sysinfo = platform.uname()
        hostname = f"{sysinfo.system} {sysinfo.release} | {sysinfo.node}"

        ram_used = ram.used // (1024 * 1024)
        ram_total = ram.total // (1024 * 1024)
        disk_used = disk.used // (1024 * 1024 * 1024)
        disk_total = disk.total // (1024 * 1024 * 1024)

        bot.reply_to(message,
            f"🏓 <b>Pong!</b>\n"
            f"⏱️ <b>Uptime:</b> <code>{uptime}</code>\n"
            f"🧠 <b>CPU:</b> <code>{cpu_percent}</code>\n"
            f"💾 <b>RAM:</b> <code>{ram_used}MB / {ram_total}MB</code> ({ram.percent}%)\n"
            f"🗂️ <b>Disk:</b> <code>{disk_used}GB / {disk_total}GB</code> ({disk.percent}%)\n"
            f"🖥️ <b>VPS:</b> <code>{hostname}</code>",
            parse_mode="HTML"
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Error in /ping: {e}")

@bot.message_handler(commands=["start"])
def welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"
    name = message.from_user.first_name

    if any(user['id'] == user_id for user in approved_users) or user_id in admins or user_id == owner_id:
        bot.reply_to(message,
            "✨ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙏𝙝𝙚 𝙐𝙡𝙩𝙞𝙢𝙖𝙩𝙚 𝙂𝙖𝙡𝙞 𝘽𝙤𝙩 ✨\n\n"
            "👑 Owner Commands:\n- /admin <user_id>\n- /remove_admin <user_id>\n- /list_admins\n\n"
            "🛡️ Admin Commands:\n- /approve <user_id>\n- /remove <user_id>\n- /remove_all\n- /list_approved\n\n"
            "🔥 User Commands:\n- /fuck <username>\n- /stop\n- /ping")
    else:
        bot.send_message(user_id,
            f"⚠️ To use this bot, follow these steps:\n\n"
            f"1️⃣ Join our Channel 👉 [Join Channel]({CHANNEL_LINK})\n"
            f"2️⃣ Join our Group 👉 [Join Group]({GROUP_LINK})\n"
            f"3️⃣ After joining, send a DM to the owner.\n\n"
            f"👑 Owner: [Click to DM]({OWNER_LINK})\n\n"
            f"⏳ Once approved, you'll be able to use the bot features.",
            parse_mode="Markdown")

        if user_id != owner_id:
            try:
                bot.send_message(owner_id, f"👤 New user started the bot:\n• Name: {name}\n• Username: @{username}\n• ID: `{user_id}`", parse_mode="Markdown")
            except:
                pass

@bot.message_handler(commands=["fuck"])
def send_all_galis(message):
    global stop_gali
    if message.from_user.id not in [u['id'] for u in approved_users] and message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 You are not approved to use this command DM @REVENGEKING199.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /fuck <username>")
        return
    username = parts[1]
    bot.reply_to(message, f"🔥 Starting gali spam for {username}...")

    def spam():
        while not stop_gali:
            random.shuffle(galis)
            for gali in galis:
                if stop_gali:
                    return
                try:
                    bot.send_message(message.chat.id, f"{username} {gali}")
                    time.sleep(0.3)
                except:
                    continue

    stop_gali = False
    for _ in range(3):
        t = threading.Thread(target=spam)
        t.daemon = True
        t.start()

@bot.message_handler(commands=["stop"])
def stop_galis(message):
    global stop_gali
    if message.from_user.id not in [u['id'] for u in approved_users] and message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 You are not approved to use this command DM REVENGEKING199.")
        return
    stop_gali = True
    bot.reply_to(message, "🛑 Stopping all galis...")

@bot.message_handler(commands=["admin"])
def make_admin(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can use this command.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /admin <user_id>")
        return
    try:
        uid = int(parts[1])
        if uid not in admins:
            admins.append(uid)
            bot.reply_to(message, f"✅ User {uid} promoted to admin.")
        else:
            bot.reply_to(message, f"ℹ️ User {uid} is already an admin.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["remove_admin"])
def remove_admin(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can remove admins.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /remove_admin <user_id>")
        return
    try:
        uid = int(parts[1])
        if uid == owner_id:
            bot.reply_to(message, "❌ You can't remove yourself (owner).")
            return
        if uid in admins:
            admins.remove(uid)
            bot.reply_to(message, f"✅ Admin {uid} removed.")
        else:
            bot.reply_to(message, "⚠️ User is not an admin.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["list_admins"])
def list_admins(message):
    if message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only the owner can view admins.")
        return
    if not admins:
        bot.reply_to(message, "📭 No admins found.")
        return
    reply = "👮 Admins:\n"
    for uid in admins:
        try:
            user = bot.get_chat(uid)
            username = f"@{user.username}" if user.username else "NoUsername"
            reply += f"- {uid} ({username})\n"
        except:
            reply += f"- {uid} (Unknown)\n"
    bot.reply_to(message, reply)

@bot.message_handler(commands=["approve"])
def approve_user(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can approve users DM: @REVENGEKING199.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /approve <user_id>")
        return
    try:
        uid = int(parts[1])
        user_obj = bot.get_chat(uid)
        username = user_obj.username or "NoUsername"
        for user in approved_users:
            if user['id'] == uid:
                bot.reply_to(message, "✅ User already approved.")
                return
        approved_users.append({'id': uid, 'username': username})
        save_approved_users()
        bot.reply_to(message, f"✅ Approved user {uid} (@{username})")
    except:
        bot.reply_to(message, "❌ Invalid user ID or user not found.")

@bot.message_handler(commands=["remove"])
def remove_user(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can remove users DM @REVENGEKING199.")
        return
    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "Usage: /remove <user_id>")
        return
    try:
        uid = int(parts[1])
        for user in approved_users:
            if user['id'] == uid:
                approved_users.remove(user)
                save_approved_users()
                bot.reply_to(message, f"❌ Removed user {uid}")
                return
        bot.reply_to(message, "⚠️ User not found.")
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.message_handler(commands=["remove_all"])
def remove_all_users(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can clear approved users DM @REVENGEKING199.")
        return
    approved_users.clear()
    save_approved_users()
    bot.reply_to(message, "🧹 All approved users removed.")

@bot.message_handler(commands=["list_approved"])
def list_approved(message):
    if message.from_user.id not in admins and message.from_user.id != owner_id:
        bot.reply_to(message, "🚫 Only admins can view approved users DM @REVENGEKING199.")
        return
    if not approved_users:
        bot.reply_to(message, "📭 No users are currently approved.")
        return
    reply = "✅ Approved Users:\n"
    for user in approved_users:
        uname = f"@{user['username']}" if user['username'] != "NoUsername" else "NoUsername"
        reply += f"- {user['id']} ({uname})\n"
    bot.reply_to(message, reply)

@bot.message_handler(func=lambda msg: msg.chat.type == 'private')
def notify_owner_on_message(msg):
    if msg.from_user.id != owner_id:
        try:
            bot.send_message(owner_id, f"📩 Message from {msg.from_user.first_name} (@{msg.from_user.username}):\n{msg.text}")
        except:
            pass

print("Bot is running...")
bot.infinity_polling()