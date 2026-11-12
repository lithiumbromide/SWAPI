---
title: "HideFeatureManager Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HideFeatureManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideFeatureManager.html"
---

# HideFeatureManager Method (IModelDocExtension)

Hides or shows the Manager Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function HideFeatureManager( _
   ByVal Hide As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Hide As System.Boolean
Dim value As System.Boolean

value = instance.HideFeatureManager(Hide)
```

### C#

```csharp
System.bool HideFeatureManager(
   System.bool Hide
)
```

### C++/CLI

```cpp
System.bool HideFeatureManager(
   System.bool Hide
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Hide`: True to hide the Manager Pane, false to not

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelDocExtension::HideFeatureManager](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~HideFeatureManager.html).

## Examples

[Hide the FeatureManager Design Tree (VBA)](Hide_the_FeatureManager_Example_VB.htm)
[Hide the FeatureManager Design Tree (VB.NET)](Hide_the_FeatureManager_Example_VBNET.htm)
[Hide the FeatureManager Design Tree (C#)](Hide_the_FeatureManager_Example_CSharp.htm)
[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

## Remarks

The FeatureManager design tree, PropertyManager, ConfigurationManager, DimXpertManager, DisplayManager, and custum tabs reside in the Manager Pane.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::FeatureManagerFilterString Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.html)
[IModelViewManager::FeatureManagerTabsVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
