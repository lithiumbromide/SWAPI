---
title: "SetSystemValue3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetSystemValue3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html"
---

# SetSystemValue3 Method (IDimension)

Sets the value of this dimension in system units (meters) in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSystemValue3( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Integer

value = instance.SetSystemValue3(NewValue, WhichConfigurations, Config_names)
```

### C#

```csharp
System.int SetSystemValue3(
   System.double NewValue,
   System.int WhichConfigurations,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.int SetSystemValue3(
   System.double NewValue,
   System.int WhichConfigurations,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewValue`: Dimension value in meters
- `WhichConfigurations`: Configuration in which to set this value as defined in [swSetValueInConfiguration_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html) (see **Remarks**)
- `Config_names`: Names of the configurations (see **Remarks**)

### Return Value

Success indicator value as defined in [swSetValueReturnStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

## VBA Syntax

See [Dimension::SetSystemValue3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetSystemValue3.html).

## Examples

[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)
[Modify Plane By Changing System Value (VBA)](Modify_Plane_by_Changing_System_Value_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

## Remarks

The WhichConfigurations argument is equivalent to the Change Parameter dialog in the SOLIDWORKS Design user interface, which gives the user the option of having the value set in all configurations or the current configuration. If there is one configuration in the part, SOLIDWORKS ignores this argument.

Config_names argument is only used if WhichConfigurations is set to swSetValue_InSpecificConfigurations and can contain either a BSTR array or a single BSTR.

This method allows you to change the value of a read-only dimension. You can use [IDimension::ReadOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ReadOnly.html) to determine if a dimension is read-only.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html)
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html)
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html)
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html)
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
