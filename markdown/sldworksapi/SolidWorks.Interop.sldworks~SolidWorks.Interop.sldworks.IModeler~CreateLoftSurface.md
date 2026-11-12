---
title: "CreateLoftSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateLoftSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.html"
---

# CreateLoftSurface Method (IModeler)

Creates a loft surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLoftSurface( _
   ByVal CurveArray As System.Object, _
   ByVal BBlendClosed As System.Boolean, _
   ByVal BForceCubic As System.Boolean, _
   ByVal GuideCrvArray As System.Object, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal NormalAtStartSection As System.Object, _
   ByVal NormalAtEndSection As System.Object, _
   ByVal StartMatchingFaceList As System.Object, _
   ByVal EndMatchingFaceList As System.Object, _
   ByVal DegeneratedStart As System.Boolean, _
   ByVal DegeneratedEnd As System.Boolean, _
   ByVal StartPointOfStartSection As System.Object, _
   ByVal StartPointOfEndSection As System.Object, _
   ByVal SectionIndexStart As System.Integer, _
   ByVal SectionIndexEnd As System.Integer, _
   ByVal GuideIndexStart As System.Integer, _
   ByVal GuideIndexEnd As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CurveArray As System.Object
Dim BBlendClosed As System.Boolean
Dim BForceCubic As System.Boolean
Dim GuideCrvArray As System.Object
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim NormalAtStartSection As System.Object
Dim NormalAtEndSection As System.Object
Dim StartMatchingFaceList As System.Object
Dim EndMatchingFaceList As System.Object
Dim DegeneratedStart As System.Boolean
Dim DegeneratedEnd As System.Boolean
Dim StartPointOfStartSection As System.Object
Dim StartPointOfEndSection As System.Object
Dim SectionIndexStart As System.Integer
Dim SectionIndexEnd As System.Integer
Dim GuideIndexStart As System.Integer
Dim GuideIndexEnd As System.Integer
Dim value As System.Object

value = instance.CreateLoftSurface(CurveArray, BBlendClosed, BForceCubic, GuideCrvArray, StartMatchingType, EndMatchingType, NormalAtStartSection, NormalAtEndSection, StartMatchingFaceList, EndMatchingFaceList, DegeneratedStart, DegeneratedEnd, StartPointOfStartSection, StartPointOfEndSection, SectionIndexStart, SectionIndexEnd, GuideIndexStart, GuideIndexEnd)
```

### C#

```csharp
System.object CreateLoftSurface(
   System.object CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.object GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.object NormalAtStartSection,
   System.object NormalAtEndSection,
   System.object StartMatchingFaceList,
   System.object EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   System.object StartPointOfStartSection,
   System.object StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
)
```

### C++/CLI

```cpp
System.Object^ CreateLoftSurface(
   System.Object^ CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.Object^ GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.Object^ NormalAtStartSection,
   System.Object^ NormalAtEndSection,
   System.Object^ StartMatchingFaceList,
   System.Object^ EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   System.Object^ StartPointOfStartSection,
   System.Object^ StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveArray`: Array of b-spline [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `BBlendClosed`: True if blend closed, false if not
- `BForceCubic`: True if force surface is cubic, false if not
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
- `NormalAtStartSection`: [Normal at start section](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) when StartMatchingType is MATCH_NORMAL or MATCH_VECTOR; otherwise, can be Nothing
- `NormalAtEndSection`: [Normal at start section](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) when EndMatchingType is MATCH_NORMAL or MATCH_VECTOR; otherwise, can be Nothing
- `StartMatchingFaceList`: Array of matching [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) at start section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be Nothing
- `EndMatchingFaceList`: Array of matching [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) at end section when startMatchingType is MATCH_ALL_FACES, MATCH_FACE_G1, or MATCH_FACE_G2; otherwise, can be Nothing
- `DegeneratedStart`: True to degenerate at start, false to not
- `DegeneratedEnd`: True to degenerate at end, false to not
- `StartPointOfStartSection`: [Start point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of start section
- `StartPointOfEndSection`: [Start point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of end section
- `SectionIndexStart`: Index of start section; default is -1
- `SectionIndexEnd`: Index of end section; default is -1
- `GuideIndexStart`: Index of start guide curve; default is -1
- `GuideIndexEnd`: Index of end guide curve; default is -1

### Return Value

Newly created loft [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Modeler::CreateLoftSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateLoftSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.html)
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.html)
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html)
[IModeler:::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.html)
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.html)
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.html)
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.html)
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.html)
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.html)
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.html)
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.html)
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.html)
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.html)
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.html)
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.html)
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Numbers 14.0
