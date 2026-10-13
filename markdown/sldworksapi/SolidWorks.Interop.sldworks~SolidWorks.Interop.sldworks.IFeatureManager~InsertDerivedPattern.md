---
title: "InsertDerivedPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDerivedPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDerivedPattern.html"
---

# InsertDerivedPattern Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertDerivedPattern2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDerivedPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDerivedPattern() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertDerivedPattern()
```

### C#

```csharp
Feature InsertDerivedPattern()
```

### C++/CLI

```cpp
Feature^ InsertDerivedPattern();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Derived pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertDerivedPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDerivedPattern.html).

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the components, which must be ordered:

- seed component = 1
- pattern feature = 2

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
