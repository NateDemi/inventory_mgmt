# main.py

from zinc_api_client import Order, load_info, logging


if __name__ == "__main__":
    api_key = 'C4A15FF5A3946E86838EC43B'

    # Load the common address from the JSON file
    address = load_info('./bin/address.json')["shipping_address"]
    payment = load_info('./bin/pmt_info.json')
    # Create an Amazon order
    amazon_order = Order(api_key, 'amazon', address)
    amazon_products = [{"product_id": "B00X4WHP5E", "quantity": 1}]
    amazon_response = amazon_order.create_order(amazon_products)
    if amazon_response.status_code == 200:
        logging.info(f"Amazon Order Response: {amazon_response.status_code} - {amazon_response.json()}")
    else:
        logging.error(f"Failed to create Amazon order: {amazon_response.status_code} - {amazon_response.text}")

    # Create a Walmart order
    walmart_order = Order(api_key, 'walmart', address)
    walmart_products = [{"product_id": "47329204", "quantity": 1}]
    walmart_response = walmart_order.create_order(walmart_products)
    if walmart_response.status_code == 200:
        logging.info(f"Walmart Order Response: {walmart_response.status_code} - {walmart_response.json()}")
    else:
        logging.error(f"Failed to create Walmart order: {walmart_response.status_code} - {walmart_response.text}")
