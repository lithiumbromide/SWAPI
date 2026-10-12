---
title: "ModelDoc::CreatePlaneAtAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtAngle.htm"
---

# ModelDoc::CreatePlaneAtAngle

This method is obsolete and has been superseded by [ModelDoc::CreatePlaneAtAngle2](ModelDoc__CreatePlaneAtAngle2.htm).

Description

This method creates a construction (reference) plane at an angle from the selected plane along the selected edge.

Syntax (OLE Automation)

void ModelDoc.CreatePlaneAtAngle ( val, flipDir)

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction away from the first direction |

Syntax (COM)

status = ModelDoc->CreatePlaneAtAngle ( val, flipDir )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction away from the first direction |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
