---
title: "InsertMoldShutOffSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoldShutOffSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.html"
---

# InsertMoldShutOffSurface Method (IFeatureManager)

Inserts the mold shut-off surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoldShutOffSurface() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertMoldShutOffSurface()
```

### C#

```csharp
Feature InsertMoldShutOffSurface()
```

### C++/CLI

```cpp
Feature^ InsertMoldShutOffSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMoldShutOffSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoldShutOffSurface.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.html)
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.html)
[IFeatureManager::InsertMoldPartingSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
