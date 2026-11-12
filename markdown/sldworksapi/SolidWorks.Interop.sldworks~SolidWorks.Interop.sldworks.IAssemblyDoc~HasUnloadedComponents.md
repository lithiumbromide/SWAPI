---
title: "HasUnloadedComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "HasUnloadedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html"
---

# HasUnloadedComponents Method (IAssemblyDoc)

Gets whether this assembly has hidden or suppressed unloaded components.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasUnloadedComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
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

True if the assembly has hidden or suppressed unloaded components, false if not

## VBA Syntax

See [AssemblyDoc::HasUnloadedComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~HasUnloadedComponents.html).

## Examples

[Get Hidden Components Filenames (C#)](Get_Hidden_Components_Filenames_Example_CSharp.htm)
[Get Hidden Components Filenames (VB.NET)](Get_Hidden_Components_Filenames_Example_VBNET.htm)
[Get Hidden Component Filenames (VBA)](Get_Hidden_Components_Filenames_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html)
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html)
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
