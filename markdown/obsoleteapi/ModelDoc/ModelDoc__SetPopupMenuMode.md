---
title: "ModelDoc::SetPopupMenuMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetPopupMenuMode.htm"
---

# ModelDoc::SetPopupMenuMode

This method is obsolete and has been superseded by [ModelDoc2::SetPopupMenuMode](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetPopupMenuMode.htm).

Description

This sets the pop-up menu mode.

Syntax (OLE Automation)

void ModelDoc.SetPopupMenuMode ( modeIn )

| Input: | (int) modeIn | Pop-up menu mode |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetPopupMenuMode ( modeIn )

| Input: | (int) modeIn | Pop-up menu mode |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When a user clicks the right-mouse button (RMB) on an entity in the graphics window, they are presented with one of two distinct menu sets. These menu sets have been defined as mode 0 and mode 1:

#### Mode

0 – Default RMB mode. This presents the user with options to Select Other, manipulate the view, access the properties dialog of the selected item, and so on

1 – The user is presented with a limited set of choices including Select Other and Clear Selection. This mode is seen typically when a SolidWorks dialog is active and the user is restricted to entity selection.

Using this method, you can simulate the same RMB menu behavior. If you have a dialog that requires user selection of entities, you can set the pop-up menu mode to 1 to simulate SolidWorks behavior. Your application should always set the menu mode back to its previous value. The previous value can be determined by calling ModelDoc::GetPopupMenuMode prior to your call to ModelDoc::SetPopupMenuMode.
