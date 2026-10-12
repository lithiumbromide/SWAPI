---
title: "InsertSweepSurface3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSweepSurface3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSweepSurface3.html"
---

# InsertSweepSurface3 Method (IFeatureManager)

Obsolete. See **Remarks**.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSweepSurface3( _
   ByVal Propagate As System.Boolean, _
   ByVal TwistCtrlOption As System.Integer, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal PathAlign As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean, _
   ByVal CircularProfile As System.Boolean, _
   ByVal CircularProfileDiameter As System.Double, _
   ByVal Direction As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Propagate As System.Boolean
Dim TwistCtrlOption As System.Integer
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim PathAlign As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim CircularProfile As System.Boolean
Dim CircularProfileDiameter As System.Double
Dim Direction As System.Integer
Dim value As Feature

value = instance.InsertSweepSurface3(Propagate, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, PathAlign, UseFeatScope, UseAutoSelect, TwistAngle, BMergeSmoothFaces, CircularProfile, CircularProfileDiameter, Direction)
```

### C#

```csharp
Feature InsertSweepSurface3(
   System.bool Propagate,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.int PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
)
```

### C++/CLI

```cpp
Feature^ InsertSweepSurface3(
   System.bool Propagate,
   System.int TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.int PathAlign,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces,
   System.bool CircularProfile,
   System.double CircularProfileDiameter,
   System.int Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`: True propagates the sweep to the next edge, false causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge
- `TwistCtrlOption`: Twist control option as defined in [swTwistControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)
- `KeepTangency`: If the sweep section has tangent segments, then true to cause the corresponding surfaces in the resulting sweep to be tangent, false to not
- `BAdvancedSmoothing`: If the sweep section has circular or elliptical arcs, then true to approximate the sections and smooth the surfaces, false to not
- `StartMatchingType`: Tangency type as defined in [swTangencyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)
- `EndMatchingType`: Tangency type as defined in swTangencyType_e
- `PathAlign`: Align path type (see **Remarks**)
- `UseFeatScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `UseAutoSelect`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)
- `TwistAngle`: If TwistCtrlOption set to swTwistControlType_e.swTwistControlConstantTwistAlongPath, then specify end twist angle
- `BMergeSmoothFaces`: True to merge smooth faces, false to not
- `CircularProfile`: True to use a circular profile, false to use the selected sketch profile or solid body
- `CircularProfileDiameter`: If CircularProfile is true, then specify the diameter of the circular profile
- `Direction`: Direction as defined in [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html) (see **Remarks**)

### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSweepSurface3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSweepSurface3.html).

## Examples

[Create Surface-sweep Feature (C#)](Create_Surface-sweep_Feature_Example_CSharp.htm)
[Create Surface-sweep Feature (VB.NET)](Create_Surface-sweep_Feature_Example_VBNET.htm)
[Create Surface-sweep Feature (VBA)](Create_Surface-sweep_Feature_Example_VB.htm)

## Remarks

SOLIDWORKS 2018 introduces a new sweep architecture, making this method obsolete. See [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm) to create this sweep surface.

Because you are creating a surface, the sections can be open.

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the sketch profile and sweep curves. Specify these marks:

- 1 = Sketch profile
- 2 = Guide curve, if provided
- 4 = Sweep path

The PathAlign argument is available when TwistCtrlOption is set to swTwistControlType_e.swTwistControlFollowPath and can take one of these values:

- 0 = None; no correction (default)
- 2 = Direction vector; a plane, planar face, or line defines the path
- 3 = All faces; includes neighboring faces

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

Direction only applies to sketch profiles and only when the sketch profile is not coincident with an end of the path.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertCutSwept5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept5.html)
[IFeatureManager::InsertProtrusionSwept4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept4.html)
[IModeler::CreateSweptSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.html)
[IModeler::ICreateSweptSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.html)
[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
