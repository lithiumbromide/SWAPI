---
title: "ICreateLoftSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateLoftSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.html"
---

# ICreateLoftSurface Method (IModeler)

Creates a loft surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateLoftSurface( _
   ByVal NCurves As System.Integer, _
   ByRef CurveArray As Curve, _
   ByVal BBlendClosed As System.Boolean, _
   ByVal BForceCubic As System.Boolean, _
   ByVal NGuides As System.Integer, _
   ByRef GuideCrvArray As Curve, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal NormalAtStartSection As MathVector, _
   ByVal NormalAtEndSection As MathVector, _
   ByVal NStartMatchingFaces As System.Integer, _
   ByRef StartMatchingFaceList As Face2, _
   ByVal NEndMatchingFaces As System.Integer, _
   ByRef EndMatchingFaceList As Face2, _
   ByVal DegeneratedStart As System.Boolean, _
   ByVal DegeneratedEnd As System.Boolean, _
   ByVal StartPointOfStartSection As MathPoint, _
   ByVal StartPointOfEndSection As MathPoint, _
   ByVal SectionIndexStart As System.Integer, _
   ByVal SectionIndexEnd As System.Integer, _
   ByVal GuideIndexStart As System.Integer, _
   ByVal GuideIndexEnd As System.Integer _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NCurves As System.Integer
Dim CurveArray As Curve
Dim BBlendClosed As System.Boolean
Dim BForceCubic As System.Boolean
Dim NGuides As System.Integer
Dim GuideCrvArray As Curve
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim NormalAtStartSection As MathVector
Dim NormalAtEndSection As MathVector
Dim NStartMatchingFaces As System.Integer
Dim StartMatchingFaceList As Face2
Dim NEndMatchingFaces As System.Integer
Dim EndMatchingFaceList As Face2
Dim DegeneratedStart As System.Boolean
Dim DegeneratedEnd As System.Boolean
Dim StartPointOfStartSection As MathPoint
Dim StartPointOfEndSection As MathPoint
Dim SectionIndexStart As System.Integer
Dim SectionIndexEnd As System.Integer
Dim GuideIndexStart As System.Integer
Dim GuideIndexEnd As System.Integer
Dim value As Surface

value = instance.ICreateLoftSurface(NCurves, CurveArray, BBlendClosed, BForceCubic, NGuides, GuideCrvArray, StartMatchingType, EndMatchingType, NormalAtStartSection, NormalAtEndSection, NStartMatchingFaces, StartMatchingFaceList, NEndMatchingFaces, EndMatchingFaceList, DegeneratedStart, DegeneratedEnd, StartPointOfStartSection, StartPointOfEndSection, SectionIndexStart, SectionIndexEnd, GuideIndexStart, GuideIndexEnd)
```

### C#

```csharp
Surface ICreateLoftSurface(
   System.int NCurves,
   ref Curve CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.int NGuides,
   ref Curve GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   MathVector NormalAtStartSection,
   MathVector NormalAtEndSection,
   System.int NStartMatchingFaces,
   ref Face2 StartMatchingFaceList,
   System.int NEndMatchingFaces,
   ref Face2 EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   MathPoint StartPointOfStartSection,
   MathPoint StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
)
```

### C++/CLI

```cpp
Surface^ ICreateLoftSurface(
   System.int NCurves,
   Curve^% CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.int NGuides,
   Curve^% GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   MathVector^ NormalAtStartSection,
   MathVector^ NormalAtEndSection,
   System.int NStartMatchingFaces,
   Face2^% StartMatchingFaceList,
   System.int NEndMatchingFaces,
   Face2^% EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   MathPoint^ StartPointOfStartSection,
   MathPoint^ StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCurves`: Number of B-spline curves
- `CurveArray`: Array of b-spline [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `BBlendClosed`: True if blend closed, false if not
- `BForceCubic`: True if force surface is cubic, false if not
- `NGuides`: Number of guide curves
- `GuideCrvArray`: Array of guide [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `StartMatchingType`: Start matching type:

  - 0 = MATCH_NONE (default)
  - 1 = MATCH_NORMAL
  - 2 = MATCH_VECTOR
  - 3 = MATCH_ALL_FACES or MATCH_FACE_G1
  - 4 = MATCH_FACE_G2
- `EndMatchingType`: End matching type:

  - 0 = MATCH_NONE (default)
  - 1 = MATCH_NORMAL
  - 2 = MATCH_VECTOR
  - 3 = MATCH_ALL_FACES or MATCH_FACE_G1
  - 4 = MATCH_FACE_G2
- `NormalAtStartSection`: [Normal at start section](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) when StartMatchingType is MATCH_NORMAL or MATCH_VECTOR; otherwise, can be NULL
- `NormalAtEndSection`: Array of matching [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) at end section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be NULL
- `NStartMatchingFaces`: Number of matching faces at start section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be 0
- `StartMatchingFaceList`: Array of matching [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) at start section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be NULL
- `NEndMatchingFaces`: Number of matching faces at end section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be 0
- `EndMatchingFaceList`: Array of matching [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) at end section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be NULL
- `DegeneratedStart`: True to degenerate at start, false to not
- `DegeneratedEnd`: True to degenerate at end, false to not
- `StartPointOfStartSection`: [Start point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of start section
- `StartPointOfEndSection`: [Start point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of end section
- `SectionIndexStart`: Index of start section; default is -1
- `SectionIndexEnd`: Index of end section; default is -1
- `GuideIndexStart`: Index of start guide curve; default is -1
- `GuideIndexEnd`: Index of end guide curve; default is -1

## VBA Syntax

See [Modeler::ICreateLoftSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateLoftSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.html)
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html)
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.html)
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.html)
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.html)
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.html)
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.html)
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.html)
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.html)
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.html)
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.html)
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.html)
