---
title: "IGetFirstModelView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetFirstModelView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html"
---

# IGetFirstModelView Method (IModelDoc2)

Gets the first view in a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstModelView() As ModelView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As ModelView

value = instance.IGetFirstModelView()
```

### C#

```csharp
ModelView IGetFirstModelView()
```

### C++/CLI

```cpp
ModelView^ IGetFirstModelView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) in the document

## VBA Syntax

See [ModelDoc2::IGetFirstModelView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetFirstModelView.html).

## Remarks

You can traverse through the model views in a document by using this method to get the initial view and [IModelView::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGetNext.html) to get each of the following views. You have reached the end of the list when IModelView::GetNext returns NULL, .

See [IModelDoc2::EnumModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EnumModelViews.html) for traversing the model views on a document.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewCount.html)
[IModelDoc2::GetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewNames.html)
[IModelDoc2::IGetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetModelViewNames.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::ModelViewManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager.html)
[IModelDoc2::EnumModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.html)
[IModelDocExtension::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViewCount.html)
[IModelDocExtension::GetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViews.html)
[IModelDocExtension::IGetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetModelViews.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
