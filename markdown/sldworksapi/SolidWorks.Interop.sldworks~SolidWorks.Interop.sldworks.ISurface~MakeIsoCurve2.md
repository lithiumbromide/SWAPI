---
title: "MakeIsoCurve2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "MakeIsoCurve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve2.html"
---

# MakeIsoCurve2 Method (ISurface)

Creates an untrimmed curve on a surface using the specified u or v surface function parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeIsoCurve2( _
   ByVal UorV As System.Boolean, _
   ByRef UvValue As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As Curve

value = instance.MakeIsoCurve2(UorV, UvValue)
```

### C#

```csharp
Curve MakeIsoCurve2(
   System.bool UorV,
   out System.double UvValue
)
```

### C++/CLI

```cpp
Curve^ MakeIsoCurve2(
   System.bool UorV,
   [Out] System.double UvValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UorV`: True to specify the surface function's v parameter in UvValue, false to specify its u parameter
- `UvValue`:

  | If UorV is... | Then UvValue is the surface function's... |
  | --- | --- |
  | True | V parameter |
  | False | U parameter |

### Return Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Surface::MakeIsoCurve2](ms-its:sldworksapivb6.chm::/sldworks~Surface~MakeIsoCurve2.html).

## Examples

[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

## Remarks

This method supersedes the now obsolete ISurface::MakeIsoCurve by normalizing UvValue when it exceeds a specific value.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::MakeIsoCurves Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html)
[ISurface::IMakeIsoCurves Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::IGetMakeIsoCurvesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.html)
[ISurface::IMakeIsoCurve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ICurve::CreateTrimmedCurve2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision Number 21.5
