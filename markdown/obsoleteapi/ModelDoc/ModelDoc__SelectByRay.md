---
title: "ModelDoc::SelectByRay"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectByRay.htm"
---

# ModelDoc::SelectByRay

This method is obsolete and has been superseded by [ModelDoc2::SelectByRay](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectByRay.htm).

Description

This method selects the first object of the specified type that is intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius.

Syntax (OLE Automation)

retval = ModelDoc.SelectByRay ( doubleInfoIn, typeWanted )

| Input: | (VARIANT) doubleInfoIn | VARIANT of type SafeArray of 7 doubles; 3 for the start point of the ray, 3 for the direction of the ray ,and 1 for the radius |
| --- | --- | --- |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Return: | (BOOL) retval | TRUE if a selection was made, FALSE if not |

Syntax (COM)

status = ModelDoc->ISelectByRay ( pointIn, vectorIn, radiusIn, typeWanted, &retval )

| Input: | (double*) pointIn | Pointer to an array containing 3 doubles that define the start point of the ray |
| --- | --- | --- |
| Input: | (double*) vectorIn | Pointer to an array containing 3 doubles that define the direction of the ray |
| Input: | (double) radiusIn | Radius of the ray |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Output: | (VARIANT_BOOL) retval | TRUE if an object was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The radiusIn value is specified in meters.

This method defines a cylindrical region of infinite length that begins at pointIn, runs parallel to vectorIn, and has a radius of radiusIn. If edge or vertex entities have been specified, then the first edge or vertex found within the selection cylinder will be selected.

For selecting face entities, the radiusIn value is ignored and a cylinder of aninfinitely small radius is used.

This method only selects entity objects, which include faces, edges, vertices, and so on. Sketch objects cannot be selected using this function.
