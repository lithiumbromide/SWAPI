---
title: "SunLightInformation Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SunLightInformation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.html"
---

# SunLightInformation Property (IModelDocExtension)

Gets the specified sunlight information.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SunLightInformation( _
   ByVal Type As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Type As System.Integer
Dim value As System.Double

value = instance.SunLightInformation(Type)
```

### C#

```csharp
System.double SunLightInformation(
   System.int Type
) {get;}
```

### C++/CLI

```cpp
property System.double SunLightInformation {
   System.double get(System.int Type);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Sunlight information as defined by [swSunlightInfoType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSunlightInfoType_e.html)

### Property Value

Sunlight information

## VBA Syntax

See [ModelDocExtension::SunLightInformation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SunLightInformation.html).

## Examples

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::UpdateSunLight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.html)
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.html)
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
