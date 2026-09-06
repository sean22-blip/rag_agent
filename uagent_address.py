 
from uagents import Agent
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);
 
agent = Agent(name="alice", seed="omnitrix recovery", port=8000, endpoint=["http://127.0.0.1:8000/submit"])
 
print("uAgent address: ", agent.address) #this determine who the agent is 
print("Fetch network address", agent.wallet.address()); # this determine where our agent fund are stored

if __name__ == "__main__":
    agent.run()
 