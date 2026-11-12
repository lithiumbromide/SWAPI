---
title: "GetParent Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html"
---

# GetParent Method (IConfiguration)

Gets the parent configuration of this derived configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParent() As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As Configuration

value = instance.GetParent()
```

### C#

```csharp
Configuration GetParent()
```

### C++/CLI

```cpp
Configuration^ GetParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Parent configuration of this derived configuration

## VBA Syntax

See [Configuration::GetParent](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetParent.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IsDerived.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.html)
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html)
[IConfigurationt::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)

## Availability

SOLIDWORKS 2003 SP1, Revision number 11.1
