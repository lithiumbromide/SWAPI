---
title: "InsertFillSurface2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFillSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface2.html"
---

# InsertFillSurface2 Method (IFeatureManager)

Inserts a fill-surface feature in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFillSurface2( _
   ByVal Resolutions As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal VPatchBoundaries As System.Object, _
   ByVal VCurvatureControlType As System.Object, _
   ByVal VFaces As System.Object, _
   ByVal VConstraintCurves As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Resolutions As System.Integer
Dim Options As System.Integer
Dim VPatchBoundaries As System.Object
Dim VCurvatureControlType As System.Object
Dim VFaces As System.Object
Dim VConstraintCurves As System.Object
Dim value As Feature

value = instance.InsertFillSurface2(Resolutions, Options, VPatchBoundaries, VCurvatureControlType, VFaces, VConstraintCurves)
```

### C#

```csharp
Feature InsertFillSurface2(
   System.int Resolutions,
   System.int Options,
   System.object VPatchBoundaries,
   System.object VCurvatureControlType,
   System.object VFaces,
   System.object VConstraintCurves
)
```

### C++/CLI

```cpp
Feature^ InsertFillSurface2(
   System.int Resolutions,
   System.int Options,
   System.Object^ VPatchBoundaries,
   System.Object^ VCurvatureControlType,
   System.Object^ VFaces,
   System.Object^ VConstraintCurves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Resolutions`: Controls the resolution or quality of the surface (see **Remarks**)
- `Options`: Options as defined in [swFeatureFillSurfaceOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFillSurfaceOptions_e.html)
- `VPatchBoundaries`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) for the patch boundaries
- `VCurvatureControlType`: Array of curve control methods as defined in [swContactType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swContactType_e.html)
- `VFaces`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to use for direction
- `VConstraintCurves`: Array of constraint curves ([edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html))

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertFillSurface2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFillSurface2.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

You must use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and the following Mark values to select edges that bound the surface to be filled:

- Boundary curves = 1
- Boundary with contact curvature control = 257
- Boundary with tangent curvature control = 513
- Constraint curves or internal curves = 4

The resolution argument can be set to 1, 2, or 3. The higher the value, the better the resolution.

Use the [IBody2::Diagnose](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Diagnose.html) and the [IDiagnoseResult](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult.html) APIs to get the gaps to fill.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
