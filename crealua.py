import os
import re
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk  # Nécessite Pillow : pip install pillow
from PIL import Image, ImageTk, ImageEnhance
from tkinter import BooleanVar
import traceback
import webbrowser





current_file = None





translations = {
    "en": {
        "title": "CREALUA",
        "files": "Files",
        "template": "Template",
        "option": "Option",
        "open_file": "Open File",
        "save_file": "Save File",
        "new_project": "New Project",
        "languages": "Languages",
        "parameter":"Parameter",
        "compte": "Account",
        "exit": "Exit",
        "success_save": "File saved successfully: ",
        "save_prompt": "Do you want to save the current file?",
        "success_new_project": "New project created successfully!",
        "error_fields": "All fields must be filled.",
        "menu_templates0": "Snow cannon",
        "menu_templates1": "Snow groomer",
        "menu_templates2": "Snowmobile",
        "menu_templates3": "Object",
        "menu_templates4": "Mod parameter",
        "en": "English",
        "fr": "French",
        "es": "Spanish",
        "it": "Italian",
        "ru": "Russian",
        "de": "German",
        "mapping_btn": "Mapping",
        "add_slopes": "Add slopes to lua",
        "add_adv": "Please add your tracks when all your info layers are finished!",
        "change_color": "Change floor paint",
        "change_size": "Change size map",
    },
    "fr": {
        "title": "CREALUA",
        "files": "Fichiers",
        "template": "Modèles",
        "option": "Option",
        "open_file": "Ouvrir un fichier",
        "save_file": "Enregistrer le fichier",
        "new_project": "Nouveau projet",
        "languages": "Langues",
        "parameter":"Paramètre",
        "compte": "Compte",
        "exit": "Quitter",
        "success_save": "Fichier sauvegardé avec succès: ",
        "save_prompt": "Voulez-vous sauvegarder le fichier actuel ?",
        "success_new_project": "Nouveau projet créé avec succès !",
        "error_fields": "Tous les champs doivent être remplis.",
        "menu_templates0": "Canon à neige",
        "menu_templates1": "Dameuse",
        "menu_templates2": "Motoneige",
        "menu_templates3": "Objet",
        "menu_templates4": "Paramètre du mod",
        "en": "Anglais",
        "fr": "Français",
        "es": "Espagnol",
        "it": "Italien",
        "ru": "Russe",
        "de": "Allemand",
        "mapping_btn":"Cartographie",
        "add_slopes": "Ajouter des pistes au Lua",
        "add_adv":"Merci d'ajouter vos piste lorsque tous vos info layer sont fini !",
        "change_color": "Changer de peinture de sol",
        "change_size": "Changer la taille de la map",
    },
    "de": {
        "title": "CREALUA",
        "files": "Dateien",
        "template": "Vorlagen",
        "option": "Option",
        "open_file": "Eine Datei öffnen",
        "save_file": "Datei speichern",
        "new_project": "Neues Projekt",
        "languages": "Sprachen",
        "parameter":"Parameter",
        "compte": "Konto",
        "exit": "Beenden",
        "success_save": "Datei erfolgreich gespeichert:",
        "save_prompt": "Möchten Sie die aktuelle Datei speichern?",
        "success_new_project": "Neues Projekt erfolgreich erstellt!",
        "error_fields": "Alle Felder müssen ausgefüllt werden.",
        "menu_templates0": "Schneekanone",
        "menu_templates1": "Groomer",
        "menu_templates2": "Schneemobil",
        "menu_templates3": "Item",
        "menu_templates4": "Einstellung",
        "en": "Englisch",
        "fr": "Französisch",
        "es": "Spanisch",
        "it": "Italienisch",
        "ru": "Russisch",
        "de": "Deutsch",
        "mapping_btn":"Abbildung",
        "add_slopes": "Hinzufügen von Steigungen zum Lua",
        "add_adv":"Bitte fügen Sie Ihre Tracks hinzu, wenn alle Ihre Infoebenen fertig sind!",
        "change_color": "Bodenfarbe wechseln",
        "change_size": "Ändern Sie die Größe der Karte",
    },
    "es": {
        "title": "CREALUA",
        "files": "Archivos",
        "template": "Plantillas",
        "option": "Opción",
        "open_file": "Abrir archivo",
        "save_file": "Guardar archivo",
        "new_project": "Nuevo proyecto",
        "languages": "Idiomas",
        "parameter":"Parámetro",
        "compte": "Cuenta",
        "exit": "Salir",
        "success_save": "Archivo guardado con éxito: ",
        "save_prompt": "¿Quieres guardar el archivo actual?",
        "success_new_project": "¡Nuevo proyecto creado con éxito!",
        "error_fields": "Todos los campos deben ser completados.",
        "menu_templates0": "Cañón de nieve",
        "menu_templates1": "Pistero",
        "menu_templates2": "Motonieve",
        "menu_templates3": "Objeto",
        "menu_templates4": "Parámetro del mod",
        "en": "Inglés",
        "fr": "Francés",
        "es": "Español",
        "it": "Italiano",
        "ru": "Ruso",
        "de": "Alemán",
        "mapping_btn":"Cartografía",
        "add_slopes": "Agregar pendientes a la lua",
        "add_adv":"¡Agregue sus pistas cuando todas sus capas de información estén terminadas!",
        "change_color": "Cambiar pintura del piso",
        "change_size": "Cambiar el tamaño del mapa",
    },
    "it": {
        "title": "CREALUA",
        "files": "File",
        "template": "Modelli",
        "option": "Opzione",
        "open_file": "Apri file",
        "save_file": "Salva file",
        "new_project": "Nuovo progetto",
        "languages": "Lingue",
        "parameter":"Parametro",
        "compte": "Account",
        "exit": "Esci",
        "success_save": "File salvato con successo: ",
        "save_prompt": "Vuoi salvare il file attuale?",
        "success_new_project": "Nuovo progetto creato con successo!",
        "error_fields": "Tutti i campi devono essere compilati.",
        "menu_templates0": "Cannon a neve",
        "menu_templates1": "Groomer",
        "menu_templates2": "Motoslitta",
        "menu_templates3": "Oggetto",
        "menu_templates4": "Parametro del mod",
        "en": "Inglese",
        "fr": "Francese",
        "es": "Spagnolo",
        "it": "Italiano",
        "ru": "Russo",
        "de": "tedesco",
        "mapping_btn":"Mappatura",
        "add_slopes": "Aggiungi piste al lua",
        "add_adv":"Aggiungi le tue tracce quando tutti i livelli di informazioni sono finiti!",
        "change_color": "Cambia la vernice del pavimento",
        "change_size": "Cambia la dimensione della mappa",
    },
    "ru": {
        "title": "КРЕАЛУА",
        "files": "Файлы",
        "template": "Шаблоны",
        "option": "Опции",
        "open_file": "Открыть файл",
        "save_file": "Сохранить файл",
        "new_project": "Новый проект",
        "languages": "Языки",
        "parameter":"Параметр",
        "compte": "Счет",
        "exit": "Выход",
        "success_save": "Файл успешно сохранен: ",
        "save_prompt": "Вы хотите сохранить текущий файл?",
        "success_new_project": "Новый проект успешно создан!",
        "error_fields": "Все поля должны быть заполнены.",
        "menu_templates0": "Снегопад",
        "menu_templates1": "Грумер",
        "menu_templates2": "Снегоход",
        "menu_templates3": "Объект",
        "menu_templates4": "Параметры мода",
        "en": "Английский",
        "fr": "Французский",
        "es": "Испанский",
        "it": "Итальянский",
        "ru": "Русский",
        "de": "немецкий",
        "mapping_btn":"картографирование",
        "add_slopes":"добавить уклоны в lua",
        "add_adv":"Пожалуйста, добавьте свои треки, когда все ваши информационные слои будут готовы!",
        "change_color": "Сменить краску пола",
        "change_size": "Изменить размер карты",
    }
}





current_language = "en"


def set_language(lang):
    global current_language
    current_language = lang
    update_texts()

def update_texts():
    """Met à jour tous les textes de l'interface utilisateur."""
    root.title(translations[current_language]["title"])
    files_button.config(text=translations[current_language]["files"])
    template_button.config(text=translations[current_language]["template"])
    option_menu_button.config(text=translations[current_language]["option"])
    mapping_menu_button.config(text=translations[current_language]["mapping_btn"])

def Save_files(event=None):
    global current_file
    if current_file:
        with open(current_file, 'w') as file:
            file.write(editor.get(1.0, tk.END).strip())
        messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{current_file}")
    else:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".lua",
            filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(editor.get(1.0, tk.END).strip())
            current_file = file_path
            messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{file_path}")
            root.title(f"{translations[current_language]['title']} - {file_path}")

def Open_files():
    file_path = filedialog.askopenfilename(
        filetypes=[("Fichiers lua", "*.lua"), ("Tous les fichiers", "*.*")]
    )
    if file_path:
        if file_path.endswith(".lua"):
            with open(file_path, 'r') as file:
                contenu = file.read()

            # Créer une nouvelle fenêtre pour l'éditeur de texte
            editor_window = tk.Toplevel(root)
            editor_window.title(f"CREAVIEW - {file_path}")
            editor_window.geometry("1300x700")  # Vous pouvez ajuster la taille de la fenêtre

            # Créer l'éditeur de texte dans cette nouvelle fenêtre
            editor = tk.Text(editor_window, wrap="none", font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
            editor.insert(tk.END, contenu)
            editor.pack(fill="both", expand=True, padx=5, pady=5)

            # Ajouter des barres de défilement
            scroll_y = tk.Scrollbar(editor_window, orient="vertical", command=editor.yview)
            scroll_y.pack(side="right", fill="y")
            scroll_x = tk.Scrollbar(editor_window, orient="horizontal", command=editor.xview)
            scroll_x.pack(side="bottom", fill="x")
 
            # Lier les barres de défilement à l'éditeur
            editor.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

            # Mettre à jour le titre de la fenêtre principale pour indiquer le fichier ouvert
            root.title(f"CREALUA - {file_path}")
        else:
            root.title(f"CREALUA - {file_path} (Non Lua)")




def open_new_snowmobile():
   
    new_project_frame = tk.Frame(root, bg="#23272e")
    new_project_frame.pack(fill="both", expand=True, padx=5, pady=5)
    

   
    labels_and_fields = [
        ("contentName:", "contentName"),
        ("title:", "title"),
        ("fullDesc:", "fullDesc"),
        ("techSpecs:", "techSpecs"),
        ("previewFilename:", "previewFilename"),
        ("logoFilename:", "logoFilename"),
        ("author:", "author"),
        ("shopCategory:", "shopCategory"),
        ("price:", "price"),
        ("depreciationPeriod:", "depreciationPeriod"),
        ("prefab:", "prefab"),
        ("maxRpm:", "maxRpm"),
        ("maxSpeed:", "maxSpeed"),
        ("strobeLights:", "strobeLights"),
    ]
    labels_and_fields1 = [
        ("wheelRadius:", "wheelRadius"),
        ("maxBrakeTorque:", "maxBrakeTorque"),
        ("parkingBrakeTorque:", "parkingBrakeTorque"),
        ("steeringAngle:", "steeringAngle"),
        ("steeringWheelIndex:", "steeringWheelIndex"),
        ("steeringWheelAngle:", "steeringWheelAngle"),
        ("steeringWheelAxis:", "steeringWheelAxis"),
        ("steeringAnimationIndex:", "steeringAnimationIndex"),
        ("rpmPointerIndex:", "rpmPointerIndex"),
        ("rpmPointerMaxAngle:", "rpmPointerMaxAngle"),
        ("speedPointerIndex:", "speedPointerIndex"),
        ("speedPointerMaxAngle:", "speedPointerMaxAngle"),
        ("fuelUsagePerHour:", "fuelUsagePerHour"),
    ]
    labels_and_fields2 = [
        ("fuelUsagePer100Km:", "fuelUsagePer100Km"),
        ("fuelTankCapacity:", "fuelTankCapacity"),
        ("leftWheelFrontIndex:", "leftWheelFrontIndex"),
        ("rightWheelFrontIndex:", "rightWheelFrontIndex"),
        ("leftWheelRearIndex:", "leftWheelRearIndex"),
        ("rightWheelRearIndex:", "rightWheelRearIndex"),
        ("gears:", "gears"),
        ("gearLabels:", "gearLabels"),
        ("motorFinalDriveRatio:", "motorFinalDriveRatio"),
        ("motorMaxRpm:", "motorMaxRpm"),
        ("motorInertiaMoment:", "motorInertiaMoment"),
        ("motorTorqueCurve:", "motorTorqueCurve"),
        ("automaticDrive (true or false):", "automaticDrive"),
    ]
    labels_and_fields3 = [
        ("automaticLowerLimitRpm:", "automaticLowerLimitRpm"),
        ("automaticUpperLimitRpm:", "automaticUpperLimitRpm"),
        ("automaticGearSwitchPace:", "automaticGearSwitchPace"),
        ("seatIndex:", "seatIndex"),
        ("cameraIndex:", "cameraIndex"),
        ("leaveIndex:", "leaveIndex"),
        ("cameraSlot:", "cameraSlot"),
        ("gearLabels:", "gearLabels"),
        ("cameraIndex:", "cameraIndex"),
        ("cameraRotationIndex:", "cameraRotationIndex"),
        ("cameraZoomIndex:", "cameraZoomIndex"),
        
        ("headlights:", "headlights"),
        ("headlightsInverse:", "headlightsInverse"),
    ]
    #labels_and_fields4 = [
    #    ("strobeLights:", "strobeLights"),
    #]


    entries = {}

    
    
    
    for idx, (label_text, entry_key) in enumerate(labels_and_fields):
        tk.Label(new_project_frame, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=1, padx=10, pady=10)
        entry = tk.Entry(new_project_frame, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=2, padx=10, pady=10)
        entries[entry_key] = entry

    for idx, (label_text, entry_key) in enumerate(labels_and_fields1):
        tk.Label(new_project_frame, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=3, padx=10, pady=10)
        entry = tk.Entry(new_project_frame, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=4, padx=10, pady=10)
        entries[entry_key] = entry

    for idx, (label_text, entry_key) in enumerate(labels_and_fields2):
        tk.Label(new_project_frame, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=5, padx=10, pady=10)
        entry = tk.Entry(new_project_frame, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=6, padx=10, pady=10)
        entries[entry_key] = entry  

    for idx, (label_text, entry_key) in enumerate(labels_and_fields3):
        tk.Label(new_project_frame, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=7, padx=10, pady=10)
        entry = tk.Entry(new_project_frame, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=8, padx=10, pady=10)
        entries[entry_key] = entry  
    
    #for idx, (label_text, entry_key) in enumerate(labels_and_fields4):
    #    tk.Label(new_project_frame, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=9, padx=10, pady=10)
    #    entry = tk.Entry(new_project_frame, bg="#4d4f54", fg="white")
    #    entry.grid(row=idx, column=10, padx=10, pady=10)
    #    entries[entry_key] = entry  
    
    ## Dynamically adding fields to the Lua content based on the 'labels_and_fields' list
    #for label, field in labels_and_fields:
    #    value = form_values.get(field, "")
    #    lua_content += f'    {label}                = "{value}",\n'

   
    def submit_form():
      
        form_values = {key: entry.get() for key, entry in entries.items()}



        if all(form_values.values()):
            is_placeable = "true" if form_values["isPlaceable"].lower() == "true" else "false"
            is_kinematic = "true" if form_values["isKinematic"].lower() == "true" else "false"

        lua_content = f'''--
-- Winter Resort Simulator - Modding lua generator
--
-- Modding lua generator CREALUA by naligator
--

ModLoader.addContent("vehicle", {{
    contentName                = "{form_values['contentName']}",
    title                    = "{form_values['title']}",
    fullDesc                = "{form_values['fullDesc']}",
    techSpecs                = "{form_values['techSpecs']}",
    previewFilename            = "{form_values['previewFilename']}",
    logoFilename            = "{form_values['logoFilename']}",
    
    author                    = "{form_values['author']}",
    shopCategory            = "{form_values['shopCategory']}",
    price                    = {form_values['price']},
    length                    = {form_values['length']},
    width                    = {form_values['width']},
    depreciationPeriod        = {form_values['depreciationPeriod']},
    
    class                    = Vehicle,
    prefab                    = "{form_values['prefab']}",
    vehicleScripts            = {{
        Seats,
        VehicleMotor,
        FuelTank,
        VehicleLighting,
        WarningSound,
        --AnimatedParts,
    }},
    
    massCenter                = Vector3:new(0, {form_values['massCenter_y']}, {form_values['massCenter_z']}),    

    maxRpm                    = {form_values['maxRpm']},
    maxSpeed                = {form_values['maxSpeed']},
    wheelRadius                = {form_values['wheelRadius']},

    maxBrakeTorque            = {form_values['maxBrakeTorque']},
    parkingBrakeTorque        = {form_values['parkingBrakeTorque']},

    steeringAngle            = {form_values['steeringAngle']},
    steeringWheelIndex        = "{form_values['steeringWheelIndex']}",
    steeringWheelAngle        = {form_values['steeringWheelAngle']},
    steeringWheelAxis        = {form_values['steeringWheelAxis']},
    steeringAnimationIndex    = "{form_values['steeringAnimationIndex']}",

    rpmPointerIndex            = "{form_values['rpmPointerIndex']}",
    rpmPointerMaxAngle        = {form_values['rpmPointerMaxAngle']},

    speedPointerIndex        = "{form_values['speedPointerIndex']}",
    speedPointerMaxAngle    = {form_values['speedPointerMaxAngle']},

    fuelUsagePerHour        = {form_values['fuelUsagePerHour']},
    fuelUsagePer100Km        = {form_values['fuelUsagePer100Km']},
    fuelTankCapacity        = {form_values['fuelTankCapacity']},

    axles                    = {{
        {{
            motor            = 0,
            useABS            = false,
            brake            = false,
            steeringScale    = 1,
            leftWheelIndex    = "{form_values['leftWheelFrontIndex']}",
            rightWheelIndex    = "{form_values['rightWheelFrontIndex']}",
        }},
        {{
            motor            = 1,
            useABS            = false,
            brake            = true,
            steeringScale    = 0,
            leftWheelIndex    = "{form_values['leftWheelRearIndex']}",
            rightWheelIndex    = "{form_values['rightWheelRearIndex']}",
        }},
    }},

    gears                    = {{ {form_values['gears']} }},
    gearLabels                = {{ {form_values['gearLabels']} }},
    motorFinalDriveRatio    = {form_values['motorFinalDriveRatio']},

    motorMaxRpm            = {form_values['motorMaxRpm']},
    motorInertiaMoment    = {form_values['motorInertiaMoment']},
    
    motorTorqueCurve        = {{
        {form_values['motorTorqueCurve']}
    }},

    automaticDrive            = {form_values['automaticDrive']},
    automaticLowerLimitRpm    = {form_values['automaticLowerLimitRpm']},
    automaticUpperLimitRpm    = {form_values['automaticUpperLimitRpm']},
    automaticGearSwitchPace    = {form_values['automaticGearSwitchPace']},

    seats                    = {{
        {{
            index            = "{form_values['seatIndex']}",
            cameraIndex        = "{form_values['cameraIndex']}",
            leaveIndex        = "{form_values['leaveIndex']}",
            isDriver        = true,
        }},
    }},
    cameras                    = {{
        {{
            slot            = {form_values['cameraSlot']},
            index            = "{form_values['cameraIndex']}",
            rotIndex        = "{form_values['cameraRotationIndex']}",
            zoomIndex        = "{form_values['cameraZoomIndex']}",
        }},
    }},

    sounds                    = {{
        setParkingBrake    = {{
            prefab          = "$sounds/parkingBrake1",
            volume          = 1,
        }},
        releaseParkingBrake = {{
            prefab          = "$sounds/parkingBrake0",
            volume          = 1,
        }},
        switchTurnOn        = {{
            prefab          = "$sounds/switchSound1",
            volume          = 1,
        }},
        switchTurnOff       = {{
            prefab          = "$sounds/switchSound0",
            volume          = 1,
        }},
        blinkTickOn         = "$sounds/blinker1",
        blinkTickOff        = "$sounds/blinker0",
        warningSound        = {{    
            prefab          = "$sounds/Pistenbully/PB_beep",
            volume          = 1,
            enabledByKey    = true,
            enableReverse   = false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
        setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
                setParkingBrake		= {{
        	prefab			= "$sounds/parkingBrake1",
        	volume			= 1,
        }},
        releaseParkingBrake	= {{
        	prefab			= "$sounds/parkingBrake0",
        	volume			= 1,
        }},
        switchTurnOn		= {{
        	prefab			= "$sounds/switchSound1",
        	volume			= 1,
        }},
        switchTurnOff		= {{
        	prefab			= "$sounds/switchSound0",
        	volume			= 1,
        }},
        blinkTickOn			= "$sounds/blinker1",
        blinkTickOff		= "$sounds/blinker0",
        warningSound			= {{	
        	prefab			= "$sounds/Pistenbully/PB_beep",
        	volume = 1,
        	enabledByKey 		= true,
        	enableReverse 		= false,
        }},
        -- motor sounds
        motorConfiguration	= {{
        	minRunFadeRpm			= 1000,
        	maxRunFadeRpm			= 3000,
        	minRunFadeSpeed			= 5,
        	maxRunFadeSpeed			= 20,
        	interieurVolumeScale    = 0.1,
        	interieurLowpass        = 0.4,
        }},
        motorIdle			= {{
			{{
				prefab			= "$sounds/SkiDoo/SkiDoo_load",
				minPitch		= 0.6,
				maxPitch		= 3,

				--baseRpm			= 800,
				pitchOffset		= 1,
				pitchScale		= 0.025/100,
				
				interieurLowpass		= 0.2,
				exterieurLowpass        = 0.2,
				
				minVolume		= 0.65,
				maxVolume		= 0.75,

				minFadeOutRpm	= 650,
				maxFadeOutRpm	= 800,

				fadeOutSpeed	= 0.05,

				--pitchOffset		= 0,
				--pitchScale		= 1,
				--volumeScale		= 1,
			}},
			{{
				prefab			= "$sounds/SkiDoo/SkiDoo_run",
				minPitch		= 0.6,
				maxPitch		= 2,

				--baseRpm			= 800,
				pitchOffset		= 0.9,
				pitchScale		= 0.017/100,

				interieurLowpass		= 0.25,
				exterieurLowpass        = 0.25,
				
				minVolume		= 0.1,
				maxVolume		= 0.8,

				minFadeInRpm	= 570,
				maxFadeInRpm	= 600,

				fadeInSpeed		= 0.1,

				--pitchOffset		= 0,
				--pitchScale		= 1,
				--volumeScale		= 1,
			}},
			{{
				prefab			= "$sounds/SkiDoo/SkiDoo_load",
				minPitch		= 0.6,
				maxPitch		= 2,

				--baseRpm			= 800,
				pitchOffset		= 1,
				pitchScale		= 0.018/100,

				interieurLowpass		= 0.25,
				exterieurLowpass        = 0.25,
				
				--minVolume		= 0.0,
				minVolume		= 0.6,
				--maxVolume		= 0.0,
				maxVolume		= 0.65,

				minFadeInRpm	= 570,
				maxFadeInRpm	= 600,

				fadeInSpeed		= 0.3,

				--pitchOffset		= 0,
				--pitchScale		= 1,
				--volumeScale		= 1,
			}},
		}},
		motorLoad			= {{
			prefab			= "$sounds/SkiDoo/SkiDoo_load",
			minPitch		= 0.7,
			maxPitch		= 3,

			--baseRpm			= 1800,
			pitchOffset 	= 0.45,
			pitchScale		= 0.03/100,

			--minVolume		= 0.3,
			minVolume		= 0.0,
			--maxVolume		= 0.55,
			maxVolume		= 0.0,
			
			-- Volume/Second
			fadeInSpeed		= 0.25,
			fadeOutSpeed	= 0.1,
		}},
		motorStart			= {{
			prefab			= "$sounds/SkiDoo/SkiDoo_start",
		}},
		motorStop			= {{
			prefab			= "$sounds/SkiDoo/SkiDoo_stop",
		}},
	}},
    lights                    = {{
        headlights            = {{
            "{form_values['headlights']}",
            "{form_values['headlightsInverse']}",
        }},
        strobeLights            = {{
            "{form_values['strobeLights']}",
        }},
    }},
}});
'''
    
        global current_file
        if current_file:
            with open(current_file, 'w') as file:
                file.write(lua_content)
            messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{current_file}")
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".lua",
                filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")]
            )
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(lua_content)
                current_file = file_path
                messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{file_path}")
                root.title(f"{translations[current_language]['title']} - {file_path}")

                messagebox.showinfo("Success", "Lua file created successfully!")
                new_project_frame.destroy()  
            else:
                messagebox.showerror("Error", "Please fill in all fields.")


    submit_button_row = len(labels_and_fields2) + 1  
    tk.Button(new_project_frame, text="Submit", bg="#23272e", fg="white", command=submit_form).grid(
    row=submit_button_row, column=4, columnspan=2, pady=10, sticky="ew") 

    
    cancel_button_row = submit_button_row + 1 
    tk.Button(new_project_frame, text="Cancel", bg="#23272e", fg="white", command=new_project_frame.destroy).grid(
    row=cancel_button_row, column=4, columnspan=2, pady=10, sticky="ew")  




def open_new_snowcannon():
   
    
    new_project_window = tk.Toplevel(root)
    new_project_window.title("Create New SnowCannon")
    new_project_window.overrideredirect(False)  # Supprime les bordures et la barre de titre
    new_project_window.attributes("-alpha", 0.8)  # Valeur entre 0 (transparent) et 1 (opaque)
    
    # Définir un fond de couleur personnalisée (non transparent)
    new_project_window.configure(bg="#23272e")

    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    details_width = 1000
    details_height = 565
    x = root_x + (root_width // 2) - (details_width // 2)
    y = root_y + (root_height // 2) - (details_height // 2-45)
    new_project_window.geometry(f"{details_width}x{details_height}+{x}+{y}")

    

   
    labels_and_fields = [
        ("contentName:", "contentName"),
        ("title:", "title"),
        ("fullDesc:", "fullDesc"),
        ("techSpecs:", "techSpecs"),
        ("previewFilename:", "previewFilename"),
        ("logoFilename:", "logoFilename"),
        ("author:", "author"),
        ("shopCategory:", "shopCategory"),
        ("price:", "price"),
        ("depreciationPeriod:", "depreciationPeriod"),
        ("prefab:", "prefab"),
        ("slaveAttachers - index:", "slaveAttachers_index"),
        ("slaveAttachers - type (SnowCannon):", "slaveAttachers_type"),
    ]

    labels_and_fields_2 = [
        ("snowSpawnIndex:", "snowSpawnIndex"),
        ("propellerIndex:", "propellerIndex"),
        ("propellerSpeed:", "propellerSpeed"),
        ("controlIndex:", "controlIndex"),
        ("cameraIndex:", "cameraIndex"),
        ("idleSound:", "idleSound"),
        ("rotX - index:", "rotX_index"),
        ("rotX - min:", "rotX_min"),
        ("rotX - max:", "rotX_max"),
    ]
    labels_and_fields_3 = [
        ("rotY - index:", "rotY_index"),
        ("rotY - min:", "rotY_min"),
        ("rotY - max:", "rotY_max"),
        ("rotY - attachValue:", "rotY_attachValue"),
        ("particleSystems:", "particleSystems"),
        ("isKinematic (true or false):", "isKinematic"),
        ("isPlaceable (true or false):", "isPlaceable"),
    ]

    entries = {}

    
    for idx, (label_text, entry_key) in enumerate(labels_and_fields):
        tk.Label(new_project_window, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=1, padx=10, pady=10)
        entry = tk.Entry(new_project_window, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=2, padx=10, pady=10)
        entries[entry_key] = entry

    for idx, (label_text, entry_key) in enumerate(labels_and_fields_2):
        tk.Label(new_project_window, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=3, padx=10, pady=10)
        entry = tk.Entry(new_project_window, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=4, padx=10, pady=10)
        entries[entry_key] = entry

    for idx, (label_text, entry_key) in enumerate(labels_and_fields_3):
        tk.Label(new_project_window, text=label_text, bg="#23272e", fg="white").grid(row=idx, column=5, padx=10, pady=10)
        entry = tk.Entry(new_project_window, bg="#4d4f54", fg="white")
        entry.grid(row=idx, column=6, padx=10, pady=10)
        entries[entry_key] = entry  
    
   
    def submit_form():
      
        form_values = {key: entry.get() for key, entry in entries.items()}
        
       
        if all(form_values.values()):
 
            is_placeable = "true" if form_values["isPlaceable"].lower() == "true" else "false"
            is_kinematic = "true" if form_values["isKinematic"].lower() == "true" else "false"
            

            lua_content = f'''--
-- Winter Resort Simulator - Modding lua generator
--
--Modding lua generator CREALUA by naligator
--
--

ModLoader.addContent("vehicle", {{
    contentName                = "{form_values['contentName']}",
    title                    = "{form_values['title']}",
    fullDesc                = "{form_values['fullDesc']}",
    techSpecs                = "{form_values['techSpecs']}",
    previewFilename            = "{form_values['previewFilename']}",
    logoFilename            = "{form_values['logoFilename']}",
    
    author                    = "{form_values['author']} with CREALUA",
    shopCategory            = "{form_values['shopCategory']}",
    price                    = {form_values['price']},
    depreciationPeriod        = {form_values['depreciationPeriod']},
    
    class                    = Vehicle,
    prefab                    = "{form_values['prefab']}",
    vehicleScripts            = {{
        SnowCannon,
        Attachable,
    }},

    massCenter                = Vector3:new(0, 0.6, 0),

    axles                    = {{ }},

    slaveAttachers            = {{
        {{
            index            = "{form_values['slaveAttachers_index']}",
            type            = "{form_values['slaveAttachers_type']}",
        }},
    }},

    isPlaceable                = {is_placeable},
    isKinematic                = {is_kinematic},

    snowCannons                = {{
        {{
            snowSpawnIndex    = "{form_values['snowSpawnIndex']}",
            propellerIndex    = "{form_values['propellerIndex']}",
            propellerSpeed    = {form_values['propellerSpeed']},
            controlIndex    = "{form_values['controlIndex']}",
            cameraIndex        = "{form_values['cameraIndex']}",
            idleSound        = "{form_values['idleSound']}",
            rotX            = {{
                index        = "{form_values['rotX_index']}",
                min            = {form_values['rotX_min']},
                max            = {form_values['rotX_max']},
            }},
            rotY            = {{
                index        = "{form_values['rotY_index']}",
                min            = {form_values['rotY_min']},
                max            = {form_values['rotY_max']},
                attachValue    = {form_values['rotY_attachValue']},
            }},
            particleSystems    = {{ "{form_values['particleSystems']}" }},
        }},
    }},
}});
'''


            global current_file
            if current_file:
                with open(current_file, 'w') as file:
                    file.write(lua_content)
                messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{current_file}")
            else:
                file_path = filedialog.asksaveasfilename(
                    defaultextension=".lua",
                    filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")]
                )
                if file_path:
                    with open(file_path, 'w') as file:
                        file.write(lua_content)
                    current_file = file_path
                    messagebox.showinfo(translations[current_language]["files"], f"{translations[current_language]['success_save']}{file_path}")
                    root.title(f"{translations[current_language]['title']} - {file_path}")


            messagebox.showinfo("Success", "Lua file created successfully!")
            new_project_window.destroy()  
        else:

            messagebox.showerror("Error", "Please fill in all fields.")

   
    submit_button_row = len(labels_and_fields_3) + 2  
    tk.Button(new_project_window, text="Submit", bg="#23272e", fg="white", command=submit_form).grid(
    row=submit_button_row, column=5, columnspan=2, pady=20, sticky="ew") 

    
    cancel_button_row = submit_button_row + 1 
    tk.Button(new_project_window, text="Cancel", bg="#23272e", fg="white", command=new_project_window.destroy).grid(
    row=cancel_button_row, column=5, columnspan=2, pady=10, sticky="ew")  














def open_add_slopes_window():
    # Chemin du répertoire cible
    savegames_path = os.path.expanduser("~/Documents/My Games/WinterResortSimulator_Season2/savegames")

    # Vérifier si le répertoire existe
    if not os.path.exists(savegames_path):
        messagebox.showerror("Erreur", f"Le chemin spécifié n'existe pas :\n{savegames_path}")
        return

    # Ouvrir une boîte de dialogue pour sélectionner un fichier
    selected_file = filedialog.askopenfilename(
        initialdir=savegames_path,
        title="CREALUA search",
        filetypes=(("Fichiers .lua", "*.lua"), ("Tous les fichiers", "*.*"))
    )

    # Vérifier si un fichier a été sélectionné
    if selected_file:
        open_slope_details_window(selected_file)
    else:
        messagebox.showwarning("Aucun fichier sélectionné", "Aucun fichier n'a été choisi.")

def open_slope_details_window(selected_file):
    # Créer une nouvelle fenêtre
    details_window = tk.Toplevel(root)
    details_window.title(translations[current_language]["add_slopes"])
    details_window.geometry("400x600")
    details_window.configure(bg="#23272e")

    # Centrer la fenêtre par rapport à root
    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    details_width = 600
    details_height = 600
    x = root_x + (root_width // 2) - (details_width // 2)
    y = root_y + (root_height // 2) - (details_height // 2)
    details_window.geometry(f"{details_width}x{details_height}+{x}+{y}")

    # Titre de la fenêtre
    tk.Label(details_window, text=f"📝 : {os.path.basename(selected_file)}",
             bg="#23272e", fg="white", font=("Arial", 12)).pack(pady=10)

    # Canvas pour permettre le défilement
    canvas_frame = tk.Frame(details_window, bg="#23272e")
    canvas_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(canvas_frame, bg="#23272e", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="#23272e")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    slope_entries = []

    def update_canvas(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_canvas)



    # Fonction pour ajouter un slope frame
    def add_slope_frame(data=None):
        flash_message()  # Afficher le message clignotant

        slope_frame = tk.Frame(inner_frame, bg="#4b4f56", bd=2, relief="solid", padx=10, pady=10)
        slope_frame.pack(fill="x", pady=10, padx=10)

        entries = {}
        fields = [
            ("Slope", "-"),
            ("Info Layer", 1),
            ("Name", "-"),
            ("From", "-"),
            ("To", "-"),
            ("Diff", 1),
            ("Length", 180),
            ("Current Guests", 0),
            ("Max Skiers Capacity", 6000)
        ]

        for field, default in fields:
            row_frame = tk.Frame(slope_frame, bg="#4b4f56")
            row_frame.pack(fill="x", pady=5)
            tk.Label(row_frame, text=f"{field}:", bg="#4b4f56", fg="white", font=("Arial", 10), width=20, anchor="w").pack(side="left")
            entry = tk.Entry(row_frame, width=30)
            entry.insert(0, str(default))
            entry.pack(side="left", padx=5)
            entries[field] = entry

        slope_entries.append(entries)

        def remove_slope_frame():
            slope_frame.destroy()
            slope_entries.remove(entries)
            update_canvas()

        tk.Button(slope_frame, text="Supprimer", command=remove_slope_frame, bg="#3b3f46", fg="white").pack(pady=5)

        update_canvas()


    # Bouton pour ajouter un nouveau slope frame
    tk.Button(details_window, text="➕ Ajouter un slope", command=lambda: add_slope_frame(),
              bg="#4b4f56", fg="white").pack(pady=20)

    # Fonction pour sauvegarder toutes les données des slopes
    def save_all_slopes():
        try:
            with open(selected_file, "r") as f:
                content = f.read()

            slopes_match = re.search(r"skiSlopes\s*=\s*\{(.*?)\}", content, re.DOTALL)
            if not slopes_match:
                messagebox.showerror("Erreur", "Section 'skiSlopes = {}' introuvable dans le fichier.")
                return

            updated_slopes = []
            for entries in slope_entries:
                updated_slopes.append(
                    f"    {{\n"
                    f"        slope = \"{entries['Slope'].get()}\",\n"
                    f"        infoLayer = {entries['Info Layer'].get()},\n"
                    f"        name = \"{entries['Name'].get()}\",\n"
                    f"        from = \"{entries['From'].get()}\",\n"
                    f"        to = \"{entries['To'].get()}\",\n"
                    f"        diff = {entries['Diff'].get()},\n"
                    f"        length = {entries['Length'].get()},\n"
                    f"        currentGuests = {entries['Current Guests'].get()},\n"
                    f"        maxSkiersCapacity = {entries['Max Skiers Capacity'].get()},\n"
                    f"    }}"
                )

            updated_content = re.sub(
                r"skiSlopes\s*=\s*\{(.*?)\}",
                f"skiSlopes = {{\n{',\n'.join(updated_slopes)}\n}}",
                content,
                flags=re.DOTALL
            )

            with open(selected_file, "w") as f:
                f.write(updated_content)

            messagebox.showinfo("Succès", "Les données ont été sauvegardées avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

    tk.Button(details_window, text="💾 Sauvegarder tout", command=save_all_slopes,
              bg="#007BFF", fg="white", font=("Arial", 12)).pack(pady=10)

    message_label = tk.Label(details_window, text=translations[current_language]["add_adv"], fg="red", bg="#23272e", font=("Arial", 12, "bold"))
    message_label.pack(pady=10)

    def flash_message():
        # Variable pour suivre le clignotement
        def toggle_color():
            current_color = message_label.cget("fg")
            new_color = "white" if current_color == "red" else "red"
            message_label.config(fg=new_color)

        # Clignotement pendant 3 secondes
        
        for i in range (199):  # 6 changements de couleur toutes les 500ms
            details_window.after(i * 250, toggle_color)
            i=i/250

        # Arrêter le clignotement après 3 secondes (3000ms)
        #details_window.after(300000, lambda: message_label.config(fg="red"))

    flash_message()








def open_change_size_map_window():
    # Ouvrir une boîte de dialogue pour choisir un fichier Lua
    savegames_path = r"C:\Users\nali7\Documents\My Games\WinterResortSimulator_Season2\savegames"
    selected_file = filedialog.askopenfilename(
        initialdir=savegames_path,
        title="Choisir un fichier Lua",
        filetypes=(("Fichiers .lua", "*.lua"), ("Tous les fichiers", "*.*"))
    )

    if selected_file:
        try:
            # Charger le contenu du fichier Lua
            with open(selected_file, 'r') as f:
                content = f.read()

            # Extraire les valeurs de sizeXZ et sizeY
            size_x_value = re.search(r'sizeXZ\s*=\s*(\d+)', content)
            size_y_value = re.search(r'sizeY\s*=\s*(\d+)', content)

            # Valeurs par défaut si elles ne sont pas trouvées
            size_x_value = int(size_x_value.group(1)) if size_x_value else 2457
            size_y_value = int(size_y_value.group(1)) if size_y_value else 1999

            # Créer la fenêtre pour changer les valeurs
            details_window = tk.Toplevel(root)
            details_window.title("Modifier la taille")
            details_window.geometry("400x300")
            details_window.configure(bg="#23272e")

            # Ajouter un titre dans la fenêtre
            title_label = tk.Label(details_window, text="Modifier les valeurs", fg="white", bg="#23272e", font=("Arial", 12))
            title_label.pack(pady=10)

            # Ajouter le curseur pour X (sizeXZ)
            size_x_label = tk.Label(details_window, text="Size XZ (Surface):", fg="white", bg="#23272e", font=("Arial", 10))
            size_x_label.pack(pady=5)
            size_x_slider = tk.Scale(details_window, from_=20, to=8000, orient="horizontal", bg="#4b4f56", fg="white", sliderlength=20)
            size_x_slider.set(size_x_value)  # Initialisation avec la valeur extraite
            size_x_slider.pack(pady=10)

            # Ajouter le curseur pour Y (sizeY)
            size_y_label = tk.Label(details_window, text="Size Y (High):", fg="white", bg="#23272e", font=("Arial", 10))
            size_y_label.pack(pady=5)
            size_y_slider = tk.Scale(details_window, from_=20, to=8000, orient="horizontal", bg="#4b4f56", fg="white", sliderlength=20)
            size_y_slider.set(size_y_value)  # Initialisation avec la valeur extraite
            size_y_slider.pack(pady=10)

            # Fonction pour sauvegarder les modifications
            def save_changes():
                new_size_x = size_x_slider.get()
                new_size_y = size_y_slider.get()

                # Vérifier si les valeurs dans le fichier Lua existent
                if 'sizeXZ' in content and 'sizeY' in content:
                    # Remplacer les valeurs dans le contenu du fichier
                    new_content = re.sub(r'sizeXZ\s*=\s*\d+', f'sizeXZ = {new_size_x}', content)
                    new_content = re.sub(r'sizeY\s*=\s*\d+', f'sizeY = {new_size_y}', new_content)

                    # Sauvegarder les modifications dans le fichier
                    with open(selected_file, 'w') as f:
                        f.write(new_content)

                    messagebox.showinfo("Succès", "Les modifications ont été sauvegardées avec succès.")
                    details_window.destroy()
                else:
                    messagebox.showerror("Erreur", "Les clés sizeXZ ou sizeY n'ont pas été trouvées dans le fichier.")

            # Ajouter un bouton pour sauvegarder
            save_button = tk.Button(
                details_window, 
                text="Sauvegarder", 
                command=save_changes, 
                bg="#4b4f56", 
                fg="white", 
                font=("Arial", 12)
            )
            save_button.pack(pady=20)

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inconnue lors de l'ouverture ou de la modification du fichier: {e}")
    else:
        messagebox.showwarning("Aucun fichier", "Aucun fichier n'a été sélectionné.")









def open_change_floor_color_window():
    # Ouvrir une boîte de dialogue pour choisir un fichier Lua
    savegames_path = r"C:\Users\nali7\Documents\My Games\WinterResortSimulator_Season2\savegames"
    selected_file = filedialog.askopenfilename(
        initialdir=savegames_path,
        title="Choisir un fichier Lua",
        filetypes=(("Fichiers .lua", "*.lua"), ("Tous les fichiers", "*.*"))
    )

    if selected_file:
        try:
            # Charger le contenu du fichier Lua
            with open(selected_file, 'r') as f:
                content = f.read()

            # Vérifier quel terrain est défini dans le fichier
            if 'terrainName = "HallsteinTerrain"' in content:
                terrain_type = "HallsteinTerrain"
                button_image = "notok.png"  # Image pour Hallstein
            elif 'terrainName = "RiedsteinTerrain"' in content:
                terrain_type = "RiedsteinTerrain"
                button_image = "ok.png"  # Image pour Riedstein
            else:
                terrain_type = None
                button_image = "notok.png"  # Par défaut, Hallstein si aucun terrain trouvé

            # Effectuer immédiatement le changement de terrain sans bouton supplémentaire
            toggle_terrain(selected_file, terrain_type, content, button_image)

        except Exception as e:
            # Afficher plus de détails sur l'erreur d'ouverture du fichier
            error_message = f"Erreur inconnue lors de l'ouverture ou de la modification du fichier: {e}\n{traceback.format_exc()}"
            messagebox.showerror("Erreur", error_message)
    else:
        messagebox.showwarning("Aucun fichier", "Aucun fichier n'a été sélectionné.")

def toggle_terrain(file, terrain_type, current_content, img):
    """Fonction qui effectue le basculement des terrains et la mise à jour du fichier."""
    if terrain_type == "HallsteinTerrain":
        new_content = current_content.replace('terrainName = "HallsteinTerrain"', 'terrainName = "RiedsteinTerrain"')
        new_button_image = "ok.png"
        terrain_type = "RiedsteinTerrain"
    elif terrain_type == "RiedsteinTerrain":
        new_content = current_content.replace('terrainName = "RiedsteinTerrain"', 'terrainName = "HallsteinTerrain"')
        new_button_image = "notok.png"
        terrain_type = "HallsteinTerrain"
    else:
        return  # Aucune action si terrain non défini

    try:
        # Sauvegarder les modifications dans le fichier
        with open(file, "w") as f:
            f.write(new_content)

        # Afficher un message de succès
        messagebox.showinfo("Succès", "Le fichier a été mis à jour avec succès.")
    except Exception as e:
        # Afficher plus de détails sur l'erreur
        error_message = f"Erreur lors de l'écriture dans le fichier : {e}\n{traceback.format_exc()}"
        messagebox.showerror("Erreur", error_message)
        













def open_selection_frame():
    # Création de la fenêtre secondaire sans bordure
    selection_window = tk.Toplevel(root)
    selection_window.title("Sélectionner une Action")
    selection_window.geometry("400x200")
    selection_window.config(bg="#23272e")
    
    # Suppression des bordures de la fenêtre
    selection_window.overrideredirect(True)
    
    # Récupérer la position et la taille de la fenêtre principale
    main_width = root.winfo_width()
    main_height = root.winfo_height()
    main_x = root.winfo_x()
    main_y = root.winfo_y()

    # Calculer la position pour centrer la fenêtre secondaire
    center_x = main_x + (main_width // 2) - 200  # 200 = la moitié de la largeur de la fenêtre secondaire
    center_y = main_y + (main_height // 2) - 100  # 100 = la moitié de la hauteur de la fenêtre secondaire

    # Positionner la fenêtre secondaire
    selection_window.geometry(f"400x200+{center_x}+{center_y}")

    # Fonction pour fermer la fenêtre secondaire
    def close_window(event=None):
        selection_window.destroy()

    # Ajouter un gestionnaire d'événements pour fermer la fenêtre si on clique en dehors
    def check_click_outside(event):
        # Vérifier si le clic se produit en dehors de la fenêtre secondaire
        if event.widget != selection_window:
            close_window()

    # Lier l'événement de clic de souris sur la fenêtre principale
    root.bind("<Button-1>", check_click_outside)

    # Titre principal
    tk.Label(selection_window, text="Not Implemanted yet :", bg="#23272e", fg="white", font=("Arial", 16)).pack(pady=10)

    # Frame pour organiser les boutons
    button_frame = tk.Frame(selection_window, bg="#23272e")
    button_frame.pack(expand=True, pady=10)

    # Fonction pour "Create New Mod Parameter"
    def tutorial():
        webbrowser.open("https://wiki.hr-innoways.com/start")

    # Fonction pour "Create New Object"
    def discord():
        webbrowser.open("https://discord.gg/ZGdtyXkjys")

    # Bouton 1 : Create New Mod Parameter
    button_mod = tk.Button(
        button_frame, 
        text="Wiki", 
        command=tutorial,
        bg="#4b4f56", fg="white", 
        activebackground="#6b6f76", 
        width=20, height=2
    )
    button_mod.grid(row=0, column=0, padx=10, pady=10)

    # Bouton 2 : Create New Object
    button_object = tk.Button(
        button_frame, 
        text="discord server", 
        command=discord,
        bg="#4b4f56", fg="white", 
        activebackground="#6b6f76", 
        width=20, height=2
    )
    button_object.grid(row=0, column=1, padx=10, pady=10)

#    # Bouton pour fermer proprement la fenêtre
#    close_button = tk.Button(
#        selection_window, 
#        text="X", 
#        command=close_window, 
#        bg="red", fg="white", 
#        width=2, height=1, 
#        font=("Arial", 12)
#    )
#    close_button.place(x=370, y=5)  # Positionner le bouton pour fermer en haut à droite














def Files_menu(event=None):
    files_menu = tk.Menu(root, tearoff=0, bg="#23272e", fg="white", activebackground="#4b4f56", activeforeground="red")
    files_menu.add_command(label=translations[current_language]["open_file"], command=Open_files)
    files_menu.add_command(label=translations[current_language]["save_file"], command=Save_files)
    files_menu.add_separator()
    files_menu.add_command(label=translations[current_language]["new_project"], command=open_selection_frame)
    files_menu.add_separator()
    files_menu.add_command(label=translations[current_language]["exit"], command=root.quit)
    files_menu.post(files_button.winfo_rootx(), files_button.winfo_rooty() + files_button.winfo_height())

def Template_load(event=None):
    template_menu = tk.Menu(root, tearoff=0, bg="#23272e", fg="white", activebackground="#4b4f56", activeforeground="red")
    template_menu.add_command(label=translations[current_language]["menu_templates0"], command=open_new_snowcannon)
    template_menu.add_separator()
    template_menu.add_command(label=translations[current_language]["menu_templates1"], command=None)
    template_menu.add_separator()
    template_menu.add_command(label=translations[current_language]["menu_templates2"], command=open_new_snowmobile)
    template_menu.add_separator()
    template_menu.add_command(label=translations[current_language]["menu_templates3"], command=None)
    template_menu.add_separator()
    template_menu.add_command(label=translations[current_language]["menu_templates4"], command=None)

    #template_menu.post(template_button.winfo_rootx(), template_button.winfo_rooty() + template_button.winfo_height())



def open_account_page():
    # Chemin du fichier "account"
    account_file = "account.crealua"

    account_window = tk.Toplevel(root)
    account_window.title("Compte")
    main_width = root.winfo_width()
    main_height = root.winfo_height()
    main_x = root.winfo_x()
    main_y = root.winfo_y()

    
    account_window.overrideredirect(True)

    # Calculer la position pour centrer la fenêtre secondaire
    center_x = main_x + (main_width // 2) - 200  # 200 = la moitié de la largeur de la fenêtre secondaire
    center_y = main_y + (main_height // 2) - 100  # 100 = la moitié de la hauteur de la fenêtre secondaire

    # Positionner la fenêtre secondaire
    account_window.geometry(f"400x300+{center_x}+{center_y}")
    account_window.config(bg="#23272e")

    def close_window(event=None):
        account_window.destroy()

    # Ajouter un gestionnaire d'événements pour fermer la fenêtre si on clique en dehors
    def check_click_outside(event):
        # Vérifier si le clic se produit en dehors de la fenêtre secondaire
        if event.widget != account_window:
            close_window()

    # Lier l'événement de clic de souris sur la fenêtre principale
    root.bind("<Button-1>", check_click_outside)

    if os.path.exists(account_file):
        # Si le fichier existe, afficher le contenu
        with open(account_file, "r") as f:
            account_info = f.read()

        # Afficher les informations du compte
        tk.Label(account_window, text="Informations du compte :", bg="#23272e", fg="white", font=("Arial", 14)).pack(pady=10)
        tk.Label(account_window, text=account_info, bg="#23272e", fg="white", font=("Arial", 12), wraplength=380).pack(pady=20)

        # Fonction pour se déconnecter
        def disconnect():
            os.remove(account_file)  # Supprimer le fichier account.txt
            messagebox.showinfo("Déconnexion", "Vous avez été déconnecté avec succès.")
            account_window.destroy()  # Fermer la fenêtre

        # Bouton pour se déconnecter 
        tk.Button(account_window, text="Déconnecter", command=disconnect, bg="#ff4d4d", fg="white", activebackground="#ff6666").pack(pady=20)

    else:
        # Si le fichier n'existe pas, afficher une option pour créer un compte
        tk.Label(account_window, text="Aucun compte trouvé.", bg="#23272e", fg="white", font=("Arial", 14)).pack(pady=10)
        tk.Label(account_window, text="Veuillez entrer vos informations pour créer un compte.", bg="#23272e", fg="white", font=("Arial", 12)).pack(pady=10)

        # Entrée pour l'email
        tk.Label(account_window, text="Adresse e-mail :", bg="#23272e", fg="white", font=("Arial", 10)).pack(pady=5)
        email_entry = tk.Entry(account_window, width=30)
        email_entry.pack(pady=5)

        # Entrée pour le mot de passe
        tk.Label(account_window, text="Mot de passe :", bg="#23272e", fg="white", font=("Arial", 10)).pack(pady=5)
        password_entry = tk.Entry(account_window, width=30, show="*")
        password_entry.pack(pady=5)

        # Fonction pour créer un compte
        def create_account():
            # Récupérer les valeurs entrées par l'utilisateur
            email = email_entry.get().strip()
            password = password_entry.get().strip()

            # Vérifications simples
            if not email or not password:
                messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
                return

            # Sauvegarder les informations dans un fichier
            with open(account_file, "w") as f:
                f.write(f"Email: {email}\nPassword: {password}\nVersion: Free")
            messagebox.showinfo("Succès", "Compte créé avec succès !")
            account_window.destroy()

        # Bouton pour créer un compte
        tk.Button(account_window, text="Créer un compte", command=create_account, bg="#4b4f56", fg="white", activebackground="#6b6f76").pack(pady=20)

# Ajoutez une commande pour ouvrir la page "Compte"
def Option_menu(event=None):
    option_menu = tk.Menu(root, tearoff=0, bg="#23272e", fg="white", activebackground="#4b4f56", activeforeground="red")

    languages_menu = tk.Menu(option_menu, tearoff=0, bg="#23272e", fg="white", activebackground="#4b4f56", activeforeground="blue")
    languages_menu.add_command(label=translations[current_language]["languages"], command=None)  # Texte "Languages" (ou son équivalent)
    languages_menu.add_separator()
    languages_menu.add_command(label=translations[current_language]["en"], command=lambda: set_language("en"))
    languages_menu.add_command(label=translations[current_language]["fr"], command=lambda: set_language("fr"))
    languages_menu.add_command(label=translations[current_language]["es"], command=lambda: set_language("es"))
    languages_menu.add_command(label=translations[current_language]["it"], command=lambda: set_language("it"))
    languages_menu.add_command(label=translations[current_language]["ru"], command=lambda: set_language("ru"))
    languages_menu.add_command(label=translations[current_language]["de"], command=lambda: set_language("de"))




    # Option "Compte" avec vérification du fichier
    option_menu.add_cascade(label=translations[current_language]["languages"], menu=languages_menu)
    option_menu.add_command(label=translations[current_language]["compte"], command=open_account_page)
    option_menu.add_separator()
    option_menu.add_command(label=translations[current_language]["exit"], command=root.quit)

    option_menu.post(option_menu_button.winfo_rootx(), option_menu_button.winfo_rooty() + option_menu_button.winfo_height())


def mapping_menu(event=None):
    mapping_menu = tk.Menu(root, tearoff=0, bg="#23272e", fg="white", activebackground="#4b4f56", activeforeground="red")
    mapping_menu.add_command(label=translations[current_language]["add_slopes"], command=open_add_slopes_window)
    mapping_menu.add_command(label=translations[current_language]["change_color"], command=open_change_floor_color_window)
    mapping_menu.add_command(label=translations[current_language]["change_size"], command=open_change_size_map_window)
    
    mapping_menu.post(mapping_menu_button.winfo_rootx(), mapping_menu_button.winfo_rooty() + mapping_menu_button.winfo_height())




def change_language(language):
    messagebox.showinfo("Language Changed", f"Language set to: {language}")


def on_mouse_wheel(event):
    if event.state & 0x0004:
        editor.xview_scroll(int(-1*(event.delta/120)), "units")


root = tk.Tk()
root.title(translations[current_language]["title"])
root.geometry("1300x700")
root.resizable(False, False)
root.configure(bg="#0f2c59")
root.iconbitmap("logoCREALUA.ico")


menu_frame = tk.Frame(root, bg="#23272e", height=30)
menu_frame.pack(fill="x")

files_button = tk.Button(menu_frame, text=translations[current_language]["files"], bg="#23272e", fg="white", relief="flat", command=Files_menu)
files_button.pack(side="left", padx=10, pady=5)

#template_button = tk.Button(menu_frame, text=translations[current_language]["template"], bg="#23272e", fg="white", relief="flat", command=Template_load)
#template_button.pack(side="left", padx=10, pady=5)

def error():
    messagebox.showerror("Error", "Not working yet.")

template_button = tk.Button(menu_frame, text=translations[current_language]["template"], bg="#23272e", fg="white", relief="flat", command=error)
template_button.pack(side="left", padx=10, pady=5)


option_menu_button = tk.Button(menu_frame, text=translations[current_language]["option"], bg="#23272e", fg="white", relief="flat", command=Option_menu)
option_menu_button.pack(side="right", padx=10, pady=5)

mapping_menu_button = tk.Button(menu_frame, text=translations[current_language]["mapping_btn"], bg="#23272e", fg="white", relief="flat", command=mapping_menu)
mapping_menu_button.pack(side="left", padx=10, pady=5)



editor = tk.Text(root, wrap="none", font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")

scroll_y = tk.Scrollbar(editor, orient="vertical", command=editor.yview)
scroll_x = tk.Scrollbar(editor, orient="horizontal", command=editor.xview)

root.bind("<Control-s>", Save_files)


def process_image(image_path, output_size):
    # Ouvrir l'image
    original_image = Image.open(image_path).convert("RGBA")

    # Créer une nouvelle image avec un fond noir
    black_background = Image.new("RGBA", original_image.size, (0, 0, 0, 255))
    black_background.paste(original_image, (0, 0), original_image)

    # Redimensionner l'image
    resized_image = black_background.resize(output_size)

    # Créer un calque noir semi-transparent pour l'effet fumé
    smoke_layer = Image.new("RGBA", resized_image.size, (0, 0, 0, 100))
    dark_image = Image.alpha_composite(resized_image, smoke_layer)

    # Améliorer le contraste pour un rendu plus sombre
    enhancer = ImageEnhance.Brightness(dark_image)
    dark_image = enhancer.enhance(0.8)

    # Convertir en format adapté pour Tkinter
    return ImageTk.PhotoImage(dark_image.convert("RGB"))


image_path = "back_img.png"
output_size = (1300, 700)
#original_image  = Image.open(image_path)
#resized_image = original_image.resize((1300, 700))  # Redimensionner à 1300x700
#background_image = ImageTk.PhotoImage(resized_image)
background_image = process_image(image_path, output_size)


main_width = root.winfo_width()
main_height = root.winfo_height()
canvas = tk.Canvas(root, width=1300, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Ajouter l'image comme fond
canvas.create_image(0, 0, anchor="nw", image=background_image)


root.bind("<Button-4>", on_mouse_wheel)
root.bind("<Button-5>", on_mouse_wheel)

root.mainloop()