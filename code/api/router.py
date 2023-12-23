from datetime import timedelta
import fastapi as fa

from starlette import status

from api.article.routes import router as article_router
from adapters import MinIOClient
import settings


router = fa.APIRouter(prefix='/api')
router.include_router(article_router)

@router.get('/greetings')
def get_greetings():
    return {'text': 'Greetings!'}


# @router.post('/upload')
# async def upload_file(file: fa.UploadFile = fa.File(...)):
#     client = MinIOClient()
#     resp = await client.upload_from_bytes(file)
#     print(777, resp.location)
    
#     url = client.get_presigned_url(
#         "GET",
#         settings.minio_bucket_name,
#         file.filename,
#         expires=timedelta(hours=2),
#     )
    
#     print(777, url)
    
#     return fa.Response(status_code=status.HTTP_204_NO_CONTENT)
