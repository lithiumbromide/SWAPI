---
title: "GetChildren Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html"
---

# GetChildren Method (IConfiguration)

Gets all of the children configurations of this derived configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildren() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Object

value = instance.GetChildren()
```

### C#

```csharp
System.object GetChildren()
```

### C++/CLI

```cpp
System.Object^ GetChildren();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the children [configurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) of this configuration

## VBA Syntax

See [Configuration::GetChildren](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetChildren.html).

## Examples

[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IsDerived.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html)
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IConfiguration::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
