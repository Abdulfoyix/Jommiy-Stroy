from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from aiogram.types import \
    InlineKeyboardMarkup, \
    InlineKeyboardButton, \
    CallbackQuery, \
    InputFile, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Regexp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
API_TOKEN = '5362182250:AAHhw8o783gHYgvyYNgwLSgESAY68ib6h6g'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


phonefiltr = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
class Info(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    phone=State()



@dp.message_handler(commands=["aloqa"])
async def aloqaadmin(message:types.Message):
    await message.answer("Admin @Abdulfoyix777")

xaridlar = """@knaufgipsokarton  +99899 8022138  +99890 9339395"""
@dp.message_handler(commands=["xarid"])
async def xaridadmin(message:types.Message):
    await message.answer("ismingizni kiriting")
    await Info.name.set()



@dp.message_handler(state=Info.name)
async def Xaridlar(mess:Message,state:FSMContext):
    name=mess.text
    await state.update_data(name=name)
    await  mess.answer("Yoshingizni kiriting")
    await Info.next()


@dp.message_handler(state=Info.age)
async def Xaridlar(mess:Message,state:FSMContext):
    age=mess.text
    await state.update_data(age=age)
    await  mess.answer("No'merizni kiriting")
    await Info.next()



@dp.message_handler(Regexp(phonefiltr),state=Info.phone)
async def Xaridlar(mess:Message,state:FSMContext):
    phone=mess.text
    await state.update_data(phone=phone)
    data=await state.get_data()
    name=data.get("name")
    age=data.get("age")
    phone=data.get("phone")
    message=f"Siznin ma'lumotlaringiz\n{name,age,phone}"
    await mess.answer(message)
    await state.finish()


@dp.message_handler(state=[Info.name,Info.age,Info.phone])
async def xaridadmin(message:types.Message):
    await message.answer("Noto'g'ri buyrug'")













@dp.message_handler(commands=['start'])
async def start(mess:types.Message):
    await mess.answer("Bosh menu",reply_markup=Reply_keyboard)




Reply_keyboard=ReplyKeyboardMarkup(
   keyboard=[
        [
            KeyboardButton(text="????Xo'jalik Mollari"),
            KeyboardButton(text="Uy Jihozlari"),
            KeyboardButton(text="???Qurilish insturmenlari")
        ],
        [
            KeyboardButton(text="????Lokatsiya"),
            KeyboardButton(text="????Dostafka")
        ],

    ]

)



@dp.message_handler(text="????Lokatsiya")
async def Lokatsiya(mess:types.Message):

    # await call.message.answer(reply_markup=Inline_keyboard)
    await mess.answer_location(latitude=41.35543973944746,longitude=69.24234055316249)


@dp.message_handler(text="????Dostafka")
async def dostafkahandler(mess:types.Message):
    id="+99899 8022138"
    await mess.answer_contact(id,first_name="Jomiy 17-18 Magazin")


@dp.message_handler(text="Orqaga")
async def orqgahandler(mess:types.Message):
    await mess.delete()
    await mess.answer("orqaga qaytish",reply_markup=Reply_keyboard)


@dp.message_handler(text="back")
async def backhandler(mess:types.Message):
    await mess.answer("back",reply_markup=Reaply_keyboard)


@dp.message_handler(text="Keyingi Sahifa")
async def Keyngibutton(mess:types.Message):
    await mess.answer("Keyngi sahifa",reply_markup=repltykeyboard)


#ReaplayKeyboard
Reaply_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Knauf gipskarton"),
            KeyboardButton(text="Azia gipskarton"),
            KeyboardButton(text="Knauf rotband"),
            KeyboardButton(text="Penopleks Komfort"),
            KeyboardButton(text="Basat wool")
        ],
        [
            KeyboardButton(text="???????????? ??????????????????????") ,
            KeyboardButton(text="?????????????????? ??????????????????"),
            KeyboardButton(text="???????????????? Monolith"),
            KeyboardButton(text="???????????????? ???????? "),
            KeyboardButton(text="MAPEI FUGA ")
        ],
        [
            KeyboardButton(text="A?????????????????? ?????????? "),
            KeyboardButton(text="??????????????????????????????  ????????????"),
            KeyboardButton(text=" Hammer ????????????"),
            KeyboardButton(text="?????? ??????????"),
            KeyboardButton(text="Drenaj membrana")
        ],
        [
            KeyboardButton(text="Orqaga"),
            KeyboardButton(text="Keyingi Sahifa")
        ]

        ],
    resize_keyboard=True

)

repltykeyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="?????????? ??????????????"),
            KeyboardButton(text="SOMAFIX"),
            KeyboardButton(text="ELEKTROD"),
            KeyboardButton(text="Knauf Insulation"),
            KeyboardButton(text="??????????????????????")

        ],
        [
            KeyboardButton(text="B-PLAST "),
            KeyboardButton(text="??????????"),
            KeyboardButton(text="???????????????????? ???????????? "),
            KeyboardButton(text="VERO"),
            KeyboardButton(text="VENTUM")
        ],
        [
            KeyboardButton(text="POLIKOR"),
            KeyboardButton(text="PROPAN BALLON"),
            KeyboardButton(text="back"),
            KeyboardButton(text="???????????????? ?? ????????????"),
            KeyboardButton(text="?????????????????????? VERO")

        ]

    ],
    resize_keyboard=True
)





#Reaply rasmlar
@dp.message_handler(text="Knauf gipskarton")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1368"
    await mess.answer_photo(url,caption="KNAUF ???????????????? - 12,5 ????"
                                        "??????????- 42 800 ?????? ")

@dp.message_handler(text="Azia gipskarton")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1632"
    await mess.answer_photo(url,caption="AZIA Gipsokartonlari / AZIA ?????????????????????? "
                                        "??????????- 39 000 ?????? ")


@dp.message_handler(text="Knauf rotband")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1369"
    await mess.answer_photo(url,caption="KNAUF ROTBAND"
                                        "??????????:  35 000 ??????")


@dp.message_handler(text="Penopleks Komfort")
async def knn(mess:types.Message):
    url="https://t.me/Dunyabunya_prays/37"
    await mess.answer_photo(url,caption="PENOPLEX Komfort 2sm (20)  14 700 ??????\n"
                                        "PENOPLEX Komfort 3sm (13)  20 900 c????\n"
                                        "PENOPLEX Komfort 4sm (10)  27 800 ??????\n"
                                        "PENOPLEX Komfort 5sm (8)     33 800 ??????\n"
                                        "PENOPLEX 1185*588 3sm STENA  21 100 c????\n"
                                        "PENOPLEX 1185*588 5sm FUNDAMENT  41 600 c????")



@dp.message_handler(text="???????????? ??????????????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1681"
    await mess.answer_photo(url,caption="???????????? ?????????????????????????? ????????\n"
                                        "?????????????? ?????????? (????????????????) ?????????????? ???????????? !\n"
                                        "?????????????? : 25.05.2022 ???? ????????\n")



@dp.message_handler(text="?????????????????? ??????????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1679"
    await mess.answer_photo(url,caption="TERMOTECH XPS - ?????????????????????????? ?????????????????? / PenoplastND\n"
                                        "?????????????? : 24.05.2022 ???? ????????")



@dp.message_handler(text="???????????????? Monolith")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1656"
    await mess.answer_photo(url,caption="MONOLITH MP-3 PROM 2,8 -   21500 ??????\n"
                                        "MONOLITH MP-3 PROM 4,0 -   21500 ??????\n"
                                        "MONOLITH MP-3 PROM 4,0 -   21500 ??????\n"
                                        "MONOLITH MP-3 PROM 4,0 -   21500 ??????\n"
                                        "Elektrod bolshoy most 2.5 J421 -    1,85 $\n"
                                        "Elektrod bolshoy most 3.2 J421 -    1,75 $\n"
                                        "Elektrod bolshoy most 4.0 J421 -    1,75 $")




@dp.message_handler(text="Basat wool")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1662"
    await mess.answer_photo(url,caption="BASALT WOOL !\n"
                                        "?????????????? ?????????? (????????????????) ?????????????? ???????????? !\n"
                                        "?????????????? : 19.05.2022 ???? ????????\n")



@dp.message_handler(text="???????????????? ????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1655"
    await mess.answer_photo(url,caption="???????????????? ???????? ???????? Made in China\n"
                                        "?????????????? ?????????? (????????????????) ?????????????? ???????????? !\n")



@dp.message_handler(text="MAPEI FUGA")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1654"
    await mess.answer_photo(url,caption="Keracolor - Ultracolor\n"
                                        "?????????????? ?????????? (????????????????) ?????????????? ???????????? !\n"
                                         "?????????????? : 16.05.2022 ???? ????????")



@dp.message_handler(text="A?????????????????? ??????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1653"
    await mess.answer_photo(url,caption="Keracolor - Ultracolor\n"
                                        "?????????? ???????? ?????????? / ???????? ??????????????????\n")


@dp.message_handler(text="A?????????????????? ??????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1652"
    await mess.answer_photo(url,caption="?????????????????????????????? ?????????????????? ???????????? ??Antipas?? (22.5????) ???? ???????????????? dunyabunya  \n"
                                        "??????????:  35$    10+ \n"
                                        "????????:      37$ ")



@dp.message_handler(text="?????? ??????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1651"
    await mess.answer_photo(url,caption="?????? ?????????? -  ?????????? ???????????????? ????????????!  (bur zver) \n"
                                        "6 ???? - 32 ???? ????????\n")




@dp.message_handler(text="Drenaj membrana")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1650"
    await mess.answer_photo(url,caption="?????????????????? ?????????????????????????????? ????????????????Drenaj membrana \n"
                                        "15.000 ??????  (??????????)\n"
                                        "16.000 ?????? (??????????????????)")



@dp.message_handler(text="??????????????????????????????  ????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1652"
    await mess.answer_photo(url,caption="?????????????????? ?????????????????????????????? ????????????????Drenaj membrana \n"
                                        "??????????:  35$    10+ \n"
                                        "????????:      37$ ")



@dp.message_handler(text="Hammer ????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1658"
    await mess.answer_photo(url,caption="Optima Hammer ????????????\n"
                                        "?????????? : 8.5 $\n"
                                        " ???????? : 9 $")



#2Bo'limga kiritildi

@dp.message_handler(text="?????????? ??????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1647"
    await mess.answer_photo(url,caption="????????:    6 000  ??????\n"
                                        "??????O???????? 100 ?????????? +\n"
                                        " 5 900 ??????")


@dp.message_handler(text="SOMAFIX")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1645"
    await mess.answer_photo(url,caption="SOMAFIX - ???????????? ???????????? S171\n"
                                        "??????????:  1.95$   (?????????? -5 % ????????????)\n"
                                        "Made in Turkey ????????")


@dp.message_handler(text="ELEKTROD")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1643"
    await mess.answer_photo(url,caption="ELEKTROD  J421 / ?????????????? J421   MP-3C\n"
                                        "????-3 ?? J 421 2.5 ????????????\n"
                                        "????-3 ?? J 421 3.2 ????????????\n"
                                        "????-3 ?? J 421 4.0 ????????????\n"
                                        "???????????????? ???????????????? ?????????????????????? ????????????")


@dp.message_handler(text="Knauf Insulation")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1642"
    await mess.answer_photo(url,caption="Knauf Insulation TR 044  - ?????????? (16,6 ????.??) \n"
                                        " 24 $        (????????)\n"
                                        "23,75 $  (??????????)\n"
                                        "Bizda Yetkazib Berish Xizmatlari Mavjud")


@dp.message_handler(text="??????????????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1641"
    await mess.answer_photo(url,caption="?????????????????????? / ???????????????? ??????????  (Serpyanka) \n"
                                        " ??????????:   5000 ?????? 1 ????.??\n"
                                        "????????????: 70 ??????????  ????.??\n"
                                        "Bizda Yetkazib Berish Xizmatlari Mavjud")


@dp.message_handler(text="B-PLAST")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1639"
    await mess.answer_photo(url,caption="B-PLAST  PENOPLAST / ?????????????????? \n"
                                        " O'lchamlar / ??????????????\n"
                                        " 2/3/4/5 SM\n"
                                        "BLOK OPTOM =   25$\n"
                                        "DONA =                26$")


@dp.message_handler(text="?????????? ????????????????????")
async def knn(mess:types.Message):
    url="https://t.me/JomiyStroy/1638"
    await mess.answer_photo(url,caption="?????????? ???????????????????? / quyoshdan soya qiluvchi setka\n"
                                        " Eniga:     4 metr /  6 metr\n"
                                        " Uzunligi  50m  / 100m\n"
                                        "\n"
                                        "DONA =                26$")







# @dp.callback_query_handler(text="Qurilish")
# async def Lokatsiya(call:CallbackQuery):
#     # await call.message.delete_reply_markup()
#     await call.message.answer(reply_markup=Reaply_keyboard)


@dp.message_handler(text="???Qurilish insturmenlari")
async def Qurilishhandler(mess:types.Message):
    await mess.answer("Qurilish Bo'limi",reply_markup=Reaply_keyboard)






#
# @dp.message_handler(text="Orqaga")
# async def back(message: types.Message):
#     await message.answer("Bosh menu", reply_markup=Inline_keyboard)




stroy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gips", callback_data="gips"),
            InlineKeyboardButton(text="Sement", callback_data="sement")
        ],
        [
            InlineKeyboardButton(text="Kraska", callback_data="kraska"),
            InlineKeyboardButton(text="Truba", callback_data="truba"),
            InlineKeyboardButton(text="Mix", callback_data='mix')
        ],
        [
            InlineKeyboardButton(text="Armatura", callback_data="armatura")
        ]
    ]
)






@dp.inline_handler()
async def inlinQueryAricle(query:types.InlineQuery):
    await query.answer(results=
                       [
                           types.InlineQueryResultArticle(
                           id="QM",
                           title="Qurilish Mollari do'koni",
                           input_message_content=types.InputTextMessageContent(
                               message_text="Ro'yxatimiz:\n"
                                            "mix gips\n"
                                            "sement\n"
                                            "karton"
                           ),
                           url="https://t.me/JomiyStroy",
                           description="Bu bizning bozor",
                           thumb_url="https://antimon.gov.uz/wp-content/uploads/2020/07/cement.jpg",
                           reply_markup=stroy_keyboard
                            ),
                           types.InlineQueryResultVideo(
                               id="vid1",
                               title="Stroy bozorimiz",
                               video_url="https://t.me/JomiyStroy/1221",
                               thumb_url="https://antimon.gov.uz/wp-content/uploads/2020/07/cement.jpg",
                               mime_type="video/mp4"
                           )
                       ]
    )







@dp.message_handler()
async def echo(message: types.Message):
    # old style:
   # await bot.send_message(message.chat.id, message.text)

   await message.answer("Bu buyruq hozircha mavjud emas!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)