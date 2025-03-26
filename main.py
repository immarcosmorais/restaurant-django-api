import requests

# URL do endpoint
url = "http://localhost:8000/dishes/"

# Lista de produtos
products = [
    {"name": "Lasanha Bolonhesa", "description": "Lasanha recheada com molho à bolonhesa e queijo gratinado.",
     "price": 24.90, "category": "Massas"},
    {"name": "Pizza Margherita", "description": "Pizza com molho de tomate, mussarela e manjericão fresco.",
     "price": 39.90, "category": "Pizzas"},
    {"name": "Hambúrguer Clássico",
     "description": "Hambúrguer com carne bovina, queijo cheddar, alface, tomate e maionese especial.", "price": 18.50,
     "category": "Lanches"},
    {"name": "Salmão Grelhado", "description": "Salmão grelhado servido com arroz integral e legumes salteados.",
     "price": 49.90, "category": "Peixes"},
    {"name": "Risoto de Funghi", "description": "Risoto cremoso com cogumelos funghi e parmesão.", "price": 34.90,
     "category": "Massas"},
    {"name": "Espaguete ao Pesto", "description": "Espaguete servido com molho pesto de manjericão e parmesão.",
     "price": 29.90, "category": "Massas"},
    {"name": "Torta de Limão", "description": "Torta de limão com merengue e massa crocante.", "price": 12.90,
     "category": "Sobremesas"},
    {"name": "Frango Grelhado", "description": "Peito de frango grelhado acompanhado de purê de batata e salada.",
     "price": 27.90, "category": "Carnes"},
    {"name": "Coxinha de Frango", "description": "Coxinha recheada com frango desfiado e catupiry.", "price": 7.50,
     "category": "Salgados"},
    {"name": "Cerveja Artesanal IPA",
     "description": "Cerveja artesanal IPA com notas de frutas cítricas e amargor equilibrado.", "price": 16.90,
     "category": "Bebidas"},
    {"name": "Churrasco Misto", "description": "Misto de carnes grelhadas com arroz, feijão tropeiro e mandioca frita.",
     "price": 54.90, "category": "Carnes"},
    {"name": "Brownie com Sorvete", "description": "Brownie de chocolate servido com sorvete de baunilha.",
     "price": 15.90, "category": "Sobremesas"},
    {"name": "Salada Caesar", "description": "Salada de alface, frango grelhado, croutons e molho caesar.",
     "price": 22.90, "category": "Saladas"},
    {"name": "Batata Frita com Cheddar e Bacon",
     "description": "Porção de batata frita coberta com cheddar cremoso e bacon crocante.", "price": 19.90,
     "category": "Aperitivos"},
    {"name": "Suco de Laranja Natural", "description": "Suco de laranja 100% natural, sem açúcar.", "price": 8.90,
     "category": "Bebidas"},
    {"name": "Picanha na Chapa", "description": "Picanha fatiada na chapa acompanhada de arroz, feijão e farofa.",
     "price": 69.90, "category": "Carnes"},
    {"name": "Filé Mignon ao Molho Madeira",
     "description": "Filé mignon servido com molho madeira, arroz e batatas sauté.", "price": 59.90,
     "category": "Carnes"},
    {"name": "Milkshake de Chocolate", "description": "Milkshake cremoso de chocolate com chantilly.", "price": 14.90,
     "category": "Bebidas"},
    {"name": "Cappuccino", "description": "Cappuccino italiano com espuma de leite e canela.", "price": 9.90,
     "category": "Bebidas"},
    {"name": "Camarão na Moranga", "description": "Camarões ao molho cremoso servidos dentro de uma moranga assada.",
     "price": 74.90, "category": "Peixes"},
    {"name": "Escondidinho de Carne Seca",
     "description": "Carne seca desfiada coberta com purê de mandioca e queijo gratinado.", "price": 32.90,
     "category": "Carnes"},
    {"name": "Sopa de Cebola", "description": "Sopa de cebola gratinada com queijo.", "price": 17.90,
     "category": "Sopas"},
    {"name": "Bife a Cavalo",
     "description": "Bife de contrafilé servido com ovo frito, arroz, feijão e batatas fritas.", "price": 38.90,
     "category": "Carnes"},
    {"name": "Coxinha Vegana", "description": "Coxinha recheada com jaca temperada.", "price": 7.90,
     "category": "Salgados"},
    {"name": "Panqueca de Frango", "description": "Panqueca recheada com frango desfiado ao molho de tomate.",
     "price": 22.90, "category": "Massas"},
    {"name": "Mojito", "description": "Drink cubano feito com rum, hortelã, limão e água com gás.", "price": 18.90,
     "category": "Bebidas"},
    {"name": "Cheesecake de Morango", "description": "Torta cheesecake com cobertura de geleia de morango.",
     "price": 16.90, "category": "Sobremesas"},
    {"name": "Bolo de Cenoura com Chocolate", "description": "Bolo de cenoura coberto com calda de chocolate.",
     "price": 10.90, "category": "Sobremesas"}
]

# Enviar POST para cada produto
for product in products:
    response = requests.post(url, json=product)
    print(f"Enviado: {product['name']} - Status: {response.status_code}")
    if response.status_code != 201:
        print(f"Erro: {response.text}")

import requests
from faker import Faker

# Configuração
fake = Faker("pt_BR")
url = "http://localhost:8000/customers/"
num_customers = 100

# Gerar 100 clientes fictícios
customers = []
for _ in range(num_customers):
    customer = {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
    }
    customers.append(customer)

# Enviar os dados via POST
for customer in customers:
    response = requests.post(url, json=customer)
    print(f"Enviado: {customer['name']} - Status: {response.status_code}")
    if response.status_code != 201:
        print(f"Erro: {response.text}")

# Configuração
url = "http://localhost:8000/tables/"
num_tables = 20

# Criar e enviar 20 mesas
for i in range(1, num_tables + 1):
    table = {
        "number": i,
        "capacity": 4  # Você pode alterar essa capacidade se quiser variar
    }

    response = requests.post(url, json=table)
    print(f"Enviando Mesa {table['number']} - Status: {response.status_code}")
    if response.status_code != 201:
        print(f"Erro: {response.text}")
