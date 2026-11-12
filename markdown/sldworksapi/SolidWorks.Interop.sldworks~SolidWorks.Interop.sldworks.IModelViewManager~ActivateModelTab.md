---
title: "ActivateModelTab Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "ActivateModelTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.html"
---

# ActivateModelTab Method (IModelViewManager)

Selects a control tab on the model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateModelTab() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Boolean

value = instance.ActivateModelTab()
```

### C#

```csharp
System.bool ActivateModelTab()
```

### C++/CLI

```cpp
System.bool ActivateModelTab();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the control tab on the model view is selected, false if not

## VBA Syntax

See [ModelViewManager::ActivateModelTab](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~ActivateModelTab.html).

## Examples

[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)
[Add ActiveX Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::ActivateControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.html)
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.html)
[IModelViewManager::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.html)
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.html)
[IModelViewManager::IsControlTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.html)
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
