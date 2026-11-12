---
title: "Reverse Order of Decals Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reverse_Order_of_Decals_Example_VB.htm"
---

# Reverse Order of Decals Example (VBA)

This example shows how to reverse the order of the decals applied on a model.

```
'---------------------------------------
' Preconditions:
' 1. Open a model that has two decals
'    applied on it.
' 2. Click the DisplayManager tab and click
'    each decal to see its order.
' 3. Click a blank spot in the DisplayManager.
'
' Postconditions:
' 1. Reverses the order of the decals.
' 2. Click each decal to see its new order.
'---------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDecal As SldWorks.Decal
Dim lNbrDecals As Long
Dim boolstatus As Boolean
Dim arrDecals As Variant
Dim i As Long
Dim iDecalID As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    arrDecals = swModelDocExt.GetDecals()
```

```
    'Get last decal ID
    lNbrDecals = swModelDocExt.GetDecalsCount
```

```
    ' Reverse order of decals
    boolstatus = swModelDocExt.ReverseDecalsOrder(lNbrDecals)
```

```
    ' Force a rebuild of the model
    boolstatus = swModel.ForceRebuild3(True)
```

```
End Sub
```
