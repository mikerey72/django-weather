#Adding a comment to my views.py file



from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        #return render(request, 'home.html', {'zipcode': zipcode}) # returns post to the screen


        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=5EC2840F-9C25-46BE-A511-3188A2080150")

        try:
            api = json.loads(api_request.content)


        except Exception as e:
            api = "Error..."  # if there are any issues if will throw out this error

        if api[0]['Category']['Name'] == "Good":
            category_description = "Good(0 - 50): Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Moderate(51 - 100): Air quality is acceptable; however, for some pollutants there may " \
                                   "be a moderate health concern for a very small number of people who are unusually " \
                                   "sensitive to air pollution."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Unhealthy for Sensitive Groups(USG)(101 - 150): Although general public is not likely to be affected at this " \
                                   "AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas " \
                                   "persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "Unhealty for Sensitive Groups"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Unhealthy(151 - 200): Everyone may begin to experience health effects; members of " \
                                   "sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Very Unhealthy(201 - 300): Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Hazardous(301 - 500) Health warnings of emergency conditions.The entire population is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92127&distance=25&API_KEY=5EC2840F-9C25-46BE-A511-3188A2080150")

        try:
            api = json.loads(api_request.content)


        except Exception as e:
            api = "Error..."  # if there are any issues if will throw out this error

        if api[0]['Category']['Name'] == "Good":
            category_description = "Good(0 - 50): Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Moderate(51 - 100): Air quality is acceptable; however, for some pollutants there may " \
                                   "be a moderate health concern for a very small number of people who are unusually " \
                                   "sensitive to air pollution."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Unhealthy for Sensitive Groups(USG)(101 - 150): Although general public is not likely to be affected at this " \
                                   "AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas " \
                                   "persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "Unhealty for Sensitive Groups"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Unhealthy(151 - 200): Everyone may begin to experience health effects; members of " \
                                   "sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Very Unhealthy(201 - 300): Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Hazardous(301 - 500) Health warnings of emergency conditions.The entire population is more likely to be affected."
            category_color = "hazardous"


        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})


