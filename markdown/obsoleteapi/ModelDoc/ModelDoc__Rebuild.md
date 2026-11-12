---
title: "ModelDoc::Rebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Rebuild.htm"
---

# ModelDoc::Rebuild

This method is obsolete and has been superseded by [ModelDoc2::Rebuild](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Rebuild.htm).

Description

This method rebuilds the model.

Syntax (OLE Automation)

void ModelDoc.Rebuild ( Options )

| Input: | (long) Options | Type of rebuild as defined in swRebuildOptions_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Syntax (COM)

status = ModelDoc->Rebuild ( Options )

| Input: | (long)O ptions | Type of rebuild as defined in swRebuildOptions_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Certain options are only valid for particular document types; use ModelDoc::GetType to check the type of document.

Option Document Types Description

swRebuildAll All Rebuilds geometry that has not been regenerated.

swForceRebuildAll All Forces a rebuild of all geometry.

swUpdateMates AssemblyDoc Only rebuilds mates, which is much faster than rebuilding the geometry. Especially for use with Component::SetXform.

swCurrentSheetDisp DrawingDoc Only rebuilds the display of the views on the current drawing sheet.

swUpdateDirtyOnly DrawingDoc Only rebuilds drawing views which are dirty when "OR'd" with swCurrentSheetDisp option.
