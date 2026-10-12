---
title: "ModelDoc::SetBendState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_SetBendState.htm"
---

# ModelDoc::SetBendState

This method is obsolete and has been superseded by [ModelDoc2::SetBendState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetBendState.htm).

Description

This method sets the current state of a sheet metal part.

Syntax (OLE Automation)

retval = ModelDoc.SetBendState ( bendState )

| Input: | (long) bendState | Sheet metal state to set in this part |
| --- | --- | --- |
| Return: | (long) retval | Status of the set operation |

Syntax (COM)

status = ModelDoc->SetBendState ( bendState, &retval )

| Input: | (long) bendState | Sheet metal state to set in this part |
| --- | --- | --- |
| Output: | (long) retval | Status of the set operation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The bendState value that is passed in must be one of the values from the swSMBendState_e enumeration:

- swSMBendStateSharps the model is rolled back to before the first FlattenBends feature
- swSMBendStateFlattened the model is rolled back to just after a FlattenBends feature, but just before the corresponding ProcessBends feature
- swSMBendStateFolded the model is rolled back to just after a FlattenBends – ProcessBends feature pair.

The retval value will be one of the values from the swSMCommandStatus_e enumeration:

- swSMErrorNone
- swSMErrorUnknown
- swSMErrorNotAPart
- swSMErrorNotASheetMetalPart
- swSMErrorInvalidBendState

If a part with bend information is edited in context of the assembly (see AssemblyDoc::EditPart), the bend state for that part will be set.

If this method is run on a part without bend information, the part is not be affected and the retval is set to swSMErrorNotASheetMetalPart. If this methodis run on an assembly, the assembly isnot be affected and the retval is set to swSMErrorNotAPart. In both of these cases, the return status is S_FALSE (COM only).
