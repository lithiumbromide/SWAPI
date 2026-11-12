---
title: "IGetFirstView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetFirstView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html"
---

# IGetFirstView Method (IDrawingDoc)

Gets the first drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) on the current sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As View

value = instance.IGetFirstView()
```

### C#

```csharp
View IGetFirstView()
```

### C++/CLI

```cpp
View^ IGetFirstView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the first drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) in this drawing document

## VBA Syntax

See [DrawingDoc::IGetFirstView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IGetFirstView.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

## Remarks

This method might be useful for starting an iteration through all the drawing views on the current sheet.

Because the drawing sheet also has sketch geometry, notes, GTols, and so on, this method returns the current drawing sheet. The next view returned by [IView::GetNextView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetNextView.html) is the first drawing view in the current sheet.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
