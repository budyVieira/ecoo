import requests
from bs4 import BeautifulSoup
import json

def extract_product_data(url):
  """
  Extrai informações de produtos de uma página web e as retorna em um objeto JSON.

  Argumentos:
    url (str): A URL da página web.

  Retorno:
    list: Uma lista de dicionários, cada um contendo as informações de um produto.
  """

  # Fazer uma requisição à página web.
  response = requests.get(url)

  # Se a requisição for bem-sucedida, continuar.
  if response.status_code == 200:

    # Criar um BeautifulSoup object a partir da página web.
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar todas as divs que contêm os produtos.
    product_divs = soup.find_all("div", class_="col-sm-3 col-xs-12 column columnWidth1 column-default")
    product_divs1 = soup.find_all("div", class_="col-sm-3 col-xs-12 column columnWidth1 first-line column-default rdc-productlist-desktop-first-row")

    # Criar uma lista para armazenar os dados dos produtos.
    products = []

    # Para cada div de produto, extrair as informações e adicionar à lista.
    for product_div in product_divs:
      # Extrair a URL da imagem do produto.
      image_url = product_div.find("img")["src"]

      # Encontrar a div que contém o nome do produto.
      name_div = product_div.find("div", class_="desc desc-top hidden-xl hidden-lg hidden-md hidden-sm")

      # Extrair o nome do produto.
      product_name = name_div.find("p", class_="name").text.strip()
      product_name1 = name_div.find("p", class_="key1-name").text.strip()

      # Encontrar a div que contém o preço do produto.
      price_div = product_div.find("div", class_="price dis-table clearfix")

      # Extrair o preço do produto.
      product_price = price_div.find("p", class_="current").text.strip()

      # Adicionar as informações do produto à lista.
      products.append({
        "image_url": image_url,
        "name": product_name1,
        "name1": product_name,
        "price": product_price
      })

    # Para cada div de produto, extrair as informações e adicionar à lista.
    for product_div in product_divs1:
      # Extrair a URL da imagem do produto.
      image_url = product_div.find("img")["src"]

      # Encontrar a div que contém o nome do produto.
      name_div = product_div.find("div", class_="desc desc-top hidden-xl hidden-lg hidden-md hidden-sm")

      # Extrair o nome do produto.
      product_name = name_div.find("p", class_="name").text.strip()
      product_name1 = name_div.find("p", class_="key1-name").text.strip()

      # Encontrar a div que contém o preço do produto.
      price_div = product_div.find("div", class_="price dis-table clearfix")

      # Extrair o preço do produto.
      product_price = price_div.find("p", class_="current").text.strip()

      # Adicionar as informações do produto à lista.
      products.append({
          "image_url": image_url,
          "name": product_name1,
          "name1": product_name,
          "price": product_price
      })

    # Retornar a lista de produtos.
    return products

  else:

    # Se a requisição falhar, retornar uma lista vazia.
    return []

# Exemplo de uso.
url = "https://www.kibabo.co.ao/pt/higiene/higiene-oral/escova-dentes_1063-238.html"
products = extract_product_data(url)

# Imprimir os dados dos produtos.
for product in products:
  print(product)
