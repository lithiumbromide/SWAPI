---
title: "GetExplodedViewNames Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetExplodedViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames.html"
---

# GetExplodedViewNames Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::GetExplodedViewNames2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodedViewNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetExplodedViewNames()
```

### C#

```csharp
System.object GetExplodedViewNames()
```

### C++/CLI

```cpp
System.Object^ GetExplodedViewNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the names of the exploded views in the active configuration

## VBA Syntax

See [AssemblyDoc::GetExplodedViewNames](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetExplodedViewNames.html).

## Examples

[Create Exploded Views of an Assembly (VBA)](Create_Exploded_Views_Example_VB.htm)
[Create Exploded Views of an Assembly (VB.NET)](Create_Exploded_Views_Example_VBNET.htm)
[Create Exploded Views of an Assembly (C#)](Create_Exploded_Views_Example_CSharp.htm)

## Remarks

To take advantage of the explode mechanism, see [IAssemblyDoc::CreateExplodedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html), [IAssemblyDoc::IGetExplodedViewNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames.html), [IAssemblyDoc::GetExplodedViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.html), [IAssemblyDoc::AutoExplode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AutoExplode.html), [IAssemblyDoc::ShowExploded2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ShowExploded2.html), [IAssemblyDoc::ViewExplodeAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html), [IAssemblyDoc::ViewCollapseAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html), [IView::ShowExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ShowExploded.html), [IView::IsExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsExploded.html), and [IModelDoc2::IsExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsExploded.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
