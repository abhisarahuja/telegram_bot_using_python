import telegram.ext 

def start(update, context):
    update.message.reply_text("Hello! Welcome to Simplilearn")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> Simplilearn offers various courses free of course through Skillup by Simplilearn
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)
    
def content(update, context):
    update.message.reply_text("We have various playlists and articles available!")

def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/Tm5u97I7OrM")

def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/pFq1pgli0OQ")
    
def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/i6AZdFxTK9I")
    
def Skillup(update, context):
    update.message.reply_text("tutorial link : https://www.simplilearn.com/?&utm_source=google&utm_medium=cpc&utm_term=%2Bwww%20%2Bsimplilearn%20%2Bcom&utm_content=803350713-40537012023-467574577661&utm_device=c&utm_campaign=Search-Brand-Broad-IN-AllDevice-adgroup-brand-navigation&gclid=Cj0KCQjw0oyYBhDGARIsAMZEuMv5mA9EysZZ5NfhK65Cb5OU0Q0TVC4con6DQzHF502-dfgA7QQFCgQaAu5sEALw_wcB")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = ("Paste your Telegram bot token here")
#print(bot.get_me())
updater = telegram.ext.Updater("Paste your Telegram bot token here", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('content',content))
disp.add_handler(telegram.ext.CommandHandler('Python',Python))
disp.add_handler(telegram.ext.CommandHandler('SQL',SQL))
disp.add_handler(telegram.ext.CommandHandler('Java',Java))
disp.add_handler(telegram.ext.CommandHandler('Skillup',Skillup))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
