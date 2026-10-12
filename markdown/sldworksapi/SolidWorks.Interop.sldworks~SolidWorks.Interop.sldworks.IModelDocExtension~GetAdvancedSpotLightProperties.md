---
title: "GetAdvancedSpotLightProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAdvancedSpotLightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSpotLightProperties.html"
---

# GetAdvancedSpotLightProperties Method (IModelDocExtension)

Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetAdvancedSpotLightProperties( _
   ByVal Name As System.String, _
   ByRef Exponent As System.Double, _
   ByRef AttenuationConst As System.Double, _
   ByRef AttenuationLinear As System.Double, _
   ByRef AttenuationQuad As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim Exponent As System.Double
Dim AttenuationConst As System.Double
Dim AttenuationLinear As System.Double
Dim AttenuationQuad As System.Double

instance.GetAdvancedSpotLightProperties(Name, Exponent, AttenuationConst, AttenuationLinear, AttenuationQuad)
```

### C#

```csharp
void GetAdvancedSpotLightProperties(
   System.string Name,
   out System.double Exponent,
   out System.double AttenuationConst,
   out System.double AttenuationLinear,
   out System.double AttenuationQuad
)
```

### C++/CLI

```cpp
void GetAdvancedSpotLightProperties(
   System.String^ Name,
   [Out] System.double Exponent,
   [Out] System.double AttenuationConst,
   [Out] System.double AttenuationLinear,
   [Out] System.double AttenuationQuad
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: SOLIDWORKS light source name
- `Exponent`: Attenuation exponent
- `AttenuationConst`: Constant attenuation factor
- `AttenuationLinear`: Linear attenuation factor
- `AttenuationQuad`: Quadratic attenuation factor

## VBA Syntax

See [ModelDocExtension::GetAdvancedSpotLightProperties](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetAdvancedSpotLightProperties.html).

## Examples

[Get Advanced Properties of Spot Light (VBA)](Get_Advanced_Properties_of_Spot_Light_Example_VB.htm)

## Remarks

See the SOLIDWORKS Help for more information about the advanced properties of spot lights.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
