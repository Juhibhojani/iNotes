from fastapi import APIRouter,Request,status
from fastapi.responses import HTMLResponse,RedirectResponse
from models.note import note
from config.db import conn
from schemas.note import noteEntity, notesEntitiy
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/",response_class=HTMLResponse)
def home_page(request:Request):
    docs = conn.notes.notes.find()
    newDocs= []
    for doc in docs:
        newDocs.append({
            "id":doc['_id'],
            "title":doc['title'],
            "desc":doc['desc'],
            "important":doc['important']
        })
    return templates.TemplateResponse("index.html",{"request":request,"docs":newDocs})


@router.post("/")
async def add_notes(request:Request):
    forms = await request.form()
    print(forms,"hi")
    form_dict = dict(forms)
    if 'important' in form_dict.keys():
        form_dict['important']=True # type: ignore
    else:
        form_dict['important'] = False #type:ignore
    inserted_note = conn.notes.notes.insert_one(form_dict)
    redirect_url = request.url_for('home_page')    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER) 