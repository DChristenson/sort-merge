import json
import sys
import csv
def main():
    sort_file = open("sortorder.csv","r")
    sort_sku = csv.reader(sort_file, delimiter="\n")
    for sku in list(sort_sku):
        id_file = open("productids.csv", "r")
        prod_ids = csv.reader(id_file, delimiter="\n")
        product_sku = sku[0].split(',')[0]
        updated_order = sku[0].split(',')[2]

        # print(updated_order)
        # print(product_sku)
        for product in list(prod_ids):
            product_id = product[0].split(",")[0]
            search_sku = product[0].split(",")[1]
            if product_sku == search_sku:
                print(product[0].split(","))
                data_obj = {}
                data_obj["product_id"] = int(product_id)
                data_obj["sort_order"] = int(updated_order)

                json_data  = json.dumps(data_obj)

                try:
                    with open("output.json", "r"):
                        pass
                except FileNotFoundError:
                    output_file = open("output.json", "a")
                    output_file.write("[" + "\n")

                output_file = open("output.json", "a")


                output_file.write(str(json_data) + ",\n")
                break

    output_file.write("]")



if __name__ == "__main__":
    main()