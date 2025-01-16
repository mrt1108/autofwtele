from telethon import TelegramClient, events

# Thông tin API từ Telegram
API_ID = '23974601'
API_HASH = '7f6db34c8e8dee5ec779d475de5cdf65'
SOURCE_CHAT = -1002125511471  # ID hoặc username của nhóm/gười gửi
TARGET_CHAT = -4692235046  # ID hoặc username của nhóm/người nhận
AUTHORIZED_USER_ID = 6381786315  # ID của người dùng bạn muốn forward (lấy từ Telegram)

# Khởi tạo client
client = TelegramClient('forward_bot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_message(event):
    # Lấy thông tin người gửi
    sender = await event.get_sender()
    if sender.id == AUTHORIZED_USER_ID:  # Chỉ xử lý tin nhắn từ người được chỉ định
        # Kiểm tra loại tin nhắn
        if event.text:  # Nếu là tin nhắn văn bản
            await client.send_message(TARGET_CHAT, event.text)
        elif event.media:  # Nếu là tin nhắn có media (hình ảnh, video, file, v.v.)
            await client.send_file(TARGET_CHAT, event.media, caption=event.message.message)
print("Bot đang chạy...")
client.start()
client.run_until_disconnected()
