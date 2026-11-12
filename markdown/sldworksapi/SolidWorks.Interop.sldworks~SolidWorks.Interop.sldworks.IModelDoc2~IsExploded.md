---
title: "IsExploded Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsExploded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsExploded.html"
---

# IsExploded Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::IsExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsExploded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.IsExploded()
```

### C#

```csharp
System.bool IsExploded()
```

### C++/CLI

```cpp
System.bool IsExploded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model is currently exploded, false if the model is collapsed

## VBA Syntax

See [ModelDoc2::IsExploded](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsExploded.html).

## Remarks

To take advantage of the explode mechanism, see [IAssemblyDoc::ShowExploded2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ShowExploded2.html), [IAssemblyDoc::CreateExplodedView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CreateExplodedView.html), [IAssemblyDoc::GetExplodedViewNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames.html), [IAssemblyDoc::IGetExplodedViewNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetExplodedViewNames.html), [IAssemblyDoc::GetExplodedViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount.html), [IAssemblyDoc::AutoExplode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AutoExplode.html), [IAssemblyDoc::ViewExplodeAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html), [IAssemblyDoc::ViewCollapseAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html), [IView::ShowExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ShowExploded.html), and [IView::IsExploded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsExploded.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
