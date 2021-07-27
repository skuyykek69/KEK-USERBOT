from userbot.events import register
from time import sleep


@register(outgoing=True, pattern='^.fajar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
sleep(1)
await typew.edit("✨")
sleep(3)
await typew.edit("`Hai👋🏼 Perkenalkan Namaku Fajar`")
sleep(3)
await typew.edit("`Umur ku 19 Tahun`")
sleep(1)
await typew.edit("`Tinggal Di Jawa Timur, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
