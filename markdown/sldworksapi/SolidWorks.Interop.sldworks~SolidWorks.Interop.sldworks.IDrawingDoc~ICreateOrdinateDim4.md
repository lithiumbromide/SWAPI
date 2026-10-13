---
title: "ICreateOrdinateDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateOrdinateDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html"
---

# ICreateOrdinateDim4 Method (IDrawingDoc)

Creates a non-associative ordinate dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateOrdinateDim4( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByRef P5 As System.Double, _
   ByVal Val As System.Double, _
   ByVal Angle As System.Double, _
   ByVal TextHeight As System.Double _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim P4 As System.Double
Dim P5 As System.Double
Dim Val As System.Double
Dim Angle As System.Double
Dim TextHeight As System.Double
Dim value As DisplayDimension

value = instance.ICreateOrdinateDim4(P0, P1, P2, P3, P4, P5, Val, Angle, TextHeight)
```

### C#

```csharp
DisplayDimension ICreateOrdinateDim4(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   ref System.double P5,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

### C++/CLI

```cpp
DisplayDimension^ ICreateOrdinateDim4(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double% P5,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Pointer to an array of 3 doubles (x,y,z); dimension point
- `P1`: Pointer to an array of 3 doubles (x,y,z); unit vector that specifies the direction of the ordinate dimension
- `P2`: Pointer to an array of 3 doubles (x,y,z); extension line start point
- `P3`: Pointer to an array of 3 doubles (x,y,z); extension line end point
- `P4`: Pointer to an array of 3 doubles (x,y,z); unit vector and specifies the orientation of the text; for example, (1, 0, 0) results in horizontal text read from left to right
- `P5`: Pointer to an array of 3 doubles (x,y,z); position of text
- `Val`: Value for the ordinate dimension
- `Angle`: Inclination angle of the text in radians (character slant)
- `TextHeight`: Text height in meters

### Return Value

[Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [DrawingDoc::ICreateOrdinateDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateOrdinateDim4.html).

## Remarks

SOLIDWORKS creates this type of dimension between the two points you specify. It has no relation to your geometry.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AddOrdinateDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddOrdinateDimension2.html)
[IDrawingDoc::CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc::CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html)
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
