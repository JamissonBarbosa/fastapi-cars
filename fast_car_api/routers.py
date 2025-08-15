from fastapi import APIRouter

router = APIRouter(
  prefix = '/api/v1/cars',
  tags = ['cars'],
)

@router.get('/')
def list_cars():
  return {'cars': [
    {'id': 1, 'name': 'Fusca'},
    {'id': 2, 'name': 'Brasília'},
    {'id': 3, 'name': 'Chevette'},
  ]}