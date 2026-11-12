---
title: "SimpleFilletFeatureData::PropagateToTangentFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__PropagateToTangentFaces.htm"
---

# SimpleFilletFeatureData::PropagateToTangentFaces

This property is obsolete and has been superseded by [SimpleFilletFeatureData2::PropagateToTangentFaces](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__PropagateToTangentFaces.htm).

Description

This property gets or sets whether to extend fillet to all faces tangent to the selected face or edge.

Syntax (OLE Automation)

propTgtFaces = SimpleFilletFeatureData.PropagateToTangentFaces (VB Get property)

SimpleFilletFeatureData.PropagateToTangentFaces = propTgtFaces (VB Set property)

propTgtFaces = SimpleFilletFeatureData.GetPropagateToTangentFaces ( ) (C++ Get property)

SimpleFilletFeatureData.SetPropagateToTangentFaces ( propTgtFaces ) (C++ Set property)

| Property: | ( BOOL ) propTgtFaces | TRUE if simple fillet feature should extend fillet to all faces tangent to the selected face or edge, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleFilletFeatureData ->get_PropagateToTangentFaces ( &propTgtFaces )

status = SimpleFilletFeatureData ->put_PropagateToTangentFaces ( propTgtFaces )

| Property: | ( VARIANT_BOOL ) propTgtFaces | TRUE if simple fillet feature should extend fillet to all faces tangent to the selected face or edge, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
