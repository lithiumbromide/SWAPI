---
title: "IsControlTabActive Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "IsControlTabActive"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.html"
---

# IsControlTabActive Method (IModelViewManager)

Gets whether the specified control is active.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsControlTabActive( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim value As System.Boolean

value = instance.IsControlTabActive(Name)
```

### C#

```csharp
System.bool IsControlTabActive(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool IsControlTabActive(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of control tab

### Return Value

True if control tab is active, false if not

## VBA Syntax

See [ModelViewManager::IsControlTabActive](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~IsControlTabActive.html).

## Examples

[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)
[Add Active Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.html)
[IModelViewManager::ActivateControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.html)
[IModelViewManager::ActivateModelTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.html)
[IModelViewManager::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.html)
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.html)
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.html)
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
