---
title: "CreateTrimmedSheet4 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "CreateTrimmedSheet4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.html"
---

# CreateTrimmedSheet4 Method (ISurface)

Obsolete. Superseded by [ISurface::CreateTrimmedSheet5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrimmedSheet4( _
   ByVal Curves As System.Object, _
   ByVal PreserveAnalyticCurves As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim Curves As System.Object
Dim PreserveAnalyticCurves As System.Boolean
Dim value As System.Object

value = instance.CreateTrimmedSheet4(Curves, PreserveAnalyticCurves)
```

### C#

```csharp
System.object CreateTrimmedSheet4(
   System.object Curves,
   System.bool PreserveAnalyticCurves
)
```

### C++/CLI

```cpp
System.Object^ CreateTrimmedSheet4(
   System.Object^ Curves,
   System.bool PreserveAnalyticCurves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) that represent the boundary of the sheet
- `PreserveAnalyticCurves`: True to preserve analytic curves, false to store all trimming curves as SP-curves

### Return Value

Temporary sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Surface::CreateTrimmedSheet4](ms-its:sldworksapivb6.chm::/Sldworks~Surface~CreateTrimmedSheet4.html).

## Examples

[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

## Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A null entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from a periodic surface without trimming curves, then the curve array must contain one entry: null or Nothing.

Before calling this method, trim the curves created by [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) and [IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html) by calling [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html). Elliptical curves created by [IModeler::CreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateEllipse.html) do not need to be trimmed before calling this method.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::ICreateTrimmedSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
