---
title: "SplitBodyFeatureData::State"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SplitBodyFeatureData/SplitBodyFeatureData__State.htm"
---

# SplitBodyFeatureData::State

This property is obsolete and has been superseded by [SpitBodyFeatureData::Consume](sldworksAPI.chm::/SplitBodyFeatureData/SplitBodyFeatureData__Consume.htm).

Description

This property gets the state of the resultant bodies of this split-body feature.

Syntax (OLE Automation)

*state = SplitBodyFeatureData.State (VB Get property)

SplitBodyFeatureData.State = state (VB Set property)

*state = SplitBodyFeatureData.GetState ( ) (C++ Get property)

SplitBodyFeatureData.SetState ( state ) (C++ Set property)

| Output: | (long ) *state | State as defined in swSplitBodyType_e |
| --- | --- | --- |

Syntax (COM)

status = SplitBodyFeatureData->get_State ( &state )

status = SplitBodyFeatureData->put_State ( state )

| Output: | (long ) *state | State as defined in swSplitBodyType_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
