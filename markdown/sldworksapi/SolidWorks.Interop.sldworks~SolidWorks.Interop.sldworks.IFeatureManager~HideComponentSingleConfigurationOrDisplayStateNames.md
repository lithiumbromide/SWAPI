---
title: "HideComponentSingleConfigurationOrDisplayStateNames Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "HideComponentSingleConfigurationOrDisplayStateNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HideComponentSingleConfigurationOrDisplayStateNames.html"
---

# HideComponentSingleConfigurationOrDisplayStateNames Property (IFeatureManager)

Gets or sets whether to hide a component's only configuration or display state.

## Syntax

### Visual Basic (Declaration)

```vb
Property HideComponentSingleConfigurationOrDisplayStateNames As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.HideComponentSingleConfigurationOrDisplayStateNames = value

value = instance.HideComponentSingleConfigurationOrDisplayStateNames
```

### C#

```csharp
System.bool HideComponentSingleConfigurationOrDisplayStateNames {get; set;}
```

### C++/CLI

```cpp
property System.bool HideComponentSingleConfigurationOrDisplayStateNames {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to hide the single configuration or display state, false to display it

## VBA Syntax

See [FeatureManager::HideComponentSingleConfigurationOrDisplayStateNames](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~HideComponentSingleConfigurationOrDisplayStateNames.html).

## Examples

See the [IFeatureManager::SetComponentIdentifiers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.html) example.

## Remarks

This property:

- Works in both SOLIDWORKS Design and [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).
- Is analogous to the **Do not show Configuration or Display State name if only one exists** check box on the Component Name and Description dialog that appears after right-clicking on the top-level component in the FeatureManager design tree and selecting **Tree Display > Component Name and Description**.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2022 SP01, Revision Number 30.1
