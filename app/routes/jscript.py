import sqlite3

from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
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

@jscript_router.get('/condition')
async def condition(request: Request):
    return templates.TemplateResponse('js/04condition.html', {'request': request})

@jscript_router.get('/loop')
async def loop(request: Request):
    return templates.TemplateResponse('js/05loop.html', {'request': request})

@jscript_router.get('/array')
async def array(request: Request):
    return templates.TemplateResponse('js/06array.html', {'request': request})

@jscript_router.get('/while')
async def while1(request: Request):
    return templates.TemplateResponse('js/07while.html', {'request': request})

@jscript_router.get('/function')
async def function(request: Request):
    return templates.TemplateResponse('js/08function.html', {'request': request})

@jscript_router.get('/callback')
async def callback(request: Request):
    return templates.TemplateResponse('js/09callback.html', {'request': request})

@jscript_router.get('/except')
async def except1(request: Request):
    return templates.TemplateResponse('js/10except.html', {'request': request})

@jscript_router.get('/bom')
async def bom(request: Request):
    return templates.TemplateResponse('js/11bom.html', {'request': request})

@jscript_router.get('/dom')
async def dom(request: Request):
    return templates.TemplateResponse('js/12dom.html', {'request': request})

@jscript_router.get('/zipcode')
async def zipcode(request: Request):
    return templates.TemplateResponse('js/16zipcode.html', {'request': request})

@jscript_router.get('/ajaxzip')
async def ajaxzip(request: Request):
    return templates.TemplateResponse('js/17ajaxzip.html', {'request': request})

@jscript_router.get('/zip2013')
async def zip2013(request: Request):
    return templates.TemplateResponse('js/17ajaxzip.html', {'request': request})

@jscript_router.get('/getsido')
# http://127.0.0.1:8000/js/getsido
async def getsido(request: Request):
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql = 'select distinct sido from zipcode2013'
    cursor.execute(sql)
    sidos = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json으로 저장
    result = []
    for sido in sidos:
        result.append({'sido': sido[0]})

    return JSONResponse(content=result)

@jscript_router.get('/getgugun')
# http://127.0.0.1:8000/js/getgugun?sido=서울
async def getgugun(sido: str):
    # zipcode 테이블에서 구군 조회
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql = 'select distinct gugun from zipcode2013 where sido = ?'
    cursor.execute(sql, (sido,))
    guguns = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json으로 저장
    result = []
    for gugun in guguns:
        result.append({'gugun': gugun[0]})

    return JSONResponse(content=result)


@jscript_router.get('/getdong')
# http://127.0.0.1:8000/js/getdong?sido=서울&gugu=강남구
async def getdong(sido: str, gugu: str):
    # zipcode 테이블에서 읍면동 조회
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql = 'select distinct dong from zipcode2013 where sido = ? and gugun = ?'
    cursor.execute(sql, (sido, gugu, ))
    dongs = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json으로 저장
    result = []
    for dong in dongs:
        result.append({'dong': dong[0]})

    return JSONResponse(content=result)
