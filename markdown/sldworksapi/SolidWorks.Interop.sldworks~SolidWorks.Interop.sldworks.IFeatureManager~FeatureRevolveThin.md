---
title: "FeatureRevolveThin Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureRevolveThin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html"
---

# FeatureRevolveThin Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureRevolveThin( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThinDir As System.Integer, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ReverseThinDir As System.Integer
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature

value = instance.FeatureRevolveThin(Angle, ReverseDir, Angle2, RevType, Thickness1, Thickness2, ReverseThinDir, Merge, UseFeatScope, UseAutoSelect)
```

### C#

```csharp
Feature FeatureRevolveThin(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

### C++/CLI

```cpp
Feature^ FeatureRevolveThin(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of revolution in radians
- `ReverseDir`: True reverses the angle direction, false does not
- `Angle2`: Angle of revolution in radians
- `RevType`: Type of revolution as defined in [swRevolveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html) (see **Remarks**)
- `Thickness1`: Wall thickness (ReverseThinDir = 2 uses (Thickness1)/2 for each direction)
- `Thickness2`: Wall thickness; use only ReverseThinDir=2
- `ReverseThinDir`: Type and direction as defined in [swThinWallType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)
- `Merge`: True to merge the results in a multibody part, false to not
- `UseFeatScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `UseAutoSelect`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see **Remarks**)

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::FeatureRevolveThin](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureRevolveThin.html).

## Remarks

The ReverseDir argument has no effect if a mid-plane revolution is specified.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureRevolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.html)
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.html)
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
