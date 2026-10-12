---
title: "EnableFeatureTree Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EnableFeatureTree"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree.html"
---

# EnableFeatureTree Property (IFeatureManager)

Gets or sets whether or not to update the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeatureTree As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.EnableFeatureTree = value

value = instance.EnableFeatureTree
```

### C#

```csharp
System.bool EnableFeatureTree {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableFeatureTree {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to update FeatureManager design tree, false to not

## VBA Syntax

See [FeatureManager::EnableFeatureTree](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EnableFeatureTree.html).

## Examples

[Only Show Selected Components (VBA)](Only_Show_Selected_Components_Example_VB.htm)

## Remarks

Use this property to temporarily enable or disable the FeatureManager design tree while an add-in is running a series of operations. Temporarily disabling the FeatureManager design tree should increase performance. However, while the FeatureManager design tree is disabled and not being updated, it may become out of date with what is actually in the model.

If an interactive user attempts to interact with the FeatureManager design tree while it is in this out-of-date state, problems could occur. Normally, this should not happen because the add-in should only be disabling the FeatureManager design tree update temporarily and then enabling it immediately after the series of operations completes. However, if there is any possibility that the interactive user could interact with the FeatureManager design tree while it is an out-of-date state, then also use [IFeatureManager::EnableFeatureTreeWindow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EnableFeatureTreeWindow.html), which prohibits any user interaction with the FeatureManager design tree because the control itself is disabled.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::UpdateFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
