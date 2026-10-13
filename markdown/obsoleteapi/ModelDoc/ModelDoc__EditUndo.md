---
title: "ModelDoc::EditUndo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditUndo.htm"
---

# ModelDoc::EditUndo

This method is obsolete and has been superseded by [ModelDoc2::EditUndo](../ModelDoc2/ModelDoc2__EditUndo.htm).

Description

This method reverses a number of steps in the SolidWorks session. This method corresponds to the Edit, Undo commands in the user interface.

Syntax (OLE Automation)

void ModelDoc.EditUndo ( nSteps)

| Input: | (ULONG) nSteps | Number of steps to reverse in the active SolidWorks session |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditUndo ( nSteps)

| Input: | (ULONG) nSteps | Number of steps to reverse in the active SolidWorks session |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
