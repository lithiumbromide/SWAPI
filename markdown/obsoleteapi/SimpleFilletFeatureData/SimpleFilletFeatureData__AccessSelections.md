---
title: "SimpleFilletFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__AccessSelections.htm"
---

# SimpleFilletFeatureData::AccessSelections

This method is obsolete and has been superseded by [SimpleFilletFeatureData2::AccessSelections](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__AccessSelections.htm).

Description

This method gains access to the selections used to define the Simple Fillet Feature.

Syntax (OLE Automation)

accessGained = SimpleFilletFeatureData.AccessSelections ( topDoc, component )

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to be modified |
| Return: | (BOOL) accessGained | TRUE if the selections are successfully accessed, FALSE if not |

Syntax (COM)

status = SimpleFilletFeatureData ->IAccessSelections ( topDoc, component, &accessGained )

| Input: | (LPMODELDOC) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to be modified |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the selections were successfully accessed, TRUE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, the topDoc argument is the ModelDoc for the part and the component argument should be NULL.

To modify a feature in an assembly, the topDoc argument should be the assembly ModelDoc object and the component argument should be the Component object in which the feature is to be modified.

NOTE: This method puts the model into a rollback state to allow access to the selections that define the simple fillet feature. You must use SimpleFilletFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
