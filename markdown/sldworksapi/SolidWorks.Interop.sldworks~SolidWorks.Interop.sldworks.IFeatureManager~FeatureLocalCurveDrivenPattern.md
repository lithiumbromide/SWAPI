---
title: "FeatureLocalCurveDrivenPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureLocalCurveDrivenPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLocalCurveDrivenPattern.html"
---

# FeatureLocalCurveDrivenPattern Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ILocalCurvePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureLocalCurveDrivenPattern( _
   ByVal FlipDir1 As System.Boolean, _
   ByVal Num1 As System.Integer, _
   ByVal EqualSpacing1 As System.Boolean, _
   ByVal Spacing1 As System.Double, _
   ByVal ReferencePoint As System.Integer, _
   ByVal CurveMethod As System.Integer, _
   ByVal AlignMethod As System.Integer, _
   ByVal Direction2 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal Num2 As System.Integer, _
   ByVal EqualSpacing2 As System.Boolean, _
   ByVal Spacing2 As System.Double, _
   ByVal PatternSeedOnly As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FlipDir1 As System.Boolean
Dim Num1 As System.Integer
Dim EqualSpacing1 As System.Boolean
Dim Spacing1 As System.Double
Dim ReferencePoint As System.Integer
Dim CurveMethod As System.Integer
Dim AlignMethod As System.Integer
Dim Direction2 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim Num2 As System.Integer
Dim EqualSpacing2 As System.Boolean
Dim Spacing2 As System.Double
Dim PatternSeedOnly As System.Boolean
Dim value As Feature

value = instance.FeatureLocalCurveDrivenPattern(FlipDir1, Num1, EqualSpacing1, Spacing1, ReferencePoint, CurveMethod, AlignMethod, Direction2, FlipDir2, Num2, EqualSpacing2, Spacing2, PatternSeedOnly)
```

### C#

```csharp
Feature FeatureLocalCurveDrivenPattern(
   System.bool FlipDir1,
   System.int Num1,
   System.bool EqualSpacing1,
   System.double Spacing1,
   System.int ReferencePoint,
   System.int CurveMethod,
   System.int AlignMethod,
   System.bool Direction2,
   System.bool FlipDir2,
   System.int Num2,
   System.bool EqualSpacing2,
   System.double Spacing2,
   System.bool PatternSeedOnly
)
```

### C++/CLI

```cpp
Feature^ FeatureLocalCurveDrivenPattern(
   System.bool FlipDir1,
   System.int Num1,
   System.bool EqualSpacing1,
   System.double Spacing1,
   System.int ReferencePoint,
   System.int CurveMethod,
   System.int AlignMethod,
   System.bool Direction2,
   System.bool FlipDir2,
   System.int Num2,
   System.bool EqualSpacing2,
   System.double Spacing2,
   System.bool PatternSeedOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FlipDir1`: True flips the direction of the first direction, false does not
- `Num1`: Number of instances in the first direction, including the original instance
- `EqualSpacing1`: True uses equal spacing between instances in the first direction, false does not
- `Spacing1`: Distance between pattern instances along the curve in the first direction when EqualSpacing1 is set to false
- `ReferencePoint`: Type of selected reference point as defined in [swLocalCurvePatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternReferencePoint_e.html) (see **Remarks**)
- `CurveMethod`: Curve method as defined in [swLocalCurvePatternCurveMethod_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternCurveMethod_e.html)
- `AlignMethod`: Alignment method as defined in [swLocalCurvePatternAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternAlignment_e.html)
- `Direction2`: True creates the pattern in the second direction, false does not
- `FlipDir2`: True flips the direction of the second direction, false does not
- `Num2`: Number of instances in the second direction
- `EqualSpacing2`: True uses equal spacing between instances in the second direction, false does not
- `Spacing2`: Distance between pattern instances along the curve in the second direction when EqualSpacing2 is set to false
- `PatternSeedOnly`: True replicates only the seed pattern, which was created under Direction 1, under Direction 2; false replicates all instances of the curve pattern, which was created under Direction 1, under Direction 2

### Return Value

Local curve pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureLocalCurveDrivenPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureLocalCurveDrivenPattern.html).

## Remarks

| To select ... | Use a mark of... |
| --- | --- |
| Components to pattern | 1 |
| Curve, edge, sketch, or sketch entity for Direction 1 | 2 |
| Curve, edge, sketch, or sketch entity for Direction 2 | 4 |
| Reference point for ReferencePoint NOTE: If ReferencePoint is set to swLocalSketchPatternReferencePoint_e.swLocalSketchPatternSelectedPoint, then the selected reference point must be a vertex. | 32 |
| Face on which a 3D curve lies | 64 |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
