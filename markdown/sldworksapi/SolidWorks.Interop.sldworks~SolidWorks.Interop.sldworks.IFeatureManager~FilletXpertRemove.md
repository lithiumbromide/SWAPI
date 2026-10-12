---
title: "FilletXpertRemove Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FilletXpertRemove"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html"
---

# FilletXpertRemove Method (IFeatureManager)

Deletes the fillets on the selected faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function FilletXpertRemove() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.FilletXpertRemove()
```

### C#

```csharp
Feature FilletXpertRemove()
```

### C++/CLI

```cpp
Feature^ FilletXpertRemove();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::FilletXpertRemove](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FilletXpertRemove.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.html)
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
