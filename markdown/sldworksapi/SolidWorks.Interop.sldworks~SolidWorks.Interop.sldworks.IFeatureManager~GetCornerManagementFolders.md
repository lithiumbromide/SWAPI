---
title: "GetCornerManagementFolders Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetCornerManagementFolders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCornerManagementFolders.html"
---

# GetCornerManagementFolders Method (IFeatureManager)

Gets the structure system corner management folders.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCornerManagementFolders() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.GetCornerManagementFolders()
```

### C#

```csharp
System.object GetCornerManagementFolders()
```

### C++/CLI

```cpp
System.Object^ GetCornerManagementFolders();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [FeatureManager::GetCornerManagementFolders](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetCornerManagementFolders.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

The features returned are [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html)s. Use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) after calling this method to get the ICornerManagementFolders.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
