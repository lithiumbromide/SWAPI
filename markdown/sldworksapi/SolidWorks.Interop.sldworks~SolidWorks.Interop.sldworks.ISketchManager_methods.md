---
title: "ISketchManager Interface Methods"
project: "SOLIDWORKS API Help"
interface: "ISketchManager_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_methods.html"
---

# ISketchManager Interface Methods

For a list of all members of this type, see [ISketchManager members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddAlongXDimension | Projects and displays along the x axis a dimension between selected points in a 3D sketch. |
| Method | AddAlongYDimension | Projects and displays along the y axis a dimension between selected points in a 3D sketch. |
| Method | AddAlongZDimension | Projects and displays along the z axis a dimension between selected points in a 3D sketch. |
| Method | ConvertEntities | Not implemented. Use ISketchManager::SketchUseEdge2 . |
| Method | Create3PointArc | Creates a 3-point arc. |
| Method | Create3PointCenterRectangle | Creates a 3-point center rectangle at any angle. |
| Method | Create3PointCornerRectangle | Creates a 3-point corner rectangle at any angle. |
| Method | CreateArc | Creates an arc based on a center point, a start point, an end point, and a direction. |
| Method | CreateBoundaryHatch | Creates area hatch/fill boundary hatches using closed sketch profiles. |
| Method | CreateCenterLine | Creates a center line between the specified points. |
| Method | CreateCenterRectangle | Creates a center rectangle. |
| Method | CreateChamfer | Creates a chamfer between two selected sketch entities. |
| Method | CreateCircle | Creates a circle based on a center point and a point on the circle. |
| Method | CreateCircleByRadius | Creates a circle based on a center point and a specified radius. |
| Method | CreateCircularSketchStepAndRepeat | Creates circular sketch pattern. |
| Method | CreateConic | Creates a conic curve in the active sketch. |
| Method | CreateConstructionGeometry | Sets selected sketch segments to be construction geometry instead of sketch geometry. |
| Method | CreateCornerRectangle | Creates a corner rectangle. |
| Method | CreateEllipse | Creates an ellipse using the specified center, major-axis, and minor-axis points. |
| Method | CreateEllipticalArc | Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points. |
| Method | CreateEquationSpline | Obsolete. Superseded by ISketchManager::CreateEquationSpline2 . |
| Method | CreateEquationSpline2 | Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve. |
| Method | CreateFillet | Creates a sketch fillet using the selected sketch entities. |
| Method | CreateLine | Creates a sketch line in the currently active 2D or 3D sketch. |
| Method | CreateLinearSketchStepAndRepeat | Creates a linear sketch pattern. |
| Method | CreateParabola | Creates a parabola in the active sketch. |
| Method | CreateParallelogram | Creates a parallelogram. |
| Method | CreatePoint | Creates a sketch point in the active 2D or 3D sketch. |
| Method | CreatePolygon | Creates a polygon in the active sketch. |
| Method | CreateRegionHatch | Creates an area hatch/fill region hatch using a closed sketch profile. |
| Method | CreateSketchBelt | Creates a sketch belt feature. |
| Method | CreateSketchPlane | Creates a 3D sketch plane. |
| Method | CreateSketchSlot | Creates a sketch slot. |
| Method | CreateSpline | Obsolete. Superseded by ISketchManager::CreateSpline2 . |
| Method | CreateSpline2 | Obsolete. Superseded by ISketchManager::CreateSpline3 . |
| Method | CreateSpline3 | Creates either a 2D spline or a spline constrained to a surface. |
| Method | CreateSplineByEqnParams | Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector. |
| Method | CreateSplineParamData | Creates an empty spline parameter data object. |
| Method | CreateSplinesByEqnParams | Obsolete. Superseded by ISketchManager::CreateSplinesByEqnParams2 . |
| Method | CreateSplinesByEqnParams2 | Creates one or more spline segments using the B-curve parameters provided. |
| Method | CreateTangentArc | Creates a tangent arc. |
| Method | EditCircularSketchStepAndRepeat | Edits a circular sketch pattern. |
| Method | EditLinearSketchStepAndRepeat | Edits a linear sketch pattern. |
| Method | EditSketchBlock | Puts the block definition in edit mode. |
| Method | EndEditSketchBlock | Saves or discards your edits of the block and then ends the current editing session of this block. |
| Method | ExplodeSketchBlockInstance | Explodes the specified block instance. |
| Method | FullyDefineSketch | Fully defines a sketch. |
| Method | GetDynamicMirror | Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled. |
| Method | GetSketchBlockDefinitionCount | Gets the number of block definitions in the model. |
| Method | GetSketchBlockDefinitions | Gets all of the block definitions. |
| Method | ICreateSpline | Obsolete. Superseded by ISketchManager::ICreateSpline2 . |
| Method | ICreateSpline2 | Creates a spline passing through the given points. |
| Method | ICreateSplineByEqnParams | Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector. |
| Method | ICreateSplinesByEqnParams | Creates one or more spline segments using the B-curve parameters provided. |
| Method | IGetSketchBlockDefinitions | Gets all of the block definitions. |
| Method | Insert3DSketch | Inserts a new 3D sketch in a model or closes the active sketch. |
| Method | InsertExplodeLineSketch | Inserts or closes an explode line sketch in an exploded view. |
| Method | InsertSketch | Inserts a new sketch in the current part or assembly document. |
| Method | InsertSketchBlockInstance | Inserts a block instance at the specified location using the block definition. |
| Method | InsertSketchPicture | Obsolete. Superseded by ISketchManager::InsertSketchPicture2 . |
| Method | InsertSketchPicture2 | Inserts a picture on the current drawing sketch. |
| Method | IntersectCurves | Creates a sketched intersection curve. |
| Method | MakeSketchBlockFromFile | Creates a block definition using the specified file. |
| Method | MakeSketchBlockFromSelected | Creates a block definition at the specified location from the selected entities. |
| Method | MakeSketchBlockFromSketch | Creates a block definition at the specified location using all of the sketch entities in the active sketch. |
| Method | MakeSketchChain | Creates a sketch path using the selected entities. |
| Method | PerimeterCircle | Draws a 3-point perimeter arc. |
| Method | ReverseEndPointTangent | Reverses the end point tangent direction of splines and arcs. |
| Method | RotateOrCopy3DAboutVector | Rotates, and optionally copies, the selected 3D sketch entities about the specified vector. |
| Method | RotateOrCopy3DAboutXYZ | Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates. |
| Method | SetDynamicMirror | Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline. |
| Method | SetGridOptions | Sets the options for the grid. |
| Method | SketchExtend | Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity. |
| Method | SketchOffset | Obsolete. Superseded by ISketchManager::SketchOffset2 . |
| Method | SketchOffset2 | Offsets the selected sketch entities. |
| Method | SketchReplace | Obsolete. Superseded by ISketchManager::SketchReplace2 . |
| Method | SketchReplace2 | Replaces a sketch entity in a model with another sketch entity, preserving all references. |
| Method | SketchTrim | Trims the selected sketch entities. |
| Method | SketchUseEdge | Obsolete. Superseded by ISketchManager::SketchUseEdge2 . |
| Method | SketchUseEdge2 | Obsolete. Superseded by ISketchManager::SketchUseEdge3 . |
| Method | SketchUseEdge3 | Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours. |
| Method | SplitClosedSegment | Splits the selected closed sketch segment into two sketch segments. |
| Method | SplitOpenSegment | Splits the selected open sketch segment into two sketch segments. |

[Top](#topBookmark)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
