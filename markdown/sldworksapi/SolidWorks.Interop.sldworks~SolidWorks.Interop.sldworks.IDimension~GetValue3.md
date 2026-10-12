---
title: "GetValue3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetValue3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html"
---

# GetValue3 Method (IDimension)

Gets the values of the dimensions in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetValue3( _
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

value = instance.GetValue3(WhichConfigurations, Config_names)
```

### C#

```csharp
System.object GetValue3(
   System.int WhichConfigurations,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetValue3(
   System.int WhichConfigurations,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichConfigurations`: Configurations in which to get this value as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)
- `Config_names`: Names of the configurations (see Remarks)

### Return Value

Array of doubles of the dimensions for the specified configurations

## VBA Syntax

See [Dimension::GetValue3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetValue3.html).

## Examples

[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)

## Remarks

The Config_names argument is only used if WhichConfigurations is set to swSpecifyConfiguration. Config_names can contain either a BSTR array or a single BSTR.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html)
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html)
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html)
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html)
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.html)
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
