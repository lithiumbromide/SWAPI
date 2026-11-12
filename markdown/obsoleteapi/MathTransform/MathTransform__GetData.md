---
title: "MathTransform::GetData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MathTransform/MathTransform__GetData.htm"
---

# MathTransform::GetData

This method is obsolete and has been superseded by [MathTransform::GetData2](sldworksAPI.chm::/MathTransform/MathTransform__GetData2.htm).

Description

This method gets the math vectors and data that describe the transformation matrix object.

Syntax (OLE Automation)

MathTransform.GetData (xAxisObjOut, yAxisObjOut, zAxisObjOut, transformObjOut, scaleOut);

| Output: | (LPDISPATCH) *xAxisObjOut | Rotation about the X axis |
| --- | --- | --- |
| Output: | (LPDISPATCH) *yAxisObjOut | Rotation about the Y axis |
| Output: | (LPDISPATCH) *zAxisObjOut | Rotation about the Z axis |
| Output: | (LPDISPATCH) *transformObjOut | Transformation vector |
| Output: | (double) *scaleOut | Scale |

Syntax (COM)

status = MathTransform->IGetData ( xAxisObjOut, yAxisObjOut, zAxisObjOut, transformObjOut, scaleOut )

| Output: | (LPMATHVECTOR) *xAxisObjOut | Rotation about the X axis |
| --- | --- | --- |
| Output: | (LPMATHVECTOR) *yAxisObjOut | Rotation about the Y axis |
| Output: | (LPMATHVECTOR) *zAxisObjOut | Rotation about the Z axis |
| Output: | (LPMATHVECTOR) *transformObjOut | Transformation vector |
| Output: | (double) *scaleOut | Scale |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
