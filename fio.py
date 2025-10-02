import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

API_TOKEN = "8307937674:AAHD6Qach_5O3wtZaQ_TR-cpgLJmkTqNS2U"
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbyPkJVtdp1JsBzBrUBD-NQ-M7OWi0FiWgzZ6kHB_isuEvQBfM6L9hNX7Zpt5y1GXeg/exec"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def get_info(message: Message):
    fio = message.text.strip()
    async with httpx.AsyncClient() as client:
        response = await client.post(WEBAPP_URL, json={"fio": fio})

    try:
        data = response.json()
    except Exception:
        await message.answer(f"⚠️ Ошибка: сервер вернул не JSON\nОтвет: {response.text}")
        return

    if "error" in data:
        await message.answer("❌ Нічого не знайдено")
    else:
        text = (f"ПІБ: {data['F']}\n"
                f"Спеціальність: {data['V']}\n"
                f"Форма навчання: {data['Z']}\n"
                f"Курс: {data['AJ']}\n"
                f"Чи скорочений термін навчання: {data['AD']}")
        await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
