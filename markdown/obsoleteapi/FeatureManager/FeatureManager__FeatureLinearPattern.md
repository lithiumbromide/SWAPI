---
title: "FeatureManager::FeatureLinearPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureLinearPattern.htm"
---

# FeatureManager::FeatureLinearPattern

This method is obsolete and has been superseded by [FeatureManager::FeatureLinearPattern2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureLinearPattern2.htm).

Description

This method inserts a linear pattern feature of the selected features or components.

Syntax (OLE Automation)

retval = FeatureManager.FeatureLinearPattern ( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2 )

| Input: | (long) num1 | Number of instances of the linear pattern in Direction 1, including the original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing between each instance of the linear pattern in Direction 1 in meters |
| Input: | (long) num2 | Number of instances of the linear pattern in Direction 2, including the original |
| Input: | (double) spacing2 | Spacing between each instance of the linear pattern in Direction 2 in meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE if you want to reverse the direction the linear pattern in Direction 1, FALSE if not |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE if you want to reverse the direction of the linear pattern in Direction 2, FALSE if not |
| Input: | (BSTR) dName1 | Name of the dimension defining Direction 1 |
| Input: | (BSTR) dName2 | Name of the dimension defining in Direction 2 |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->FeatureLinearPattern ( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2, retval )

| Input: | (long) num1 | Number of instances of the linear pattern in Direction 1, including the original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing between each instance of the linear pattern in Direction 1 in meters |
| Input: | (long) num2 | Number of instances of the linear pattern in Direction 2, including the original |
| Input: | (double) spacing2 | Spacing between each instance of the linear pattern in Direction 2, meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE if you want to reverse the direction the linear pattern in Direction 1 |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE if you want to reverse the direction of the linear pattern in Direction 2, FALSE if not |
| Input: | (BSTR) dName1 | Name of the dimension defining Direction 1 |
| Input: | (BSTR) dName2 | Name of the dimension defining Direction 2 |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features and components.

- Features. Use ModelDocExtension::SelectByID 1 and 2 for the directions and ModelDocExtension::SelectByID 4 for the features to pattern.
- Components. Use ModelDocExtension::SelectByID 1 for the components to pattern and ModelDocExtension::SelectByID 2 and 4 for the directions.
