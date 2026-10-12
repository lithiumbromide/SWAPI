---
title: "Turn Lights On Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Turn_Lights_On_Example_VB.htm"
---

# Turn Lights On Example (VBA)

This example shows how to:

- turn all of the lights on.
- pack two integers into a double value.

```
'------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Turns on all of the lights.
' 2. Examine the Immediate window.
'-------------------------------------------
Option Explicit
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Int2Rec
    iLower As Long ' Assuming that a C int has 4 bytes
    iUpper As Long
End Type
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim nLightCount As Long
    Dim vLightProp As Variant
    Dim dr As DoubleRec
    Dim i2r As Int2Rec
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
```

```
    ' Forcibly turn lights on
    i2r.iLower = 0
    i2r.iUpper = 0
    LSet dr = i2r
```

```
    swFeatMgr.EnableFeatureTree = False
```

```
    Debug.Print "File = " & swModel.GetPathName
    nLightCount = swModel.GetLightSourceCount
    For i = 0 To nLightCount - 1
        vLightProp = swModel.LightSourcePropertyValues(i)
        Debug.Print "  SOLIDWORKS Design name for light = " & swModel.GetLightSourceName(i)
        Debug.Print "  User name for light = " & swModel.LightSourceUserName(i)
        vLightProp(17) = dr.dValue
        swModel.LightSourcePropertyValues(i) = vLightProp
    Next i
```

```
    swFeatMgr.EnableFeatureTree = True

    swFeatMgr.UpdateFeatureTree
```

```
    swModel.EditRebuild3
```

```
End Sub
```
