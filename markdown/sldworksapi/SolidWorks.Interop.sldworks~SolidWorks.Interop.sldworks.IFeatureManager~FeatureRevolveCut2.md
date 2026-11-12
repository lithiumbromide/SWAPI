---
title: "FeatureRevolveCut2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureRevolveCut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.html"
---

# FeatureRevolveCut2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureRevolveCut2( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean, _
   ByVal PropagateFeatureToParts As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Options As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim PropagateFeatureToParts As System.Boolean
Dim value As Feature

value = instance.FeatureRevolveCut2(Angle, ReverseDir, Angle2, RevType, Options, UseFeatScope, UseAutoSelect, AssemblyFeatureScope, AutoSelectComponents, PropagateFeatureToParts)
```

### C#

```csharp
Feature FeatureRevolveCut2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
)
```

### C++/CLI

```cpp
Feature^ FeatureRevolveCut2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of revolution in radians
- `ReverseDir`: True reverses the angle direction, false does not
- `Angle2`: Angle of revolution in radians
- `RevType`: Type of revolution as defined in [swRevolveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html) (can be either mid-plane or two-direction)
- `Options`: Additional control (see **Remarks**)
- `UseFeatScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `UseAutoSelect`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see Remarks)
- `AssemblyFeatureScope`: True if the assembly feature only affects selected components in the assembly, false if the assembly feature affects all components in the assembly
- `AutoSelectComponents`: True to auto-select all affected components, false to not (use the selected components)
- `PropagateFeatureToParts`: True to propagate the assembly feature to the components, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureRevolveCut2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureRevolveCut2.html).

## Remarks

The Options argument allows additional control of the feature creation.Supported value is swRevolveOptions_e.swAutoCloseSketch, which closes the sketch if it is open.When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

For extruded feature cuts, see [IFeatureManager::FeatureCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCut.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureRevolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.html)
[IFeatureManager::FeatureRevolveThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
