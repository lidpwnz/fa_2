from datetime import datetime
import fastapi


router = fastapi.APIRouter(prefix='/api')


@router.get('/greetings')
def get_greetings():
    return {'text': 'Greetings!', 'current_time': datetime.now().time()}


@router.get('/articles/{id_}')
def get_article(id_: int):
    return {'id': id_, 'name': 'Test Article'}


app = fastapi.FastAPI()
app.include_router(router)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=1026, reload=True)
