from uagents import Agent, Context, Protocol
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);

agent = Agent(
    name='alice',
    port=8000,
    seed='register alice',
    endpoint=["http://127.0.0.1:8000/submit"],#alice will be listening at this end point 
)
@agent.on_interval(period=3) #async timer that tell the agent to execute the below function every 3 seconds
async def hi(ctx: Context):
    ctx.logger.info(f"Hello There :)")
agent.run()