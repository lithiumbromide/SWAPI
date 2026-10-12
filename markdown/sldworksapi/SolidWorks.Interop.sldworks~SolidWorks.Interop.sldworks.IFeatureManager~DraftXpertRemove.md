---
title: "DraftXpertRemove Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "DraftXpertRemove"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertRemove.html"
---

# DraftXpertRemove Method (IFeatureManager)

Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it.

## Syntax

### Visual Basic (Declaration)

```vb
Function DraftXpertRemove() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.DraftXpertRemove()
```

### C#

```csharp
Feature DraftXpertRemove()
```

### C++/CLI

```cpp
Feature^ DraftXpertRemove();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::DraftXpertRemove](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~DraftXpertRemove.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::DraftXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertChange.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
