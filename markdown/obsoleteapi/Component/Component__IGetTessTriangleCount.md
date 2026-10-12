---
title: "Component::IGetTessTriangleCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetTessTriangleCount.htm"
---

# Component::IGetTessTriangleCount

This method is obsolete and has been superseded by [Component2::IGetTessTriangleCount](sldworksAPI.chm::/Component2/Component2__IGetTessTriangleCount.htm).

Description

This method returns the number of triangles that make up the shaded picture tessellation for this component.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->IGetTessTriangleCount ( retval )

| Output: | (long) retval | Triangle count |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.
