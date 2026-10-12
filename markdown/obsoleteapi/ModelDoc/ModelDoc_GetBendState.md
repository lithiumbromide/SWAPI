---
title: "ModelDoc::GetBendState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_GetBendState.htm"
---

# ModelDoc::GetBendState

This method is obsolete and has been superseded by [ModelDoc2::GetBendState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetBendState.htm).

Description

This method returns the current state of a sheet metal part.

Syntax (OLE Automation)

retval = ModelDoc.GetBendState ( )

| Return: | (long) retval | Current state of sheet metal bends in this part |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetBendState (&retval )

| Output: | (long) retval | Current state of sheet metal bends in this part |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The retval value is one of the values from the swSMBendState_e enumeration:

- swSMBendStateNone - model is not a sheet metal part
- swSMBendStateSharps - model is rolled back to before the first FlattenBends feature
- swSMBendStateFlattened - model is rolled back to just after a FlattenBends feature, but just before the corresponding ProcessBends feature
- swSMBendStateFolded - model is rolled back to just after a FlattenBends – ProcessBends feature pair.

If a part with bend information is being edited in context of the assembly (see AssemblyDoc::EditPart), then the bend state for that part is returned.

If this API is run on a part without bend information, or on an assembly directly, swSMBendStateNone is returned, and the return status is S_FALSE (COM only).
