---
title: "EnableFeatureTreeWindow Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EnableFeatureTreeWindow"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTreeWindow.html"
---

# EnableFeatureTreeWindow Property (IFeatureManager)

Gets or sets whether the FeatureManager design tree is enabled or not.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeatureTreeWindow As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.EnableFeatureTreeWindow = value

value = instance.EnableFeatureTreeWindow
```

### C#

```csharp
System.bool EnableFeatureTreeWindow {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableFeatureTreeWindow {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FeatureManager::EnableFeatureTreeWindow](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EnableFeatureTreeWindow.html).

## Remarks

Use this property with [IFeatureManager::EnableFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EnableFeatureTree.html), which temporarily enables or disables the FeatureManager design tree update when an add-in is running a series of operations.

While the FeatureManager design tree is disabled and not being updated, the FeatureManager tree may become out of date with what is actually in the model. If an interactive user attempts to interact with the FeatureManager design tree while it is in this out-of-date state, problems could occur. Normally, this should not happen because the add-in should only be disabling the FeatureManager design tree update temporarily and then enabling it immediately after the series of operations complete. However, if there is any possibility that an interactive user could interact with the FeatureManager design tree, then use FeatureManager::EnableFeatureTreeWindow, which prohibits any user interaction with the FeatureManager design tree because the control is disabled.

Just as with the IFeatureManager::EnableFeatureTree property, this property is meant to be used for temporary disabling. If it is necessary to disable the FeatureManager design tree control, then it should only be disabled while the add-in is performing some series of operations and enabled immediately after these operations complete. Do not to leave the FeatureManager design tree window disabled when control is returned to SOLIDWORKS, i.e., the interactive user.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::UpdateFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
