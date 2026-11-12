---
title: "Feature::SetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__SetSuppression.htm"
---

# Feature::SetSuppression

This method is obsolete and has been superseded by [Feature::SetSuppression2](sldworksAPI.chm::/Feature/Feature__SetSuppression2.htm).

Description

This method sets the suppression state of this feature.

Syntax (OLE Automation)

suppressSet = Feature.SetSuppression ( suppressState )

| Input: | ( long ) suppressState | Suppression state of this feature as defined in swFeatureSuppressionAction_e |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) suppressSet | TRUE if the suppression state was successfully set, FALSE if not |

Syntax (COM)

status = Feature->SetSuppression ( suppressState, &suppressSet )

| Input: | (long) suppressState | Suppression state of this feature as defined in swFeatureSuppressionAction_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) suppressSet | TRUE if the suppression state was successfully set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
