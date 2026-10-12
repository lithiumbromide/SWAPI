---
title: "GetViews Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViews.html"
---

# GetViews Method (IDrawingDoc)

Gets the all of the views, including the sheets, in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetViews()
```

### C#

```csharp
System.object GetViews()
```

### C++/CLI

```cpp
System.Object^ GetViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

An array of arrays (see **Remarks**)

## VBA Syntax

See [DrawingDoc::GetViews](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetViews.html).

## Examples

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

## Remarks

The return value is an array of arrays with a length equal to the number of sheets in the drawing document. Each of those arrays is a list of views with the first view in the list being the sheet itself.

If there are multiple sheets in the drawing document, then the order in which the sheets are returned is undetermined. So, the active sheet and its views might not be returned in the first array.

For example, when there are three sheets in the drawing document:

| One sheet contains 6 views, so first array has this number of elements | = 7 (sheet + 6 views) |
| --- | --- |
| Another sheet contains 2 views, so second array has this number of elements | = 3 (sheet + 2 views) |
| Another sheet contains no views, so third array has this number of elements | = 1 (sheet + 0 views) |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViewCount.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[ISheet::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetViews.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
