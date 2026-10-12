---
title: "FeatureManager::InsertFillSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertFillSurface.htm"
---

# FeatureManager::InsertFillSurface

This method is obsolete and has been superseded by [FeatureManager::InsertFillSurface2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertFillSurface2.htm).

Description

This method inserts a fill-surface feature in the model.

Syntax (OLE Automation)

bRet = FeatureManager.InsertFillSurface ( resolution )

| Input: | (long) resolution | Controls the resolution or quality of the surface (see Remarks ) |
| --- | --- | --- |
| Output: | (LPFEATURE) bRet | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertFillSurface ( resolution, &bRet )

| Input: | (long) resolution | Controls the resolution or quality of the surface (see Remarks ) |
| --- | --- | --- |
| Output: | (LPFEATURE) bRet | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You must use ModelDocExtension::SelectByID2 and the following Mark values to select edges that bound the surface to be filled:

- Boundary curves = 1
- Boundary with contact curvature control = 257
- Boundary with tangent curvature control = 513
- Constraint curves or internal curves = 4

The resolution argument can be set to 1, 2, or 3. The higher the value, the better the resolution.

Use the Body2::Diagnose and the DiagnoseResult APIs to get the gaps to fill.
