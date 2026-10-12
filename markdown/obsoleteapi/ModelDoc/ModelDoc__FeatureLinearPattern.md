---
title: "ModelDoc::FeatureLinearPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureLinearPattern.htm"
---

# ModelDoc::FeatureLinearPattern

This method is obsolete and has been superseded by [ModelDoc2::FeatureLinearPattern](../ModelDoc2/ModelDoc2__FeatureLinearPattern.htm).

Description

This method creates a linear pattern of the selected feature.

Syntax (OLE Automation)

void ModelDoc.FeatureLinearPattern ( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2)

| Input: | (long) num1 | Number of copies in first direction, including original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing in meters |
| Input: | (long) num2 | Number of copies in second direction, including original |
| Input: | (double) spacing2 | Spacing in meters |
| Input: | (BOOL) flipDir1 | TRUE for other way for first direction |
| Input: | (BOOL) flipDir2 | TRUE for other way for second direction |
| Input: | (BSTR) dName1 | Name of dimension defining the first direction of the pattern |
| Input: | (BSTR) dName2 | Name of dimension defining the second direction of the pattern |

Syntax (COM)

status = ModelDoc->FeatureLinearPattern ( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2 )

| Input: | (long) num1 | Number of copies in first direction, including original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing in meters |
| Input: | (long) num2 | Number of copies in second direction, including original |
| Input: | (double) spacing2 | Spacing in meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE for other way for first direction |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE for other way for second direction |
| Input: | (BSTR) dName1 | Name of dimension defining the first direction of the pattern |
| Input: | (BSTR) dName2 | Name of dimension defining the second direction of the pattern |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features. Use ModelDoc::SelectByMark 1 and 2 for the directions and ModelDoc::SelectByMark 4 for the features to be patterned.
