---
title: "ICreateAngDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateAngDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html"
---

# ICreateAngDim4 Method (IDrawingDoc)

Creates a non-associative angular dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateAngDim4( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByRef P5 As System.Double, _
   ByRef P6 As System.Double, _
   ByRef TextPoint As System.Double, _
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
Dim P6 As System.Double
Dim TextPoint As System.Double
Dim TextHeight As System.Double
Dim value As DisplayDimension

value = instance.ICreateAngDim4(P0, P1, P2, P3, P4, P5, P6, TextPoint, TextHeight)
```

### C#

```csharp
DisplayDimension ICreateAngDim4(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   ref System.double P5,
   ref System.double P6,
   ref System.double TextPoint,
   System.double TextHeight
)
```

### C++/CLI

```cpp
DisplayDimension^ ICreateAngDim4(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double% P5,
   System.double% P6,
   System.double% TextPoint,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Pointer to an array of 3 doubles (x,y,z); dimension end point
- `P1`: Pointer to an array of 3 doubles (x,y,z); dimension point
- `P2`: Pointer to an array of 3 doubles (x,y,z); extension1 start point
- `P3`: Pointer to an array of 3 doubles (x,y,z); extension1 end point
- `P4`: Pointer to an array of 3 doubles (x,y,z); extension2 start point
- `P5`: Pointer to an array of 3 doubles (x,y,z); extension2 end point
- `P6`: Pointer to an array of 3 doubles (x,y,z); plane normal
- `TextPoint`: Pointer to an array of 3 doubles (x,y,z); position of text
- `TextHeight`: Text height in meters

### Return Value

Pointer to [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object

## VBA Syntax

See [DrawingDoc::ICreateAngDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateAngDim4.html).

## Remarks

SOLIDWORKS creates this type of dimension between the two points that you specify. It has no relation to your geometry.

This method does not replace [IDrawingDoc::ICreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html); it changes the number of arguments required to construct the [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html)
[IDrawingDoc::CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html)
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
