from telethon import TelegramClient

api_id = 12345678
api_hash = 'hash'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    usernames = ['@SPARKICHAT','@liveccbycp', '@cyberpirateschats',
  '@BesTIRCCHECKER', '@cpscr', '@Venexchk', '@mtctechxclan',
  '@FamilyCreditCard', '@cyperDropsReference', '@cyper_public_cc_drops',
  '@ChkBotLand', '@paddilivecc2022', '@MasterLordCC', '@ccs_lives',
  '@SK_LIVE_STRIPE', '@CheckCCRU', '@dailytoolx', '@CRKSOO_CC7', '@SPARKICHAT',
  '@ccxenchat', '@deadcclivechat', '@TeamBlackCard', '@TeamNastyofficial',
  '@blindscrap', '@VegetaScrap', '@BinnersHub', '@botsakuraa', '@ccdrops',
  '@allccscraper ', '@ccxen', '@ccauth', '@rarachk', '@paidchargedcc',
  '@GodsOfTheBins', '@botsakuraa', '@xforce_group8', '@sakura', '@m7_crack',
  '@alivesk', '@ccauth', '@NfPrBroScraper', '@teamnastyscr', '@ccdropperchat',
  '@OzarkScrapper', '@alivesk', '@skkeysdrop', '@rcxchat', '@binlandchecker',
  '@RevyDrops', '@crackingbinz', '@binlandchecker', '@allccscraper', '@ccxen',
  '@skkeysdrop', '@Mrx001_Configs', '@ccdropperchat', '@ccs_drop',
  '@telethon00', 'unkn0wn_drops', '@DrBins_Group', '@Dr_hackerr',
  '@MoroccanBinnersChatbox', '@fsociety_001_1', '@XenpaiScrapper',
  '@liveccbinss', '@sparsh_checker', '@SitesYCCS', '@Blackhat_Hacking_Tools',
  '@CRKSOO_CC', '@tmbinners', '@vscendolsmarket', '@CCBY_VENOM',
  '@RoldexVerse', '@paddi2022', '@ccs_lives', '@ScrapperLost', '@global_Frd',
  'type_xz'
]

    for username in usernames:
        entity = await client.get_entity(username)
        print(f"The ID for {username} is {entity.id}")

with client:
    client.loop.run_until_complete(main())


#if u want add more
