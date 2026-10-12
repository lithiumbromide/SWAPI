---
title: "IGetNext Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html"
---

# IGetNext Method (IModelView)

Gets the next model view after this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As ModelView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As ModelView

value = instance.IGetNext()
```

### C#

```csharp
ModelView IGetNext()
```

### C++/CLI

```cpp
ModelView^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) or NULLif no more model views exist

## VBA Syntax

See [ModelView::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~ModelView~IGetNext.html).

## Remarks

You can traverse through the model views in a document by using this method to get the initial view and each of the following views. When this method returns Nothing, you have reached the end of the list.

See [IModelDoc2::EnumModelViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EnumModelViews.html) for a method for traversing the model views on a document.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IEnumModelViews::Next Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
