---
title: "WizardHoleFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__AccessSelections.htm"
---

# WizardHoleFeatureData::AccessSelections

This method is obsolete and has been superseded by [WizardHoleFeatureData2::AccessSelections](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__AccessSelections.htm).

Description

This method gains access to the selections used to define the hole wizard feature.

Syntax (OLE Automation)

accessGained = WizardHoleFeatureData.AccessSelections ( topDoc, component )

| Input: | (LPDISPATCH) topDoc | Top-level document. |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to be modified |
| Return: | (BOOL) accessGained | TRUE if the selections were successfully accessed |

Syntax (COM)

status = WizardHoleFeatureData ->IAccessSelections ( topDoc, component, &accessGained )

| Input: | (LPMODELDOC) topDoc | Top-evel document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to be modified |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the selections were successfully accessed |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, the TopDoc argument is the ModelDoc for the part and the component argument should be NULL.

To modify a feature in an assembly, the TopDoc argument should be the assembly ModelDoc object and the Component argument should be the Component object in which the feature is to be modified.

NOTE: This method puts the model into a rollback state to allow access to the selections that define the hole wizard feature. You must use WizardHoleFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
