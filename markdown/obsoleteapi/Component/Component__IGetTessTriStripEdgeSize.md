---
title: "Component::IGetTessTriStripEdgeSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetTessTriStripEdgeSize.htm"
---

# Component::IGetTessTriStripEdgeSize

This method is obsolete and has been superseded by [Component2::IGetTessTriStripEdgeSize](sldworksAPI.chm::/Component2/Component2__IGetTessTriStripEdgeSize.htm).

Description

This method gets the number of triangles.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->IGetTessTriStripEdgeSize ( long* retval )

| Input: | (double) x | X component of the direction vector |
| --- | --- | --- |
| Input: | (double) y | Y component of the direction vector |
| Input: | (double) z | Z component of the direction vector |
| Input: | (VARIANT_BOOL) found | TRUE if a point is found |
| Input: | (double*) startPoint | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPASSEMBLYDOC) retval | Pointer to a newly created assembly or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.
