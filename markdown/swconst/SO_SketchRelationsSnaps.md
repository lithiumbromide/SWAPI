---
title: "System Options > Sketch > Relations/Snaps"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_SketchRelationsSnaps.htm"
---

# System Options > Sketch > Relations/Snaps

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog, but are now obsolete and replaced by the specified system-level snap-related enumerator.

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Enable snapping | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchInference) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchInference, < OnFlag >) | Boolean value | Specifies whether to enable snapping |
| Snap to model geometry | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchInferFromModel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchInferFromModel, < OnFlag >) | Boolean value | Specifies whether to display inferencing lines that relate to lines and vertices of underlying model when sketching on face of extruded part |
| Automatic relations | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAutomaticRelations) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAutomaticRelations, < OnFlag >) | Boolean value | Specifies whether to automatically create geometric relations when adding sketch entities |
| Sketch Snaps - End points and sketch points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsPoints, < OnFlag >) | Boolean value | Specifies whether to snap to the end of the following sketch entities: lines, polygons, rectangles, parallelograms, fillets, arcs, parabolas, partial ellipses, splines, points, chamfers, and centerlines |
| Sketch Snaps - Center Points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsCenterPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsCenterPoints, < OnFlag >) | Boolean value | Specifies whether to snap to the center of the following sketch entities: circles, arcs, fillets, parabolas, and partial ellipses |
| Sketch Snaps - Mid-points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsMidPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsMidPoints, < OnFlag >) | Boolean value | Specifies whether to snap to the midpoints of lines, polygons, rectangles, parallelograms, fillets, arcs, parabolas, partial ellipses, splines, points, chamfers, and centerlines |
| Sketch Snaps - Quadrant Points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsQuadrantPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsQuadrantPoints, < OnFlag >) | Boolean value | Specifies whether to snap to the quadrants of circles, arcs, fillets, parabolas, ellipses, and partial ellipses |
| Sketch Snaps - Intersections | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsIntersections) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsIntersections, < OnFlag >) | Boolean value | Specifies whether to snap to the intersections of entities that meet or entities that intersect |
| Sketch Snaps - Nearest | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsNearest) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsNearest, < OnFlag >) | Boolean value | Specifies whether to support all entities; turn on to enable all snaps; your pointer does not need to be in the immediate vicinity of another sketch entity to show inference or snap to that point; turn off to enable snaps only when the pointer is in the vicinity of the snap point |
| Sketch Snaps - Tangent | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsTangent) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsTangent, < OnFlag >) | Boolean value | Specifies wither to snap to tangents on circles, arcs, fillets, parabolas, ellipses, partial ellipses, and splines |
| Sketch Snaps - Perpendicular | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsPerpendicular) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsPerpendicular, < OnFlag >) | Boolean value | Specifies whether to snap a line to another line |
| Sketch Snaps - Parallel | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsParallel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsParallel, < OnFlag >) | Boolean value | Specifies whether to create a parallel entity to lines |
| Sketch Snaps - Horizontal/vertical lines | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsHVLines) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsHVLines, < OnFlag >) | Boolean value | Specifies whether to snap a line vertically to an existing horizontal sketch line, and horizontally to an existing vertical sketch line |
| Sketch Snaps - Horizontal/vertical to points | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsHVPoints) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsHVPoints, < OnFlag >) | Boolean value | Specifies whether to snap a line vertically or horizontally to an existing sketch point |
| Sketch Snaps - Length | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsLength) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsLength, < OnFlag >) | Boolean value | Specifies whether to snap to lines to the increments that are set by the grid, without requiring display of the grid |
| Sketch Snaps - Grid | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsGrid) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsGrid, < OnFlag >) | Boolean value | Specifies whether to snap sketch entities to the grid's vertical and horizontal divisions; this is the only sketch snap that is not active by default; replaces the now obsolete document-level Boolean swSnapToPoints |
| Sketch Snaps - Snap only when grid is displayed | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapToGridIfDisplayed) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapToGridIfDisplayed, < OnFlag >) | Boolean value | Specifies whether to only snap to the grid when it is displayed; replaces the now obsolete document-level Boolean enumerator swSnapOnlyIfGridSplayed |
| Sketch Snaps - Angle | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsAngle) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchSnapsAngle, < OnFlag >) | Boolean value | Specifies whether to snap to angles; replaces the now obsolete document-level Boolean enumerator swSnapToAngle |
| Sketch Snaps - Snap angle | ISldWorks::GetUserPreferenceDoubleValue ( swUserPreferenceDoubleValue_e.swSketchSnapsAngleValue) ISldWorks::SetUserPreferenceDoubleValue ( swUserPreferenceDoubleValue_e.swSketchSnapsAngleValue, < Value >) | Double value | Specifies angle to which to snap; replaces the now obsolete document-level double enumerator swSnapToAngleValue |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swSnapOnlyIfGridDisplayed | Obsolete ; formerly a document-level Boolean enumerator that specified to snap to grid if swGridDisplay was turned on; replaced by the system-level Boolean swSketchSnapToGridIfDisplayed |
| swSnapToAngle | Obsolete ; formerly a document-level Boolean enumerator that specified whether sketched lines snap to predefined angle; replaced by the system-level Boolean swSketchSnapsAngle |
| swSnapToAngleValue | Obsolete ; formerly a document-level double enumerator that specified angle to which sketched lines should snap; double value; replaced by the system-level double enumerator swSketchSnapsAngleValue |
| swSnapToPoints | Obsolete ; formerly a document-level Boolean enumerator that specified whether points snap to grid; replaced by the system-level Boolean enumerator swSketchSnapsGrid |
