---
title: "ModelDoc2::HoleWizard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__HoleWizard.htm"
---

# ModelDoc2::HoleWizard

This method is obsolete and has been superseded by [FeatureManager::HoleWizard](sldworksAPI.chm::/FeatureManager/FeatureManager__HoleWizard.htm).

Description

This method invokes the hole wizard to create a new hole.

Syntax (OLE Automation)

void ModelDoc2.HoleWizard ( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12)

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type as defined in swEndConditions_e |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type |
| Input: | (double) d1 | Dimension value |
| Input: | (double) d12 | Dimension value |

Syntax (COM)

status = ModelDoc2->HoleWizard ( depth, endType, flip, dir, hType, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 )

| Input: | (double) depth | Depth in meters |
| --- | --- | --- |
| Input: | (short) endType | Termination type as defined in swEndConditions_e |
| Input: | (BOOL) flip | TRUE to flip cut, FALSE to not |
| Input: | (BOOL) dir | TRUE to flip direction of extrusion, FALSE to not |
| Input: | (long) hType | Hole type, see below |
| Input: | (double) d1 | Dimension value |
| Input: | (double) d12 | Dimension value |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The hType argument controls the type of hole that is created:

- 0 - Simple
- 1 - Tapered
- 2 - Counter Bore
- 3 - Counter Sunk
- 4 - Counter Drilled
- 5 - Simple Drilled
- 6 - Tapered Drilled
- 7 - C-Bored Drilled
- 8 - C-Sunk Drilled
- 9 - C-Drilled Drilled
