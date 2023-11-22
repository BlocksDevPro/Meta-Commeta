import config
import traceback
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import channel
from pyrogram.handlers import MessageHandler


async def channelPostHandler(client: Client, message: Message):
    try:
        chatId, messageId = message.chat.id, message.id

        discussionGroupMessage = await client.get_discussion_message(chatId, messageId)
        if discussionGroupMessage:
            groupChatId, groupMessageId = discussionGroupMessage.chat.id, discussionGroupMessage.id
            if config.PHOTO_LINK:
                if config.PHOTO_LINK.startswith('https'):
                    return await client.send_photo(groupChatId, config.PHOTO_LINK, config.MESSAGE_TEXT, reply_to_message_id=groupMessageId)
                else:
                    with open(config.PHOTO_LINK, 'rb') as photo:
                        return await client.send_photo(groupChatId, photo, config.MESSAGE_TEXT, reply_to_message_id=groupMessageId)
            else:
                return await client.send_message(groupChatId, config.MESSAGE_TEXT, reply_to_message_id=groupMessageId)
    except:
        traceback.print_exc()


def registerHandlers(client: Client):
    postHandler = MessageHandler(channelPostHandler, channel)
    client.add_handler(postHandler)
    return
