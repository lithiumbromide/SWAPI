---
title: "InsertSubWeldFolder Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSubWeldFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder.html"
---

# InsertSubWeldFolder Method (IFeatureManager)

Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSubWeldFolder() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertSubWeldFolder()
```

### C#

```csharp
Feature InsertSubWeldFolder()
```

### C++/CLI

```cpp
Feature^ InsertSubWeldFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSubWeldFolder](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSubWeldFolder.html).

## Remarks

The part must contain a weldment folder (Solid Bodies or Cut List) to create a sub-weldment folder. See [IFeatureManager::InsertWeldmentFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertWeldmentFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertSubWeldFolder2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
