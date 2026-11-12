---
title: "GetEditTarget Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetEditTarget"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTarget.html"
---

# GetEditTarget Method (IAssemblyDoc)

Gets the model document that is currently being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditTarget() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetEditTarget()
```

### C#

```csharp
System.object GetEditTarget()
```

### C++/CLI

```cpp
System.Object^ GetEditTarget();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the model document being edited

## VBA Syntax

See [AssemblyDoc::GetEditTarget](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetEditTarget.html).

## Examples

[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

## Remarks

This method is useful when the user is performing an in-context edit of a part component because the currently active document returned from [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) might not be the document that the user is editing. For example, the user can use in-context editing to modify an assembly component. The active document is the assembly, but this method returns the IModelDoc2 for the component being edited.

The IModelDoc2 object returned by this method might be that of the assembly if no part is being in-place edited. In other words, this method returns a valid pointer (non-NULL) even when user is not editing a part in-context.

You can use the IModelDoc2 object returned by this method to determine which assembly component is being edited in-context. In general, you should not use this IModelDoc2 object for feature creation within the component part. Feature creation typically requires the IModelDoc2 of the active document. During feature creation, SOLIDWORKS automatically determines whether the feature should be created and owned by the active assembly, or if it is an in-context edit in which the feature should be created and owned by the component part.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetEditTargetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.html)
[IGetEditTarget2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget2.html)
[IsInEditTarget2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.html)
[ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[IsEditingSelf Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsEditingSelf.html)
