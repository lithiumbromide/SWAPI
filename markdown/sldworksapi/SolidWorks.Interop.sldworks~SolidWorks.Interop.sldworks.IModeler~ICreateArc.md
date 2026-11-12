---
title: "ICreateArc Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.html"
---

# ICreateArc Method (IModeler)

Creates an arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateArc( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByVal Radius As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Center As System.Double
Dim Axis As System.Double
Dim Radius As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As Curve

value = instance.ICreateArc(Center, Axis, Radius, StartPoint, EndPoint)
```

### C#

```csharp
Curve ICreateArc(
   ref System.double Center,
   ref System.double Axis,
   System.double Radius,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

### C++/CLI

```cpp
Curve^ ICreateArc(
   System.double% Center,
   System.double% Axis,
   System.double Radius,
   System.double% StartPoint,
   System.double% EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array containing 3 doubles for location of the center of the arc (x,y,z )
- `Axis`: Array containing 3 doubles (x,y,z)
- `Radius`: Arc radius
- `StartPoint`: Array of 3 doubles (x,y,z)
- `EndPoint`: Array of 3 doubles (x,y,z)

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::ICreateArc](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateArc.html).

## Remarks

If your application uses [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html) or [ISurface::ICreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html), then your application must also use [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html) for the curves created by [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) or IModeler::ICreateArc and [IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html) or [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IBody2::AddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.html)
[IBody2::IAddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.html)
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.html)
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.html)
