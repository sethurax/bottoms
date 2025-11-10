import time
import datetime

import discord as d
from discord.ext import commands as c, tasks


class EventsCog(c.Cog):
    def __init__(self, bot: d.Bot):
        self.bot = bot


    @c.Cog.listener()
    async def on_ready(self):
        print(
            f"Logged in as {self.bot.user} (ID: {self.bot.user.id if self.bot.user.id is not None else 'N/A'})"
        )

        self.reset_claims.start()
        print(f"Daily claim reset task started.")
        print(f"Next reset: {time.strftime('%H:%M:%S', self.reset_claims.next_iteration.utctimetuple())}")

    @c.Cog.listener()
    async def on_application_command(self, ctx: d.ApplicationContext):
        print(
            f"Time: {time.strftime('%H:%M:%S', time.localtime())} | Command: /{ctx.command.qualified_name} | Guild: {ctx.guild.name if ctx.guild else 'DM'} | User: {ctx.author.display_name}"
        )

    @tasks.loop(time = datetime.time(hour=0, minute=0, second=0, microsecond=0))
    async def reset_claims(self):
        print(f"Claims have been reset. Next reset: {time.strftime('%H:%M:%S', self.reset_claims.next_iteration.utctimetuple())}")


def setup(bot: d.Bot):
    bot.add_cog(EventsCog(bot))
