---
title: "Get Language and Localized Menu Names Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Language_and_Localized_Menu_Names_Example_VB.htm"
---

# Get Language and Localized Menu Names Example (VBA)

This example shows how to get the current language used by the SOLIDWORKS
application and the names of some of the menus in the local language.

```
'----------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp  As SldWorks.SldWorks
```

```
    Set swApp = Application.SldWorks
    Debug.Print "Language = " & swApp.GetCurrentLanguage
    Debug.Print "  File Menu            = " + swApp.GetLocalizedMenuName(swFileMenu)
    Debug.Print "  EditMenu             = " + swApp.GetLocalizedMenuName(swEditMenu)
    Debug.Print "  View Menu            = " + swApp.GetLocalizedMenuName(swViewMenu)
    Debug.Print "  Insert Menu          = " + swApp.GetLocalizedMenuName(swInsertMenu)
    Debug.Print "  Tools Menu           = " + swApp.GetLocalizedMenuName(swToolsMenu)
    Debug.Print "  Window Menu          = " + swApp.GetLocalizedMenuName(swWindowMenu)
    Debug.Print "  Help Menu            = " + swApp.GetLocalizedMenuName(swHelpMenu)
    Debug.Print "  View Toolbars Menu   = " + swApp.GetLocalizedMenuName(swViewToolbarsMenu)
End Sub
```

```
'Language = english
'File Menu = &File
'Edit Menu = &Edit
'View Menu = &View
'Insert Menu = &Insert
'Tools Menu = &Tools
'Window Menu = &Window
'Help Menu = &Help
'View Toolbars Menu = &Toolbars
```

```
'Language = spanish
'File Menu = &Archivo
'Edit Menu = &Edición
'View Menu = &Ver
'Insert Menu = &Insertar
'Tools Menu = &Herramientas
'Window Menu = Ven&tana
'Help Menu = &?
'View Toolbars Menu = Barras de &herramientas
```

```
'Language = french
'File Menu = &Fichier
'Edit Menu = &Edition
'View Menu = Affic&hage
'Insert Menu = &Insertion
'Tools Menu = &Outils
'WindowMenu = Fe&nêtre
'Help Menu = &?
'View Toolbars Menu = &Barre d'outils
```

```
'Language = german
'File Menu = &Datei
'Edit Menu = &Bearbeiten
'View Menu = &Ansicht
'Insert Menu = &Einfügen
'Tools Menu = E&xtras
'Window Menu = &Fenster
'Help Menu = &Hilfe
'View Toolbars Menu = S&ymbolleisten
```

```
'Language = italian
'File Menu = &File
'Edit Menu = &Modifica
'View Menu = &Visualizza
'Insert Menu = &Inserisci
'Tools Menu = &Strumenti
'Window Menu = Fi&nestra
'HelpMenu = &?
'View Toolbars Menu = &Barre degli strumenti
```
