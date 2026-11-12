---
title: "ModelDoc::Toolbars"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Toolbars.htm"
---

# ModelDoc::Toolbars

This method is obsolete and has been superseded by [ModelDoc2::Toolbars](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Toolbars.htm).

Description

This method turns the main SolidWorks toolbars on and off.

Syntax (OLE Automation)

void ModelDoc.Toolbars ( m, vw, skMain, sk, feat, constr, macro)

| Input: | (BOOL) m | TRUE for main toolbar on, FALSE for off |
| --- | --- | --- |
| Input: | (BOOL) vw | TRUE for view manipulation toolbar on, FALSE for off |
| Input: | (BOOL) skMain | TRUE for main sketch toolbar on, FALSE for off |
| Input: | (BOOL) sk | TRUE for sketch entity toolbar on, FALSE for off |
| Input: | (BOOL) feat | TRUE for feature toolbar on, FALSE for off |
| Input: | (BOOL) constr | TRUE for relationships toolbar on, FALSE for off |
| Input: | (BOOL) macro | TRUE for macro toolbar on, FALSE for off |

Syntax (COM)

status = ModelDoc->Toolbars ( m, vw, skMain, sk, feat, constr, macro )

| Input: | (VARIANT_BOOL) m | TRUE for main toolbar on, FALSE for off |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) vw | TRUE for view manipulation toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) skMain | TRUE for main sketch toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) sk | TRUE for sketch entity toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) feat | TRUE for feature toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) constr | TRUE for relationships toolbar on, FALSE for off |
| Input: | (VARIANT_BOOL) macro | TRUE for macro toolbar on, FALSE for off |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See ModelDoc.SetToolbarVisibility for control of all SolidWorks toolbars.
