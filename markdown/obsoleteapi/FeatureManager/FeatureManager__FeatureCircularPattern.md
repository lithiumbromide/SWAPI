---
title: "FeatureManager::FeatureCircularPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureCircularPattern.htm"
---

# FeatureManager::FeatureCircularPattern

This method is obsolete and has been superseded by [FeatureManager::FeatureCircularPattern2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureCircularPattern2.htm).

Description

This method inserts a circular pattern feature in the selected features or components.

Syntax (OLE Automation)

retval = FeatureManager.FeatureCircularPattern ( num, spacing, flipDir, dName )

| Input: | (long) num | Number of instances of the circular pattern to insert, including the original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing between each instance of the circular pattern in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction of the circular pattern |
| Input: | (BSTR) dName | Name of the angular dimension defining the direction of the pattern |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->FeatureCircularPattern ( num, spacing, flipDir, dName, retval )

| Input: | (long) num | Number of instances of the circular pattern to insert, including the original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing between each instance of the circular pattern in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction of the circular pattern |
| Input: | (BSTR) dName | Name of the angular dimension defining the direction of the pattern |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features and components.

- Features. Use ModelDocExtension::SelectByID 4 for the features to pattern.
- Components. Use ModelDocExtension::SelectByID 1 for the components to pattern and ModelDocExtension::SelectByID 2 for the axis.
