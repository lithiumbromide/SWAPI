---
title: "ModelDoc2::CreatePlaneAtAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtAngle.htm"
---

# ModelDoc2::CreatePlaneAtAngle

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtAngle2](ModelDoc2__CreatePlaneAtAngle2.htm).

Description

This method creates a construction (also called reference) plane at an angle from the selected plane along the selected edge.

Syntax (OLE Automation)

void ModelDoc2.CreatePlaneAtAngle ( val, flipDir)

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE for other way for first direction |

Syntax (COM)

status = ModelDoc2->CreatePlaneAtAngle ( val, flipDir )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE for other way for first direction |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
