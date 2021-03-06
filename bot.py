from discord.ext import commands
import discord
import config
target_guild_id = 712581579351785503
log_channel_id = 712587428426416149


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), **kwargs)
        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(cog, exc))

    async def on_ready(self):
        print('Logged on as {0} (ID: {0.id})'.format(self.user))

    async def log(self, message):
        channel = self.get_channel(log_channel_id)
        await channel.send(message)


bot = Bot()

# write general commands here

if __name__ == '__main__':
    bot.run(config.token)
