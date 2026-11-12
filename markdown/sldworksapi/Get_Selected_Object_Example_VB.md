---
title: "Get Selected Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Object_Example_VB.htm"
---

# Get Selected Object Example (VBA)

This example shows how to select and get that object in a SOLIDWORKS Design document.

```
'------------------------------------------------------------
' Preconditions.
' 1. Open public_documents\samples\tutorial\api\box.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the Boss-Extrude1 feature.
' 2. Examine the Immediate window and graphics area.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Model As ModelDoc2
Dim feature As feature
Dim boolstatus As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Model = swApp.ActiveDoc
```

```
    boolstatus = Model.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
```

```
    If boolstatus = True Then
        Dim SelMgr As SelectionMgr
        Set SelMgr = Model.SelectionManager
        Set feature = SelMgr.GetSelectedObject6(1, 0)
        Debug.Print (feature.Name & " selected")
    Else
        Debug.Print "Error"
    End If
```

```
End Sub
```
