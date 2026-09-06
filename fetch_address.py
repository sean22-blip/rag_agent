 
from uagents import Agent
import asyncio
loop = asyncio.new_event_loop();
asyncio.set_event_loop(loop);
 
agent = Agent(name="omnitrix", seed="3442", port=8000, endpoint=["http://127.0.0.1:8000/submit"])
 
print("Fetch network address", agent.wallet.address());

if __name__ == "__main__":
    agent.run()
    # Check balance (if the library supports it)