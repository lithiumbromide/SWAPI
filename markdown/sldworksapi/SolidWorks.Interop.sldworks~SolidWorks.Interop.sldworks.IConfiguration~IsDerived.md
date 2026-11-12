---
title: "IsDerived Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IsDerived"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.html"
---

# IsDerived Method (IConfiguration)

Gets whether this configuration is a derived configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDerived() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

value = instance.IsDerived()
```

### C#

```csharp
System.bool IsDerived()
```

### C++/CLI

```cpp
System.bool IsDerived();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this configuration is a derived configuration, false if not

## VBA Syntax

See [Configuration::IsDerived](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IsDerived.html).

## Examples

[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)
[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::IsDefeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDefeature.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
