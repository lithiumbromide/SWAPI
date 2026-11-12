---
title: "GetStructureSystemFolders Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetStructureSystemFolders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetStructureSystemFolders.html"
---

# GetStructureSystemFolders Method (IFeatureManager)

Gets the structure system folders.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStructureSystemFolders() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.GetStructureSystemFolders()
```

### C#

```csharp
System.object GetStructureSystemFolders()
```

### C++/CLI

```cpp
System.Object^ GetStructureSystemFolders();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [FeatureManager::GetStructureSystemFolders](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetStructureSystemFolders.html).

## Remarks

The features returned are [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html)s. Use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) after calling this method to get the IStructureSystemFolders.

See the [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html) Remarks.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
