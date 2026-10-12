---
title: "ModelDoc::SketchAddConstraints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchAddConstraints.htm"
---

# ModelDoc::SketchAddConstraints

This method is obsolete and has been superseded by [ModelDoc2::SketchAddConstraints](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchAddConstraints.htm).

Description

This method adds a constraint of the type specified to the entity, or entities, selected. The constraint name passed to this function is a string, not an enumerated integer.

Syntax (OLE Automation)

void ModelDoc.SketchAddConstraints ( idStr)

| Input: | (BSTR) idStr | Constraint name |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SketchAddConstraints ( idStr )

| Input: | (BSTR) idStr | Constraint name |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The available constraints are as follows. Embed the string containing the name of the constraint in double quotes.

| sgHORIZONTAL sgHORIZPOINTS sgVERTICAL sgVERTPOINTS sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT | sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT | sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE |
| --- | --- | --- |
