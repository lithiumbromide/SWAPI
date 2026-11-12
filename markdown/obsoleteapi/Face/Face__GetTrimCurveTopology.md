---
title: "Face::GetTrimCurveTopology"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTrimCurveTopology.htm"
---

# Face::GetTrimCurveTopology

This method is obsolete and has been superseded by [Face2::GetTrimCurveTopology](sldworksAPI.chm::/Face2/Face2__GetTrimCurveTopology.htm).

Description

This method gets the trim curve topology for this face.

Syntax (OLE Automation)

retval = Face.GetTrimCurveTopology ()

| Return: | (VARIANT) retval | Trim curve topology for this face |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTrimCurveTopology ( &topolList )

| Output: | (LPDISPATCH*) topolList | Trim curve topology for this face |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method returns a list of CoEdges, Vertex's and NULLs.

You must successfully call [GetTrimCurves2](Face__GetTrimCurves2.htm) before calling this method. If you successfully call GetTrimCurves2 prior to this call, this method returns a list of proper edges corresponding to the list of SP curves that GetTrimCurves2 passed back. Otherwise, this method asks the modeler for the list of edges that it thinks are on the face. These two lists differ in order and content.

Use [GetTrimCurveTopologyTypes](Face__GetTrimCurveTopologyTypes.htm) to get an array of types corresponding to the returned objects in topolList.
