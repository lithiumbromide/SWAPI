---
title: "ModelDoc2::CreatePlaneAtOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtOffset.htm"
---

# ModelDoc2::CreatePlaneAtOffset

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtOffset2](ModelDoc2__CreatePlaneAtOffset2.htm).

Description

This method creates a construction (also called a reference) plane at an offset from the selected plane or planar face.

Syntax (OLE Automation)

void ModelDoc2.CreatePlaneAtOffset ( val, flipDir)

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Determines the offset direction for the resulting plane |

Syntax (COM)

status = ModelDoc2->CreatePlaneAtOffset ( val, flipDir )

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Determines the offset direction for the resulting plane |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
