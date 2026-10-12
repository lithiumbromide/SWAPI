---
title: "VariableFilletFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__AccessSelections.htm"
---

# VariableFilletFeatureData::AccessSelections

This method is obsolete and has been superseded by [VariableFilletFeatureData2::AccessSelections](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__AccessSelections.htm).

Description

This method allows you to gain access to the selections used to define the variable-fillet feature.

Syntax (OLE Automation)

accessGained = VariableFilletFeatureData.AccessSelections ( topDoc, component )

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to be modified |
| Return: | (BOOL) accessGained | TRUE if the Selections were successfully accessed |

Syntax (COM)

status = VariableFilletFeatureData ->IAccessSelections ( topDoc, component, &accessGained )

| Input: | (LPMODELDOC) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to be modified |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the Selections were successfully accessed |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, the TopDoc argument is the ModelDoc for the part and the Component argument should be NULL.

To modify a feature in an Assembly, the TopDoc argument should be the assembly'a ModelDoc object and the Component argument should be the Component object in which the feature is to be modified.

NOTE: This method will put the model into a rollback state to allow access to the selections that define the Variable Fillet Feature. You must use VariableFilletFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
