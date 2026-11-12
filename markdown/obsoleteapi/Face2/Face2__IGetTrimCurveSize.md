---
title: "Face2::IGetTrimCurveSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face2/Face2__IGetTrimCurveSize.htm"
---

# Face2::IGetTrimCurveSize

This method is obsolete and has been superseded by [Face2::IGetTrimCurveSize2](sldworksAPI.chm::/Face2/Face2__IGetTrimCurveSize2.htm).

Description

This method gets the trim curve size.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face2->IGetTrimCurveSize ( wantCubic, &retval )

| Input: | (VARIANT_BOOL) wantCubic | TRUE if the trim curves are to be cubic, FALSE otherwise |
| --- | --- | --- |
| Output: | (long) retval | Size of the array required for Face2::IGetTrimCurve |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
