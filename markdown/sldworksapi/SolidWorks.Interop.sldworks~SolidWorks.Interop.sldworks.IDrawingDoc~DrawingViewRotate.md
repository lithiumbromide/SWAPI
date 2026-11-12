---
title: "DrawingViewRotate Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DrawingViewRotate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DrawingViewRotate.html"
---

# DrawingViewRotate Method (IDrawingDoc)

Rotates the selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DrawingViewRotate( _
   ByVal NewAngle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim NewAngle As System.Double
Dim value As System.Boolean

value = instance.DrawingViewRotate(NewAngle)
```

### C#

```csharp
System.bool DrawingViewRotate(
   System.double NewAngle
)
```

### C++/CLI

```cpp
System.bool DrawingViewRotate(
   System.double NewAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewAngle`: New angle value for the drawing view

### Return Value

True if successfully rotated, false if not

## VBA Syntax

See [DrawingDoc::DrawingViewRotate](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DrawingViewRotate.html).

## Examples

[Rotate Drawing View 45 Degrees (C#)](Rotate_Drawing_View_45_Degrees_Example_CSharp.htm)
[Rotate Drawing Veiw 45 Degrees (VB.NET)](Rotate_Drawing_View_45_Degrees_Example_VBNET.htm)
[Rotate Drawing View 45 Degrees (VBA)](Rotate_Drawing_View_45_Degrees_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AlignHorz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AlignHorz.html)
[IDrawingDoc::AlignVert Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AlignVert.html)
[IDrawingDoc::RestoreRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~RestoreRotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
