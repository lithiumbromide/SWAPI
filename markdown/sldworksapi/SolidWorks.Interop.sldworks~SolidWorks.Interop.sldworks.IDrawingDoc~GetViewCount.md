---
title: "GetViewCount Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViewCount.html"
---

# GetViewCount Method (IDrawingDoc)

Gets all of the number of all of views, including the number of sheets, in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Integer

value = instance.GetViewCount()
```

### C#

```csharp
System.int GetViewCount()
```

### C++/CLI

```cpp
System.int GetViewCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of views, including the number of sheets, in this drawing document (see **Remarks**)

## VBA Syntax

See [DrawingDoc::GetViewCount](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetViewCount.html).

## Examples

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

## Remarks

For example, when:

| Number of sheets in drawing document | = 2 |
| --- | --- |
| Number of views on Sheet1 | = 6 |
| Number of views on Sheet2 | = 2 |
| Return value | = 10 |

The active sheet might not be the first sheet in the return value.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetViews.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[ISheet::GetViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetViews.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
