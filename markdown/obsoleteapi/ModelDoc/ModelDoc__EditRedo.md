---
title: "ModelDoc::EditRedo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditRedo.htm"
---

# ModelDoc::EditRedo

This method is obsolete and has been superseded by [ModelDoc2::EditRedo](../ModelDoc2/ModelDoc2__EditRedo.htm).

Description

This method repeats a number of steps in the SolidWorks session.

Syntax (OLE Automation)

void ModelDoc.EditRedo ( nSteps)

| Input: | (ULONG) nSteps | Number of steps to repeat in the active SolidWorks session |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditRedo ( nSteps)

| Input: | (ULONG) nSteps | Number of steps to repeat in the active SolidWorks session |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method performs the same functionality as clicking Edit, Redo in the SolidWorks user interface.
