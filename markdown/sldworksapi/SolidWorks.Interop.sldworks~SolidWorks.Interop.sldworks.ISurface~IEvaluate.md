---
title: "IEvaluate Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IEvaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluate.html"
---

# IEvaluate Method (ISurface)

Evaluates the surface, given the u and v parameters of the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEvaluate( _
   ByVal UParam As System.Double, _
   ByVal VParam As System.Double, _
   ByVal NumUDeriv As System.Integer, _
   ByVal NumVDeriv As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UParam As System.Double
Dim VParam As System.Double
Dim NumUDeriv As System.Integer
Dim NumVDeriv As System.Integer
Dim value As System.Double

value = instance.IEvaluate(UParam, VParam, NumUDeriv, NumVDeriv)
```

### C#

```csharp
System.double IEvaluate(
   System.double UParam,
   System.double VParam,
   System.int NumUDeriv,
   System.int NumVDeriv
)
```

### C++/CLI

```cpp
System.double IEvaluate(
   System.double UParam,
   System.double VParam,
   System.int NumUDeriv,
   System.int NumVDeriv
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UParam`: Value of u parameter
- `VParam`: Value of v parameter
- `NumUDeriv`: Number of u derivatives required
- `NumVDeriv`: Number of v derivatives required

## VBA Syntax

See [Surface::IEvaluate](ms-its:sldworksapivb6.chm::/sldworks~Surface~IEvaluate.html).

## Remarks

This method returns the evaluated point, normal, and derivatives with respect to u and v up to order NumUDerivs and NumVDerivs, respectively. If NumUDerivs and NumVDerivs are 0, then no derivatives are returned.

For more information on the valid u and v parameters of the surface, see [ISurface::Parameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization.html) or [ISurface::IParameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IParameterization.html). Also, use [IFace2::FaceInSurfaceSense](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~FaceInSurfaceSense.html) to check to see if the normal of the face is in the same direction or in the opposite direction of the surface normal.

The evaluation returns the following array of (3 *((( NumUDerivs +1) * (NumVDerivs + 1)) + 1 )) doubles:

[ evaluatedPoint[3], evaluatedDerivatives[xx], evaluatedNormal[3] ]

where:

evaluatedPoint[3] = point representing the evaluated X,Y,Z point in meters

evaluatedDerivatives[xx] = array of vectors representing the derivatives

where the nth derivative wrt u (i <= `NumUDerivs`)

and the nth derivative wrt v (j <= NumVDerivs)

would be vector number ( i + (NumUDerivs + 1) * j ) - 1 in the evaluatedDerivatives array.

If NumUDerivs and `NumVDerivs` are 0, then no derivatives are returned.

evaluatedNormal[3] = a vector representing the evaluated normal

The following table describes the number of derivatives that can be requested based on the surface type. If you request more derivatives than allowed, then this method returns all data as zeros. To determine the surface type, see [ISurface::Identity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Identity.html).

|  | U Derivatives |
| --- | --- |

|  |  | 0 | 1 | 2 |
| --- | --- | --- | --- | --- |
|  | 0 | a | a | b |
| V Derivatives | 1 | a | a | c |
|  | 2 | b | c | d |

where:

- a - All surface types
- b - All surface types except blend surfaces
- c - All surface types except blend surfaces and offset surfaces
- d - All surface types except blend surfaces but offset surfaces will only return 0th, 1st, and 2nd derivatives (the uncalculated 3rd and 4th derivatives are returned as 0 vectors).

For example, if you specified 2 derivatives in both u and v, then an array containing 10 vectors is returned. The returned data is in model space coordinates.

[P(u,v) P(u,v)/du P(u,v)/dudu]

[P(u,v)/dv P(u,v)/dudv P(u,v)/dududv]

[P(u,v)/dvdv P(u,v)/dudvdv P(u,v)/dududvdv]

[N(u,v)]

where:

If you request 2 derivatives for u and 1 for v, then an array containing 7 vectors is returned:

[P(u,v) P(u,v)/du P(u,v)/dudu]

[P(u,v)/dv P(u,v)/dudv P(u,v)/dududv]

[N(u,v)]

If u = 1 and v = 2, then:

[P(u,v) P(u,v)/du]

[P(u,v)/dv P(u,v)/dudv]

[P(u,v)/dvdv P(u,v)/dudvdv]

[N(u,v)]

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Evaluate.html)
[ISurface::EvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~EvaluateAtPoint.html)
[ISurface::IEvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluateAtPoint.html)
[ISurface::IReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.html)
[ISurface::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate.html)
