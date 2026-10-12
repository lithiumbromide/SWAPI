---
title: "CreateAngDim4 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateAngDim4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.html"
---

# CreateAngDim4 Method (IDrawingDoc)

Creates a non-associative angular dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAngDim4( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal P4 As System.Object, _
   ByVal P5 As System.Object, _
   ByVal P6 As System.Object, _
   ByVal TextPoint As System.Object, _
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
Dim P6 As System.Object
Dim TextPoint As System.Object
Dim TextHeight As System.Double
Dim value As System.Object

value = instance.CreateAngDim4(P0, P1, P2, P3, P4, P5, P6, TextPoint, TextHeight)
```

### C#

```csharp
System.object CreateAngDim4(
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object P4,
   System.object P5,
   System.object P6,
   System.object TextPoint,
   System.double TextHeight
)
```

### C++/CLI

```cpp
System.Object^ CreateAngDim4(
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ P4,
   System.Object^ P5,
   System.Object^ P6,
   System.Object^ TextPoint,
   System.double TextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`: Array of 3 doubles (x,y,z); dimension end point
- `P1`: Array of 3 doubles (x,y,z); dimension point
- `P2`: Array of 3 doubles (x,y,z); extension1 start point
- `P3`: Array of 3 doubles (x,y,z); extension1 end point
- `P4`: Array of 3 doubles (x,y,z); extension2 start point
- `P5`: Array of 3 doubles (x,y,z); extension2 end point
- `P6`: Array of 3 doubles (x,y,z); plane normal
- `TextPoint`: Array of 3 doubles (x,y,z); position of text
- `TextHeight`: Text height in meters

### Return Value

Newly created display dimension

## VBA Syntax

See [DrawingDoc::CreateAngDim4](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateAngDim4.html).

## Remarks

SOLIDWORKS creates this type of dimension between the two points that you specify. It has no relation to your geometry.

This method does not replace [IDrawingDoc::CreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html) or [IDrawingDoc::ICreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html); it changes the number of arguments required to construct the [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html)
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html)
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.html)
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
