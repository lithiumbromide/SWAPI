---
title: "ModelDoc2::PreTrimSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__PreTrimSurface.htm"
---

# ModelDoc2::PreTrimSurface

This method is obsolete and has been superseded by [FeatureManager::PreTrimSurface](sldworksAPI.chm::/FeatureManager/FeatureManager__PreTrimSurface.htm).

Description

This method sets the Mutual trim option before trimming a surface.

Syntax (OLE Automation)

void ModelDoc2.PreTrimSurface ( bMutualTrimIn)

| Input: | (BOOL) bMutualTrimIn | TRUE to use the Mutual trim option, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->PreTrimSurface ( bMutualTrimIn )

| Input: | (VARIANT_BOOL) bMutualTrimIn | TRUE to use the Mutual trim option, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See SolidWorks Help for details about this option.
