---
title: "ModelDoc2::EditUndo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditUndo.htm"
---

# ModelDoc2::EditUndo

This method is obsolete and has been obsoleted by [ModelDoc2::EditUndo2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditUndo2.htm).

Description

This method undoes the specified number of actions in the active SolidWorks session.

Syntax (OLE Automation)

ModelDoc2.EditUndo ( nSteps )

| Input: | (ULONG) nSteps | Number of actions to undo in the active SolidWorks session |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->EditUndo ( nSteps )

| Input: | (ULONG) nSteps | Number of actions to undo in the active SolidWorks session |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
