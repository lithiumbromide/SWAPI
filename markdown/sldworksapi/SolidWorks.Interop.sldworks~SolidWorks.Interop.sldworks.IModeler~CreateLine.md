---
title: "CreateLine Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.html"
---

# CreateLine Method (IModeler)

Creates a line.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As System.Object

value = instance.CreateLine(RootPoint, Direction)
```

### C#

```csharp
System.object CreateLine(
   System.object RootPoint,
   System.object Direction
)
```

### C++/CLI

```cpp
System.Object^ CreateLine(
   System.Object^ RootPoint,
   System.Object^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Array containing 3 doubles (x, y, z) for the start point of the line
- `Direction`: Array containing 3 doubles (x, y, z) for the end point of the line

### Return Value

Newly created [line](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::CreateLine](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateLine.html).

## Examples

[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

## Remarks

If your application uses [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html) or [ISurface::ICreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html), then your application must also use [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html) for the curves created by [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) or [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html) and IModeler::CreateLine or [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.html)
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.html)
