from helpers import get_price, create_dictionary

def get_data():
    urls = ["https://www.sondadelivery.com.br/delivery/produto/ARROZCAMILAG5kg/1000001195",
            "https://www.clubeextra.com.br/produto/41329/arroz-agulhinha-tipo-1-camil-pacote-5kg",
            "https://www.paodeacucar.com/produto/41329/arroz-agulhinha-tipo-1-camil-pacote-5kg",
            "https://www.clubeextra.com.br/produto/9461/feijao-carioca-tipo-1-camil-pacote-1kg",
            "https://www.paodeacucar.com/produto/9461/feijao-carioca-tipo-1-camil-pacote-1kg",
            "https://www.sondadelivery.com.br/delivery/produto/FEIJCAMCART11kg/1000001726",
            "https://www.paodeacucar.com/produto/37565/cafe-a-vacuo-torrado-e-moido-tradicional-melitta-caixa-500g",
            "https://www.clubeextra.com.br/produto/37565/cafe-a-vacuo-torrado-e-moido-tradicional-melitta-caixa-500g",
            "https://www.sondadelivery.com.br/delivery/produto/CAFMELITTRAD500g/1000001210"]
        
    price_arroz = {}
    price_feijao = {}
    price_cafe = {}

    for url in urls:
        if "arroz" in url.lower():
            price = get_price(url)
            create_dictionary(url, price, price_arroz)
        elif "feij" in url.lower():
            price = get_price(url)
            create_dictionary(url, price, price_feijao)
        else:
            price = get_price(url)
            create_dictionary(url, price, price_cafe)

    return {"Arroz Camil 5kg": price_arroz, "Feijao carioca Camil 1kg": price_feijao, "Cafe Melitta 500g": price_cafe}
