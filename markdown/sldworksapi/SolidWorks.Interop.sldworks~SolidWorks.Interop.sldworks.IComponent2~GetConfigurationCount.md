---
title: "GetConfigurationCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetConfigurationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetConfigurationCount.html"
---

# GetConfigurationCount Method (IComponent2)

Gets the number of configurations for this lightweight assembly component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetConfigurationCount()
```

### C#

```csharp
System.int GetConfigurationCount()
```

### C++/CLI

```cpp
System.int GetConfigurationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of configurations for this lightweight assembly component

## VBA Syntax

See [Component2::GetConfigurationCount](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetConfigurationCount.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
