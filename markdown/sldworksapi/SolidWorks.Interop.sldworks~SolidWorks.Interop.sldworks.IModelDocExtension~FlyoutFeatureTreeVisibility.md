---
title: "FlyoutFeatureTreeVisibility Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "FlyoutFeatureTreeVisibility"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FlyoutFeatureTreeVisibility.html"
---

# FlyoutFeatureTreeVisibility Property (IModelDocExtension)

Gets or sets the state of the flyout FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlyoutFeatureTreeVisibility As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

instance.FlyoutFeatureTreeVisibility = value

value = instance.FlyoutFeatureTreeVisibility
```

### C#

```csharp
System.int FlyoutFeatureTreeVisibility {get; set;}
```

### C++/CLI

```cpp
property System.int FlyoutFeatureTreeVisibility {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

State of the flyout FeatureManager design tree as defined in [swFeatureTreeState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureTreeState_e.html)

## VBA Syntax

See [ModelDocExtension::FlyoutFeatureTreeVisibility](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~FlyoutFeatureTreeVisibility.html).

## Examples

[Get and Set the State of the Flyout FeatureManager Design Tree (VBA)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_VB.htm)
[Get and Set the State of the Flyout FeatureManager Design Tree (VB.NET)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_VBNET.htm)
[Get and Set the State of the Flyout FeatureManager Design Tree (C#)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
