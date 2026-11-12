---
title: "ExtrudeFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__AccessSelections.htm"
---

# ExtrudeFeatureData::AccessSelections

This method is obsolete and has been superseded by [ExtrudeFeatureData2::AccessSelections](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__AccessSelections.htm).

Description

This method gains access to the selections used to define the extrusion feature.

Syntax (OLE Automation)

accessGained = ExtrudeFeatureData.AccessSelections ( topDoc, component )

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to be modified |
| Return: | (BOOL) accessGained | TRUE if the selections were successfully accessed, FALSE if not |

Syntax (COM)

status = ExtrudeFeatureData->IAccessSelections ( topDoc, component, &accessGained )

| Input: | (LPMODELDOC) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to be modified |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the selections were successfully accessed, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

To modify a feature in a part, set the topDoc argument to the ModelDoc for the part and the component argument to NULL.

To modify a feature in an assembly, set the topDoc argument to the assembly ModelDoc object and the component argument to the component object in which the feature is to be modified.

This method puts the model into a rollback state to allow access to the selections that define the extrusion feature. Use [ExtrudeFeatureData::ReleaseSelectionAccess](ExtrudeFeatureData__ReleaseSelectionAccess.htm) to restore the rollback state, unless you call Feature::ModifyDefinition.
