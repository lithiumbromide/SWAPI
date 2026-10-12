---
title: "InsertCenterMark3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCenterMark3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark3.html"
---

# InsertCenterMark3 Method (IDrawingDoc)

Inserts a center mark in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCenterMark3( _
   ByVal Style As System.Integer, _
   ByVal Propagate As System.Boolean, _
   ByVal Slot As System.Boolean _
) As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Style As System.Integer
Dim Propagate As System.Boolean
Dim Slot As System.Boolean
Dim value As CenterMark

value = instance.InsertCenterMark3(Style, Propagate, Slot)
```

### C#

```csharp
CenterMark InsertCenterMark3(
   System.int Style,
   System.bool Propagate,
   System.bool Slot
)
```

### C++/CLI

```cpp
CenterMark^ InsertCenterMark3(
   System.int Style,
   System.bool Propagate,
   System.bool Slot
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style as defined in [swCenterMarkStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkStyle_e.html)
- `Propagate`: True if the center mark should propagate throughout the pattern, false if not
- `Slot`: True if this is slot-style center mark, false if not

### Return Value

[Center mark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html)

## VBA Syntax

See [DrawingDoc::InsertCenterMark3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCenterMark3.html).

## Remarks

Call [IView::AutoInsertCenterMarks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~AutoInsertCenterMarks.html) to automatically insert center marks in multiple drawing views.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
