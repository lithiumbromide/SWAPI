---
title: "ShowFeatureDetails Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowFeatureDetails"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.html"
---

# ShowFeatureDetails Property (IFeatureManager)

Gets or sets whether to show the feature details in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowFeatureDetails As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowFeatureDetails = value

value = instance.ShowFeatureDetails
```

### C#

```csharp
System.bool ShowFeatureDetails {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowFeatureDetails {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show the feature details in the FeatureManager design tree, false to hide them (see **Remarks**)

## VBA Syntax

See [FeatureManager::ShowFeatureDetails](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowFeatureDetails.html).

## Examples

[Get and Set FeatureManager Design Tree Display (C#)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_CSharp.htm)
[Get and Set FeatureManager Design Tree Display (VB.NET)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VBNET.htm)
[Get and Set FeatureManager Design Tree Display (VBA)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VB.htm)

## Remarks

Setting IFeatureManager::ShowFeatureDetails to true sets [IFeatureManager::ShowHierarchyOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.html) to false, and vice versa.

This property affects the FeatureManager design tree view of the current configuration of an assembly. It does not affect other configurations.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ViewDependencies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewDependencies.html)
[IFeatureManager::ViewFeatures Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewFeatures.html)
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html)

## Availability

SOLIDWORKS 2010 SP5, Revision Number 18.5
