import requests
import json

class BkmKitap:
    def __init__(self, book_title):
        self.book_title = book_title
    
    def get_books(self):
        data = {
            "cm":"conv",
            "f":True,
            "d":True,
            "q":self.book_title
        }
        r = requests.get("https://bkm.wawlabs.com/avx_wse", params=data)
        return r.text
    
    def parse_books(self):
        books = self.get_books()
        jsonify = json.loads(books)
        results = []
        for book in jsonify["res"]:
            result = {}
            result["book_title"] = book["Title_txt_tr"]
            result["book_author"] = book["Brand_txt_tr"]
            result["book_price"] = book["Price_txt_tr"]
            result["book_sale_price"] = book["Sale_Price_txt_tr"]
            result["book_publisher"] = book["Publisher"]
            result["book_rating"] = book["Rating"]
            results.append(result)
        return results

if __name__ == "__main__":
    book_input = input("Kitap adı giriniz: ")
    data = BkmKitap(book_input).parse_books()
    print("--SORGU SONUCU GELEN KİTAP BİLGİLERİ--")
    for i in data:
        print(f"Kitap Adı: {i['book_title']}\nKitap Yazarı: {i['book_author']}\nKitap Fiyatı: {i['book_price']}\nKitap İndirimli Fiyatı: {i['book_sale_price']}")
        print(f"Yayımcı: {i['book_publisher']}\nKitap Puanı: {i['book_rating']}\n")
