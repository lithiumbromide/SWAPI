---
title: "ModelDoc::GetPopupMenuMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPopupMenuMode.htm"
---

# ModelDoc::GetPopupMenuMode

This method is obsolete and has been superseded by [ModelDoc2::GetPopupMenuMode](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPopupMenuMode.htm).

Description

This method determines the current pop-up menu mode.

Syntax (OLE Automation)

retval = ModelDoc.GetPopupMenuMode ( )

| Return: | (int) retval | Current pop-up menu mode |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetPopupMenuMode ( &retval )

| Output: | (int) retval | Current pop-up menu mode |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When the user clicks the a right-mouse button (RMB) on an entity in the graphics window, the user is presented with one of two distinct menu sets. These menu sets are defined as mode 0 and mode 1:

##### Mode

0 – Default RMB mode. This will present user with options to Select Other, manipulate the view, access the properties dialog of the selected item, and so on.

1 – The user is presented with a limited set of choices including Select Other and Clear Selection. This mode is seen typically when a SolidWorks dialog is active and the user is restricted to entity selection.

Using ModelDoc::SetPopupMenuMode, your application can simulate the same RMB menu behavior as SolidWorks. If you have a dialog that requires user selection of entities, you can set the popup menu mode to 1 to simulate SolidWorks behavior. You should always set the menu mode back to its previous value. Call ModelDoc::GetPopupMenuMode to determine the previous value prior to calling ModelDoc::SetPopupMenuMode.
