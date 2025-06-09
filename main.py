from fastapi import FastAPI
import root
#import items

app = FastAPI()

# Include routes from other files (modular structure)
app.include_router(root.router)
#app.include_router(items.router)