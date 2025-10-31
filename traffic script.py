import requests
from datetime import datetime
import csv
locations = [
    {"name": "Diwan Cheruvu", "lat": 17.04629016871151, "lon": 81.84391764161728},
    {"name": "Morumpudi Junction", "lat": 16.996048288046573, "lon": 81.80198795480973},
    {"name": "VL Puram", "lat": 17.000361116740542, "lon": 81.79457900941965},
    {"name": "Bommuru Junction", "lat": 16.970026044376908, "lon": 81.7982077898937},
    {"name": "Lala Cheruvu", "lat": 17.02593120555252, "lon": 81.80629901087161},
    {"name": "Pushkar Ghat Cir", "lat": 17.006969029272703, "lon": 81.767905981993721},
    {"name": "Azad Chowk", "lat": 17.006653914430878, "lon": 81.77629003487216},
    {"name": "Devi Chowk Circle", "lat": 17.00979647101888, "lon": 81.77610012750917},
    {"name": "Balajipeta Junction", "lat": 16.97671457656731, "lon": 81.79384356744096},
    {"name": "Kesavaram Railway gate", "lat": 16.93112749732291, "lon": 81.88170907194181},
    {"name": "GIET NH", "lat": 17.059489892275263, "lon": 81.869371840258811},
    {"name": "DELTA hospital NH", "lat": 17.011499419423277, "lon": 81.80917916023519},
    {"name": "GSL NH", "lat": 17.067684063534045, "lon": 81.88328358025326},
    {"name": "JN Road NH", "lat": 17.008003289850134, "lon": 81.80995996296429},
    {"name": "RTC CS Mall", "lat": 17.000363703893182, "lon": 81.78944972209622},
    {"name": "Old Bypass Road", "lat": 17.005045820972253, "lon": 81.7801544865445},
    {"name": "Jampeta", "lat": 17.00493586307353, "lon": 81.780213297543},
    {"name": "Syamalamba Temple Rd", "lat": 16.999305680527787, "lon": 81.77559463029415},
    {"name": "Stadium Rd", "lat": 16.996918736129484, "lon": 81.7777554114391},
    {"name": "Anala venkata Apparao road", "lat": 17.007811731690097, "lon": 81.7921873982832},
    {"name": "Manasa Hospital", "lat": 17.007717340321364, "lon": 81.78586393475791},
    {"name": "Apex Hospital", "lat": 17.006938634443195, "lon": 81.79054340970453},
    {"name": "Nandamgani raju junction", "lat": 17.009486970902955, "lon": 81.77954016677567},
    {"name": "Y juncton", "lat": 17.012826235294103, "lon": 81.78265351880752},
    {"name": "Chiranjeevi Bus Stand", "lat": 17.014572541382044, "lon": 81.77861516264718},
    {"name": "Gokavaram Bus stand", "lat": 17.00967984828635, "lon": 81.77120172225537},
    {"name": "Devichowk to Mochi veedhi", "lat": 17.00897558377485, "lon": 81.77516315124535},
    {"name": "jandapanja road", "lat": 17.005793945788838, "lon": 81.77361261386221},
    {"name": "CMR Mall", "lat": 17.006285650143596, "lon": 81.77066111476915},
    {"name": "Markandeya swamy Temple Road", "lat": 17.002419348927187, "lon": 81.76737485108524},
    {"name": "Kathreru Road", "lat": 17.021766650089877, "lon": 81.77483965237695},
    {"name": "Tirumala College Road", "lat": 17.04317118735671, "lon": 81.77557759223698},
    {"name": "Dhavaleswaram Main Road", "lat": 16.95028007716461, "lon": 81.78232137122522},
    {"name": "Church Center Bypass", "lat": 17.004904032408977, "lon": 81.78017113264912},
    {"name": "Central Jail Road", "lat": 17.0183461072747, "lon": 81.79134447760869},
    {"name": "Brothern Church", "lat": 17.02347300450597, "lon": 81.78349635298017},
    {"name": "Quary Market", "lat": 17.032306965496208, "lon": 81.78809778066346},
    {"name": "Airport Road", "lat": 17.04178820195048, "lon": 81.79431781829038},
    {"name": "Rial cum Road Bridge", "lat": 16.99704707573163, "lon": 81.76927353762291},
    {"name": "Main Road", "lat": 16.999891585565052, "lon": 81.77174995367827},
    {"name": "Bhanu Gudi", "lat": 16.970727621131044, "lon": 82.23604297660549},
    {"name": "Vankata Narayana Railway Gate", "lat": 16.973097407997937, "lon": 82.22603037626632},
    {"name": "Munsif Gari Junction", "lat": 16.937053050836603, "lon": 82.23297479867091},
    {"name": "Apt College Road", "lat": 16.92997583523028, "lon": 82.23448294817929},
    {"name": "Dairyfarm Centre", "lat": 16.956302106919356, "lon": 82.24871504989581},
    {"name": "Gaati Center", "lat": 16.93563418662961, "lon": 82.22835108063681},
    {"name": "Nagamalli Thota Centre", "lat": 16.986766105909542, "lon": 82.24004443228684},
    {"name": "Temple Street", "lat": 16.94692319878384, "lon": 82.2319585390418},
    {"name": "Main Road", "lat": 16.9477758788922, "lon": 82.23388897523365},
    {"name": "Sarpavaram Junction", "lat": 16.994895450984338, "lon": 82.24274883366579},
    {"name": "Pr Clg Road", "lat": 16.95806544175642, "lon": 82.23109820773215},
    {"name": "Bala Cheruvu", "lat": 16.95281937073767, "lon": 82.2323379008641},
    {"name": "Nukalamma Temple", "lat": 16.96300884823827, "lon": 82.23441835065452},
    {"name": "Cinema Road", "lat": 16.94826208774934, "lon": 82.23632529143106},
    {"name": "Beach Road", "lat": 17.008947642214952, "lon": 82.28321349284704},
    {"name": "Glass House Centre", "lat": 16.948718637695816, "lon": 82.23396555251772},
    {"name": "Gold Market Centre", "lat": 16.946806476806653, "lon": 82.23381228730807},
    {"name": "Masjid Centre", "lat": 16.951018411377465, "lon": 82.2340447518843},
    {"name": "Fire Office Road", "lat": 16.95625954468796, "lon": 82.23319640172481},
    {"name": "District Court", "lat": 16.957505554489668, "lon": 82.22707180043267},
    {"name": "Ggh", "lat": 16.9551649315784, "lon": 82.23011317679611},
    {"name": "Kokila Centre", "lat": 16.95965297508154, "lon": 82.22372616365254},
    {"name": "Drivers Colony", "lat": 16.9195687218521, "lon": 82.23867107250433},
    {"name": "Rto Office", "lat": 16.975555403090365, "lon": 82.24875195678766},
    {"name": "Vakalapudi Junction", "lat": 17.006117793712892, "lon": 82.26343084127797},
    {"name": "Indrapalem Bridge", "lat": 16.95965297508154, "lon": 82.22372616365254},
    {"name": "Revenue Office", "lat": 16.953915323179874, "lon": 82.23158617323973},
    {"name": "Bus Stand", "lat": 16.968628884485902, "lon": 82.2396254653395},
    {"name": "Jntuk Road", "lat": 16.9733394966521, "lon": 82.23687898351096},
    {"name": "Kalpana Centre", "lat": 16.95614085026494, "lon": 82.23667031643537},
    {"name": "Jagannadhapuram Bridge", "lat": 16.94224348809935, "lon": 82.23327482540806},
    {"name": "Kakinada Anchorage Port", "lat": 16.93999009392696, "lon": 82.25623410490785},
    {"name": "Karnam Gari Junction", "lat": 16.977303001042785, "lon": 82.22772653959622},
    {"name": "Pitapuram Kakinada Road", "lat": 17.001239678156328, "lon": 82.24517313922694},
    {"name": "Pitapuram Kakinada Highway", "lat": 17.05454405203872, "lon": 82.25091475318834},
    {"name": "Achampeta Junction", "lat": 17.022515117068984, "lon": 82.24885404796437},
    {"name": "Satya Gowri Theatre Road", "lat": 16.9448962699546, "lon": 82.23602478600985},
    {"name": "Madhavapatam Centre", "lat": 16.99251444215439, "lon": 82.2106751103578},
    {"name": "Gandhi Circle", "lat": 16.96469875062046, "lon": 82.22472639247694},
    {"name": "Light House", "lat": 17.014006865277864, "lon": 82.28410306612057}
]

API_KEY = "tyNlQV3fROY2ltdXEU4paXe1ZhrmX0Fd"

def get_traffic_level(current_speed, free_flow_speed):
    ratio = current_speed / free_flow_speed
    if ratio >= 0.85:
        return "Low"
    elif ratio >= 0.5:
        return "Medium"
    else:
        return "High"

# Open CSV for appending
with open(r"C:\Users\vamsi\traffic_data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    # Add header if file is empty
    # writer.writerow(["day","hour","area", "lat", "lon", "current_speed", "free_flow_speed", "traffic_level","temperature","code","windspeed"])

    for loc in locations:
        lat, lon = loc["lat"], loc["lon"]
        url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&unit=KMPH&key={API_KEY}"
        response = requests.get(url)
        url2= ("https://api.open-meteo.com/v1/forecast"f"?latitude={lat}&longitude={lon}&current_weather=true")
        response2=requests.get(url2)
        if response.text.strip():  # Check response is not empty
            data = response.json()
            w_data=response2.json()
            temp=w_data["current_weather"]["temperature"]
            code=w_data["current_weather"]["weathercode"]
            wind=w_data["current_weather"]["windspeed"]
            current_speed = data['flowSegmentData']['currentSpeed']
            free_flow_speed = data['flowSegmentData']['freeFlowSpeed']
            traffic_level = get_traffic_level(current_speed, free_flow_speed)
            writer.writerow([datetime.now().weekday(),datetime.now().hour,loc["name"], lat, lon, current_speed, free_flow_speed, traffic_level,temp,code,wind])
        else:
            print(f"No data for {loc['name']} at {lat},{lon}")