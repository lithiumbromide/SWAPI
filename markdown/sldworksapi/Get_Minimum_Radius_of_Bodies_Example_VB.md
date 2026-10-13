---
title: "Get Minimum Radius of Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Minimum_Radius_of_Bodies_Example_VB.htm"
---

# Get Minimum Radius of Bodies Example (VBA)

This example shows how to get the minimum radius of each body in a multibody part.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document
'    to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document as read only.
' 2. Gets the minimum radius of each body.
' 3. Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim bodies As Variant
Dim vbody As Variant
Dim radius As Double
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swPart = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
    bodies = swPart.GetBodies2(SwConst.swBodyType_e.swAllBodies, False)
```

```
    i = 1
    For Each vbody In bodies
        radius = vbody.MinimumRadius()
        Debug.Print vbody.Name & "'s " & "minimum radius: " & radius
        i = i + 1
    Next vbody
```

```
End Sub
```
