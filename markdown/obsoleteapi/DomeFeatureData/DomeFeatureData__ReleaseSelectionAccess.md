---
title: "DomeFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__ReleaseSelectionAccess.htm"
---

# DomeFeatureData::ReleaseSelectionAccess

This method is obsolete and hs been superseded by [DomeFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access to selections used to define the dome feature.

Syntax (OLE Automation)

void DomeFeatureData.ReleaseSelectionAccess( )

Syntax (COM)

status = DomeFeatureData->ReleaseSelectionAccess( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method restores the rollback state of the model after you call DomeFeatureData::AccessSelections.
