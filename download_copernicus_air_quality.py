import cdsapi

dataset = "cams-europe-air-quality-forecasts"
request = {
    "model": [
        "ensemble",
        "monarch"
    ],
    "date": ["2025-08-28/2025-08-28"],
    "data_format": "netcdf_zip"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()


