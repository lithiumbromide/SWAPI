---
title: "ShowHierarchyOnly Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowHierarchyOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.html"
---

# ShowHierarchyOnly Property (IFeatureManager)

Gets or sets whether to show only the hierarchy in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowHierarchyOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowHierarchyOnly = value

value = instance.ShowHierarchyOnly
```

### C#

```csharp
System.bool ShowHierarchyOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowHierarchyOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to only show the hierarchy in the FeatureManager design tree, false to not (see **Remarks**)

## VBA Syntax

See [FeatureManager::ShowHierarchyOnly](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowHierarchyOnly.html).

## Examples

[Get and Set FeatureManager Design Tree Display (C#)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_CSharp.htm)
[Get and Set FeatureManager Design Tree Display (VB.NET)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VBNET.htm)
[Get and Set FeatureManager Design Tree Display (VBA)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VB.htm)

## Remarks

Setting IFeatureManager::ShowHierarchyOnly to true sets [IFeatureManager::ShowFeatureDetails](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~ShowFeatureDetails.html) to false, and vice versa.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ViewDependencies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewDependencies.html)
[IFeatureManager::ViewFeatures Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewFeatures.html)
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html)

## Availability

SOLIDWORKS 2010 SP5, Revision Number 18.5
