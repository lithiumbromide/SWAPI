---
title: "ModelDoc::AlignParallelDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AlignParallelDimensions.htm"
---

# ModelDoc::AlignParallelDimensions

This method is obsolete and has been superseded by [ModelDoc2::AlignParallelDimensions](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AlignOrdinate.htm).

Description

This method aligns any linear dimensions selected in a parallel fashion.

Syntax (OLE Automation)

(void) ModelDoc.AlignParallelDimensions ( )

Syntax (COM)

status = ModelDoc->AlignParallelDimensions ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

The distance between dimensions is determined by the A and B distance values in Tools, Options, Detailing, Arrows.
