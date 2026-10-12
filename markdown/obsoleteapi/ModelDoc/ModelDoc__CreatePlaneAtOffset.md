---
title: "ModelDoc::CreatePlaneAtOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtOffset.htm"
---

# ModelDoc::CreatePlaneAtOffset

This method is obsolete and has been superseded by [ModelDoc::CreatePlaneAtOffset2](ModelDoc__CreatePlaneAtOffset2.htm).

Description

This method creates a construction (reference) plane at an offset from the selected plane or planar face.

Syntax (OLE Automation)

void ModelDoc.CreatePlaneAtOffset ( val, flipDir)

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the offset direction for the resulting plane, FALSE to not |

Syntax (COM)

status = ModelDoc->CreatePlaneAtOffset ( val, flipDir )

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the offset direction for the resulting plane, FALSE to not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
