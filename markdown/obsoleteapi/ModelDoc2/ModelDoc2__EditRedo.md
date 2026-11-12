---
title: "ModelDoc2::EditRedo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditRedo.htm"
---

# ModelDoc2::EditRedo

This method is obsolete and has been superseded by [ModelDoc2::EditRedo2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditUndo2.htm).

Description

This method repeats the specified number of actions in this SolidWorks session.

Syntax (OLE Automation)

void ModelDoc2.EditRedo ( nSteps)

| Input: | (ULONG) nSteps | Number of actions to repeat in this SolidWorks session |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->EditRedo ( nSteps)

| Input: | (ULONG) nSteps | Number of actions to repeat in the active SolidWorks session |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method mimics a user clicking Edit, Redo in the SolidWorks user interface.
