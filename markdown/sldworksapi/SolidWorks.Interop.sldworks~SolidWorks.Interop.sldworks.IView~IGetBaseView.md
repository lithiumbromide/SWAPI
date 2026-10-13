---
title: "IGetBaseView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetBaseView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.html"
---

# IGetBaseView Method (IView)

Gets the base (parent) view used to create this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBaseView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As View

value = instance.IGetBaseView()
```

### C#

```csharp
View IGetBaseView()
```

### C++/CLI

```cpp
View^ IGetBaseView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Base [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::IGetBaseView](ms-its:sldworksapivb6.chm::/sldworks~View~IGetBaseView.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
