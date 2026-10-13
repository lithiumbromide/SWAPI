---
title: "SuppressView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SuppressView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.html"
---

# SuppressView Method (IDrawingDoc)

Hides the selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SuppressView()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.SuppressView()
```

### C#

```csharp
void SuppressView()
```

### C++/CLI

```cpp
void SuppressView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::SuppressView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SuppressView.html).

## Examples

[Automatically Insert Center Marks (C#)](Auto_Insert_Center_Marks_Example_CSharp.htm)
[Automatically Insert Center Marks (VB.NET)](Auto_Insert_Center_Marks_Example_VBNET.htm)
[Automatically Insert Center Marks (VBA)](Auto_Insert_Center_Marks_Example_VB.htm)

## Remarks

Dependent views are not suppressed.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::HideShowDrawingViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDrawingViews.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::AutomaticViewUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutomaticViewUpdate.html)
[IDrawingDoc::HiddenViewsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HiddenViewsVisible.html)
[IDrawingDoc::IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
