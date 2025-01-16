import random

from pyrogram import filters
from pyrogram.types import Message

from Dev import app
from Devine.misc import db
from Devine.utils.decorators import AdminRightsCheck
from Devine.utils.inline import close_markup
from configuration import filter_users


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & filters.group & ~filter_users
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
