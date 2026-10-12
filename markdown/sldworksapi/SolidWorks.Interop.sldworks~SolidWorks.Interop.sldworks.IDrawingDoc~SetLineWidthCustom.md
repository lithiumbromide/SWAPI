---
title: "SetLineWidthCustom Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetLineWidthCustom"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidthCustom.html"
---

# SetLineWidthCustom Method (IDrawingDoc)

Sets the line thickness to the specified custom width for a selected edge or sketch entity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineWidthCustom( _
   ByVal Width As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Width As System.Double

instance.SetLineWidthCustom(Width)
```

### C#

```csharp
void SetLineWidthCustom(
   System.double Width
)
```

### C++/CLI

```cpp
void SetLineWidthCustom(
   System.double Width
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Custom width for the line in meters

## VBA Syntax

See [DrawingDoc::SetLineWidthCustom](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetLineWidthCustom.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.html)
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.html)
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
