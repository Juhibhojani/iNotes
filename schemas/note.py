def noteEntity(item)->dict:
    return {
        "id":item['_id'],
        "title":item['title'],
        "desc":item['desc'],
        "important":item['important']
    }
    
def notesEntitiy(items) -> list:
    return [noteEntity(item) for item in items]
    