from google.ads.googleads.client import GoogleAdsClient

# Initialize Google Ads API client
# Set up your credentials, developer_token, and other necessary parameters
# client = GoogleAdsClient.load_from_storage("path_to_your_config_file")
credentials = {
    "use_proto_plus": True,
    "developer_token": "NXkpkoK5o2Sotj6ARIyIUw",
    "refresh_token": "1//0gIJZNijlIRhaCgYIARAAGBASNwF-L9IreI2K693naFZf9VM5v9cD63GVU55kf63tIPU7yXXkjLJ3RnBicj2HL5JowPn_P_xw8Uk",
    "client_id": "1008631645143-b8ulhnab7k7gj1fuibgasrupb60od3gt.apps.googleusercontent.com",
    "client_secret": "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",
    }
client = GoogleAdsClient.load_from_dict(credentials)


# Define a query to retrieve product data
query = """
    SELECT
      product.id,
      product.title,
      product.price
    FROM
      product_partition_view
"""

try:
    # google_ads_service = client.service.google_ads_service
    ga_service = client.get_service("GoogleAdsService")
    # Issue a query to retrieve product data
    response = ga_service.search(
        customer_id="6978926768",  # Replace with your Google Ads account's customer ID
        query=query
    )

    # Process the response
    for row in response:
        print(f"Product ID: {row.product.id}, Title: {row.product.title}, Price: {row.product.price}")

except Exception as e:
    print(f"An error occurred: {e}")
