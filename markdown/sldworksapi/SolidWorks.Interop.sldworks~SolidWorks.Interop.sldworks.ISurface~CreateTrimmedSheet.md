---
title: "CreateTrimmedSheet Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "CreateTrimmedSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.html"
---

# CreateTrimmedSheet Method (ISurface)

Obsolete. Superseded by [ISurface::CreateTrimmedSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~CreateTrimmedSheet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrimmedSheet( _
   ByVal Curves As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim Curves As System.Object
Dim value As System.Object

value = instance.CreateTrimmedSheet(Curves)
```

### C#

```csharp
System.object CreateTrimmedSheet(
   System.object Curves
)
```

### C++/CLI

```cpp
System.Object^ CreateTrimmedSheet(
   System.Object^ Curves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) that represent the boundary of the sheet

### Return Value

Temporary sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Surface::CreateTrimmedSheet](ms-its:sldworksapivb6.chm::/sldworks~Surface~CreateTrimmedSheet.html).

## Examples

[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

## Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. An empty entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from a periodic surface without trimming curves, then the curve array must contain one entry: null or Nothing.

If your application uses ISurface::CreateTrimmedSheet, then your application must also use [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html) for the curves created by [IModeler::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateArc.html) or [IModeler::ICreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateArc.html) and [IModeler::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateLine.html) or [IModeler::ICreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateLine.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
