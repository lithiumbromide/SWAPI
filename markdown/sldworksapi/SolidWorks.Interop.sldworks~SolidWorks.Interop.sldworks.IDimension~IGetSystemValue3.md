---
title: "IGetSystemValue3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IGetSystemValue3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html"
---

# IGetSystemValue3 Method (IDimension)

Gets the value of the current dimension in system units in the named configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSystemValue3( _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim WhichConfigurations As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Double

value = instance.IGetSystemValue3(WhichConfigurations, Config_count, Config_names)
```

### C#

```csharp
System.double IGetSystemValue3(
   System.int WhichConfigurations,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.double IGetSystemValue3(
   System.int WhichConfigurations,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichConfigurations`: Configurations to get this value from as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)
- `Config_count`: Number of configurations (see Remarks)
- `Config_names`: Names of the configuration (see Remarks)

### Return Value

Value in system units

## VBA Syntax

See [Dimension::IGetSystemValue3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IGetSystemValue3.html).

## Remarks

The Config_count and Config_names arguments are only used if WhichConfigurations is set to swSpecifyConfiguration.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html)
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html)
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html)
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.html)
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
