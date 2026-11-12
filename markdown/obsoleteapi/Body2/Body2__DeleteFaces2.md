---
title: "Body2::DeleteFaces2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__DeleteFaces2.htm"
---

# Body2::DeleteFaces2

This method is obsolete and has been superseded by [Body2::DeleteFaces3](sldworksAPI.chm::/Body2/Body2__DeleteFaces3.htm).

Description

This method deletes a set of faces from a temporary body.

Syntax (OLE Automation)

retval = Body2.DeleteFaces2 ( numOfFaces, faceList, healOption)

| Input: | (long) numOfFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (VARIANT) faceList | SafeArray containing an array of the faces for deletion |
| Input: | (int) healOption | Additional control (see below) |
| Return: | (BOOL) retval | TRUE if the faces are successfully deleted, FALSE if not |

Syntax (COM)

This method is obsolete and has been superseded Body2::IDeleteFaces3.

status = Body2->IDeleteFaces2 ( numOfFaces, faceList, healOption, &retval )

| Input: | (long) numOfFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (LPFACE2) *faceList | Faces for deletion of size numOfFaces |
| Input: | (int) healOption | Additional control (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the faces are successfully deleted, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

All of the specified faces, which must belong to this temporary body, are deleted from the Body2. If the resulting body does not have a complete boundary, then SolidWorks treats any holes as wounds and heals them as specified by the healOption argument.

The healOption argument takes the following values:

| Value | Loops on the faces to delete are... |
| --- | --- |
| 0 | Dependent on each other and should be healed at the same time. If extending faces does not yield a solution, then SolidWorks tries to shrink the faces. |
| 1 | Independent and should be healed separately. This option also grows the parent faces around the hole to cover it. |
| 2 | Independent and should be healed separately. This option also finds a surface in which all edges of a hole lie and attaches this to a face covering the hole (SolidWorks creates a new face to cover the hole). |

For example, consider a cube with a through hole made up of four faces (a square hole). To delete these four faces, specify option 0 because the loop on the first face to be deleted is dependent on the loop of the second face to be deleted. Likewise, the loop on the second face to be deleted is dependent on the third face to be deleted, and so on.

Now consider the same cube with a through hole, except this through hole is a simple cylinder (one face). To delete the cylindrical face, specify option 1 to heal the loops independently. This is necessary because the cylindrical face actually has two loops (one at either end of the cylinder) that need to be healed separately.

It is possible to generate invalid geometry when you use this method (because checking is disabled). Call Body2::Check2 to verify the body is a valid solid after you use this method.
