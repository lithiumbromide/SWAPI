---
title: "Face::IGetTessTriStripEdgeSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetTessTriStripEdgeSize.htm"
---

# Face::IGetTessTriStripEdgeSize

This method is obsolete and has been superseded by [Face2::IGetTessTriStripEdgeSize](sldworksAPI.chm::/Face2/Face2__IGetTessTriStripEdgeSize.htm).

Description

This method gets the size of the array returned by Face::GetTessTriStripEdges.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetTessTriStripEdgeSize ( &retval )

| Output: | (long) retval | Size of the array returned by Face::GetTessTriStripEdges |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value from this method is the number of longs returned from Face::GetTessTriStripEdges, which is (1 + NumStrips + EdgeCount).
