from uagents import Agent, Bureau, Context, Model, Protocol
from uagents.setup import fund_agent_if_low
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);

# create agents
# alice and bob will support the protocol
# charles will try to reach all agents supporting the protocol
alice = Agent(name="alice", seed="alice recovery phrase", port=8000, endpoint=["http://127.0.0.1:8000/submit"])
#alice seem to not have enough fund
fund_agent_if_low(alice)
bob = Agent(name="bob", seed="bob recovery phrase", port=8001, endpoint=["http://127.0.0.1:8001/submit"])
#bob also seem to not have enough fund
fund_agent_if_low(bob)
charles = Agent(name="charles", seed="charles recovery phrase", port=8002, endpoint=["http://127.0.0.1:8002/submit"])
#charles also seem to not have enough fund
fund_agent_if_low(charles)
print("alice:", alice.wallet.address())
print("bob:", bob.wallet.address())
print("charles:", charles.wallet.address())

class BroadcastExampleRequest(Model):
    pass
class BroadcastExampleResponse(Model):
    text: str

#defining a prototype aka rules
proto = Protocol(name="proto", version='1.0')
proto.on_message(model=BroadcastExampleRequest, replies=BroadcastExampleResponse)
async def handle_request(ctx: Context, sender: str, _msg: BroadcastExampleRequest):
    await ctx.send(
        sender, BroadcastExampleResponse(text=f"Hello from {ctx.agent.name}")
    )

# include protocol
# Note: after the first registration on the almanac smart contract, it will
# take about 5 minutes before the agents can be found through the protocol
alice.include(proto)
bob.include(proto)
 
# let charles send the message to all agents supporting the protocol
@charles.on_interval(period=5)
async def say_hello(ctx: Context):
    status_list = await ctx.broadcast(proto.digest, message=BroadcastExampleRequest())
    ctx.logger.info(f"Trying to contact {len(status_list)} agents.")
 
 
@charles.on_message(model=BroadcastExampleResponse)
async def handle_response(ctx: Context, sender: str, msg: BroadcastExampleResponse):
    ctx.logger.info(f"Received response from {sender}: {msg.text}")

#using Bureau for the agents to be run together at the same time
# Bureau (a group of agents running together)
bureau = Bureau(port=8000, endpoint="https://web.archive.org/web/20250127103831/http://localhost:8000/submit")
bureau.add(alice)
bureau.add(bob)
bureau.add(charles)
 
if __name__ == "__main__":
    bureau.run()
 