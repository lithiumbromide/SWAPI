---
title: "FeatureManager::InsertStructuralWeldment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertStructuralWeldment.htm"
---

# FeatureManager::InsertStructuralWeldment

This method is obsolete and has been superseded by [FeatureManager::InsertStructuralWeldment2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertStructuralWeldment2.htm).

Description

This method inserts a structural weldment feature using the selected sketch segment.

Syntax (OLE Automation)

retval = FeatureManager.InsertStructuralWeldment ( path, endCond, angle)

| Input: | (BSTR) path | Path, filename, and name of the type of structural member to insert |
| --- | --- | --- |
| Input: | (long) endCond | End condition as defined in swSolidWorksWeldmentEndCondOptions_e |
| Input: | (double) angle | Angle of rotation of the sketch about the sketch segment |
| Output: | (LPFEATURE*) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertStructuralWeldment ( path, endCond, angle, &retval)

| Input: | (BSTR) path | Path, filename, and name of the type of structural member to insert |
| --- | --- | --- |
| Input: | (long) endCond | End condition as defined in swSolidWorksWeldmentEndCondOptions_e |
| Input: | (double) angle | Angle of rotation of the sketch about the sketch segment |
| Output: | (LPFEATURE*) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
