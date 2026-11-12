---
title: "Body::DeleteFaces2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DeleteFaces2.htm"
---

# Body::DeleteFaces2

This method is obsolete and has been superseded by [Body2::DeleteFaces2](sldworksAPI.chm::/Body2/Body2__DeleteFaces3.htm).

Description

This method deletes a set of faces from this body, which must be a temporary body.

Syntax (OLE Automation)

retval = Body.DeleteFaces2 ( numOfFaces, faceList, healOption)

| Input: | (long) numOfFaces | Number of faces to delete |
| --- | --- | --- |
| Input: | (VARIANT) faceList | SafeArray containing an array of the faces to delete |
| Input: | (int) healOption | Additional control (see Remarks ) |
| Return: | (BOOL) retval | TRUE if the faces are successfully deleted, FALSE if they are not |

Syntax (COM)

This version of DeleteFaces2 has been superseded by Body::IDeleteFaces3.

status = Body->IDeleteFaces2 ( numOfFaces, faceList, healOption, &retval )

| Input: | (long) numOfFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (LPFACE) *faceList | Array of faces to delete of size numOfFaces |
| Input: | (int) healOption | Additional control (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the faces are successfully deleted, FALSE if they are not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

All of the specified faces, which must belong to this temporary body, are deleted from the body. If the resulting body does not have a complete boundary, then SolidWorks treats any holes as wounds that are healed as specified by the healOption argument. The healOption argument can take the following values:

| Value | Loops on the faces to be deleted are... |
| --- | --- |
| 0 | Dependent on each other and healed at the same time. If extending faces does not yield a solution, then shrinking the faces is tried. |
| 1 | Independent and healed separately. This option also grows the faces the parent had around the hole to cover the hole. |
| 2 | Independent and healed separately. This option also finds a surface in which all edges of a hole lie and attach this to a face covering the hole (SolidWorks creates a new face to cover the hole). |

For example, consider a cube with a through hole made up of four faces (a square hole). To delete these four faces, specify option 0 because the loop on the first face to be deleted is dependent on the loop of the second face to be deleted. Likewise, the loop on the second face to be deleted is dependent on the third face to be deleted, and so on.

Now consider the same cube with a through hole, except this through hole is a simple cylinder ( one face). To delete the cylindrical face, specify option 1 because it heals the loops independently. This is necessary because the cylindrical face actually has two loops (one at either end of the cylinder) that need to be healed separately.

NOTE: It is possible to generate invalid geometry using this method when checking is turned off. Call Body::Check to verify the body is valid after you use this method.
