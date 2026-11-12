---
title: "ModelDoc::SketchFillet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchFillet2.htm"
---

# ModelDoc::SketchFillet2

This method is obsolete and has been superseded by [ModelDoc2::SketchFillet2](../ModelDoc2/ModelDoc2__SketchFillet2.htm).

Description

This method creates a sketch fillet between the two sketch selected entities.

Syntax (OLE Automation)

retval = ModelDoc.SketchFillet2 ( radius, constrainedCorners )

| Input: | (double) radius | Radius in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to fillet is constrained or has a dimension |
| Return: | (BOOL) retval | TRUE if the fillet was successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchFillet2 ( radius, constrainedCorners, &retval )

| Input: | (double) radius | Radius in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to fillet is constrained or has a dimension |
| Output: | (VARIANT_BOOL)retval | TRUE if the fillet was successfully created, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The constrainedCorners:

- indicates what action should be taken if the corner to be filleted is constrained in some manner or has a dimension related to it. In this case, adding a fillet to the corner cannot be done without certain consequences. If the corner is not involved with any constraints, this argument is ignored.
- can take a value found in the swConstrainedCornerAction_e enumeration.
