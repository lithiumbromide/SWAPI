---
title: "Face::GetTrimCurveTopologyTypes"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTrimCurveTopologyTypes.htm"
---

# Face::GetTrimCurveTopologyTypes

This method is obsolete and has been superseded by [Face2::GetTrimCurveTopologyTypes](sldworksAPI.chm::/Face2/Face2__GetTrimCurveTopologyTypes.htm).

Description

This method gets the trim curve topology type array for this face.

Syntax (OLE Automation)

retval = Face.GetTrimCurveTopologyTypes ( )

| Return: | (VARIANT) retval | SafeArray of long topology types as defined in swSelectType_e |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTrimCurveTopologyTypes ( &retval )

| Output: | (long) retval | Array of long topology types as defined in swSelectType_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
