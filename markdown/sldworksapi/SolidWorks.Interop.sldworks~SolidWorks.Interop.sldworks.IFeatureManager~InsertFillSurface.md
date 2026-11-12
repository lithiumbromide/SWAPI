---
title: "InsertFillSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFillSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface.html"
---

# InsertFillSurface Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertFillSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFillSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFillSurface( _
   ByVal Resolution As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Resolution As System.Integer
Dim value As Feature

value = instance.InsertFillSurface(Resolution)
```

### C#

```csharp
Feature InsertFillSurface(
   System.int Resolution
)
```

### C++/CLI

```cpp
Feature^ InsertFillSurface(
   System.int Resolution
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Resolution`:

## VBA Syntax

See [FeatureManager::InsertFillSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFillSurface.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
