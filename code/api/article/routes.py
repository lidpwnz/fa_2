from uuid import UUID
from starlette import status
import fastapi as fa

from api import schemas
from db.repository import ArticleRepository
from exceptions import common as common_exc, http as http_exc


router = fa.APIRouter(prefix='/article', tags=['article'])
repo = ArticleRepository()


@router.get('')
async def get_articles(query: schemas.ArticleGetSchema = fa.Depends()):
    return await repo.get_list(**query.dict(exclude_none=True))


@router.get('/{id}')
async def get_article(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.post('')
async def create_article(
    body: schemas.ArticleSchema = fa.Depends(schemas.ArticleSchema.as_form), 
    avatar: fa.UploadFile = fa.File(...),
):
    try:
        return await repo.create(**body.dict(), avatar=avatar)
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.patch('/{id}')
async def update_article(id: UUID, body: schemas.ArticleUpdateSchema):
    try:
        return await repo.update(id, **body.dict(exclude_none=True))
    
    except common_exc.UpdateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.delete('/{id}')
async def delete_article(id: UUID):
    try:
        await repo.delete(id)
        
        return fa.responses.Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
