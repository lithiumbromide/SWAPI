---
title: "ModelDoc::SetTessellationQuality"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetTessellationQuality.htm"
---

# ModelDoc::SetTessellationQuality

This method is obsolete and has been superseded by [ModelDoc2::SetTessellationQuality](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetTessellationQuality.htm).

Description

This method sets the tessellation quality index for the application.

Syntax (OLE Automation)

void ModelDoc.SetTessellationQuality ( qualityNum)

| Input: | (long) qualityNum | Number between 0 and 100, which indicates the quality of tessellation to use for this part; a higher index means finer tessellation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetTessellationQuality ( qualityNum )

| Input: | (long) qualityNum | Number between 0 and 100, which indicates the quality of tessellation to use for this part; a higher index means finer tessellation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method changes the shaded-display quality setting that you find on the Tools, Option, Performance menu.

The numeric deviation value will change based on the current part. This deviation is calculated as follows:

Deviation = 0.025 * (BodyDiameter) / qualityIndex;

where BodyDiameter is the diagonal distance across the bounds of the part box . See PartDoc::GetPartBox.

The resulting Deviation value is in meters.

NOTE: This method sets the quality in the overall environment, not just the current part.
