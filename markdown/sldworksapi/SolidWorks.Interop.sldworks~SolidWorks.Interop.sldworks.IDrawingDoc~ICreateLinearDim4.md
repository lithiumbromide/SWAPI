---
title: "ICreateLinearDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateLinearDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html"
---

# ICreateLinearDim4 Method (IDrawingDoc)

Creates a non-associative linear dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateLinearDim4( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByRef TextPoint As System.Double, _
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
Dim TextPoint As System.Double
Dim Val As System.Double
Dim Angle As System.Double
Dim TextHeight As System.Double
Dim value As DisplayDimension

value = instance.ICreateLinearDim4(P0, P1, P2, P3, P4, TextPoint, Val, Angle, TextHeight)
```

### C#

```csharp
DisplayDimension ICreateLinearDim4(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   ref System.double TextPoint,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

### C++/CLI

```cpp
DisplayDimension^ ICreateLinearDim4(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double% TextPoint,
   System.double Val,
   System.double Angle,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Pointer to an array of 3 doubles (x,y,z), dimension point
- `P1`: Pointer to an array of 3 doubles (x,y,z), dimension end
- `P2`: Pointer to an array of 3 doubles (x,y,z), normal to the plane of sketch
- `P3`: Pointer to an array of 3 doubles (x,y,z), extension line 1 reference point
- `P4`: Pointer to an array of 3 doubles (x,y,z), extension line 2 reference point
- `TextPoint`: Pointer to an array of 3 doubles (x,y,z), position of text
- `Val`: Value for the non-associative linear dimension
- `Angle`: Inclination angle of the text in radians
- `TextHeight`: Text height in meters

### Return Value

Pointer to [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object

## VBA Syntax

See [DrawingDoc::ICreateLinearDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateLinearDim4.html).

## Remarks

SOLIDWORKS creates this type of dimension between the two points you specify. It has no relation to your geometry.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html)
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html)
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
