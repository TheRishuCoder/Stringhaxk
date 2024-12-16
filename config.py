# TEAM RISHU ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20948838"
    API_HASH = "0d81af6bc752fd069824375a9d668839"
    
    TOKEN = os.environ.get("TOKEN","6956731651:AAGt_HkoQFhhnuyx3P6srgirrweSSQi6ltA")
    MONGO_URL = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://envs.sh/kU9.jpg"
    SUDOERS = filters.user(["5738579437"])
