---
title: "ModelDoc::SetBlockingState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetBlockingState.htm"
---

# ModelDoc::SetBlockingState

This method is obsolete and has been superseded by [ModelDoc2::SetBlockingState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetBlockingState.htm).

Description

This method sets the blocking state for the SolidWorks menus.

Syntax (OLE Automation)

(void) ModelDoc.SetBlockingState ( stateIn )

| Input: | (long) stateIn | One of the swBlockingStates_e options |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetBlockingState ( stateIn )

| Input: | (long) stateIn | One of the swBlockingStates_e options |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Reset the state when operations are completed by calling ModelDoc::ResetBlockingState.

NOTE: There must be a corresponding call to ModelDoc::ResetBlockingState for every call to ModelDoc::SetBlocking. It is not enough to call ModelDoc::ResetBlockingState once at the end of a sequence of operations that have called ModelDoc::SetBlockingState several times.
