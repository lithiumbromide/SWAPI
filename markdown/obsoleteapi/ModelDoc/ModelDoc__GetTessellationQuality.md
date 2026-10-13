---
title: "ModelDoc::GetTessellationQuality"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetTessellationQuality.htm"
---

# ModelDoc::GetTessellationQuality

This method is obsolete and has been superseded by [ModelDoc2::GetTessellationQuality](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetTessellationQuality.htm).

Description

This method gets the tessellation quality index for the application.

Syntax (OLE Automation)

retval = ModelDoc.GetTessellationQuality ()

| Return: | (long) retval | Number between 0 and 100 that indicates the quality of tessellation to use for this part; a higher index means finer tessellation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetTessellationQuality ( &retval )

| Output: | (long) retval | Number between 0 and 100 that indicates the quality of tessellation to use for this part; a higher index means finer tessellation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the shaded-display quality setting that you find on the Tools, Options, Performance menu. The numeric deviation value changes based on the current part. This deviation is calculated as follows:

Deviation = 0.025 * (BodyDiameter) / qualityIndex;

where the BodyDiameter is the diagonal distance across the bounds of the part box. See PartDoc::GetPartBox for details.

The Deviation value is in meters.
