---
title: "FeatureFolderLocation Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureFolderLocation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFolderLocation.html"
---

# FeatureFolderLocation Method (IFeatureManager)

Gets the folder feature for the specified feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureFolderLocation( _
   ByVal Feature As Feature _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Feature As Feature
Dim value As Feature

value = instance.FeatureFolderLocation(Feature)
```

### C#

```csharp
Feature FeatureFolderLocation(
   Feature Feature
)
```

### C++/CLI

```cpp
Feature^ FeatureFolderLocation(
   Feature^ Feature
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Feature`: [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

whose folder to get

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

folder

## VBA Syntax

See

[FeatureManager::FeatureFolderLocation](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureFolderLocation.html)

.

## Examples

[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)

[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IFeatureManager::CutListFolderLocation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CutListFolderLocation.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
