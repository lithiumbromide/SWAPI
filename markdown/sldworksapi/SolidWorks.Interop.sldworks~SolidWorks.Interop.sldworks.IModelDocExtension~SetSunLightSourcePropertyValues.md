---
title: "SetSunLightSourcePropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetSunLightSourcePropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.html"
---

# SetSunLightSourcePropertyValues Method (IModelDocExtension)

Sets the property values for a sunlight source.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSunLightSourcePropertyValues( _
   ByVal NorthDirection As MathVector, _
   ByVal NorthLatitude As System.Double, _
   ByVal EastLongitude As System.Double, _
   ByVal TimeZone As System.Double, _
   ByVal DateTime As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NorthDirection As MathVector
Dim NorthLatitude As System.Double
Dim EastLongitude As System.Double
Dim TimeZone As System.Double
Dim DateTime As System.String
Dim value As System.Boolean

value = instance.SetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
```

### C#

```csharp
System.bool SetSunLightSourcePropertyValues(
   MathVector NorthDirection,
   System.double NorthLatitude,
   System.double EastLongitude,
   System.double TimeZone,
   System.string DateTime
)
```

### C++/CLI

```cpp
System.bool SetSunLightSourcePropertyValues(
   MathVector^ NorthDirection,
   System.double NorthLatitude,
   System.double EastLongitude,
   System.double TimeZone,
   System.String^ DateTime
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NorthDirection`: [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html); north direction of the sunlight source
- `NorthLatitude`: North latitude of the sunlight source
- `EastLongitude`: East longitude of the sunlight source
- `TimeZone`: Standard time zone of the sunlight source
- `DateTime`: Date and time stamp in the specified TimeZone

### Return Value

True if sunlight source property values are successfully set, false if not

## VBA Syntax

See [ModelDocExtension::SetSunLightSourcePropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetSunLightSourcePropertyValues.html).

## Examples

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
