---
title: "VariableFilletFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__ReleaseSelectionAccess.htm"
---

# VariableFilletFeatureData::ReleaseSelectionAccess

This method is obsolete and has been superseded by [VariableFilletFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access to the selections used to define the variable fillet feature.

Syntax (OLE Automation)

void VariableFilletFeatureData.ReleaseSelectionAccess ( )

Syntax (COM)

status = VariableFilletFeatureData ->ReleaseSelectionAccess ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

VariableFilletFeatureData::AccessSelections pust the model into a rollback state to allow access to the selections that define the variable fillet Feature. You must use VariableFilletFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
