# Stukaartlezer
Vanaf 2022-2023 worden aan de Associatie KU Leuven duurzame studentenkaart
uitgereikt. Deze duurzame kaarten bevatten een andere chip dan voorheen. Hierdoor werken de scanners die gebruikernamen (r-nummers) uitlezen niet meer. Dit script heeft als doel zo goed mogelijk de "oude" kaartlezers te simuleren met de nieuwe.

## Benodigdheden

### Kaartlezer

De oude kaartlezer moet geherconfigueerd worden door icts. Op de volgende pagina is hier meer info over te vinden https://icts.kuleuven.be/sc/printenkaart/verhuur-kaartlezer#aanvraag. Op deze pagina staat een link voor een herconfiguratie aan te vragen. Belangrijk is om als profiel **Aanwezigheidsregistratie** te kiezen

### Service account

Dit programma maakt gebruik van een interne API ontwikkeld door ICTS. Hiervoor zijn credentials nodig in de vorm van een "service account". Zo een account kan je aanvragen door te mailen naar [kaartintegratie@kuleuven.be](mailto:kaartintegratie@kuleuven.be). Je hebt een service account nodig per usecase (bv. cudi, inschrijvingen...).
Elk service account wordt gespecifieerd door een client_id en een client_secret. Deze 2 waarden zijn nodig om het script te laten werken en **moeten worden ingevuld op lijn 3 en 4 in stukaart.py**

## Technische details

- Het script runt op python 3.10 met de volgende packages: `keyboard, requests, json, re`. Mochten de packages niet geinstalleerd zijn kunnen ze via pip geïnstalleerd worden

	`pip install naam_package`

- Werkt op Windows via Powershell of Cmd

- Werkt **niet volledig** op Linux **als root user**, dit komt door de manier waarop de input wordt ingelezen. De input wordt te traag herkend en geeft onverwacht gedrag.

- Het script draait op de achtergrond in een terminal venster en wordt opgestart met `python3 stukaart.py`
- Het script kan gestopt worden door `esc + enter` 2 keer in te voeren

## Limitaties

- Een actieve internet connectie is ten alle tijde nodig
- Doordat het script luistert op input gevolgd door een `enter` kan men niet zomaar een nieuwe lijn typen, dit gebeurt door 2 keer de `enter` toets te gebruiken.
- Het omzetten van scanner input naar een gebruikersnummer kan enige tijd (10-20sec) in beslag nemen. Dit komt door een trage API response. De tool geeft aan wanneer er gewacht wordt op de API. 

## Disclaimer

Dit programma is niet goedgekeurd noch ontwikkeld door KULeuven of ICTS, gebruik op eigen verantwoordelijkheid. Support kan via github of per mail.
