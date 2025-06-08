import sqlite3
import random
import os

# Comment out the deletion if you want to update slots on each run
# if os.path.exists("parking.db"):
#     os.remove("parking.db")

# Connect to SQLite database
conn = sqlite3.connect('parking.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS parking_locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    latitude REAL,
    longitude REAL,
    total_slots INTEGER,
    empty_slots INTEGER
)
''')

# Example locations (you forgot to define "locations" in your code)
locations = {
    "Location A": (22.5726, 88.3639),
    "Location B": (22.5856, 88.4021),
    "Location C": (22.5678, 88.3680),
}

# Function to generate total and empty slots realistically
def generate_random_parking_data():
    total = random.randint(20, 50)
    empty = random.randint(0, total)
    return total, empty

# Realistic coordinates for each location (expanded)
locations = {
    
    #Victoria Memorial
    "Parking place": (22.545589118045232, 88.34792759316451),
    "Paid bike and Car PArking": (22.544637862109354, 88.35131790513401),
    "Camac Street parking ground":(22.544281139443118, 88.35239078866867),
    "Sorvey parking": (22.556924413289238, 88.35054542898908),
    "Park-o-mart": (22.56009495861151, 88.3520045513607),
    "Pataka house public parking": (22.554308658642757, 88.35384991104029),
    "Car Parking": (22.550900176576018, 88.355266117306),
    "Govt. college parking": (22.557809208917643, 88.35148537365744),
    "Parking": (22.545888859170574, 88.35240732626073),
    "Parking, KMC Road Side Car & Bike Paid Parking Nandan Exide Crossing": (22.542143828872025, 88.34560753168144),

    #Howrah
    "Howrah station parking place": (22.58252696102351, 88.34322275623938),
    "Howrah Station new complex outside parking": (22.581558870724923, 88.34243639902463),
    "Car parking": (22.582103422354944, 88.34931702465373),
    "Bortola car parking lot": (22.57901760132563, 88.35252798328067),
    "Parking": (22.58137735303659, 88.35469046562122),
    "Car Parking": (22.57393492171172, 88.35691847818273),
    "Chandni chowk parking": (22.56733926066976, 88.35429728746688),
    "Parked Car": (22.56861000890042, 88.35239692419789),
    "PCA parking": (22.567581308854834, 88.34158451249502),
    "Court Parking": (22.57272473231819, 88.34577841764037),

    #Indian Museum
    "New Market parking Kol": (22.559977078424673, 88.35390326691301),
    "Dharmatala sahid minar": (22.560532904059464, 88.35254248610022),
    "New market car parking": (22.56157205032424, 88.35105086097848),
    "Sribridhi bhwan Parking": (22.55345200131181, 88.3500041065071),
    "Lindsay street cab parking": (22.560122076632318, 88.3508415100842),
    "car parking on street": (22.554660372212247, 88.35594443813223),
    "Jeewan sudha parking": (22.549270956267414, 88.34882650777371),
    "DMI finance office": (22.55891375350755, 88.36578393069895),
    "Car parking": (22.550551867849546, 88.35521171056915),
    "Paid parking place": (22.553887015936024, 88.35235930463459),

    #Dakshineswar Kali Temple
    "Dakshineswar kali temple car parking lot 1": (22.655520854062196, 88.35874134155563),
    "Dakshineswar kali temple car parking 2": (22.657124579152857, 88.35849308014613),
    "Railway parking": (22.65799516492667, 88.36196873987888),
    "Abhoys Car parking": (22.65620816710967, 88.36762910001507),
    "Apanjan Car Parking": (22.653229785716313, 88.37259432820471),
    "Car parking": (22.666746536169143, 88.3579469050453),
    "Ranjit Mondal": (22.664638927102285, 88.3754741605547),
    "Suman Car park": (22.666700718924993, 88.37651685847452),
    "Car garage": (22.664868016612637, 88.36723188175989),
    "Adyapeeth parking": (22.66166693134319, 88.3631376057541),

    #Kalighat
    "Hindi party in bengal": (22.52122353367575, 88.34425222230176),
    "Kalighat car parking": (22.522571372825116, 88.3438659842293),
    "car parking": (22.525187728934444, 88.35094701555794),
    "Paban Home": (22.51741779922902, 88.34858667178173),
    "Parking rashbehari": (22.51753673001689, 88.35073243885101),
    "LT ParkSmart": (22.515871689673535, 88.33502542390382),
    "Consultivo parking": (22.516188841761608, 88.34687005812629),
    "Alipore Museum parking": (22.526416606369096, 88.33429586310027),
    "Prepaid parking lot": (22.518329599320527, 88.33618413812124),
    "Bike stand": (22.517378155610327, 88.34571134390889),
    
    #Science City
    "Science city parking area": (22.542831723134395, 88.39503430247208),
    "TB Parking": (22.53637085190953, 88.39134358311291),
    "Labbaik Apartment": (22.537996007489266, 88.38782452511927),
    "Bantalla Dumping ground": (22.53569700130309, 88.40052746616946),
    "My Parking": (22.53288264851783, 88.3946480643996),
    "Abhishek House": (22.543426266642587, 88.38203095403219),
    "Pankaj Kumar Yadav": (22.52943399718806, 88.3974375615897),
    "SWASTIK VALET SERVICE - Best Valet Parking Specialist": (22.530227586560127, 88.37909347156847),
    "Karim Ka Parking": (22.533081632734795, 88.3796084575649),
    "My Parking": (22.53387441282784, 88.39385635090497),

    #Nicco Park
    "Parking area Nicco Park": (22.57108285464943, 88.41999376489933),
    "SNBNCBS parking": (22.569497717453675, 88.41664636827126),
    "Parking lot": (22.568824028625883, 88.41192568071881),
    "PARKOSi Digital Smart Parking": (22.573143505752093, 88.42883432522481),
    "Parkwiz:The best parking": (22.5778194843569, 88.4273322882763),
    "Rudra's Parking": (22.583208551008603, 88.42076624104429),
    "Parking place": (22.573302016099305, 88.413170225619),
    "Nalban Car parking": (22.568110707455066, 88.43286836731508),
    "Webel More PArking Lane": (22.573658663714014, 88.43213880651152),
    "Salt lake Sector 5 parking ground": (22.576630691278094, 88.4321817218529),

    #College Street
    "Money view": (22.571816891471922, 88.36623940149235),
    "Paid parking": (22.570063020358557, 88.36244069775744),
    "Amtoli bypass word office": (22.571703739170296, 88.3699768358122),
    "Tairaj": (22.574136493184177, 88.35956103524869),
    "Sealdah Parking": (22.56847885952724, 88.36991556639711),
    "My Car Parking": (22.579680748847036, 88.36170546477648),
    "Pension Office": (22.57809669856273, 88.36378862488917),
    "Bike Parking": (22.57781383052425, 88.36274704483282),
    "Paid Parking": (22.569788699429747, 88.36201101354625),
    "Alqamar": (22.577234382562104, 88.36099137290168),

    #Shyambazar
    "Bikash": (22.59187157514851, 88.38000247971667),
    "Belgachia Jheel Parking": (22.60346089652713, 88.38611384374259),
    "R G Kar Car Parking Area": (22.607272960011354, 88.37835075970966),
    "My Garage": (22.60635807440625, 88.37042250367602),
    "Golabari Car Parking": (22.59568395960175, 88.34564670357089),
    "Bada Bazar Parking": (22.58561903571333, 88.35506150731439),
    "Court Parkig": (22.574943313182487, 88.34548153127373),
    "Duttabagan": (22.61093478470445, 88.39159417300392),
    "Rocky": (22.60490818918293, 88.40455022775336),
    "Rudra's Parking": (22.583581193745342, 88.42122236022166),

    #Rajarhat
    "Spencer's Chiner Park": (22.62589778337664, 88.43870427377581),
    "M M Parking space": (22.621063403084683, 88.43677143012611),
    "THE DAY & NIGHT CAR PARKING": (22.616861958355777, 88.4291647551176),
    "Space centre underground car parking": (22.628890409792593, 88.43028705143034),
    "Singha Roy Car Parking": (22.619049027794762, 88.44599919980857),
    "CC2 parking lot": (22.62422879034623, 88.45030133567407),
    "Neelesh House Kolkata": (22.65255649346697, 88.42671897677052),
    "UTSAV parking plcae": (22.65188478748504, 88.42186662461047),
    "UMPESL CESC METER ROOM": (22.651362347227078, 88.4363428085546),
    "Parking lot": (22.650839904981126, 88.4390116022426),

    #New Town 
    "Aircraft Museum Parking": (22.577949252417852, 88.47687115024564),
    "Biswa Bangla Parking": (22.579019156412333, 88.47103466381718),
    "Newtown Sarbojanin Parking": (22.584447800503398, 88.45850338413254),
    "Vibgyor Parking": (22.578107757237543, 88.45485558011474),
    "JVT basement parking": (22.568438629610817, 88.47275127747261),
    "DA-87": (22.572916629604272, 88.46326698702637),
    "Snape Hub": (22.585279909521255, 88.47717155763533),
    "NKDA parking space": (22.57770692851013, 88.47852074953762),
    "Cafe Ekante car parking": (22.60491813497006, 88.45406711935186),
    "DLF1 parking": (22.58399799446734, 88.44823063292338),

    #Rabindra Sarobar
    "Rabindra Sarobar Parking": (22.511783501139213, 88.35444861229682),
    "Lake Club's parking": (22.511426693617782, 88.35427695093128),
    "Gol Park": (22.51638227120561, 88.36676531527455),
    "Parking Place under Gariahat Bridge": (22.520901603056814, 88.3647912095708),
    "Deshapriya Parking lot": (22.519910534162136, 88.3530324060311),
    "Consultivo Parking": (22.51626333942431, 88.3469384275543),
    "Begbagan Store": (22.54087479926963, 88.36347966779375),
    "Chittaranjan Hospital Parking Area": (22.54737509471716, 88.37141900595014),
    "Parkomart": (22.547573269647252, 88.35978894843457),
    "Quest Mall Parking": (22.539408226876827, 88.36601167293551),
    
    #Botanical garden
    "Toto Parking Garage": (22.559361561916877, 88.2822178612368),
    "Car Parking": (22.57317864228375, 88.30820095455819),
    "Shalimar Station Car Parking Area": (22.55770672891663, 88.31268079823428),
    "Car Parking": (22.564243203626557, 88.29959965528961),
    "Das Parking": (22.572185844408477, 88.31079926447985),
    "Multi level Car Parking": (22.569041937150978, 88.31420394567368),
    "Nabanna Car parking": (22.569869288118113, 88.31420394567368),
    "Car Parking Area": (22.571275773388905, 88.30963450499308),
    "Narayana Hospital Car Parking": (22.564044169243353, 88.30764750522239),
    "Saddam Toto And Bike Parking": (22.56389700678309, 88.31610958677958),

    #South city Mall
    "South city mall parking lot2": (22.500537165039795, 88.36287659059701),
    "ParkWiz": (22.50110555952751, 88.36243361634826),
    "Mall Parking Lot": (22.50123702792128, 88.36175768392732),
    "South city Mall rooftop Parking": (22.501499964333924, 88.36216680091894),
    "Parking reserve": (22.500037374145332, 88.35665261524505),
    "IICB Parking Lot": (22.497950280539577, 88.36949533153715),
    "Clean City KMC": (22.496290443399804, 88.37527633259779),
    "KPC parking ground": (22.493529482159403, 88.37472491441272),
    "Rajib Bhadra Car Parking": (22.491244304771712, 88.38553815864718),
    "Kamarpara Adibasibrinda Parking Lot": (22.49298894297152, 88.37652593690619),

    #Princepghat
    "Netaji Parking": (22.566193972375377, 88.34197741155059),
    "Raj Bhawan Parking 1": (22.569205789641114, 88.34811430536874),
    "PCA parking": (22.56777914755923, 88.34163408881949),
    "Civil Parking": (22.569998362322096, 88.34305029511656),
    "OFFICE parking": (22.56900764591654, 88.3461831150377),
    "Parking Area": (22.56813580958997, 88.34274988772684),
    "The 42 Parking": (22.54879547710775, 88.3495734268988),
    "Parking Place": (22.545267952042806, 88.34781389790196),
    "SCHOOL PARKING": (22.548320953661683, 88.34844388593359),
    "Simpark": (22.544869219596706, 88.35837773765866),

    #New Garia
    "Neotia Car Parking": (22.475218789183828, 88.40036427280295),
    "Upohar Parking": (22.47632336545683, 88.40106157512595),
    "Srijit Kumar Dey": (22.474390351197655, 88.40823382759098),
    "Gariya Parking": (22.470722762501836, 88.40414822254183),
    "Sanjiv Sanyal 5561": (22.468975398363806, 88.404006403443),
    "Garia Station": (22.467970654004446, 88.40362821917945),
    "Car Parking": (22.481034906115866, 88.38297447082483),
    "RN Tagore Hospital Parking": (22.49348482148613, 88.40177004089115),
    "Vehicle Parking metro Cash and carry": (22.4950250236613, 88.39893055095962),
    "Ruby general hospital Car Parking": (22.514868116550804, 88.40281794469087),

    #Quest Mall
    "Quest Mall Parking": (22.538808366043412, 88.36573942060788),
    "Begbagan Store": (22.540829199258017, 88.36339981513788),
    "Z's Auto World": (22.54042903660736, 88.37063526230318),
    "Birla Mandir Car Parking": (22.530444603006664, 88.36534948677901),
    "Karim Ka Parking": (22.5318052495781, 88.37917048975225),
    "Kasba Bazaar Parking": (22.521238602241688, 88.37323265054805),
    "SSB GTO ground": (22.523064942233297, 88.3764320109659),
    "Youth Corner": (22.51764342440116, 88.36488772762551),
    "Gol Park": (22.51648816358413, 88.36653325339846),
    "Car Parking": (22.525851578429734, 88.35764741422457),

    #Birati
    "Biswas House": (22.67166226507335, 88.42278805735648),
    "Neelesh House Kolkata": (22.652494901242985, 88.42656460794609),
    "UTSAV parking place": (22.65138596357947, 88.42218724312474),
    "Alok Sangha parking place": (22.651148332914815, 88.41394749757866),
    "Parking": (22.652257272497692, 88.4132608521165),
    "Rajat car parking": (22.65954436690892, 88.4165224180618),
    "7971 car parking": (22.649257445509697, 88.45665984430201),
    "Udayan Sangha club Car parking": (22.666865944193646, 88.46005786217454),
    "Middle": (22.644915276781546, 88.45561430034122),
    "Parking lot": (22.651549090315868, 88.43888559696876),

    #St.Xavier's College
    "Paid parking": (22.57936274041886, 88.48590553317301),
    "Block L basement parking": (22.58150251814843, 88.4856480411247),
    "s-parking": (22.589982051196053, 88.4853047183936),
    "Narayana School Parking": (22.59901574560706, 88.49114120482207),
    "Car Parking": (22.578570221715385, 88.47852409445466),
    "Visitor's Parking": (22.564380742599457, 88.49534688817648),
    "JVT basement parking": (22.568819245557872, 88.47217260382818),
    "Mega Earth project": (22.55243610849858, 88.51354686542419),
    "Dark Knight 4795": (22.569625636624522, 88.51165848518795),
    "DPS megacity bus parking": (22.58963586568074, 88.49870959188843),

    #Dum Dum
    "Car Parking Plot": (22.63299605169943, 88.40256719181373),
    "D Mandal": (22.63426357802097, 88.40445546568225),
    "Loknath Parking": (22.614811501335893, 88.4237139296293),
    "Ambagan Gas Godown": (22.615009579276233, 88.42058111014735),
    "Laketown Garage Rental": (22.61259300878161, 88.41697622147093),
    "RKG garage": (22.62935555086171, 88.42553793785433),
    "Parking": (22.634980258609644, 88.41618239343224),
    "Ethereum": (22.624126742847345, 88.42244803327456),
    "Saha Para More": (22.61687738452052, 88.42828451970588),
    "Smart Bazar Parking Space": (22.617115369358473, 88.43194371947180),

    #Shibpur
    "Das Parking": (22.57093860826868, 88.31086258675954),
    "Car Parking Area": (22.570535121848394, 88.30982482025365),
    "Car Parking": (22.571720359846942, 88.30794045475615),
    "Nabanna Car Parking complex": (22.56848804989445, 88.31482183086256),
    "Multi level car parking": (22.56822291176554, 88.31454906161673),
    "Mandir tala parking": (22.56946905652782, 88.31697527252791),
    "Mukherjee Garage Shibpur": (22.57445352305155, 88.31777922398344),

    #Santragachi
    "Santragachi parking lot 2": (22.585289204379116, 88.28550673359973),
    "Baksara Milan Tirtha": (22.58247586337238, 88.28945494500722),
    "Rainbow Apartment car parking lot": (22.59047986584182, 88.27962733182989),

    #Dasnagar
    "Shiv Durga Wrigh Bridge": (22.60839931968479, 88.315151154276),
    "Tirupati Balaji Banquet tower 2": (22.61228177651158, 88.31055921274772),
    "Todi Parking": (22.604073317843838, 88.323482962714440),

    #Belur
    "Underground car parking": (22.63072159641546, 88.3576543266345),
    "NEXA Parking": (22.628995569201443, 88.35502247666949),
    "Belur Math Parking": (22.632703304633495, 88.35183655302761),
    
    #Garden Reach
    "New House": (22.547364837353783, 88.28609762721494),
    "Maharaj Parking": (22.536635176153773, 88.29109744840298),

    #Metiaburuj
    "Ashik House": (22.5150026658439, 88.25419799203176),
    
    #Khiddirpore
    "Multilevel car parking system": (22.538342616004368, 88.32347382596883),

    #Taratala
    "Mullik builder's car parking": (22.516202007828344, 88.29137093301253),
    "Car parking lot": (22.516162363860918, 88.30918079968762),
    "Parking lot": (22.51203932916439, 88.30497509623181),

    #Behala 
    "14 no, parking lot": (22.503028975487442, 88.31878130889822),
    "Saha Parking": (22.499282896194153, 88.32090342665002),
    "Behala trum depo bike and car parking zone": (22.499983105640723, 88.31874341393836),
    "Tavera": (22.50068331154278, 88.31309706492024),
    "New": (22.50516454537644, 88.31870551897852),
    "Free parking lot": (22.510100736440872, 88.32548871679225),

    #Majherhat
    "Sunil Yadav": (22.522574299332277, 88.32364768390516),

    #joka
    "Roni": (22.453493918708446, 88.3024765020883),
    "South end hotel parking": (22.456733749186906, 88.30135695312671),
    "Sristir Parking zone": (22.46192903823908, 88.30654423854695),

    #Bansdroni
    "Maa Tara parking": (22.47444344911166, 88.36135179395991),
    "Kali Mandir Auto Stand": (22.474086545292018, 88.35976392632863),

    #haridepur
    "Basuri bagan parking": (22.480455770083093, 88.33768090364377),
    "Car Parking": (22.47946441135509, 88.334590999064),

    #Nangi
    "Mitra Car Parking": (22.49722103131581, 88.21648747692707),
    "Maa Sidheswari parking": (22.496229792667084, 88.21434170985779),
    "Suva Parking": (22.501216607809887, 88.22610217351668),
    "Maa Dhanalaxmi enterprice": (22.501042260806248, 88.22495273754241),
    



}
# Check if table has data
cursor.execute('SELECT COUNT(*) FROM parking_locations')
count = cursor.fetchone()[0]

if count == 0:
    # Insert new records
    for name, (lat, lon) in locations.items():
        total, empty = generate_random_parking_data()
        cursor.execute('''
            INSERT INTO parking_locations (name, latitude, longitude, total_slots, empty_slots)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, lat, lon, total, empty))
    print("Inserted all locations with total and initial empty slots.")
else:
    # Update only empty slots
    cursor.execute('SELECT id, total_slots FROM parking_locations')
    for row in cursor.fetchall():
        id, total = row
        new_empty = random.randint(0, total)
        cursor.execute('UPDATE parking_locations SET empty_slots = ? WHERE id = ?', (new_empty, id))
    print("Updated only empty_slots for all locations.")

conn.commit()
conn.close()

print("Database updated successfully.")
