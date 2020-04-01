# cord-holmes-server

A REST API serving searches of the COVID-19 Open Research Dataset via holmes-extractor

To start the server, run:

```bash
docker-compose up -d
```

To perform a search, run (in python):

```python
import requests
response = requests.post('http://HOSTNAME:5000/holmes_search',
                         {'query': SEARCH_QUERY}).json()
```

Where `HOSTNAME` is the host where you're running the server, and 
`SEARCH_QUERY` is a string containing the search query.
