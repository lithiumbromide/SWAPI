---
title: "InsertSubFolder Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSubFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubFolder.html"
---

# InsertSubFolder Method (IFeatureManager)

Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSubFolder() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertSubFolder()
```

### C#

```csharp
Feature InsertSubFolder()
```

### C++/CLI

```cpp
Feature^ InsertSubFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object, the new subfolder

## VBA Syntax

See [FeatureManager::InsertSubFolder](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSubFolder.html).

## Remarks

This method requires that the features (solid bodies or subfolders or both) be selected interactively or programmatically. To select the features programmatically, you can use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and pass the feature names and the appropriate object types and the selection coordinates 0,0,0. To determine the feature names and object types, use the [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) and [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html) methods, respectively.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
