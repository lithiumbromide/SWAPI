---
title: "ICreateLine Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.html"
---

# ICreateLine Method (IModeler)

Creates a line.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateLine( _
   ByRef RootPoint As System.Double, _
   ByRef Direction As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim RootPoint As System.Double
Dim Direction As System.Double
Dim value As Curve

value = instance.ICreateLine(RootPoint, Direction)
```

### C#

```csharp
Curve ICreateLine(
   ref System.double RootPoint,
   ref System.double Direction
)
```

### C++/CLI

```cpp
Curve^ ICreateLine(
   System.double% RootPoint,
   System.double% Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Array containing 3 doubles (x, y, z) for the start point of the line
- `Direction`: Array containing 3 doubles (x, y, z) for the end point of the line

### Return Value

Newly created [line](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::ICreateLine](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateLine.html).

## Remarks

If your application uses [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html) or [ISurface::ICreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html), then your application must also use [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html) for the curves created by [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) or [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html) and [IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html) or IModeler::ICreateLine.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.html)
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.html)
