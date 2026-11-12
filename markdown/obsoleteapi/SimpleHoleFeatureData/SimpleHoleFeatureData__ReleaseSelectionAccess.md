---
title: "SimpleHoleFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__ReleaseSelectionAccess.htm"
---

# SimpleHoleFeatureData::ReleaseSelectionAccess

This method is obsolete and has been superseded by [SimpleHoleFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access to the selections used to define the simple hole feature.

Syntax (OLE Automation)

void SimpleHoleFeatureData.ReleaseSelectionAccess ( )

Syntax (COM)

status = SimpleHoleFeatureData ->ReleaseSelectionAccess ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

SimpleHoleFeatureData::AccessSelections puts the model into a rollback state to allow access to the selections that define the simple hole Feature. You must use SimpleHoleFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
