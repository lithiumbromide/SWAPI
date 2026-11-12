---
title: "InsertFeatureLock Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFeatureLock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureLock.html"
---

# InsertFeatureLock Method (IFeatureManager)

Locks or freezes a selected feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFeatureLock() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertFeatureLock()
```

### C#

```csharp
Feature InsertFeatureLock()
```

### C++/CLI

```cpp
Feature^ InsertFeatureLock();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertFeatureLock](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFeatureLock.html).

## Examples

'VBA

' Preconditions:

' 1. Open a part.

' 2. Select a feature.

' Postconditions: Observe that the selected feature is locked, and a gold freeze bar appears after the feature in the FeatureManager design tree.

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat, swLockFeat As SldWorks.Feature
Dim swFeatMgr As SldWorks.FeatureManager

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swFeatMgr = swModel.FeatureManager
Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
Set swLockFeat = swFeatMgr.**InsertFeatureLock**

End Sub

## Remarks

After calling this method, a temporary freeze bar displays after the feature in the FeatureManager design tree. If you move the freeze bar to the top, the feature unlocks and the freeze bar disappears. To permanently enable the freeze bar, select **Tools > Options > System Options > General > Enable Freeze bar**.

This method is analogous to freezing a feature. For more information, see **SOLIDWORKS Design user-interface help > Parts and Features > Features > Feature Freeze > Freezing Features**.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeature::IsFrozen Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
