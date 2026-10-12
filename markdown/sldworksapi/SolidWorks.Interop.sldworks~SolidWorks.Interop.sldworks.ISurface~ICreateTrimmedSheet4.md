---
title: "ICreateTrimmedSheet4 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ICreateTrimmedSheet4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html"
---

# ICreateTrimmedSheet4 Method (ISurface)

Obsolete. Superseded by [ISurface::CreateTrimmedSheet5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTrimmedSheet4( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve, _
   ByVal PreserveAnalyticCurves As System.Boolean _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim NCurves As System.Integer
Dim Curves As Curve
Dim PreserveAnalyticCurves As System.Boolean
Dim value As Body

value = instance.ICreateTrimmedSheet4(NCurves, Curves, PreserveAnalyticCurves)
```

### C#

```csharp
Body ICreateTrimmedSheet4(
   System.int NCurves,
   ref Curve Curves,
   System.bool PreserveAnalyticCurves
)
```

### C++/CLI

```cpp
Body^ ICreateTrimmedSheet4(
   System.int NCurves,
   Curve^% Curves,
   System.bool PreserveAnalyticCurves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCurves`: Number of curves in the array of curves
- `Curves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) that represent the boundary of the sheet
- `PreserveAnalyticCurves`: True to preserve analytic curves, false to store all trimming curves as SP-curves

### Return Value

Newly created sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A NULL entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from an input periodical surface without trimming curves, then the curve array may be empty.

Before calling this method, trim the curves created by [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html) and [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html) by calling [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html). Elliptical curves created by [IModeler::ICreateEllipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateEllipse.html) do not need to be trimmed before calling this method.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::CreateTrimmedSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
