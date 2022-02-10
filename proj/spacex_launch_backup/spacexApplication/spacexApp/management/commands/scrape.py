from django.core.management.base import BaseCommand

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

from spacexApp.models import futureLaunch

class Command(BaseCommand):
    help = "Collect Data"

    # defin logic of command
    def handle(self, *args, **options):

        # Collect html
        req = Request("https://spaceflightnow.com/launch-schedule/", headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()

        #convert to soup 
        soup = BeautifulSoup(html, 'html.parser')

        # grab all postings
        main_data = soup.find_all("div", class_="mh-content")

        for data in main_data:
            title =       data.find('span', class_='mission').text
            launch_date = data.find('span', class_='launchdate').text
            launch_info = data.find('div', class_='missiondata').text
            description = data.find('div', class_='missdescrip').text

            # Check if url in db 
            try:
                # save in db
                futureLaunch.objects.create(
                    title=title, 
                    launch_date=launch_date,
                    launch_info=launch_info,
                    description=description
                )
                print('%s added' % (title,))
            except:
                print('%s already exists' % (title,))

        self.stdout.write( 'Job complete')


