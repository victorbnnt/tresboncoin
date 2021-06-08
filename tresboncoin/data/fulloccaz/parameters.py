import numpy as np
import pandas as pd

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}

fulloccaz_page_url = "https://www.fulloccaz.com/?&"

fulloccaz_announce_template = pd.DataFrame({"url": [np.nan],
                                            "unique id": [np.nan],
                                            "date_scrapped": [np.nan],
                                            "announce_publication_date": [np.nan],
                                            "vehicle brand": [np.nan],
                                            "vehicle type": [np.nan],
                                            "color": [np.nan],
                                            "price": [np.nan],
                                            "city": [np.nan],
                                            "postal code": [np.nan],
                                            "seller": [np.nan],
                                            "seller_name": [np.nan],
                                            "vehicle release date": [np.nan],
                                            "mileage": [np.nan],
                                            "motorisation": [np.nan],
                                            "fiscal power": [np.nan],
                                            "guarantee": [np.nan],
                                            "hand": [np.nan],
                                            "chassis": [np.nan],
                                            "engine capacity [CC]": [np.nan],
                                            "comments": [np.nan]})

full_occaz_brand_list = ["AC+EMOTION",
                         "ACCESS+MOTOR",
                         "APRILIA",
                         "ARCTIC+CAT",
                         "BENELLI",
                         "BETA",
                         "BIMOTA",
                         "BMW",
                         "BUELL",
                         "CAN-AM",
                         "CF+MOTO",
                         "DAELIM",
                         "DERBI",
                         "DUCATI",
                         "FANTIC",
                         "FB+MONDIAL",
                         "GAS+GAS",
                         "GENERIC",
                         "GILERA",
                         "HARLEY+DAVIDSON",
                         "HARLEY-DAVIDSON",
                         "HER+CHEE",
                         "HM",
                         "HONDA",
                         "HONGYI",
                         "HUSQVARNA",
                         "HYOSUNG",
                         "HYTRACK",
                         "IMF+scooter",
                         "INDIAN",
                         "IRBIT",
                         "JM+MOTORS",
                         "JORDON",
                         "JOTAGAS",
                         "KAWASAKI",
                         "KEEWAY",
                         "KSR+MOTO",
                         "KTM",
                         "KYMCO",
                         "LAMBRETTA",
                         "LAZIO",
                         "LIGIER",
                         "LINHAI",
                         "LONGJIA",
                         "Magnum",
                         "MAGPOWER",
                         "MALAGUTI",
                         "MARTIN",
                         "MASAI",
                         "MASH",
                         "MBK",
                         "MOTO+MORINI",
                         "MOTO-GUZZI",
                         "MOTOCONFORT",
                         "MOTRAC",
                         "MV+AGUSTA",
                         "NECO",
                         "NIU",
                         "NORTON",
                         "ORCAL",
                         "PEUGEOT",
                         "PIAGGIO",
                         "POLARIS",
                         "QUADDY",
                         "QUADRO",
                         "RIEJU",
                         "RIVAL+MOTORS",
                         "RIYA",
                         "ROYAL+ENFIELD",
                         "SHERCO",
                         "SUPER+SOCO",
                         "SUZUKI",
                         "SVM+%28SWM%29",
                         "SWM",
                         "SYM",
                         "TGB",
                         "TNT+MOTOR",
                         "TRIUMPH",
                         "VASTRO",
                         "VESPA",
                         "Victory+Motorcycle",
                         "VOGE",
                         "VOXAN",
                         "WANGYE",
                         "XINGYUE",
                         "YAMAHA",
                         "ZERO+MOTORCYCLES"]
