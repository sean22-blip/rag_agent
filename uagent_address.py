 
from uagents import Agent
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);
 
agent = Agent(name="alice", seed="alice recovery phrase", port=8000, endpoint=["http://127.0.0.1:8000/submit"])
 
print("uAgent address: ", agent.address)
 
if __name__ == "__main__":
    agent.run()
 