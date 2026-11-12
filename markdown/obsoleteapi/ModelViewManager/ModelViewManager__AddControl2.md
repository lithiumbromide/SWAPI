---
title: "ModelViewManager::AddControl2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelViewManager/ModelViewManager__AddControl2.htm"
---

# ModelViewManager::AddControl2

This method is obsolete and has been superseded by [ModelViewManager::AddControl3](sldworksAPI.chm::/ModelViewManager/ModelViewManager__AddControl3.htm).

Description

This method adds an ActiveX control to this model view.

NOTE: If your ActiveX control does not need tab traversal support, then use ModelViewManager::AddControl.

Syntax (OLE Automation)

retval = ModelViewManager.AddControl2 ( Name, ControlName, BstrLicKey )

| Input: | (BSTR) Name | User-defined label that appears on the tab |
| --- | --- | --- |
| Input: | (BSTR) ControlName | Name or class ID for the ActiveX control |
| Input: | (BSTR) BstrLicKey | Optional license key; this data is needed to create ActiveX controls that require a runtime license key; if the ActiveX control supports licensing, then provide a license key for the creation of the ActiveX control; default value is NULL |
| Output: | (LPUNKNOWN) Retval | Pointer to the new ActiveX control |

Syntax (COM)

status = ModelViewManager->AddControl2 ( Name, ControlName, BstrLicKey, &Retval )

| Input: | (BSTR) Name | User-defined label that appears on the tab |
| --- | --- | --- |
| Input: | (BSTR) ControlName | Name or class ID for the ActiveX control |
| Input: | (BSTR) BstrLicKey | Optional license key; this data only is needed to create ActiveX controls that require a runtime license key; if the ActiveX control supports licensing, then provide a license key for the creation of the ActiveX control; default value is NULL |
| Output: | (LPUNKNOWN) Retval | Pointer to the new ActiveX control |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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

To delete a tab created by this method, use ModelViewManager::DeleteControlTab.
