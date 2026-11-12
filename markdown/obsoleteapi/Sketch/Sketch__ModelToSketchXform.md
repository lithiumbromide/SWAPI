---
title: "Sketch::ModelToSketchXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__ModelToSketchXform.htm"
---

# Sketch::ModelToSketchXform

This property is obsolete and has been superseded by [Sketch::ModelToSketchTransform](sldworksAPI.chm::/Sketch/Sketch__ModelToSketchTransform.htm).

Description

This property contains the model-to-sketch transform for the sketch member. As indicated by its name, this method allows you to go from the model to the sketch. For example, if you have a point located in model space coordinates, then you can multiply (Point x Matrix) to give you its coordinates in terms of this sketch.

Syntax (OLE Automation)

xform = Sketch.ModelToSketchXform (VB Get property)

xform = Sketch.GetModelToSketchXform ( ) (C++ Get property)

| Property: | (VARIANT) xform | VARIANT of type SafeArray of 13 doubles |
| --- | --- | --- |

Syntax (Com)

status = Sketch->get_IModelToSketchXform( xform )

| Property: | (double*) xform | Pointer to an array of 13 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The transform is returned as an array of 13 doubles. The first 9 are elements of 3x3 matrix, the next three define translation, and the last one is scaling.

This transformation matrix is returned in column-major order. For a description of a column-major type of matrix, see ModelView::Orientation2, which describes the layout of a 4x4 column-major matrix.

The portion of this matrix representing the translation vector should be interpreted in terms of sketch space. In other words, the translation is in relation to the XYZ coordinate system of the sketch.
