---
title: "IActiveDrawingView Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IActiveDrawingView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html"
---

# IActiveDrawingView Property (IDrawingDoc)

Gets the currently active drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IActiveDrawingView As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As View

value = instance.IActiveDrawingView
```

### C#

```csharp
View IActiveDrawingView {get;}
```

### C++/CLI

```cpp
property View^ IActiveDrawingView {
   View^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to interface object of the currently active drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::IActiveDrawingView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IActiveDrawingView.html).

## Remarks

This property returns the active drawing view, if one is active. If the drawing sheet is active, the property returns NULL and you can use [IDrawingDoc::IGetCurrentSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html) to get the current sheet for this drawing.

This is a read-only property. Use [IDrawingDoc::ActivateView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActivateView.html) to set the active drawing view.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.html)
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.html)
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
