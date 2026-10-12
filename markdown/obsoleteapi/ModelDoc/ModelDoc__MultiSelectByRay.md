---
title: "ModelDoc::MultiSelectByRay"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__MultiSelectByRay.htm"
---

# ModelDoc::MultiSelectByRay

This method is obsolete and has been superseded by [ModelDoc2::MultiSelectByRay](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IMultiSelectByRay.htm).

Description

This method selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius.

Syntax (OLE Automation)

retval = ModelDoc.MultiSelectByRay ( doubleInfoIn, typeWanted, append )

| Input: | (VARIANT) doubleInfoIn | VARIANT of type SafeArray of 7 doubles: 3 for the start point of the ray, 3 for the direction of the ray, and 1 for the radius. |
| --- | --- | --- |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Input: | (BOOL) append | TRUE if a you wish to append the selections to the current selection list, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if a selection was made |

Syntax (COM)

status = ModelDoc->IMultiSelectByRay ( pointIn, vectorIn, radiusIn, typeWanted, append, &retval )

| Input: | (double*) pointIn | Pointer to an array containing 3 doubles that define the start point of the ray |
| --- | --- | --- |
| Input: | (double*) vectorIn | Pointer to an array containing 3 doubles that define the direction of the ray |
| Input: | (double) radiusIn | Radius of the ray in meters |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Input: | (VARIANT_BOOL) append | TRUE if a you wish to append the selections to the current selection list, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if an object was selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method defines a cylindrical region of infinite length that begins at pointIn, runs parallel to vectorIn, and has a radius of radiusIn. If edge or vertex entities have been specified, then any edge or vertex found within the selection cylinder is selected.

This method selects only entity objects, which include faces, edges, and vertices. You cannot use this method to select Sketch objects.

For selecting face entities, the radiusIn value is ignored and a cylinder of infinitely small radius is used.
