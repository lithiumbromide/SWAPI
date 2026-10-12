---
title: "ModelDoc::SetSaveFlag"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSaveFlag.htm"
---

# ModelDoc::SetSaveFlag

This method is obsolete and has been superseded by [ModelDoc2::SetSaveFlag](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSaveFlag.htm).

Description

This method flags the document as dirty. If the user tries to close the part, SolidWorks pops up the Do you wish to save changes dialog.

Syntax (OLE Automation)

void ModelDoc.SetSaveFlag ()

Syntax (COM)

status = ModelDoc->SetSaveFlag ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If your application data has changed, this method allows you to mark the SolidWorks document as dirty so that the user is prompted if he or she tries to close it. This could be used, for example, with applications that use the IGet3rdPartyStorage mechanism to save stream data in SolidWorks files.

This method is not needed when you have programmatically changed the SolidWorks model because doing so automatically flags the document as dirty.
