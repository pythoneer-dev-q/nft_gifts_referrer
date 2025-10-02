from motor.motor_asyncio import AsyncIOMotorClient
from uuid import uuid4

DataBase = AsyncIOMotorClient('127.0.0.1', 27017) #думаю можно догадаться зайти на mongodb.org и скачать оттуда датабейс сервер

DB = DataBase["CloudMamont"]
NFT_DB = DB["TRANSFERS"]
USERS_DB = DB["USERS"]
async def init():
    await NFT_DB.create_index(('uid', 1), ('nft', 1))
    await USERS_DB.create_index(('user_id', 1))
    print('database initialized. 200, status: OK.')
    return None


async def register_user(user_id: int):
    reg_doc = {
        'user_id': user_id,
        'nfts': [

        ]
    }
    try:
        await USERS_DB.insert_one(reg_doc)
        return reg_doc['user_id']
    except Exception as e:
        print(f'database: 26: err {e}')
        return None
async def search_user(user_id: int):
    user = await USERS_DB.find_one({'user_id': user_id}, projection={'_id': False})
    if user is not None:
        return user
    else:
        return await register_user(user_id)
async def search_nftPlusAndDelete(uid: str, user_id: int):
    data = await NFT_DB.find_one_and_delete({'uid': uid}, projection={'_id': False})
    if data is not None:
        await USERS_DB.update_one({'user_id': user_id},
                                  {'$push': {'nfts': f'{data['name']}'}})
        return data['name'], data['link'], uid
    else:
        return None, None, None
async def search_nft(uid: str):
    data = await NFT_DB.find_one({'uid': uid}, projection={'_id': False})
    if data is not None:
        return data['name'], data['link'], uid, data['from_user']
    else:
        return None, None, None, None
    
async def search_nftByName(name: str):
    data = await NFT_DB.find_one({'name': name}, projection={'_id': False})
    if data is not None:
        return data['name'], data['link'], data['uid']
    else:
        return None, None, None
    
async def register_nft(nft_Link: str, from_user: int):
    nft_name = nft_Link.replace('https://t.me/nft/', '')
    name, link, uid = await search_nftByName(name=nft_name)

    if name is not None:
        return name, link, uid, None
    else:
        nft_uuid = f'{uuid4()}'
        reg_nftDoc = {
            'name': nft_name,
            'link': nft_Link,
            'uid': nft_uuid[:10],
            'from_user': from_user,
            'status': 1
        }
        try:
            await NFT_DB.insert_one(reg_nftDoc)
            return reg_nftDoc['name'], reg_nftDoc['link'], reg_nftDoc['uid'], reg_nftDoc['from_user']
        except Exception as e:
            print(f'database: 43: err {e}')
            return None, None, None, None