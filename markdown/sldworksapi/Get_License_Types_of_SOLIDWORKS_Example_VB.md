---
title: "Get License Type of SOLIDWORKS Design Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_License_Types_of_SOLIDWORKS_Example_VB.htm"
---

# Get License Type of SOLIDWORKS Design Example (VBA)

This example shows how to get the type of license used when the model was created.

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part document.
' 2. Gets the type of license used when
'    the model was created.
' 3. Examine the Immediate window.
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim licenseType As Long
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    licenseType = swModelDocExt.GetLicenseType
    Debug.Print "Type of license used when the model was created as defined by swLicenseType_e: " & licenseType
```

```
End Sub
```
