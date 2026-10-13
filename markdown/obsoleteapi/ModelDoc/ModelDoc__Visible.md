---
title: "ModelDoc::Visible"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Visible.htm"
---

# ModelDoc::Visible

This property is obsolete and has been superseded by [ModelDoc2::Visible](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Visible.htm).

Description

This property gets and sets the visibility property of the active document.

Syntax (OLE Automation)

visibility = ModelDoc.Visible (VB Get property)

ModelDoc.Visible = visibility (VB Set property)

visibility = ModelDoc.GetVisible ( ) (C++ Get property)

ModelDoc.SetVisible ( visibility ) (C++ Set property)

| Property: | (BOOL) visibility | TRUE if the document is be visible, FALSE otherwise |
| --- | --- | --- |

Syntax (Com)

status = ModelDoc->get_Visible( visibility )

status = ModelDoc->put_Visible( visibility )

| Property: | (VARIANT_BOOL) visibility | TRUE if the document is be visible, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
