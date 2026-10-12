---
title: "FeatureFillPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureFillPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillPattern.html"
---

# FeatureFillPattern Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [IFillPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFillPattern( _
   ByVal PatternLayoutType As System.Integer, _
   ByVal LayoutSpacingType As System.Integer, _
   ByVal InstanceSpacing As System.Double, _
   ByVal StaggerAngle As System.Double, _
   ByVal Margins As System.Double, _
   ByVal LoopSpacing As System.Double, _
   ByVal NoOfInstances As System.Integer, _
   ByVal PatternLayoutPolygonSides As System.Integer, _
   ByVal FeaturesToPatternType As System.Integer, _
   ByVal CreateSeedCutType As System.Integer, _
   ByVal Diameter As System.Double, _
   ByVal Dimension As System.Double, _
   ByVal Rotation As System.Double, _
   ByVal Diagonal As System.Double, _
   ByVal CreateSeedCutPolygonSides As System.Integer, _
   ByVal OuterRadius As System.Double, _
   ByVal InnerRadius As System.Double, _
   ByVal FlipShapeDirection As System.Boolean, _
   ByVal GeometryPattern As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim PatternLayoutType As System.Integer
Dim LayoutSpacingType As System.Integer
Dim InstanceSpacing As System.Double
Dim StaggerAngle As System.Double
Dim Margins As System.Double
Dim LoopSpacing As System.Double
Dim NoOfInstances As System.Integer
Dim PatternLayoutPolygonSides As System.Integer
Dim FeaturesToPatternType As System.Integer
Dim CreateSeedCutType As System.Integer
Dim Diameter As System.Double
Dim Dimension As System.Double
Dim Rotation As System.Double
Dim Diagonal As System.Double
Dim CreateSeedCutPolygonSides As System.Integer
Dim OuterRadius As System.Double
Dim InnerRadius As System.Double
Dim FlipShapeDirection As System.Boolean
Dim GeometryPattern As System.Boolean
Dim value As Feature

value = instance.FeatureFillPattern(PatternLayoutType, LayoutSpacingType, InstanceSpacing, StaggerAngle, Margins, LoopSpacing, NoOfInstances, PatternLayoutPolygonSides, FeaturesToPatternType, CreateSeedCutType, Diameter, Dimension, Rotation, Diagonal, CreateSeedCutPolygonSides, OuterRadius, InnerRadius, FlipShapeDirection, GeometryPattern)
```

### C#

```csharp
Feature FeatureFillPattern(
   System.int PatternLayoutType,
   System.int LayoutSpacingType,
   System.double InstanceSpacing,
   System.double StaggerAngle,
   System.double Margins,
   System.double LoopSpacing,
   System.int NoOfInstances,
   System.int PatternLayoutPolygonSides,
   System.int FeaturesToPatternType,
   System.int CreateSeedCutType,
   System.double Diameter,
   System.double Dimension,
   System.double Rotation,
   System.double Diagonal,
   System.int CreateSeedCutPolygonSides,
   System.double OuterRadius,
   System.double InnerRadius,
   System.bool FlipShapeDirection,
   System.bool GeometryPattern
)
```

### C++/CLI

```cpp
Feature^ FeatureFillPattern(
   System.int PatternLayoutType,
   System.int LayoutSpacingType,
   System.double InstanceSpacing,
   System.double StaggerAngle,
   System.double Margins,
   System.double LoopSpacing,
   System.int NoOfInstances,
   System.int PatternLayoutPolygonSides,
   System.int FeaturesToPatternType,
   System.int CreateSeedCutType,
   System.double Diameter,
   System.double Dimension,
   System.double Rotation,
   System.double Diagonal,
   System.int CreateSeedCutPolygonSides,
   System.double OuterRadius,
   System.double InnerRadius,
   System.bool FlipShapeDirection,
   System.bool GeometryPattern
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PatternLayoutType`: Pattern layout type as defined in [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html)
- `LayoutSpacingType`: Pattern layout spacing as defined in [swPatternLayoutSpacingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutSpacingType_e.html)
- `InstanceSpacing`: Distance between pattern instance centers; valid always for PatternLayoutType = swPatternLayoutType_e.swPatternLayoutPerforation; valid for all other PatternLayoutTypes only if LayoutSpacingType = swPatternLayoutSpacingType_e.swPatternLayoutTargetSpacing
- `StaggerAngle`: Angle by which to stagger rows of pattern instances; valid only if PatternLayoutType = swPatternLayoutType_e.swPatternLayoutPerforation
- `Margins`: Distance between the fill boundary and the outermost instance in the pattern layout; 0 for no margin
- `LoopSpacing`: Distance between instance centers of adjacent pattern loops; valid for all PatternLayoutTypes except swPatternLayoutType_e.swPatternLayoutPerforation
- `NoOfInstances`: Number of pattern instances per loop or side of the pattern layout; valid only if both are true:

  - LayoutSpacingType = swPatternLayoutSpacingType_e.swPatternLayoutInstances
  - PatternLayoutType is set to one of the following:

    - swPatternLayoutType_e.swPatternLayoutCircular
    - swPatternLayoutType_e.swPatternLayoutPolygon
    - swPatternLayoutType_e.swPatternLayoutSquare
- `PatternLayoutPolygonSides`: Number of sides in the polygonal layout of the pattern; valid only if PatternLayoutType = swPatternLayoutType_e.swPatternLayoutPolygon
- `FeaturesToPatternType`: Type of objects to pattern as defined in [swFeaturesToPatternType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeaturesToPatternType_e.html)
- `CreateSeedCutType`: Pattern seed cut types as defined in [swCreateSeedCutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSeedCutType_e.html)
- `Diameter`: Diameter of the circle-cut seed instance; valid only if both are true:

  FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut

  CreateSeedCutType = swCreateSeedCutType_e.swCreateSeedCutCircle
- `Dimension`: Length of the side of a diamond-cut or square-cut seed instance; valid only if both are true:

  FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut

  CreateSeedCutType is set to one of the following:
- `Rotation`: Counterclockwise rotation of the seed instance; valid only if both are true:

  FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut

  CreateSeedCutType is set to one of the following:
- `Diagonal`: Length of the diagonal in the diamond-cut seed instance; valid only if both are true:

  FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut

  CreateSeedCutType = swCreateSeedCutType_e.swCreateSeedCutDiamond
- `CreateSeedCutPolygonSides`: Number of sides in the polygon-cut seed instance; valid only if both are true:

  - FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut
  - CreateSeedCutType = swCreateSeedCutType_e.swCreateSeedCutPolygon
- `OuterRadius`: Radius of circle that circumscribes the polygon-cut seed instance; valid only if both are ture:

  - FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut
  - CreateSeedCutType = swCreateSeedCutType_e.swCreateSeedCutPolygon
- `InnerRadius`: Radius of circle that inscribes the polygon-cut seed instance; valid only if both are true:

  - FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut
  - CreateSeedCutType = swCreateSeedCutType_e.swCreateSeedCutPolygon
- `FlipShapeDirection`: True to reverse the direction of the pattern seed cut; valid only if FeaturesToPatternType = swFeaturesToPatternType_e.swFeaturesToPatternCreateSeedCut
- `GeometryPattern`: True to create the pattern using an exact copy of the seed instance, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureFillPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureFillPattern.html).

## Remarks

**Insert > Pattern/Mirror > Fill Pattern** in the SOLIDWORKS menu opens the Fill Pattern PropertyManager. The parameters in this method correspond to the options in the Fill Pattern PropertyManager.

For all pattern layouts except [swPatternLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPatternLayoutType_e.html).swPatternLayoutPerforation, the fill pattern is created by positioning a pattern seed instance within the fill boundary and copying the pattern in concentric loops about the seed instance.

See the SOLIDWORKS Help for more information about fill pattern features.

To create a fill pattern:

1. Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) or another selection method to select the entities required to create a fill pattern feature.

| Select... | For the Fill Pattern's... | Using Mark... |
| --- | --- | --- |
| Sketch, face, planar curve on a face, or coplanar faces | Fill boundary | 1 |
| Direction reference (e.g., edge or axis) | Pattern direction (if not selected, SOLIDWORKS chooses a direction reference appropriate for the specified layout) | 2 |
| Vertex or sketch point | Location of the pattern seed instance (if a point is not selected, the pattern seed instance is placed at the center of the fill boundary region) | 3 |
| Features | Pattern objects | 4 |
| Faces | Pattern objects | 5 |
| Bodies | Pattern objects | 6 |

1. Call this method, specifying the following parameters:

- PatternLayoutType
- LayoutSpacingType
- FeaturesToPatternType
- GeometryPattern
- LoopSpacing (for all PatternLayoutTypes except swPatternLayoutType_e.swPatternLayoutPerforation)

Depending on the settings above, other parameters might need to be specified.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
