---
title: "ModelDoc::SketchConstraintsDel"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchConstraintsDel.htm"
---

# ModelDoc::SketchConstraintsDel

This method is obsolete and has been superseded by [ModelDoc2::SketchConstraintsDel](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchConstraintsDel.htm).

Description

This method deletes the specified relationship on the currently selected item.

Syntax (OLE Automation)

void ModelDoc.SketchConstraintsDel ( constrInd, idStr)

| Input: | (long) constrInd | Constraint number on the selected entity; this is a 0-based index |
| --- | --- | --- |
| Input: | (BSTR) idStr | Constraint to delete |

Syntax (COM)

status = ModelDoc->SketchConstraintsDel ( constrInd, idStr )

| Input: | (long) constrInd | Constraint number on the selected entity; this is a 0-based index |
| --- | --- | --- |
| Input: | (BSTR) idStr | Constraint to delete |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To delete a tangency relation that is the third relation on the selected arc, you would specify:

Part.SketchConstraintsDel 2, "sgTANGENT"

The available constraint names used in the idStr argument are as follows. Embed the string containing the name of the constraint in double quotes.

| sgHORIZONTAL sgHORIZPOINTS sgVERTICAL sgVERTPOINTS sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT | sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT | sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE |
| --- | --- | --- |
