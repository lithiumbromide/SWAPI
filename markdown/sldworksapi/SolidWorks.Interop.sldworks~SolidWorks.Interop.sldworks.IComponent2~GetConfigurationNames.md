---
title: "GetConfigurationNames Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetConfigurationNames.html"
---

# GetConfigurationNames Method (IComponent2)

Gets the names of configurations for this lightweight assembly component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetConfigurationNames()
```

### C#

```csharp
System.object GetConfigurationNames()
```

### C++/CLI

```cpp
System.Object^ GetConfigurationNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of configuration names

## VBA Syntax

See [Component2::GetConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetConfigurationNames.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
