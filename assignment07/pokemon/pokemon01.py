import aiofiles
import asyncio
import json

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonapi'

async def main():
    async with aiofiles.open(f"{pokemonapi_directory}/articuno.json",mode='r')as f:
        contents = await f.read()
    

    pokemon = json.loads(contents)
    print(pokemon['name'])

asyncio.run(main())