---
title: "FeatureRevolve Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureRevolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.html"
---

# FeatureRevolve Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureRevolve( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSel As System.Boolean _
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
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSel As System.Boolean
Dim value As Feature

value = instance.FeatureRevolve(Angle, ReverseDir, Angle2, RevType, Options, Merge, UseFeatScope, UseAutoSel)
```

### C#

```csharp
Feature FeatureRevolve(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSel
)
```

### C++/CLI

```cpp
Feature^ FeatureRevolve(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSel
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of revolution in radians
- `ReverseDir`: True reverses the angle direction, false does not
- `Angle2`: Angle of revolution in radians
- `RevType`: Type of revolution as defined in [swRevolveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html)
- `Options`: Additional control as defined in [swRevolveOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveOptions_e.html)
- `Merge`: True to merge the results in a multibody part, false to not
- `UseFeatScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `UseAutoSel`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies or components the feature affects (see **Remarks**)

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::FeatureRevolve](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureRevolve.html).

## Remarks

To select an axis for a revolve feature, first call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Mark set to 4. When UseAutoSel is false, the user must select the bodies or components that the feature will affect.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.html)
[IFeatureManager::FeatureRevolveThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
