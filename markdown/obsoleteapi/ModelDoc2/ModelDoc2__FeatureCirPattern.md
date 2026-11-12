---
title: "ModelDoc2::FeatureCirPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureCirPattern.htm"
---

# ModelDoc2::FeatureCirPattern

This method is obsolete and has been superseded by [FeatureManager::FeatureCircularPattern](../FeatureManager/FeatureManager__FeatureCircularPattern.htm).

Description

This method creates a circular pattern of the selected features or components.

Syntax (OLE Automation)

void ModelDoc2.FeatureCirPattern ( num, spacing, flipDir, dName)

| Input: | (long) num | Number of copies, including original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing in radians |
| Input: | (BOOL) flipDir | TRUE if able to flip direction, FALSE if not |
| Input: | (BSTR) dName | Name of angular dimension defining the direction of the pattern |

Syntax (COM)

status = ModelDoc2->FeatureCirPattern ( num, spacing, flipDir, dName )

| Input: | (long) num | Number of copies, including original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE if able to flip direction, FALSE if not |
| Input: | (BSTR) dName | Name of angular dimension defining the direction of the pattern |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires an ordered selection of the features and components.

- Features. Use ModelDoc2::SelectByMark 4 for the features to pattern.
- Components. Use ModelDoc2::SelectByMark 1 for the components to pattern and ModelDoc2::SelectByMark 2 for the axis.
