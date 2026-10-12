---
title: "SetAdvancedSpotLightProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetAdvancedSpotLightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetAdvancedSpotLightProperties.html"
---

# SetAdvancedSpotLightProperties Method (IModelDocExtension)

Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAdvancedSpotLightProperties( _
   ByVal Name As System.String, _
   ByVal Exponent As System.Double, _
   ByVal AttenuationConst As System.Double, _
   ByVal AttenuationLinear As System.Double, _
   ByVal AttenuationQuad As System.Double _
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

instance.SetAdvancedSpotLightProperties(Name, Exponent, AttenuationConst, AttenuationLinear, AttenuationQuad)
```

### C#

```csharp
void SetAdvancedSpotLightProperties(
   System.string Name,
   System.double Exponent,
   System.double AttenuationConst,
   System.double AttenuationLinear,
   System.double AttenuationQuad
)
```

### C++/CLI

```cpp
void SetAdvancedSpotLightProperties(
   System.String^ Name,
   System.double Exponent,
   System.double AttenuationConst,
   System.double AttenuationLinear,
   System.double AttenuationQuad
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

See [ModelDocExtension::SetAdvancedSpotLightProperties](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~SetAdvancedSpotLightProperties.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
