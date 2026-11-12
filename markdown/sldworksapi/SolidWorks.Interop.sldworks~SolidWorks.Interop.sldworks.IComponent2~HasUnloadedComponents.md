---
title: "HasUnloadedComponents Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "HasUnloadedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html"
---

# HasUnloadedComponents Method (IComponent2)

Gets whether this component has hidden or suppressed unloaded children components.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasUnloadedComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.HasUnloadedComponents()
```

### C#

```csharp
System.bool HasUnloadedComponents()
```

### C++/CLI

```cpp
System.bool HasUnloadedComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component has hidden or suppressed unloaded children components, false if not

## VBA Syntax

See [Component2::HasUnloadedComponents](ms-its:sldworksapivb6.chm::/sldworks~Component2~HasUnloadedComponents.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html)
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html)
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
