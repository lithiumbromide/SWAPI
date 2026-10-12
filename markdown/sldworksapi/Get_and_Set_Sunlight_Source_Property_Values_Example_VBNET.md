---
title: "Get and Set Sunlight Source Property Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm"
---

# Get and Set Sunlight Source Property Values Example (VB.NET)

This example shows how to get and set sunlight properties.

```vb
 '----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part with a sunlight source.
' 2. Open an Immediate window.
'
' Postconditions: Inspect the Immediate window for the sunlight properties.
' ---------------------------------------------------------------------------
```

```vb
Imports
```

SolidWorks.Interop.sldworks

```vb
Imports
```

SolidWorks.Interop.swconst

```vb
Imports
```

System.Runtime.InteropServices

```vb
Imports
```

System

```vb
Imports
```

System.Diagnostics

```vb
Partial
```

Class

SolidWorksMacro

Dim swModelDoc As

ModelDoc2

Dim swModelDocExt As

ModelDocExtension

Dim retval As Boolean

Dim NorthDirection As

MathVector

Dim DateTime As String

Dim vVector As Object

Dim nVector(2) As Double

Dim swMathUtil As

MathUtility

Dim NorthLatitude As Double

Dim EastLongitude As Double

Dim TimeZone As Double

Dim Haze As Double

Dim SunDiameter As Double

Dim GroundAlbedo As Integer

Dim SkyGamma As Double

Sub

main()

```vb
swModelDoc = swApp.ActiveDoc
swModelDocExt = swModelDoc.Extension
```

'Get sunlight property values

```vb
retval = swModelDocExt.GetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
retval = swModelDocExt.GetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)
Debug.Print(
```

"North direction: " & NorthDirection.**ArrayData**(0) & "," & NorthDirection.**ArrayData**(1) & ","

& NorthDirection.**ArrayData**(2))

```vb
Debug.Print(
```

"North latitude: "

& NorthLatitude)

```vb
Debug.Print(
```

"East longitude: "

& EastLongitude)

```vb
Debug.Print(
```

"Time zone: "

& TimeZone)

```vb
Debug.Print(
```

"Date and time: "

& DateTime)

```vb
Debug.Print(
```

"Haze (0.0 - 1.0): "

& Haze)

```vb
Debug.Print(
```

"Sun diameter (0.01 - 21474836.47): "

& SunDiameter)

```vb
Debug.Print(
```

"RGB for ground albedo: "

& GroundAlbedo)

```vb
Debug.Print(
```

"Sky Gamma (0.1 = 100.0): "

& SkyGamma)

Debug.Print("Minutes of sunlight: " & swModelDocExt.**SunLightInformation**(swSunlightInfoType_e.swSunlight_LengthOfDay**))**

```vb
Debug.Print("Sunrise (hours from midnight): " & swModelDocExt.SunLightInformation(swSunlightInfoType_e.swSunlight_Sunrise))
Debug.Print("Sunset (hours from midnight): " & swModelDocExt.SunLightInformation(swSunlightInfoType_e.swSunlight_Sunset))
'Set sunlight source property values
```

```vb
swMathUtil = swApp.GetMathUtility
nVector(0) = 1 : nVector(1) = 0 : nVector(2) = 0
vVector = nVector
NorthDirection = swMathUtil.CreateVector((vVector))
DateTime =
```

"11/9/2012 2:48:13 PM"

```vb
NorthLatitude = NorthLatitude + 0.1
EastLongitude = EastLongitude + 0.1
TimeZone = TimeZone + 0.5
retval = swModelDocExt.SetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
```

End Sub

Public swApp As SldWorks

```vb
End
```

Class
