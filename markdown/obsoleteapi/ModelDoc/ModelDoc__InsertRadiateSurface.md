---
title: "ModelDoc::InsertRadiateSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRadiateSurface.htm"
---

# ModelDoc::InsertRadiateSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertRadiateSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertRadiateSurface.htm).

Description

This method creates a radiate surface based on the selections.

Syntax (OLE Automation)

void ModelDoc.InsertRadiateSurface( distance, flipDir, tangentPropagate )

| Input: | (double) distance | Distance to extend the surface |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction; by default the direction is out from the center of the face |
| Input: | (BOOL) tangentPropagate | TRUE to propagate the surface along tangent faces, FALSE limits the surface to the selected face. |

Syntax (COM)

status = ModelDoc->InsertRadiateSurface( distance, flipDir, tangentPropagate )

| Input: | (double) distance | Distance to extend the surface |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction; by default the direction is out from the center of the face |
| Input: | (BOOL) tangentPropagate | TRUE to propagate the surface along tangent faces, FALSE limits the surface to the selected face. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a Radiate Surface by selecting Insert, Reference Geometry, Radiate Surface. See SolidWorks Help for more information about what entities are valid for selection.

To use this method, make the selections using SelectByMark with mark of 2.
