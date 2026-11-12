---
title: "GetSpotlightProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetSpotlightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSpotlightProperties.html"
---

# GetSpotlightProperties Method (IModelDoc2)

Gets the spotlight properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpotlightProperties( _
   ByVal Name As System.String, _
   ByRef Ambient As System.Double, _
   ByRef Diffuse As System.Double, _
   ByRef Specular As System.Double, _
   ByRef Colour As System.Integer, _
   ByRef Enabled As System.Boolean, _
   ByRef Fixed As System.Boolean, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef Targetx As System.Double, _
   ByRef Targety As System.Double, _
   ByRef Targetz As System.Double, _
   ByRef ConeAngle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim Ambient As System.Double
Dim Diffuse As System.Double
Dim Specular As System.Double
Dim Colour As System.Integer
Dim Enabled As System.Boolean
Dim Fixed As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Targetx As System.Double
Dim Targety As System.Double
Dim Targetz As System.Double
Dim ConeAngle As System.Double
Dim value As System.Boolean

value = instance.GetSpotlightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, X, Y, Z, Targetx, Targety, Targetz, ConeAngle)
```

### C#

```csharp
System.bool GetSpotlightProperties(
   System.string Name,
   ref System.double Ambient,
   ref System.double Diffuse,
   ref System.double Specular,
   ref System.int Colour,
   ref System.bool Enabled,
   ref System.bool Fixed,
   ref System.double X,
   ref System.double Y,
   ref System.double Z,
   ref System.double Targetx,
   ref System.double Targety,
   ref System.double Targetz,
   ref System.double ConeAngle
)
```

### C++/CLI

```cpp
System.bool GetSpotlightProperties(
   System.String^ Name,
   System.double% Ambient,
   System.double% Diffuse,
   System.double% Specular,
   System.int% Colour,
   System.bool% Enabled,
   System.bool% Fixed,
   System.double% X,
   System.double% Y,
   System.double% Z,
   System.double% Targetx,
   System.double% Targety,
   System.double% Targetz,
   System.double% ConeAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Light name used internally (returned by [IModelDoc2::GetLightSourceName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceName.html))
- `Ambient`: Light source ambient value
- `Diffuse`: Light source diffuse value
- `Specular`: Light source specular value
- `Colour`: COLORREF color value
- `Enabled`: True if a light is enabled, false if not
- `Fixed`: True if a light is fixed, false if not
- `X`: x location of the spot light
- `Y`: y location of the spot light
- `Z`: location of the spot light target
- `Targetx`: x location of the spot light target
- `Targety`: y location of the spot light target
- `Targetz`: z location of the spot light target
- `ConeAngle`: Cone angle through which the beam spreads in degrees

### Return Value

True if light properties determined without a problem, false if not

## VBA Syntax

See [ModelDoc2::GetSpotlightProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetSpotlightProperties.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetPointLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPointLightProperties.html)
[IModelDoc2::GetAmbientLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAmbientLightProperties.html)
[IModelDoc2::GetDirectionLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDirectionLightProperties.html)
[IModelDoc2::GetPointLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPointLightProperties.html)
[IModelDoc2::SetAmbientLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAmbientLightProperties.html)
[IModelDoc2::SetDirectionLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDirectionLightProperties.html)
[IModelDoc2::SetPointLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPointLightProperties.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
