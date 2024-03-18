from flask import Flask, jsonify
from selenium import webdriver
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/get_products', methods=['GET'])
def get_products():
    # Inicializar o WebDriver (neste exemplo, vamos usar o Chrome)
    driver = webdriver.Chrome()

    # URL da página com os produtos
    url = 'https://shop.manoapp.com/pt/categories/245-petiscos'

    # Carregar a página
    driver.get(url)

    # Obter o conteúdo HTML da página após o carregamento completo
    html_content = driver.page_source

    # Parse do conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Lista para armazenar os dados dos produtos
    products = []

    # Encontrar todas as divs de produtos na página
    product_divs = soup.find_all('div', class_='product')

    # Iterar sobre as divs dos produtos
    for product_div in product_divs:
        # Dicionário para armazenar os dados de cada produto
        product_data = {}

        # Encontrar o link da imagem do produto
        image_link = product_div.find('img')['src']
        product_data['img'] = image_link

        # Encontrar o preço do produto
        price = product_div.find('h2').text.strip()
        product_data['preco'] = price

        # Encontrar o nome do produto
        name = product_div.find('p').text.strip()
        product_data['nome'] = name

        # Adicionar os dados do produto à lista de produtos
        products.append(product_data)

    # Fechar o WebDriver
    driver.quit()

    # Converter a lista de produtos para JSON
    products_json = json.dumps(products, ensure_ascii=False, indent=4)

    # Retornar os produtos como JSON
    return jsonify(products_json)

if __name__ == '__main__':
    app.run(debug=True)
