import random

NAMES = [
    "Анна",
    "Валерия",
    "Диана",
    "Ольга",
    "Светлана",
    "Татьяна",
    "Ирина",
    "Анастасия",
    "Елизавета",
    "Дарья",
    "Мария",
    "Марина"
    ]
    
PRODUCTS = {
    "матрас Serta Denver Hard": 22,
    "матрас Family Strong": 14,
    "кровать Pola": 14,
    "матрас Askona Ortho Hard": 8,
    "матрас Serta Atlanta Medium": 15,
    "матрас Family Comfort": 7,
    "матрас Askona Ortho Medium": 5,
    "матрас Classic Brilliant Duo":	5,
    "матрас Serta Vermont Medium":	5,
    "кровать VIRGINIO":	4,
    "диван Локо ПРО":	4,
    "матрас ASKONA BENEFIT": 5,
    "кровать ELISA":	3,
    "кровать Innovo ice": 3,
    "кровать Вега Nova": 3,
    "матрас Family Lovely": 2,
    "кровать Milora": 2,
    "кровать ORLANDO": 2,
    "кровать Vanessa": 2,
    "кровать Milana New": 2,
    "матрас Askona Flash": 1,
    "матрас COMFORT PLUS": 1,
    "матрас Ergo Adaptive Hard": 1,
    "кровать Luara": 1,
    "матрас Original": 1,
    "матрас Serta Arizona Duo": 1,
    "диван Карина Nova": 1,
    "диван Кларк": 1,
    "диван Меллоу": 1,
    "диван Сван": 1,
    "диван Трентон": 1,
    "диван Квина Нью": 1,
    "кровать Niks": 1,
    "кровать Marcello": 1,
}

POPULATION = [s for s in PRODUCTS.keys()]
WEIGHTS = [s for s in PRODUCTS.values()]
SIZES = ["200*160","200*180","200*140"]
SIZES_W = [6,3,1]
    
def generate_phone():
    return f"9{random.randint(10,89)}{random.randint(100,999)}{random.randint(10,99)}{random.randint(10,99)}"

def generate_lead():
    name = random.choice(NAMES)
    phone = generate_phone()
    comment = random.choices(POPULATION, weights = WEIGHTS)[0]
    return name, phone, comment
    
    
if __name__=="__main__":
    for i in range(10):
        name, phone, comment = generate_lead()
        if "матрас" in comment or "кровать" in comment:
            size = random.choices(SIZES, weights=SIZES_W)[0]
            comment+=" "+size
        print(f"{name}|{phone}|*{comment}")
    
