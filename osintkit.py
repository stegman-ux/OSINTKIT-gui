import whois
import customtkinter as ctk
import requests



app = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")




app.title("Osint-kit Gui - By intrable")
app.geometry("900x750")



def whhois():
    link = entry.get()
    whhois = whois.whois(link)
    clear = result_textbox.delete(1.0 , ctk.END)
    result = result_textbox.insert(1.0 ,whhois)

whois_label = ctk.CTkLabel(
    app,
    text="Whois Lookup",
    font=ctk.CTkFont(size=28, weight="bold")  ,
    text_color="red"
)
whois_label.pack()

labeel = ctk.CTkLabel(master=app,text="Lien du site à scanner avec WHOIS : ")
labeel.pack()

entry = ctk.CTkEntry(master=app,width=200,height=10)
entry.pack()

button = ctk.CTkButton(master=app,text="Scanner l'url",command=whhois)
button.pack()


label_info = ctk.CTkLabel(master=app,text="Output de la recherche whois : ")
label_info.pack()

result_textbox = ctk.CTkTextbox(app, height=150,width=3900)
result_textbox.pack()



def ipinfo():
    ip = entry_ip.get()
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    ip_lookup_result = (
    f"[*] Country     : {data.get('country')}\n"
    f"[*] CountryCode : {data.get('countryCode')}\n"
    f"[*] City        : {data.get('city')}\n"
    f"[*] Zip Code    : {data.get('zip')}\n"
    f"[*] Timezone    : {data.get('timezone')}\n"
    f"[*] Org         : {data.get('org')}\n"
    f"[*] Region      : {data.get('region')}\n"
    f"[*] RegionName  : {data.get('regionName')}\n"
    f"[*] AS          : {data.get('as')}\n"
    f"[*] Latitude    : {data.get('lat')}\n"
    f"[*] Longitude   : {data.get('lon')}"
    )
    clear = result_textbox_ip.delete(1.0 , ctk.END)
    result = result_textbox_ip.insert(1.0 ,ip_lookup_result)


ipinfo_label = ctk.CTkLabel(
    app,
    text="Ip Lookup",
    font=ctk.CTkFont(size=28, weight="bold")  ,
    text_color="red"
)
ipinfo_label.pack()

label_ip = ctk.CTkLabel(master=app,text="Adresse IP : ")
label_ip.pack()

entry_ip = ctk.CTkEntry(master=app,width=200,height=10)
entry_ip.pack()

button_ip = ctk.CTkButton(master=app,text="Obtenir les infos de l'ip",command=ipinfo)
button_ip.pack()


label_ip2 = ctk.CTkLabel(master=app,text="Output de la recherche des informations de l'IP : ")
label_ip2.pack()

result_textbox_ip = ctk.CTkTextbox(app, height=150,width=3900)
result_textbox_ip.pack()



def phone():
    phone_number = entry_phone.get()
    response = requests.get(f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_pWHeBCRhv2VgqQ9nFOBTaDEDgVsKeHBa6VE6oghz")
    data = response.json()
    phone_lookup_result = (
    f"[*] Valid              : {data.get('valid')}\n"
    f"[*] Number             : {data.get('number')}\n"
    f"[*] Local Format       : {data.get('local_format')}\n"
    f"[*] International      : {data.get('international_format')}\n"
    f"[*] Country Prefix     : {data.get('country_prefix')}\n"
    f"[*] Country Code       : {data.get('country_code')}\n"
    f"[*] Country Name       : {data.get('country_name')}\n"
    f"[*] Location           : {data.get('location')}\n"
    f"[*] Carrier            : {data.get('carrier')}\n"
    f"[*] Line Type          : {data.get('line_type')}"
    )
    clear = result_textbox_phone.delete(1.0 , ctk.END)
    result = result_textbox_phone.insert(1.0 ,phone_lookup_result)


phone_label = ctk.CTkLabel(
    app,
    text="Phone number Lookup",
    font=ctk.CTkFont(size=28, weight="bold")  ,
    text_color="red"
)
phone_label.pack()

label_phone = ctk.CTkLabel(master=app,text="Numéro de télephone : ")
label_phone.pack()

entry_phone = ctk.CTkEntry(master=app,width=200,height=10)
entry_phone.pack()

button_phone = ctk.CTkButton(master=app,text="Obtenir les infos du numéro.",command=phone)
button_phone.pack()


label_phone2 = ctk.CTkLabel(master=app,text="Output de la recherche des informations du numéro : ")
label_phone2.pack()

result_textbox_phone = ctk.CTkTextbox(app, height=150,width=3900)
result_textbox_phone.pack()

app.mainloop()
