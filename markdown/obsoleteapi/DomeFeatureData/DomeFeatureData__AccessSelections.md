---
title: "DomeFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__AccessSelections.htm"
---

# DomeFeatureData::AccessSelections

This method is obsolete and has been superseded by [DomeFeatureData2::AccessSelections](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__AccessSelections.htm).

Description

This method gains access to the selections used to define this dome feature.

Syntax (OLE Automation)

retval = DomeFeatureData.AccessSelections( TopDoc, Component )

| Input: | (LPDISPATCH) TopDoc | Top-level document (see Remarks ) |
| --- | --- | --- |
| Input: | (LPDISPATCH) Component | Component for the feature (see Remarks ) |
| Return: | (BOOL) retval | TRUE if the selections where successfully accessed, FALSE if not |

Syntax (COM)

status = DomeFeatureData->IAccessSelections( TopDoc, Component, &retval )

| Input: | (LPMODELDOC) TopDoc | Top-level document (see Remarks ) |
| --- | --- | --- |
| Input: | (LPCOMPONENT) Component | Component for the feature (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the selections where successfully accessed, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, set the TopDoc argument to the ModelDoc for the part and the Component argument to NULL.

To modify a feature in an assembly, set the TopDoc to the ModelDoc for the assembly and the Component argument to the component in which the feature is to be modified.

Because the face on which the dome was defined is not accessible once the dome has been created, this method puts the model into a rollback state to allow access to the selections that define the dome. You must use DomeFeatureData::ReleaseSelectionAccess to restore the rollback state, unless you call Feature::ModifyDefinition.
