---
title: "SimpleFilletFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__ReleaseSelectionAccess.htm"
---

# SimpleFilletFeatureData::ReleaseSelectionAccess

This method is obsolete and has been superseded by [SimpleFilletFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access to the selections used to define the simple fillet feature.

Syntax (OLE Automation)

void SimpleFilletFeatureData.ReleaseSelectionAccess ( )

Syntax (COM)

status = SimpleFilletFeatureData ->ReleaseSelectionAccess ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

SimpleFilletFeatureData::AccessSelections puts the model into a rollback state to allow access to the selections that define the simple fillet feature. You must use SimpleFilletFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
