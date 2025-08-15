from fastapi import FastAPI

from fast_car_api.routers import router as car_router

app = FastAPI(
  title='Fast Car API',
  description='PycodeBR modern Car API',
  version='0.1.0',
)

app.include_router(car_router)

@app.get('/')
def read_root():
  return {'status': 'ok'}

@app.get('/cars')
def read_car():
  return {'status': 'cars routes'}

@app.get('/cars/2')
def read_cars():
  return {'status': 'cars routes 2'}