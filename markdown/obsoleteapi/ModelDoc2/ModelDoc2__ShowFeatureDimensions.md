---
title: "ModelDoc2::ShowFeatureDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ShowFeatureDimensions.htm"
---

# ModelDoc2::ShowFeatureDimensions

This method is obsolete and has been superseded. Use [ModelDoc2::GetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceToggle.htm) or [ModelDoc2::SetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceToggle.htm) and swDisplayFeatureDimensions.

Description

This method displays all of the dimensions of the selected feature.

Syntax (OLE Automation)

void ModelDoc2.ShowFeatureDimensions ( )

Syntax (COM)

status = ModelDoc2->ShowFeatureDimensions ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method supports part and assembly documents; it does not affect drawing documents.
