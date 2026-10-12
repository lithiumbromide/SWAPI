---
title: "GetSunLightAdvancedPropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSunLightAdvancedPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.html"
---

# GetSunLightAdvancedPropertyValues Method (IModelDocExtension)

Gets the specified sunlight advanced properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSunLightAdvancedPropertyValues( _
   ByRef Haze As System.Double, _
   ByRef SunDiameter As System.Double, _
   ByRef GroundAlbedo As System.Integer, _
   ByRef SkyGamma As System.Double _
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

value = instance.GetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)
```

### C#

```csharp
System.bool GetSunLightAdvancedPropertyValues(
   out System.double Haze,
   out System.double SunDiameter,
   out System.int GroundAlbedo,
   out System.double SkyGamma
)
```

### C++/CLI

```cpp
System.bool GetSunLightAdvancedPropertyValues(
   [Out] System.double Haze,
   [Out] System.double SunDiameter,
   [Out] System.int GroundAlbedo,
   [Out] System.double SkyGamma
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

See [ModelDocExtension::GetSunLightAdvancedPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSunLightAdvancedPropertyValues.html).

## Examples

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.html)
[IModelDocExtension::UpdateSunLight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.html)
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.html)
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
