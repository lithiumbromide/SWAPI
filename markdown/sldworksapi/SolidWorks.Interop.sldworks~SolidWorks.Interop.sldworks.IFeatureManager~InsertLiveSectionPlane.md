---
title: "InsertLiveSectionPlane Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertLiveSectionPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertLiveSectionPlane.html"
---

# InsertLiveSectionPlane Method (IFeatureManager)

Inserts a Live Section Plane using the selected plane or planar face.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertLiveSectionPlane( _
   ByVal Type As System.Short _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Short
Dim value As Feature

value = instance.InsertLiveSectionPlane(Type)
```

### C#

```csharp
Feature InsertLiveSectionPlane(
   System.short Type
)
```

### C++/CLI

```cpp
Feature^ InsertLiveSectionPlane(
   System.short Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Not used. Specify any integer value.

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertLiveSectionPlane](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertLiveSectionPlane.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::MoveRotateLiveSectionPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveRotateLiveSectionPlane.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
