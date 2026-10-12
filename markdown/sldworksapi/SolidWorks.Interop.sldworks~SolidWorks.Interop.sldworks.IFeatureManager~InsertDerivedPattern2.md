---
title: "InsertDerivedPattern2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDerivedPattern2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDerivedPattern2.html"
---

# InsertDerivedPattern2 Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDerivedPattern2() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertDerivedPattern2()
```

### C#

```csharp
Feature InsertDerivedPattern2()
```

### C++/CLI

```cpp
Feature^ InsertDerivedPattern2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Derived pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertDerivedPattern2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDerivedPattern2.html).

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the seed components and pattern feature in any order.

- seed component = 1
- pattern feature = 2

**NOTE**: A derived pattern feature is also called a pattern driven pattern feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
