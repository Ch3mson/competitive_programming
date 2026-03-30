from api import get_products
import json
"""
Add a retry with 5 second timer, until we get response

part 2:
might have fallback sku, which is a single string.

Could have a cycle
modify products and append item to each of the entries

create a dfs, where base case is relatedItems = null
optimization: 

{
product1: [product2]
product2: null
}


"""
import time
from collections import defaultdict
class ProductClient:
  def __init__(self):
      pass

  def products(self):
    products = []
    while not products:
      try: 
        products = get_products()
        return products['data']['products']
      except Exception as e:
        print('Error', e)
      time.sleep(5)


  def getProductsWithFallback(self, products):

    relatedItemsAdjList = defaultdict(str) # id -> fallbackSku
    visited = set()

    for p in products:
      id = p["id"]
      if p["fallbackSku"]: # if this is not null
        relatedItemsAdjList[id] = p["fallbackSku"]

    relatedItemsFallbacks = defaultdict(list) # p["id"] -> [childrens]

    def traverseProduct(p_id):
      if p_id not in relatedItemsAdjList:
        return []
      if p_id in relatedItemsFallbacks:
        return relatedItemsFallbacks[p_id]
      
      if p_id in visited:
        return relatedItemsFallbacks[p_id]

      if p_id in relatedItemsAdjList and p_id not in visited:
        visited.add(p_id)
        base_arr = traverseProduct(relatedItemsAdjList[p_id])

        relatedItemsFallbacks[p_id] = base_arr + [relatedItemsAdjList[p_id]]

    for p in products: # populate relatedItemsFallbakcs
      traverseProduct(p["id"])

    for p in products:
      if p["id"] in relatedItemsFallbacks:
        p["relatedItems"] = relatedItemsFallbacks[p["id"]]
      else:
        p["relatedItems"] = []

    return products



def main():
  """Main function to run the product client"""
  client = ProductClient()
  products = client.products()

  json.dumps(products, indent=2)
  print(client.getProductsWithFallback(products))
main()