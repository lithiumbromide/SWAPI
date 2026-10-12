---
title: "Component::IGetTessTriStripSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetTessTriStripSize.htm"
---

# Component::IGetTessTriStripSize

This method is obsolete and has been superseded by [Component2::IGetTessTriStripSize](sldworksAPI.chm::/Component2/Component2__IGetTessTriStripSize.htm).

Description

This method returns the array size of floats required to contain the data returned by Component::GetTessTriStrips.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->IGetTessTriStripSize ( &retval )

| Output: | (long) retval | Size of the array returned by Component::GetTessTriStrips |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.

SolidWorks calculates the array size as ( 3 + FaceCount + StripCount + 3 * VertexCount).
