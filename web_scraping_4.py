def main():
    from lxml import html
    import requests
    response = requests.get('https://data.usajobs.gov/api/jobs', params = {'series': 1410})
    print response.json()['TotalJobs']

if __name__ == '__main__':
    main()
