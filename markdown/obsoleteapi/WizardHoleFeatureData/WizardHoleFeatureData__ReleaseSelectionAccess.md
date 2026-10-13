---
title: "WizardHoleFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__ReleaseSelectionAccess.htm"
---

# WizardHoleFeatureData::ReleaseSelectionAccess

This method is obsolete and has been superseded by [WizardHoleFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access to the selections used to define the hole wizard feature.

Syntax (OLE Automation)

void WizardHoleFeatureData.ReleaseSelectionAccess ( )

Syntax (COM)

status = WizardHoleFeatureData ->ReleaseSelectionAccess ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

WizardHoleFeatureData::AccessSelections puts the model into a rollback state to allow access to the selections that define the hole wizard feature. You must use WizardHoleFeatureData::ReleaseSelectionAccess to restore the rollback state unless you call Feature::ModifyDefinition.
