---
title: "CreateOrdinateDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateOrdinateDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html"
---

# CreateOrdinateDim4 Method (IDrawingDoc)

Creates a non-associative ordinate dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateOrdinateDim4( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal P4 As System.Object, _
   ByVal P5 As System.Object, _
   ByVal Val As System.Double, _
   ByVal Angle As System.Double, _
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
Dim P4 As System.Object
Dim P5 As System.Object
Dim Val As System.Double
Dim Angle As System.Double
Dim TextHeight As System.Double
Dim value As System.Object

value = instance.CreateOrdinateDim4(P0, P1, P2, P3, P4, P5, Val, Angle, TextHeight)
```

### C#

```csharp
System.object CreateOrdinateDim4(
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object P4,
   System.object P5,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

### C++/CLI

```cpp
System.Object^ CreateOrdinateDim4(
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ P4,
   System.Object^ P5,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Array of 3 doubles (x,y,z); dimension point
- `P1`: Array of 3 doubles (x,y,z); unit vector that specifies the direction of the ordinate dimension
- `P2`: Array of 3 doubles (x,y,z); extension line start point
- `P3`: Array of 3 doubles (x,y,z); extension line end point
- `P4`: Array of 3 doubles (x,y,z); unit vector and specifies the orientation of the text; for example, (1, 0, 0) results in horizontal text read from left to right
- `P5`: Array of 3 doubles (x,y,z); position of text
- `Val`: Value for the ordinate dimension
- `Angle`: Inclination angle of the text in radians (character slant)
- `TextHeight`: Text height in meters

### Return Value

[Display dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [DrawingDoc::CreateOrdinateDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateOrdinateDim4.html).

## Remarks

SOLIDWORKS creates this type of dimension between the two specified points. The dimension is not related to the geometry.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc::CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html)
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)
[IDrawingDoc::AddOrdinateDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddOrdinateDimension2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
