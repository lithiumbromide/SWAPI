---
title: "SetValue3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetValue3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html"
---

# SetValue3 Method (IDimension)

Sets the values of the dimensions in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValue3( _
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

value = instance.SetValue3(NewValue, WhichConfigurations, Config_names)
```

### C#

```csharp
System.int SetValue3(
   System.double NewValue,
   System.int WhichConfigurations,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.int SetValue3(
   System.double NewValue,
   System.int WhichConfigurations,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewValue`: Value for this dimension in the units of owning document
- `WhichConfigurations`: Configurations in which to set this value as defined in [swSetValueInConfiguration_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html) (see **Remarks**)
- `Config_names`: Names of the configurations for which to set dimension values (see **Remarks**)

### Return Value

Error code as defined in [swSetValueReturnStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

## VBA Syntax

See [Dimension::SetValue3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetValue3.html).

## Remarks

The Config_names argument is only used if WhichConfigurations is set to swSetValue_InSpecificConfigurations and can contain either a BSTR array or a single BSTR.

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
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
