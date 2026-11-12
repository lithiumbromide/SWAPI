---
title: "InsertFlexFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFlexFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlexFeature.html"
---

# InsertFlexFeature Method (IFeatureManager)

Inserts a Flex feature using the selected solid or surface body.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFlexFeature( _
   ByVal RotX As System.Double, _
   ByVal RotY As System.Double, _
   ByVal RotZ As System.Double, _
   ByVal TanX As System.Double, _
   ByVal TanY As System.Double, _
   ByVal TanZ As System.Double, _
   ByVal RadX As System.Double, _
   ByVal RadY As System.Double, _
   ByVal RadZ As System.Double, _
   ByVal Angle As System.Double, _
   ByVal PivotX As System.Double, _
   ByVal PivotY As System.Double, _
   ByVal PivotZ As System.Double, _
   ByVal Type As System.Integer, _
   ByVal LeftTrim As System.Double, _
   ByVal RightTrim As System.Double, _
   ByVal HardEdges As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim RotX As System.Double
Dim RotY As System.Double
Dim RotZ As System.Double
Dim TanX As System.Double
Dim TanY As System.Double
Dim TanZ As System.Double
Dim RadX As System.Double
Dim RadY As System.Double
Dim RadZ As System.Double
Dim Angle As System.Double
Dim PivotX As System.Double
Dim PivotY As System.Double
Dim PivotZ As System.Double
Dim Type As System.Integer
Dim LeftTrim As System.Double
Dim RightTrim As System.Double
Dim HardEdges As System.Boolean
Dim value As Feature

value = instance.InsertFlexFeature(RotX, RotY, RotZ, TanX, TanY, TanZ, RadX, RadY, RadZ, Angle, PivotX, PivotY, PivotZ, Type, LeftTrim, RightTrim, HardEdges)
```

### C#

```csharp
Feature InsertFlexFeature(
   System.double RotX,
   System.double RotY,
   System.double RotZ,
   System.double TanX,
   System.double TanY,
   System.double TanZ,
   System.double RadX,
   System.double RadY,
   System.double RadZ,
   System.double Angle,
   System.double PivotX,
   System.double PivotY,
   System.double PivotZ,
   System.int Type,
   System.double LeftTrim,
   System.double RightTrim,
   System.bool HardEdges
)
```

### C++/CLI

```cpp
Feature^ InsertFlexFeature(
   System.double RotX,
   System.double RotY,
   System.double RotZ,
   System.double TanX,
   System.double TanY,
   System.double TanZ,
   System.double RadX,
   System.double RadY,
   System.double RadZ,
   System.double Angle,
   System.double PivotX,
   System.double PivotY,
   System.double PivotZ,
   System.int Type,
   System.double LeftTrim,
   System.double RightTrim,
   System.bool HardEdges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RotX`: x coordinate for the rotation axis
- `RotY`: y coordinate for the rotation axis
- `RotZ`: z coordinate for the rotation axis
- `TanX`: x coordinate for the tangent axis
- `TanY`: y coordinate for the tangent axis
- `TanZ`: z coordinate for the tangent axis
- `RadX`: x coordinate for the radius axis
- `RadY`: y coordinate for the radius axis
- `RadZ`: z coordinate for the radius axis
- `Angle`: Angle
- `PivotX`: x coordinate for the pivot triad reference
- `PivotY`: y coordinate for the pivot triad reference
- `PivotZ`: z coordinate for the pivot triad reference
- `Type`: - -1 =None

  0 = Bending

  1 = Twisting

  2 = Tapering

  3 = Stretching

  4 = Experimental
- `LeftTrim`: Left trimming distance
- `RightTrim`: Right trimming distance
- `HardEdges`: True to embed edges where the trim planes intersect the body, false to create smoother continuous faces

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertFlexFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFlexFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
