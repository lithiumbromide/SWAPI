---
title: "ModelDoc2::SketchFillet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchFillet2.htm"
---

# ModelDoc2::SketchFillet2

This method is obsolete and has been superseded by [SketchManager::CreateFillet](sldworksAPI.chm::/SketchManager/SketchManager__CreateFillet.htm).

Description

This method creates a sketch fillet between the two sketch selected entities.

Syntax (OLE Automation)

retval = ModelDoc2.SketchFillet2 ( radius, constrainedCorners )

| Input: | (double) radius | Radius of the fillet in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to be filleted is constrained or has a dimension (see Remarks ) |
| Return: | (BOOL) retval | TRUE if the fillet is created, FALSE if not |

Syntax (COM)

status = ModelDoc2->SketchFillet2 ( radius, constrainedCorners, &retval )

| Input: | (double) radius | Radius of the fillet in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to be filleted is constrained or has a dimension (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the fillet s created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The constrainedCorners argument:

- Indicates what action to take if the corner to be filleted is constrained in some manner or has a dimension related to it. In this case, adding a fillet to the corner cannot be done without certain consequences. If the corner is not involved with any constraints, this argument is ignored.
- Can take one of the values found in swConstrainedCornerAction_e.
