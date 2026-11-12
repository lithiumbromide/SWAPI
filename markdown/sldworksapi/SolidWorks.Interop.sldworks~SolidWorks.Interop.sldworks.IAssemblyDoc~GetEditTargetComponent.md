---
title: "GetEditTargetComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetEditTargetComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.html"
---

# GetEditTargetComponent Method (IAssemblyDoc)

Gets the component that is currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditTargetComponent() As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As Component2

value = instance.GetEditTargetComponent()
```

### C#

```csharp
Component2 GetEditTargetComponent()
```

### C++/CLI

```cpp
Component2^ GetEditTargetComponent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) being edited

## VBA Syntax

See [AssemblyDoc::GetEditTargetComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetEditTargetComponent.html).

## Examples

[Reorganize Components (VBA)](Reorganize_Components_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetEditTarget Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTarget.html)
[IGetEditTarget Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget.html)
[IsEditingSelf Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsEditingSelf.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
