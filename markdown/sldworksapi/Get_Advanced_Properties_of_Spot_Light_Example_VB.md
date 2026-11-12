---
title: "Get Advanced Properties of Spot Light Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Advanced_Properties_of_Spot_Light_Example_VB.htm"
---

# Get Advanced Properties of Spot Light Example (VBA)

This example shows how to get the attenuation-related, advanced properties of a specified SOLIDWORKS Design spot light.

```
'--------------------------------------------
' Preconditions:
' 1. Open a part that has a spot light
'    whose SOLIDWORKS Design-internal light source
'    name is SW#3.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets advanced properties of SOLIDWORKS Design-internal
'    light source SW#3.
' 2. Examine the Immediate window.
'-------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim sLightName As String
Dim lLightCount As Long, i As Long
Dim dExponent As Double, dAttenuationConst As Double, dAttenuationLinear As Double, dAttenuationQuad As Double
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
    lLightCount = swModel.GetLightSourceCount
    Debug.Print "Number of lights: " & lLightCount
    For i = 0 To lLightCount - 1
       ' Get the SOLIDWORKS-internal light source name
        sLightName = swModel.GetLightSourceName(i)
        Debug.Print "SOLIDWORKS-internal light source name: " & sLightName
        If sLightName = "SW#3" Then
            swModelDocExt.GetAdvancedSpotLightProperties sLightName, dExponent, dAttenuationConst, dAttenuationLinear, dAttenuationQuad
            Debug.Print "  Attenuation exponent: " & dExponent
            Debug.Print "  Attenuation constant factor: " & dAttenuationConst
            Debug.Print "  Attenuation linear factor: " & dAttenuationLinear
            Debug.Print "  Attenuation quadratic factor: " & dAttenuationQuad
        End If
    Next i
```

```
End Sub
```
