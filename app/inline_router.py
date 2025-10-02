from aiogram import Router, F
from aiogram.types import InlineQueryResult, InlineQueryResultArticle, InlineQuery, InputTextMessageContent
from utils import keyboards as kbs
from database import dataUtil as db
inline_router = Router()


@inline_router.inline_query(F.query.startswith("https://t.me/nft"))
async def main_SenderNFT(query: InlineQuery):
    data = query.query
    if data:
        nft_name = data.replace('-', ' #').replace('https://t.me/nft/', '')
        name, link, nft_uid, from_user = await db.register_nft(nft_Link=data, from_user=query.from_user.id)

        results = [
            InlineQueryResultArticle(
                id=str(query.from_user.id),
                title=f"🎁 Send {nft_name}",
                input_message_content=InputTextMessageContent(
                    message_text=(
                        f"✨🎁 Вам передают подарок: "
                        f"<a href=\"{data}\">{nft_name}</a>\n\n"
                        f"Нажмите на кнопку ниже, <b>чтобы получить его.</b>"
                    ),
                    parse_mode="HTML"
                ),
                reply_markup=await kbs.format_nftBtn(uid=nft_uid, name=nft_name)
            )
        ]

        return await query.answer(results, cache_time=2)
    return None
