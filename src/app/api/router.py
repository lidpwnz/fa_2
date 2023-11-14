from fastapi import APIRouter


router = APIRouter(prefix='/api')

@router.get('/greetings')
def get_greetings():
    return {'text': 'Greetings!'}
