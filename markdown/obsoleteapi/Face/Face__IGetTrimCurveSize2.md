---
title: "Face::IGetTrimCurveSize2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetTrimCurveSize2.htm"
---

# Face::IGetTrimCurveSize2

This method is obsolete and has been superseded by [Face2::IGetTrimCurveSize2](sldworksAPI.chm::/Face2/Face2__IGetTrimCurveSize2.htm).

Description

This method returns the size of the array needed to hold data for [Face::IGetTrimCurve](Face__GetTrimCurves2.htm).

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetTrimCurveSize2 ( wantCubic, wantNRational, &retval )

| Input: | (VARIANT_BOOL) wantCubic | TRUE if the trim curves are to be cubic, FALSE if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) wantNRational | TRUE if the trim curves are to be non-rational, FALSE if not |
| Output: | (long) retval | Size of the array required for Face::IGetTrimCurve |
| Return: | (HRESULT)status | S_OK if successful |
