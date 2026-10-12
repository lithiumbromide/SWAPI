---
title: "IsEditingSelf Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsEditingSelf"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsEditingSelf.html"
---

# IsEditingSelf Method (IModelDoc2)

Gets whether this model is being edited in the context of another document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsEditingSelf() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.IsEditingSelf()
```

### C#

```csharp
System.bool IsEditingSelf()
```

### C++/CLI

```cpp
System.bool IsEditingSelf();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model document is the active edit target, false if the model document is not the active edit target of this SOLIDWORKS Design session

## VBA Syntax

See [ModelDoc2::IsEditingSelf](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsEditingSelf.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IAssemblyDoc::EditPart2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.html)
[IAssemblyDoc::IGetEditTarget2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget2.html)
[IAssemblyDoc::GetEditTarget Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTarget.html)
[IAssemblyDoc::GetEditTargetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.html)
[IAssemblyDoc::EditAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
