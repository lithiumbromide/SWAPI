---
title: "Get and Set Sunlight Source Property Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm"
---

# Get and Set Sunlight Source Property Values Example (C#)

This example shows how to get and set sunlight properties.

```vb
 //----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part with a sunlight source.
// 2. Open an Immediate window.
//
// Postconditions: Inspect the Immediate window for the sunlight properties.
// ---------------------------------------------------------------------------
```

```vb
using
```

Microsoft.VisualBasic;

```vb
using
```

System;

```vb
using
```

System.Collections;

```vb
using
```

System.Collections.Generic;

```vb
using
```

System.Data;

```vb
using
```

System.Diagnostics;

```vb
using
```

SolidWorks.Interop.sldworks;

```vb
using
```

SolidWorks.Interop.swconst;

```vb
using
```

System.Runtime.InteropServices;

```vb
namespace
```

SunlightProperties_CSharp.csproj

```vb
{
```

partial class SolidWorksMacro

```vb
{
```

ModelDoc2

swModelDoc;

ModelDocExtension

swModelDocExt;

bool

retval;

MathVector

NorthDirection;

string

DateTime;

object

vVector;

double[] nVector = new double

[3];

MathUtility

swMathUtil;

double

NorthLatitude;

double

EastLongitude;

double

TimeZone;

double

Haze;

double

SunDiameter;

int

GroundAlbedo;

double

SkyGamma;

public void

Main()

```vb
{
```

```vb
swModelDoc = (
```

ModelDoc2

)swApp.**ActiveDoc**;

```vb
swModelDocExt = swModelDoc.Extension;
```

//Get sunlight properties

```vb
retval = swModelDocExt.GetSunLightSourcePropertyValues(
```

out NorthDirection, out NorthLatitude, out EastLongitude, out TimeZone, out

DateTime);

```vb
retval = swModelDocExt.GetSunLightAdvancedPropertyValues(
```

out Haze, out SunDiameter, out GroundAlbedo, out

SkyGamma);

Debug.Print("North direction: " + ((double[])(NorthDirection.**ArrayData**))[0] + "," + ((double[])(NorthDirection.**ArrayData**))[1] + "," + ((double

[])(NorthDirection.**ArrayData**))[2]);

Debug.Print("North latitude: "

+ NorthLatitude);

Debug.Print("East longitude: "

+ EastLongitude);

Debug.Print("Time zone: "

+ TimeZone);

Debug.Print("Date and time: "

+ DateTime);

Debug.Print("Haze (0.0 - 1.0): "

+ Haze);

Debug.Print("Sun diameter (0.01 - 21474836.47): "

+ SunDiameter);

Debug.Print("RGB for ground albedo: "

+ GroundAlbedo);

Debug.Print("Sky Gamma (0.1 = 100.0): "

+ SkyGamma);

```vb
Debug.Print("Minutes of sunlight: " + swModelDocExt.get_SunLightInformation((int)swSunlightInfoType_e.swSunlight_LengthOfDay));
Debug.Print("Sunrise (hours from midnight): " + swModelDocExt.get_SunLightInformation((int)swSunlightInfoType_e.swSunlight_Sunrise));
Debug.Print("Sunset (hours from midnight): " + swModelDocExt.get_SunLightInformation((int)swSunlightInfoType_e.swSunlight_Sunset));
```

```vb
//Set sunlight source property values
```

```vb
swMathUtil = (
```

MathUtility

)swApp.**GetMathUtility**();

```vb
nVector[0] = 1;
nVector[1] = 0;
nVector[2] = 0;
vVector = nVector;
NorthDirection = (
```

MathVector

)swMathUtil.**CreateVector**((vVector));

```vb
DateTime =
```

"11/9/2012 2:48:13 PM"

;

```vb
NorthLatitude = NorthLatitude + 0.1;
EastLongitude = EastLongitude + 0.1;
TimeZone = TimeZone + 0.5;
retval = swModelDocExt.SetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime);
}
```

public SldWorks

swApp;

```vb
}
}
```
