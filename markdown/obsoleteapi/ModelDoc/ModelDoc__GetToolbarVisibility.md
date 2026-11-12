---
title: "ModelDoc::GetToolbarVisibility"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetToolbarVisibility.htm"
---

# ModelDoc::GetToolbarVisibility

This method is obsolete and has been superseded by [ModelDoc2::GetToolbarVisibility](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetToolbarVisibility.htm).

Description

This method gets the visibility of a toolbar.

Syntax (OLE Automation)

Visible = ModelDoc.GetToolbarVisibility( Toolbar )

| Input: | (long) Toolbar | Identifier of toolbar as defined in swToolbar_e |
| --- | --- | --- |
| Return: | (BOOL) Visible | TRUE if the toolbar is visible, FALSE if it is hidden |

Syntax (COM)

status = ModelDoc->GetToolbarVisibility( Toolbar , &Visible)

| Input: | (long) Toolbar | Identifier of toolbar as defined in swToolbar_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) Visible | TRUE if the toolbar is visible, FALSE if it is hidden |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
