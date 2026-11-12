---
title: "CreateExtrudedBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateExtrudedBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html"
---

# CreateExtrudedBody Method (IModeler)

Creates a temporary extruded body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateExtrudedBody( _
   ByVal SheetBody As Body2, _
   ByVal Direction As MathVector, _
   ByVal Length As System.Double _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SheetBody As Body2
Dim Direction As MathVector
Dim Length As System.Double
Dim value As Body2

value = instance.CreateExtrudedBody(SheetBody, Direction, Length)
```

### C#

```csharp
Body2 CreateExtrudedBody(
   Body2 SheetBody,
   MathVector Direction,
   System.double Length
)
```

### C++/CLI

```cpp
Body2^ CreateExtrudedBody(
   Body2^ SheetBody,
   MathVector^ Direction,
   System.double Length
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SheetBody`: Sheet body that defines the profile for the temporary extruded body (see **Remarks**)
- `Direction`: Direction of the axis for the temporary extruded body
- `Length`: Length of the temporary extruded body

### Return Value

Temporary extruded [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateExtrudedBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateExtrudedBody.html).

## Examples

[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)
[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)
[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html), [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html), [IModeler::CreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateEllipse.html), [IModeler::ICreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateEllipse.html), [IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html), or [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html) to create curves that define the profile of the body that you want to extrude.
2. Call [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html) to trim the curves of arcs and lines only.
3. Call [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html) or [ISurface::ICreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html) to create the profile body, passing in either trimmed arcs and lines or untrimmed elliptical curves.
4. Set SheetBody to the profile body.

After calling this method, call [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html) to display the extrusion.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
