---
title: "ModelDoc::GetBlockingState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetBlockingState.htm"
---

# ModelDoc::GetBlockingState

This method is obsolete and has been superseded by [ModelDoc2::GetBlockingState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetBlockingState.htm).

Description

This method gets the current value of the SolidWorks blocking state within the

range of values accessible by ModelDoc2::SetBlockingState, for example, swFullBlock,

swModifyBlock, or swNoBlock.

Syntax (OLE Automation)

retval = ModelDoc.GetBlockingState ( )

| Return: | (long) retval | Value as defined in swBlockingStates_e |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetBlockingState ( &retval )

| Output: | (long) retval | Value as defined in swBlockingStates_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
