from fastapi import APIRouter

router = APIRouter()

Studentlist={
    1:{"names":"Sai","Gender":"M"},
    2:{"names":"Vijay","Gender":"M"},
    3:{"names":"Chanu","Gender":"M"},
    4:{"names":"Priya","Gender":"F"},
    5:{"names":"Suhas","Gender":"M"},
    6:{"names":"Sohan","Gender":"M"}
}

@router.get("/")
def read_root():
    return { 
        "Welcome to the Student API"
        }

@router.get("/search/{name}")
def search_items(name: str):
    # names = ["Sai", "Vijay", "Chanu","Priya","suhuaas","sohan"]
    # id=[1,2,3,4,5,6]
    # gender=[ "M","M","M","M","F","M","M", ]

    for id, student in Studentlist.items():
        if student["names"].lower() == name.lower():
            return Studentlist[id]