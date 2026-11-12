---
title: "AddControl Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "AddControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.html"
---

# AddControl Method (IModelViewManager)

Adds a tab to this model view using the specified ActiveX control.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddControl( _
   ByVal Name As System.String, _
   ByVal ControlName As System.String, _
   ByVal BstrLicKey As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim ControlName As System.String
Dim BstrLicKey As System.String
Dim value As System.Object

value = instance.AddControl(Name, ControlName, BstrLicKey)
```

### C#

```csharp
System.object AddControl(
   System.string Name,
   System.string ControlName,
   System.string BstrLicKey
)
```

### C++/CLI

```cpp
System.Object^ AddControl(
   System.String^ Name,
   System.String^ ControlName,
   System.String^ BstrLicKey
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: User-defined label that appears on the tab
- `ControlName`: Name or class ID for the ActiveX control
- `BstrLicKey`: Optional license key; this data is needed to create ActiveX controls that require a runtime license key; if the ActiveX control supports licensing, then provide a license key for the creation of the ActiveX control; default value is NULL

### Return Value

Pointer to the new ActiveX control

## VBA Syntax

See [ModelViewManager::AddControl](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~AddControl.html).

## Examples

[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)
[Add ActiveX Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

## Remarks

If your ActiveX control needs tab traversal support, then use [IModelViewManager::AddControl3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~AddControl3.html).

This method sets the class ID and license key information for the ActiveX control when the API PropertyManager page is shown and the ActiveX control is created. The controlName argument can be either the name of the control (ProgID) or the class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". Both provide the calendar protocol. You can obtain these strings using a combination of the Microsoft OLE/COM Object Viewer and the registry editor.

For example:

```vb
' ProgID
bRet = m_pActiveXControl.SetClass("MSCAL.Calendar", "")
bRet = m_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl", "")

' CLSID
bRet = m_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}", "")
bRet = m_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}", "")
```

To delete a tab created by this method, use [IModelViewManager::DeleteControlTab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~DeleteControlTab.html).

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::ActivateControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateControlTab.html)
[IModelViewManager::ActivateModelTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActivateModelTab.html)
[IModelViewManager::DeleteControlTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteControlTab.html)
[IModelViewManager::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetControl.html)
[IModelViewManager::IGetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IGetControl.html)
[IModelViewManager::IsControlTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsControlTabActive.html)
[IModelViewManager::IsModelTabActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~IsModelTabActive.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
