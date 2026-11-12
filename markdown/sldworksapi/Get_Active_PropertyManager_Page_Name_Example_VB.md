---
title: "Get Active PropertyManager Page Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Active_PropertyManager_Page_Name_Example_VB.htm"
---

# Get Active PropertyManager Page Name Example (VBA)

This example shows how to get the name of the active PropertyManager page.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. At Stop:
'    a. In the SOLIDWORKS Design user-interface,
'       click Insert > Features > Fillet/Round.
'    b. In the IDE, click Continue.
' 2. Gets the name of the active PropertyManager page.
' 4. Examine the Immediate window.
' 5. In the SOLIDWORKS Design user-interface:
'    a. Close the PropertyManager page.
'    b. Close the part document.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'----------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim file As String
Dim errors As Long
Dim warnings As Long
Dim pageName As String
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
file = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
Set swModel = swApp.OpenDoc6(file, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
```

```
Stop
' 1. Click Insert > Features > Fillet/Round in the SOLIDWORKS user-interface
' 2. Click Continue in the IDE
```

```
' Print the name of the active PropertyManager page in the Immediate window
pageName = swModelDocExt.GetActivePropertyManagerPage
Debug.Print "Name of active PropertyManager page: " & pageName
```

```
End Sub
```
