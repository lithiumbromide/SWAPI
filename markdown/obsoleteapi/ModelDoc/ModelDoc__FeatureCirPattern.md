---
title: "ModelDoc::FeatureCirPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureCirPattern.htm"
---

# ModelDoc::FeatureCirPattern

This method is obsolete and has been superseded by [ModelDoc2::FeatureCirPattern](../ModelDoc2/ModelDoc2__FeatureCirPattern.htm).

Description

This method creates a circular pattern.

Syntax (OLE Automation)

void ModelDoc.FeatureCirPattern ( num, spacing, flipDir, dName)

| Input: | (long) num | Number of copies, including original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing in radians |
| Input: | (BOOL) flipDir | TRUE if able to flip direction, FALSE to not |
| Input: | (BSTR) dName | Name of angular dimension defining the direction of the pattern |

Syntax (COM)

status = ModelDoc->FeatureCirPattern ( num, spacing, flipDir, dName )

| Input: | (long) num | Number of copies, including original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE if able to flip direction, FALSE to not |
| Input: | (BSTR) dName | Name of angular dimension defining the direction of the pattern |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not require ordered selection of the features.
