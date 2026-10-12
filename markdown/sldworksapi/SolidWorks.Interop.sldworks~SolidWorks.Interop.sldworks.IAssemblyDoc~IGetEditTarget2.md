---
title: "IGetEditTarget2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetEditTarget2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget2.html"
---

# IGetEditTarget2 Method (IAssemblyDoc)

Gets the model document that is currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEditTarget2() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As ModelDoc2

value = instance.IGetEditTarget2()
```

### C#

```csharp
ModelDoc2 IGetEditTarget2()
```

### C++/CLI

```cpp
ModelDoc2^ IGetEditTarget2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) being edited

## VBA Syntax

See [AssemblyDoc::IGetEditTarget2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IGetEditTarget2.html).

## Remarks

This method is useful when the user is performing an in-context edit of a part component because the currently active document returned from [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) might not be the document that the user is editing. For example, the user can use in-context editing to modify an assembly component. The active document is the assembly, but this method returns the IModelDoc2 for the component being edited.

The IModelDoc2 object returned by this method might be that of the assembly if no part is being in-place edited. In other words, this method returns a valid pointer (non-NULL) even when user is not editing a part in-context.

You can use the IModelDoc2 object returned by this method to determine which assembly component is being edited in-context. In general, you should not use this IModelDoc2 object for feature creation within the component part. Feature creation typically requires the IModelDoc2 of the active document. During feature creation, SOLIDWORKS automatically determines whether the feature should be created and owned by the active assembly, or if it is an in-context edit in which the feature should be created and owned by the component part.

COM applications need to release the IModelDoc2 object returned because this method increments the reference count on the IModelDoc2 object even if the edit target is the active document.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IModelDoc2::IsEditingSelf Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsEditingSelf.html)
[IAssemblyDoc::GetEditTarget Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTarget.html)
[IAssemblyDoc::GetEditTargetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.html)
[ISelectionMgr::IsInEditTarget2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.html)
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.html)
