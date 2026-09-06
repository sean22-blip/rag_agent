from uagents import Agent
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);
 
# Create an agent named Alice
alice = Agent(name="omnitrix", seed="ben tennyson", port=8000, endpoint=["http://localhost:8000/submit"])
 
# Define a periodic task for Alice
@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f' {alice.name} at your service' )
 
 
# Run the agent
if __name__ == "__main__":
    alice.run()