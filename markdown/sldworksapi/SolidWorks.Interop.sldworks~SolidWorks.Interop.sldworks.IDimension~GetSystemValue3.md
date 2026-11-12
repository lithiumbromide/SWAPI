---
title: "GetSystemValue3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetSystemValue3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html"
---

# GetSystemValue3 Method (IDimension)

Gets the value of the current dimension in system units in the named configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSystemValue3( _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.GetSystemValue3(WhichConfigurations, Config_names)
```

### C#

```csharp
System.object GetSystemValue3(
   System.int WhichConfigurations,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetSystemValue3(
   System.int WhichConfigurations,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichConfigurations`: Configurations to get this value from as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)
- `Config_names`: Names of the configurations (see **Remarks**)

### Return Value

Array of doubles of the dimension values in system units

## VBA Syntax

See [Dimension::GetSystemValue3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetSystemValue3.html).

## Examples

[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)
[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Dimension of Distance Mate (VBA)](Get_Dimension_of_Distance_Mate_Example_VB.htm)
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Modify Plane By Changing System Value (VBA)](Modify_Plane_by_Changing_System_Value_Example_VB.htm)
[Get Depth of Extrusion (VBA)](Get_Depth_of_Extrusion_Example_VB.htm)
[Get Depth of Extrusion (VB.NET)](Get_Depth_of_Extrusion_Example_VBNET.htm)
[Get Depth of Extrusion (C#)](Get_Depth_of_Extrusion_Example_CSharp.htm)

## Remarks

The Config_names argument is only used if WhichConfigurations is set to swSpecifyConfiguration.

In OLE, Config_names can be either a BSTR array or a single BSTR.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html)
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html)
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.html)
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
