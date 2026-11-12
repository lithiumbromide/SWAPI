---
title: "ModelDoc::ResetBlockingState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ResetBlockingState.htm"
---

# ModelDoc::ResetBlockingState

This method is obsolete and has been superseded by [ModelDoc2::ResetBlockingState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ResetBlockingState.htm).

Description

This method resets the blocking state for the SolidWorks menus.

Syntax (OLE Automation)

(void) ModelDoc.ResetBlockingState ( )

Syntax (COM)

status = ModelDoc->ResetBlockingState ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method should be called after ModelDoc::SetBlockingState to set the SolidWorks menus back to their previous state.

NOTE: There must be a corresponding call to this method for every call to ModelDoc::SetBlocking state. It is not enough to call this method once at the end of a sequence of operations that have called ModelDoc::SetBlockingState several times.
