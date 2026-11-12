---
title: "ModelDoc::InsertSplitLineProject"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSplitLineProject.htm"
---

# ModelDoc::InsertSplitLineProject

This method is obsolete and has been superseded by [ModelDoc2::InsertSplitLineProject](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSplitLineProject.htm).

Description

This method split a face by projecting sketch lines onto the face.

Syntax (OLE Automation)

void ModelDoc.InsertSplitLineProject ( isDirectional, flipDir)

| Input: | (BOOL) isDirectional | Direction where: 0 = project in both directions 1 = project in one direction |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Used only when isDirectional = 1. Valid values are: 0 = project in the direction opposite to the normal of the sketch plane 1 = project in the direction along the normal of the sketch plane |

Syntax (COM)

status = ModelDoc->InsertSplitLineProject ( isDirectional, flipDir )

| Input: | (VARIANT_BOOL) isDirectional | Direction where: 0 = project in both directions 1 = project in one direction |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Used only when isDirectional = 1. Valid values are: 0 = project in the direction opposite to the normal of the sketch plane 1 = project in the direction along the normal of the sketch plane |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch must be selected and marked using SelectByMark or AndSelectByMark with a mark value of 4. The faces to be spilt must be selected and marked by SelectByMark or AndSelectByMark with a mark value of 8.
