---
title: "ModelDoc::AlignDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AlignDimensions.htm"
---

# ModelDoc::AlignDimensions

This method is obsolete and has been superseded by [ModelDoc2::AlignDimensions](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AlignDimensions.htm).

Description

This method aligns the selected dimensions co-linearly.

Syntax (OLE Automation)

(void) ModelDoc.AlignDimensions ( )

Syntax (COM)

status = ModelDoc->AlignDimensions ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method attempts to sort the dimensions selected into three groups: linear, ordinate, and angular dimensions. Within the linear group, this method sorts by measured direction. Each of these dimensions are then aligned with the other like dimensions. These dimensions are then updated and dragged together.
