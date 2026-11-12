---
title: "IGetExplodedViewNames Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetExplodedViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames.html"
---

# IGetExplodedViewNames Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::GetExplodedViewNames2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExplodedViewNames( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetExplodedViewNames(Count)
```

### C#

```csharp
System.string IGetExplodedViewNames(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetExplodedViewNames(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of exploded views in the active configuration (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the exploded views in the active configuration
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IAssemblyDoc::GetExplodedViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.html) to get the value of Count.

To take advantage of the explode mechanism, see [IAssemblyDoc::CreateExplodedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html), [IAssemblyDoc::GetExplodedViewNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames.html), [IAssemblyDoc::GetExplodedViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.html), [IAssemblyDoc::AutoExplode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AutoExplode.html), [IAssemblyDoc::ShowExploded2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ShowExploded2.html), [IAssemblyDoc::ViewExplodeAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html), [IAssemblyDoc::ViewCollapseAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html), [IView::ShowExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ShowExploded.html), [IView::IsExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsExploded.html), and [IModelDoc2::IsExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsExploded.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
