---
title: "ModelDoc::FeatureReferenceCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureReferenceCurve.htm"
---

# ModelDoc::FeatureReferenceCurve

This method is obsolete and has been superseded by [ModelDoc2::FeatureReferenceCurve](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureReferenceCurve.htm).

Description

This method create a reference curve feature from an array of curves.

Syntax (OLE Automation)

retval = ModelDoc.FeatureReferenceCurve ( numOfCurves, baseCurves, merge, fromFileName, &errorCode )

| Input: | (long) numOfCurves | Number of curves from which to create the object |
| --- | --- | --- |
| Input: | (VARIANT) baseCurves | SafeArray of Dispatch pointers to the curves |
| Input: | (BOOL) merge | TRUE creates a single reference curve feature, FALSE creates a reference curve feature for each curve in the array |
| Input: | (BSTR) fromFileName | Not used |
| Output: | (long) errorCode | Error code as defined in swFeatureError_e |
| Return: | (LPDISPATCH) retval | Dispatch pointer to ReferenceCurve Object. |

Syntax (COM)

status = ModelDoc->IFeatureReferenceCurve ( numOfCurves, baseCurves, merge, fromFileName, &errorCode, &retval )

| Input: | (long)numOfCurves | Number of curves from which to create the object |
| --- | --- | --- |
| Input: | (LPCURVE)*baseCurves | Pointer to an array of curves |
| Input: | (VARIANT_BOOL) merge | TRUE creates a single reference curve feature, FALSE creates a reference curve feature for each curve in the array |
| Input: | (BSTR) fromFileName | Not used |
| Output: | (long) errorCode | Error code as defined in swFeatureError_e |
| Output: | (LPREFERENCECURVE) retval | Pointer to ReferenceCurve object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
