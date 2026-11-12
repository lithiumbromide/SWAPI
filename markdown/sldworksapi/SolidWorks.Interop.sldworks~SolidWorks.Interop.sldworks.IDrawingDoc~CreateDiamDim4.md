---
title: "CreateDiamDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateDiamDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html"
---

# CreateDiamDim4 Method (IDrawingDoc)

Creates a non-associative diameter dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDiamDim4( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal TextPoint As System.Object, _
   ByVal Val As System.Double, _
   ByVal TextHeight As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim P0 As System.Object
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim TextPoint As System.Object
Dim Val As System.Double
Dim TextHeight As System.Double
Dim value As System.Object

value = instance.CreateDiamDim4(P0, P1, P2, P3, TextPoint, Val, TextHeight)
```

### C#

```csharp
System.object CreateDiamDim4(
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object TextPoint,
   System.double Val,
   System.double TextHeight
)
```

### C++/CLI

```cpp
System.Object^ CreateDiamDim4(
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ TextPoint,
   System.double Val,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Array of 3 doubles (x,y,z); location of dimension point
- `P1`: Array of 3 doubles (x,y,z); nearest point on circle
- `P2`: Array of 3 doubles (x,y,z); farthest point on circle diametrically opposite to P1
- `P3`: Array of 3 doubles (x,y,z); plane normal
- `TextPoint`: Array of 3 doubles (x,y,z); position of text
- `Val`: Dimension value in meters
- `TextHeight`: Text height in meters

### Return Value

Newly created display dimension

## VBA Syntax

See [DrawingDoc::CreateDiamDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateDiamDim4.html).

## Examples

[Create Non-associative Diameter Dimension (VBA)](Create_Non-associative_Diameter_Dimension_Example_VB.htm)

## Remarks

SOLIDWORKS creates this type of dimension between the two points you specify. It has no relation to your geometry.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)
[IDrawingDoc::IICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::IICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc::IICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
