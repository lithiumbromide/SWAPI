---
title: "PartDoc::EditRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EditRebuild.htm"
---

# PartDoc::EditRebuild

This method is obsolete and has been superseded by [ModelDoc2::EditRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditRebuild3.htm).

Description

This method rebuilds the part.

Syntax (OLE Automation)

void PartDoc.EditRebuild ()

Syntax (COM)

status = PartDoc->EditRebuild ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

Certain situations exist where this command is blocked.

For example, if the end-user is interactively editing the properties of a face, then this method is blocked because calling it would invalidate all the pointers in the document. If this command is not blocked, then closing the Face, Properties dialog might cause problems because the dialog is looking for the original face pointer.
