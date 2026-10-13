---
title: "ModelDoc::SelectionManager"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectionManager.htm"
---

# ModelDoc::SelectionManager

This property is obsolete and has been superseded by [ModelDoc2::SelectionManager](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectionManager.htm).

Description

This property makes the current selected object available to the user. Selection Manager selected objects are transient since they will be invalid as soon as another selection is made. So these pointers should not be kept around for long.

Syntax (OLE Automation)

SelectionManager = ModelDoc.SelectionManager (VB Get property)

SelectionManager = ModelDoc.GetSelectionManager ( ) (C++ Get property)

| Property: | (LPDISPATCH) SelectionManager | Pointer a Dispatch object, the SelectionMgr object for this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->get_ISelectionManager(&SelectionMananger)

| Property: | (LPSELECTIONMGR) SelectionManager | Pointer to the SelectionMgr object for this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
