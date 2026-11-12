---
title: "FeatureAdvancedTableDrivenPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureAdvancedTableDrivenPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.html"
---

# FeatureAdvancedTableDrivenPattern Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [IDimPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureAdvancedTableDrivenPattern() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.FeatureAdvancedTableDrivenPattern()
```

### C#

```csharp
Feature FeatureAdvancedTableDrivenPattern()
```

### C++/CLI

```cpp
Feature^ FeatureAdvancedTableDrivenPattern();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureAdvancedTableDrivenPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureAdvancedTableDrivenPattern.html).

## Remarks

This method inserts a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances.

Call this method after calling [IFeatureManager::InsertVaryInstanceOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.html) to create an advanced variable pattern feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
