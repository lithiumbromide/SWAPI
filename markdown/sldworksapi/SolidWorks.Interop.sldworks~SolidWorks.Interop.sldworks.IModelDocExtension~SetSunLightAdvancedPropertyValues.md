---
title: "SetSunLightAdvancedPropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetSunLightAdvancedPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.html"
---

# SetSunLightAdvancedPropertyValues Method (IModelDocExtension)

Sets the specified sunlight advanced properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSunLightAdvancedPropertyValues( _
   ByVal Haze As System.Double, _
   ByVal SunDiameter As System.Double, _
   ByVal GroundAlbedo As System.Integer, _
   ByVal SkyGamma As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Haze As System.Double
Dim SunDiameter As System.Double
Dim GroundAlbedo As System.Integer
Dim SkyGamma As System.Double
Dim value As System.Boolean

value = instance.SetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)
```

### C#

```csharp
System.bool SetSunLightAdvancedPropertyValues(
   System.double Haze,
   System.double SunDiameter,
   System.int GroundAlbedo,
   System.double SkyGamma
)
```

### C++/CLI

```cpp
System.bool SetSunLightAdvancedPropertyValues(
   System.double Haze,
   System.double SunDiameter,
   System.int GroundAlbedo,
   System.double SkyGamma
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Haze`: 0.0 <= Haze setting < = 1.0
- `SunDiameter`: 0.01 < = sun diameter visible in the scene <= 21474836.47
- `GroundAlbedo`: RGB color reflected from the ground upwards
- `SkyGamma`: 0.1 <= visible sky Output Gamma <= 100.0

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelDocExtension::SetSunLightAdvancedPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetSunLightAdvancedPropertyValues.html).

## Remarks

After calling this method, call [IModelDocExtension::UpdateSunLight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.html)
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.html)
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
