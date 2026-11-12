---
title: "InsertWeldmentCutList Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWeldmentCutList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList.html"
---

# InsertWeldmentCutList Method (IFeatureManager)

Inserts a cut-list-item folder feature containing pre-selected weldment bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentCutList() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertWeldmentCutList()
```

### C#

```csharp
Feature InsertWeldmentCutList()
```

### C++/CLI

```cpp
Feature^ InsertWeldmentCutList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertWeldmentCutList](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWeldmentCutList.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IFeatureManager::InsertWeldmentCutList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentCutList2.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
