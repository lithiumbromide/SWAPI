---
title: "DropDrawingViewFromPalette Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DropDrawingViewFromPalette"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette.html"
---

# DropDrawingViewFromPalette Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::DropDrawingViewFromPalette2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DropDrawingViewFromPalette( _
   ByVal Layout As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As View

value = instance.DropDrawingViewFromPalette(Layout, X, Y, Z)
```

### C#

```csharp
View DropDrawingViewFromPalette(
   System.int Layout,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
View^ DropDrawingViewFromPalette(
   System.int Layout,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layout`: ID of the drawing view to move to the drawing sheet
- `X`: x coordinate where to drop the drawing view
- `Y`: y coordinate where to drop the drawing view
- `Z`: z coordinate where to drop the drawing view; this coordinate is always 0

### Return Value

Pointer to the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [DrawingDoc::DropDrawingViewFromPalette](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DropDrawingViewFromPalette.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
