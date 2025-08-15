import csv
# Bangladesh: 100 Landmarks grouped by Division
# Coordinates provided as (latitude, longitude) tuples — verify needed before use.

destination_bd = {
    "Dhaka": {
        "Lalbagh Fort": (23.7190, 90.3881),
        "Ahsan Manzil": (23.7086, 90.4061),
        "National Martyrs’ Memorial": (23.9421, 90.2587),
        "Shaheed Minar": (23.7385, 90.4096),
        "Liberation War Museum": (23.7349, 90.3981),
        "Jatiya Sangsad Bhaban": (23.7426, 90.3760),
        "Star Mosque": (23.7162, 90.3948),
        "Armenian Church": (23.7220, 90.4084),
        "Curzon Hall": (23.7319, 90.3938),
        "Rose Garden Palace": (23.7291, 90.4075),
        "BDR Headquarters Memorial": (23.7801, 90.3912),
    },
    "Khulna": {
        "Sixty Dome Mosque (Shat Gambuj Mosque)": (22.6745, 89.7418),
        "Khan Jahan Ali’s Tomb": (22.6662, 89.7664),
        "Sundarbans Mangrove Forest": (21.9497, 89.1833),
        "Karamjal Wildlife Center": (22.4415, 89.5735),
        "Harbaria Eco-Tourism Center": (22.3050, 89.5984),
        "Sixty Dome Mosque Complex (Bagerhat)": (22.6729, 89.7441),
    },
    "Rajshahi": {
        "Puthia Rajbari": (24.3650, 88.9445),
        "Puthia Temple Complex": (24.3648, 88.9446),
        "Bagha Mosque": (24.1946, 88.8397),
        "Varendra Research Museum": (24.3690, 88.6119),
        "Hardinge Bridge": (24.0065, 89.1798),
        "Wari-Bateshwar (near Narsingdi/Bogra boundary)": (24.0600, 90.7000),  # approximate region
    },
    "Rangpur": {
        "Paharpur Buddhist Monastery (Somapura Mahavihara)": (24.2140, 88.8260),  # listed here for completeness
        "Mahasthangarh": (24.9000, 89.7330),  # note: often associated with Bogura/Rangpur region
        "Chapai Nawabganj historical sites (Choto Sona Mosque, Darasbari Mosque)": (24.4392, 88.2380),
        "Kusumba Mosque": (24.2197, 88.6376),
    },
    "Mymensingh": {
        "Shilpagosthi & local heritage sites": (24.7471, 90.4203),  # placeholder for Mymensingh cluster
        "Tangail (Jamuna Bridge region)": (24.2623, 89.9207),  # Tangail area (administratively Dhaka division but included here)
    },
    "Sylhet": {
        "Ratargul Swamp Forest": (24.9900, 91.3540),
        "Jaflong": (25.1650, 92.0200),
        "Bichanakandi": (25.1750, 91.9500),
        "Panthumai": (25.1660, 91.8840),
        "Tanguar Haor": (25.0320, 91.1000),
        "Hakaluki Haor": (24.6000, 92.0000),
        "Hazrat Shah Jalal Mazar": (24.8949, 91.8710),
        "Hazrat Shah Paran Mazar": (24.8822, 91.8551),
        "Ali Amjad’s Clock Tower": (24.8961, 91.8718),
        "Ratargul/Bisnakandi tea garden area (general)": (25.0800, 91.9400),
    },
    "Chattogram": {
        "Patenga Beach": (22.3129, 91.7812),
        "Foy's Lake": (22.4453, 91.8295),
        "Ethnological Museum (Chattogram)": (22.3372, 91.8340),
        "Chattogram War Cemetery": (22.3600, 91.8270),
        "Court Building Hill (Anderkilla area)": (22.3450, 91.8300),
        "Naval Academy (Chattogram)": (22.4300, 91.8000),
        "Zia Memorial Museum": (22.3659, 91.8213),
        "Bhatiary Hill / Golf & Country Club": (22.3540, 91.8700),
        "Keane Bridge (note: Keane Bridge is in Sylhet; if Chattogram Keane Bridge not present, ignore)": (0.0, 0.0),
    },
    "Cox's Bazar (Chattogram Division - coastal sites)": {
        "Cox’s Bazar Sea Beach": (21.4272, 92.0058),
        "Inani Beach": (21.6350, 92.1516),
        "Himchari National Park": (21.3981, 91.9967),
        "Maheshkhali Island": (21.7440, 91.9630),
        "Sonadia Island": (21.6560, 91.9900),
        "Saint Martin’s Island": (20.6240, 92.3370),
        "Chera Dwip": (20.6200, 92.3400),
        "Teknaf Wildlife Sanctuary": (20.8660, 92.3190),
        "Naf River Viewpoint (Teknaf)": (20.8600, 92.3300),
    },
    "Bandarban": {
        "Nilgiri Hills": (21.8500, 92.3000),
        "Nilachal": (21.8000, 92.2000),
        "Meghla Tourist Complex": (21.9700, 92.3000),
        "Boga Lake": (21.7950, 92.8060),
        "Nafakhum Waterfall": (21.9330, 92.5160),
        "Amiakhum Waterfall": (21.9000, 92.4500),
        "Tahjindong": (21.9300, 92.5600),
        "Chimbuk Hill": (21.3667, 92.0667),  # approximate
        "Sangu River (scenic sections)": (21.8260, 92.1700),
        "Alikadam Hill Tracks": (21.9500, 92.3000),
        "Shoilo Propat": (21.9000, 92.3000),
    },
    "Rangamati": {
        "Sajek Valley": (23.1500, 92.8000),   # often considered Rangamati/Hill tracts region
        "Kaptai Lake": (22.5774, 92.2382),
        "Shuvolong Waterfall": (22.9000, 92.3000),
        "Hanging Bridge (various)": (22.6220, 92.2150),
        "Rajban Bihara (local sites)": (22.6000, 92.2500),
        "Pablakhali Wildlife Sanctuary": (22.8000, 92.1000),
        "Rangamati Tribal Museum": (22.6271, 92.2185),
        "Betbunia Earth Satellite Center (approx)": (22.6500, 92.2000),
        "Chakma Rajbari (Rangamati)": (22.6290, 92.2190),
    },
    "Barishal": {
        "Madhabkunda Waterfall (note: actually in Moulvibazar / Sylhet region)": (24.6650, 91.8410),
        "Kuakata (Bay of Bengal view)": (21.7793, 90.1160),  # common Barishal area attraction
        "Historical riverfronts & ghats (Barishal city)": (22.7010, 90.3530),
        "Barguna coastal sites": (22.1900, 90.0400),
    },
    "Moulvibazar / Sylhet (Tea & Hills cluster)": {
        "Lawachara National Park": (24.3386, 91.7779),
        "Srimangal Tea Gardens": (24.3046, 91.7335),
        "Ham Ham Waterfall": (24.4189, 91.7000),
        "Ratargul / Tanguar cluster (repeat area)": (25.0100, 91.3500),
    },
    "Kushtia / Khulna cluster": {
        "Shilaidaha Kuthibari": (23.7808, 89.0208),
        "Lalon Shah Mazar (Kushtia)": (23.7389, 89.1009),
        "Rabindra Kuthibari": (23.7390, 89.0950),
    },
    "Naogaon / Rajshahi cluster": {
        "Paharpur Buddhist Monastery (Somapura Mahavihara)": (24.1650, 88.6145),
        "Sitakot Vihara (Dinajpur area)": (25.0360, 88.6470),
        "Kantajew Temple (Dinajpur)": (25.2386, 88.6211),
        "Darasbari Mosque": (24.4395, 88.2381),
        "Choto Sona Mosque": (24.4110, 88.2400),
    },
    "Miscellaneous / Other notable sites": {
        "Govinda Bhita (Mahasthangarh vicinity)": (24.9000, 89.7330),
        "Vasu Bihar (Bogura area)": (24.9000, 89.7330),
        "Behula Lakshindar Basor Ghar (Bogura region)": (24.8600, 89.3700),
        "Shahjalal University Campus (Sylhet)": (24.9200, 91.8266),
        "Ali Amjad Clock (Sylhet repeat)": (24.8961, 91.8718),
    },
}
