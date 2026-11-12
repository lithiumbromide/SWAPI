---
title: "InsertDeleteHoleForSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDeleteHoleForSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteHoleForSurface.html"
---

# InsertDeleteHoleForSurface Method (IFeatureManager)

Inserts a Delete Hole feature for one or more selected hole edges on a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDeleteHoleForSurface() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertDeleteHoleForSurface()
```

### C#

```csharp
Feature InsertDeleteHoleForSurface()
```

### C++/CLI

```cpp
Feature^ InsertDeleteHoleForSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertDeleteHoleForSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDeleteHoleForSurface.html).

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the hole edges to remove from the surface.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
