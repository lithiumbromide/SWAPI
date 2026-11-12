---
title: "Face::RemoveRedundantTopology"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__RemoveRedundantTopology.htm"
---

# Face::RemoveRedundantTopology

This method is obsolete and has been superseded by [Face2::RemoveRedundantTopology](sldworksAPI.chm::/Face2/Face2__RemoveRedundantTopology.htm).

Description

This method removes redundant topology from the face.

Syntax (OLE Automation)

retval = Face.RemoveRedundantTopology ()

| Return: | (BOOL) retval | TRUE if the redundant topology was removed successfully, FALSE if it was not |
| --- | --- | --- |

Syntax (COM)

status = Face->RemoveRedundantTopology ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the redundant topology was removed successfully, FALSE if it was not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |
