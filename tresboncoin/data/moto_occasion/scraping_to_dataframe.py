import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
import glob
import pandas as pd
import time
import random
import codecs
import shutil
from datetime import datetime

PATH_TO_CSV = os.path.dirname(os.path.abspath(__file__)).replace('/moto_occasion', '') + '/scraping_outputs/moto-occasion.csv'
PATH_TO_LOG = os.path.dirname(os.path.abspath(__file__)).replace('/moto_occasion', '') + "/log.csv"
PATH_TO_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_IMG_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/img'
PATH_TO_PAGES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + ('/pages')
PATH_TO_ANNONCES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + ('/annonces')
PATH_TO_INDEX = os.path.dirname(os.path.abspath(__file__)) + '/index.csv'


def scraping_to_dataframe():
    try:
        source = 'moto-occasion'
        url_site = 'http://moto-occasion.motorevue.com'

        # Start time
        start_time = datetime.now()

        # log update
        log_import = pd.read_csv(PATH_TO_LOG)
        log_new = pd.DataFrame({'source': [source],
                                'step': ['to dataframe'],
                                'status': ['started'],
                                'time': [datetime.now()],
                                'details': [""]})
        log = log_import.append(log_new, ignore_index=True)
        log.to_csv(PATH_TO_LOG, index=False)

        # import index
        index_df = pd.read_csv(PATH_TO_INDEX)

        for filename in [file for file in os.listdir(PATH_TO_ANNONCES_FOLDER) if file.endswith(".html")]:

            # cinitialize list for dataframe
            price_ls = []
            vendor_type_ls = []
            vendor_name_ls = []
            vendor_city_ls = []
            vendor_country_ls = []
            reference_ls = []
            uniq_id_ls = []
            bike_type_ls = []
            bike_size_ls = []
            bike_year_ls = []
            bike_km_ls = []
            bike_brand_ls = []
            bike_model_ls = []
            bike_description_ls = []

            f = codecs.open(PATH_TO_ANNONCES_FOLDER + f"{'/'+filename}", 'r')
            bike_soup = BeautifulSoup(f, "html.parser")
            reference = filename.split("-")[2]
            uniq_id = source+"-"+reference

            # vendor contact soup & info
            vendor_info = bike_soup.find("div", class_="item-contact__content").find_all("div", class_="grid-5-8 phab-7-10")
            vendor_anonyme = bike_soup.find("div", class_="item-contact__content").find("p").text

            if vendor_anonyme == 'Annonceur anonyme':
                vendor_type = 'PARTICULIER'
                vendor_name = ''
                vendor_localisation = vendor_info[1].text.strip().replace('\t', '').split('(')
                vendor_city = vendor_localisation[0]
                vendor_country = vendor_localisation[1].replace(")", "").upper()
            else:
                vendor_type = vendor_info[0].text.strip().upper()
                vendor_name = vendor_info[1].text.strip().replace('\t', '').replace('\n', ', ')
                vendor_localisation = vendor_info[3].text.strip().replace('\t', '').split('(')
                vendor_city = vendor_localisation[0]
                vendor_country = vendor_localisation[1].replace(")", "").upper()

            # moto description
            bike_info_1 = bike_soup.find("div", class_="item-description").find("div", class_="grids").find_all("span", class_="item-data")
            bike_type = bike_info_1[0].text.strip().upper()
            bike_size = int(bike_info_1[1].text.replace("cm3", "").strip())
            bike_year = int(bike_info_1[2].text.strip())
            bike_km = int(bike_info_1[3].text.strip().replace("km", "").strip())

            bike_info_2 = bike_soup.find("div", class_="item-description").find("div", class_="grids").find_all("h2", class_="item-data")
            bike_brand = bike_info_2[0].text.strip()
            bike_model = bike_info_2[1].text.strip()

            bike_description = bike_soup.find(id="infos").text.strip()

            # price
            price_soup = bike_soup.find("p", class_="item__price").text
            price = price_soup.replace("???", "").replace("TTC", "").replace(" ","")
            price = float("".join(price.split()).replace(",", ".").replace('PrixNC', '0'))

            # price estimated from the website
            price_estimated_soup = bike_soup.find("div", id="estimations").find('span',class_="item-data")
            if price_estimated_soup is None:
                price_estimated = 0.0
            else:
                price_estimated = price_estimated_soup.text.replace("???", "").replace("TTC", "").replace(" ","")
                price_estimated = float("".join(price_estimated.split()).replace(",", ".").replace('Cotenondisponiblepourcemod??le.','0'))

            # pictures
            try:
                if reference not in [file.split('-')[2] for file in glob.glob(PATH_TO_IMG_FOLDER + '/*')]:
                    img_soup = bike_soup.find("div", class_="slideshow__container").find_all("img")
                    k = 0
                    for image in img_soup:
                        image_url = url_site + image['src']
                        img_data = requests.get(image_url).content
                        with open(PATH_TO_IMG_FOLDER + f'/{uniq_id}-{k}.jpg', 'wb') as handler:
                            handler.write(img_data)

                        image = Image.open(PATH_TO_IMG_FOLDER + f'/{uniq_id}-{k}.jpg')
                        ratio = image.size[0] / image.size[1]
                        image = image.resize((300, int(300/ratio)))
                        image.save(PATH_TO_IMG_FOLDER + f'/{uniq_id}-{k}.jpg', optimize=True, quality = 50)
                        k += 1
            except:
                # no picture found for this bike
                pass

            price_ls.append(price)
            vendor_type_ls.append(vendor_type)
            vendor_name_ls.append(vendor_name)
            vendor_city_ls.append(vendor_city)
            vendor_country_ls.append(vendor_country)
            reference_ls.append(reference)
            uniq_id_ls.append(uniq_id)
            bike_type_ls.append(bike_type)
            bike_size_ls.append(bike_size)
            bike_year_ls.append(bike_year)
            bike_km_ls.append(bike_km)
            bike_brand_ls.append(bike_brand)
            bike_model_ls.append(bike_model)
            bike_description_ls.append(bike_description)

            df = pd.DataFrame(list(zip(
                uniq_id_ls,
                reference_ls,
                bike_type_ls,
                bike_size_ls,
                bike_year_ls,
                bike_km_ls,
                bike_brand_ls,
                bike_model_ls,
                bike_description_ls,
                price_ls,
                vendor_type_ls,
                vendor_name_ls,
                vendor_city_ls,
                vendor_country_ls)),
                             columns=[
                                'uniq_id',
                                'reference',
                                'bike_type',
                                'bike_size',
                                'bike_year',
                                'bike_km',
                                'bike_brand',
                                'bike_model',
                                'bike_description',
                                'price',
                                'vendor_type',
                                'vendor_name',
                                'vendor_city',
                                'vendor_country'])

            df['source'] = source
            df['scrap_date'] = datetime.now()

            # merge dataframes
            df = df.merge(index_df, on='reference', how='left')

            # import history
            history = pd.read_csv(PATH_TO_CSV)

            # concatenate new and history
            final_df = history.append(df, ignore_index=True)

            # export to csv
            final_df.to_csv(PATH_TO_CSV, index=False)

            # move file to vault after process
            # source path
            source_folder = PATH_TO_ANNONCES_FOLDER + f"/{filename}"
            # destination path
            destination = PATH_TO_ANNONCES_FOLDER + f"/vault/{filename}"
            # Move the content of
            # source to destination
            shutil.move(source_folder, destination)

            #time.sleep(random.randint(1, 2))

        # End time
        end_time = datetime.now()
        td = end_time - start_time

        # log update
        log_import = pd.read_csv(PATH_TO_LOG)
        log_new = pd.DataFrame({'source': [source],
                                'step': ['to dataframe'],
                                'status': ['completed'],
                                'time': [datetime.now()],
                                'details': [f"{td.seconds/60} minutes elapsed"]})
        log = log_import.append(log_new, ignore_index=True)
        log.to_csv(PATH_TO_LOG, index=False)

        # remove duplicates
        df = pd.read_csv(PATH_TO_CSV)
        df.drop_duplicates(subset=['reference', 'price'], inplace=True)
        df.to_csv(PATH_TO_CSV, index=False)

    except (ValueError, TypeError, NameError, KeyError, RuntimeWarning) as err:
        # log update
        log_import = pd.read_csv(PATH_TO_LOG)
        log_new = pd.DataFrame({'source': [source],
                                'step': ['to dataframe'],
                                'status': ['error'],
                                'time': [datetime.now()],
                                'details': [err]})
        log = log_import.append(log_new, ignore_index=True)
        log.to_csv(PATH_TO_LOG, index=False)


if __name__ == "__main__":
    scraping_to_dataframe()
