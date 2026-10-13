---
title: "SimpleHoleFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__AccessSelections.htm"
---

# SimpleHoleFeatureData::AccessSelections

This method is obsolete and superseded by [SimpleHoleFeatureData2::AccessSelections](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__AccessSelections.htm).

Description

This method gains access to the selections used to define the simple hole feature.

Syntax (OLE Automation)

accessGained = SimpleHoleFeatureData.AccessSelections ( topDoc, component )

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to modify |
| Return: | (BOOL) accessGained | TRUE if the selections are successfully accessed |

Syntax (COM)

status = SimpleHoleFeatureData ->IAccessSelections ( topDoc, component, &accessGained )

| Input: | (LPMODELDOC) topDoc | Top-evel document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to modify |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the Selections are successfully accessed |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, the TopDoc argument is the ModelDoc for the part and the Component argument should be NULL.

To modify a feature in an assembly, the TopDoc argument should be the assembly's ModelDoc object and the Component argument should be the Component object in which the feature is to be modified.

This method puts the model into a rollback state to allow access to the selections that define the simple hole feature. You must use SimpleHoleFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
