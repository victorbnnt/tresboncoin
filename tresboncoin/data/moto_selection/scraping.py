from tresboncoin.data.moto_selection.scraping_pages import scraping_pages
from tresboncoin.data.moto_selection.scraping_annonces import scraping_annonces
from tresboncoin.data.moto_selection.scraping_to_dataframe import scraping_to_dataframe


def scraping():
    '''
    function to:
    1 - scraping pages
    2 - scrapping annonces
    3 - tranform to dataframe
    '''

    scraping_pages()
    scraping_annonces()
    scraping_to_dataframe()


if __name__ == "__main__":
    scraping()
