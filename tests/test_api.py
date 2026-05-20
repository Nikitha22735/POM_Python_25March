from playwright.sync_api import sync_playwright, expect
import json
# import 
# def test_get_api():
#     with sync_playwright() as p:
#         context = p.request.new_context()

def get_api(playwright):
    context = playwright.request.new_context()
    ## basic auth
    # context = playwright.request.new_context(http_credentials={"username": "us", "password":"pw"})
    ## bearerToken
    token = {"Authorization": "Bearer 12345"}
    headersData = {
        "Authorization": "Bearer 12345",
        "Content-Type": "application/json"
    }
    response = context.get("https://dummyjson.com/products", headers=headersData, params={"limit": 5})
    #api key
    # token = {"x-api-key": "Bearer 12345"}
    # response = context.get("https://dummyjson.com/products", headers=token)

    ## basic auth

    print(response)
    print(response.status)
    # expect(response.status).tobe(200)
    assert response.status==200

    result = response.json()
    assert result["products"][0]["title"]=="Essence Mascara Lash Princess"




def postAPI(playwright):
    context = playwright.request.new_context()
    token = {"Authorization": "Bearer 12345"}
    requestBody = {
  "title": "Gaming Chair",
  "price": 299.99,
  "brand": "DXRacer"
}
    response = context.post("https://dummyjson.com/products/add",headers=token, data=requestBody)
    print(response)



def test_mock_getAPI(page):

    def mockvalues(route):
        route.fulfill(
            status = 201,
            body=json.dumps({
                "product":[
                    {
                        "title": "test"
                    }
                ]
            })
        )


    page.route("https://dummyjson.com/products",mockvalues)
    
    response = page.goto("https://dummyjson.com/products")
    print(response.status)
    print(response.json())










