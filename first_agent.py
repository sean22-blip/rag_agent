from uagents import Agent, Context
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);

omnitrix = Agent(name="alien-force", seed="command function overide code 10", port=8000, endpoint=["http://localhost:8000/submit"])


@omnitrix.on_event("startup") #defining a behavior for this action when it runs
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I am {omnitrix.name} and my address is {omnitrix.address}")

if __name__ == "__main__":
    omnitrix.run()