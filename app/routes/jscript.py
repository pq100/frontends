from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# 라우터 생성
jscript_router = APIRouter()

# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정

@jscript_router.get('/')
async def semantic(request: Request):
    return templates.TemplateResponse('js/index.html', {'request': request})

@jscript_router.get('/hello')
async def hello(request: Request):
    return templates.TemplateResponse('js/01hello.html', {'request': request})

@jscript_router.get('/type')
async def type(request: Request):
    return templates.TemplateResponse('js/02type.html', {'request': request})

@jscript_router.get('/operator')
async def operator(request: Request):
    return templates.TemplateResponse('js/03operator.html', {'request': request})
