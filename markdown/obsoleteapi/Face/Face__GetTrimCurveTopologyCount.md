---
title: "Face::GetTrimCurveTopologyCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTrimCurveTopologyCount.htm"
---

# Face::GetTrimCurveTopologyCount

This method is obsolete and has been superseded by [Face2::GetTrimCurveTopologyCount](sldworksAPI.chm::/Face2/Face2__GetTrimCurveTopologyCount.htm).

Description

This method gets the trim curve topology count for this face.

Syntax (OLE Automation)

topologyCount = Face.GetTrimCurveTopologyCount ( )

| Return: | (long) topologyCount | Number of elements returned by GetTrimCurveTopology |
| --- | --- | --- |

Syntax (COM)

status = Face->GetTrimCurveTopologyCount ( &topologyCount )

| Output: | (long) topologyCount | Number of elements returned by GetTrimCurveTopology |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
