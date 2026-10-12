---
title: "GetSunLightSourcePropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSunLightSourcePropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.html"
---

# GetSunLightSourcePropertyValues Method (IModelDocExtension)

Gets the property values for a sunlight source.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSunLightSourcePropertyValues( _
   ByRef NorthDirection As MathVector, _
   ByRef NorthLatitude As System.Double, _
   ByRef EastLongitude As System.Double, _
   ByRef TimeZone As System.Double, _
   ByRef DateTime As System.String _
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

value = instance.GetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
```

### C#

```csharp
System.bool GetSunLightSourcePropertyValues(
   out MathVector NorthDirection,
   out System.double NorthLatitude,
   out System.double EastLongitude,
   out System.double TimeZone,
   out System.string DateTime
)
```

### C++/CLI

```cpp
System.bool GetSunLightSourcePropertyValues(
   [Out] MathVector^ NorthDirection,
   [Out] System.double NorthLatitude,
   [Out] System.double EastLongitude,
   [Out] System.double TimeZone,
   [Out] System.String^ DateTime
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

True if getting the value is successful, false if not

## VBA Syntax

See [ModelDocExtension::GetSunLightSourcePropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSunLightSourcePropertyValues.html).

## Examples

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
