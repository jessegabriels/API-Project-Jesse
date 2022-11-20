# API-Project-Jesse

# Concept
Het concept van mijn project is om meetingen van een ESP32 bij te houden. Met behulp van een php script kan ik data doorsturen naar MySQL.
Eens de data in mijn databse staat, kan ik met python een API maken. Deze API host ik via Okteto. Eens dit allemaal werkt, kan ik met HTML en AlpineJS een front-end maken. Hierin zouden de teruggegeven waardes van de API in een grafieken te komen staan. Hierdoor wordt het waterniveau mooi weergegeven.

# Okteto
De laatste les heb ik samen met mijn leerkracht gezocht naar de oorzaak van een error. Zowel de leerkracht als ikzelf vonden het niet. Hierdoor was ik genoodzaakt om mijn database op een andere manier te betreden. Bij het uploaden van mijn repo op Okteto Cloud krijg ik een foutmelding. 

![image](https://user-images.githubusercontent.com/81410142/202868255-19a29c9d-0929-4be3-ac50-0ae31fc88979.png)

Hierdoor heb ik besloten om een lijst te hard coderen.
![image](https://user-images.githubusercontent.com/81410142/202900307-34d81759-b836-48dc-aad1-b85b1fae2de2.png)

# Postman

![image](https://user-images.githubusercontent.com/81410142/202900354-1033dc4f-d1ce-4dca-b6e2-762d3f172069.png)

Op de bovenstaande screenshot is te zien dat ik een GET request stuur naar API. De laatste 4 waardes worden weergeven. Dit komt omdat de ESP 4 meetingen per dag doet (om de 6 uur). 

![image](https://user-images.githubusercontent.com/81410142/202901292-c930e068-72b0-4341-ba14-305d58d73415.png)


Omdat het niet nodig is om zelf een meetingen de posten, heb ik er voor gekozen om dit niet te integreren in mijn systeem.


# Andere Repositories + Okteto
Front-end: https://github.com/jessegabriels/API-Project-Jesse-Front.git

ESP32: https://github.com/jessegabriels/API-Project-Jesse-ESP.git

Okteto: https://project-service-jessegabriels.cloud.okteto.net

Hosted Front-end: https://jessegabriels.github.io/API-Project-Jesse-Front/



