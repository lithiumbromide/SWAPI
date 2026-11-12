---
title: "HasAssemblyFeatures Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "HasAssemblyFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasAssemblyFeatures.html"
---

# HasAssemblyFeatures Method (IComponent2)

Gets whether this component has assembly features in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasAssemblyFeatures( _
   ByRef ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.HasAssemblyFeatures(ConfigurationName)
```

### C#

```csharp
System.bool HasAssemblyFeatures(
   out System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool HasAssemblyFeatures(
   [Out] System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Configuration name

### Return Value

True if has assembly features, false if not

## VBA Syntax

See [Component2::HasAssemblyFeatures](ms-its:sldworksapivb6.chm::/sldworks~Component2~HasAssemblyFeatures.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
