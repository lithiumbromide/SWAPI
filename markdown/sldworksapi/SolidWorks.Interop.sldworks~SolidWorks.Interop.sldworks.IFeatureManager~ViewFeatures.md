---
title: "ViewFeatures Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ViewFeatures"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewFeatures.html"
---

# ViewFeatures Property (IFeatureManager)

Gets or sets whether to view the FeatureManager design tree by its features.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewFeatures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ViewFeatures = value

value = instance.ViewFeatures
```

### C#

```csharp
System.bool ViewFeatures {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to view the FeatureManager design tree by its features, false to not (see **Remarks**)

## VBA Syntax

See [FeatureManager::ViewFeatures](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ViewFeatures.html).

## Examples

[Get and Set FeatureManager Design Tree Display (C#)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_CSharp.htm)
[Get and Set FeatureManager Design Tree Display (VB.NET)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VBNET.htm)
[Get and Set FeatureManager Design Tree Display (VBA)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VB.htm)

## Remarks

Setting IFeatureManager::ViewFeatures to true sets [IFeatureManager::ViewDependencies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~ViewDependencies.html) to false, and vice versa.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ShowFeatureDetails Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.html)
[IFeatureManager::ShowHierarchyOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.html)

## Availability

SOLIDWORKS 2010 SP5, Revision Number 18.5
