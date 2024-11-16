from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Store trip data in memory
TRIP_DATA = {
    'destination': 'Paris',
    'start_date': '18/11/24 11am',
    'end_date': '18/11/24 5pm',
    'participants': ['Bora', 'Rose', 'Solene', 'Aya'],
    'stops': ['Marseille']
}

class RoadTripBot:
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /start is issued."""
        welcome_message = (
            "🚗 Welcome to Road Trip Planner Bot! 🗺️\n\n"
            "Available commands:\n"
            "/mytrip - View your trip\n"
            "/expenses - Manage trip expenses\n"
            "/checklist - View/edit trip checklist\n"
            "/help - Show this help message"
        )
        await update.message.reply_text(welcome_message)

    async def view_trip(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View trip details."""
        trip_message = (
            f"🌟 Destination: {TRIP_DATA['destination']}\n"
            f"📅 Start: {TRIP_DATA['start_date']} to {TRIP_DATA['end_date']}\n"
            f"👥 Participants: {', '.join(TRIP_DATA['participants'])}\n"
            f"🛑 Stops: {', '.join(TRIP_DATA['stops'])}\n"
            f"-------------------\n"
        )
        await update.message.reply_text(trip_message)

def main():
    """Start the bot."""
    # Initialize the bot with your token
    app = Application.builder().token('8055519601:AAGpcCKvvcto_ma9S5dubEeYr57MLYW2HNk').build()

    bot = RoadTripBot()

    # Add command handlers
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("mytrip", bot.view_trip))

    # Start the Bot
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()