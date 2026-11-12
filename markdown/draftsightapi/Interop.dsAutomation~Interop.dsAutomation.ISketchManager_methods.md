---
title: "ISketchManager Interface Methods"
project: ""
interface: "ISketchManager_methods"
member: ""
kind: "methods"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager_methods.html"
---

# ISketchManager Interface Methods

For a list of all members of this type, see [ISketchManager members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddTemporaryEntity | Inserts the specified temporary entity in the drawing. |
| Method | Align3DEntities | Aligns the specified entities in 3D space. |
| Method | AlignEntities1Point | Aligns the specified entities, without rotating them, using one pair of points. |
| Method | AlignEntities2Point | Aligns the specified entities, rotating them based on the current coordinate system, using two pairs of points. |
| Method | AlignEntities3Point | Aligns the specified entities using three pairs of points. |
| Method | AttachLinkToArea | Attaches the specified hyperlink to the specified rectangular area. |
| Method | BringAboveEntities | Moves the specified entities above the specified reference entities. |
| Method | BringToFrontEntities | Moves the specified entities to the top of the drawing order. |
| Method | ChamferEntities | Connects two sketch entities that meet in a beveled corner. |
| Method | ChamferPolyLine | Chamfers the specified 2D PolyLine. |
| Method | CopyEntities | Obsolete. Superseded by ISketchManager::CopyEntities2 . |
| Method | CopyEntities2 | Copies the specified entities, places the copies at the specified relative location, and returns the copies. |
| Method | CrossSectionEntitiesBy3Points | Cross sections the specified solid entities using the plane described by the specified points. |
| Method | CrossSectionEntitiesByEntity | Cross sections the specified solid entities using the specified 2D entities. |
| Method | CrossSectionEntitiesByView | Cross sections the specified solid entities at the specified point on the active view plane. |
| Method | CrossSectionEntitiesByXY | Cross sections the specified solid entities at the specified point on the XY plane. |
| Method | CrossSectionEntitiesByYZ | Cross sections the specified solid entities at the specified point on the YZ plane. |
| Method | CrossSectionEntitiesByZAxis | Cross sections the specified solid entities at the specified point on the section plane that is normal to the specified Z-axis. |
| Method | CrossSectionEntitiesByZX | Cross sections the specified solid entities at the specified point on the ZX plane. |
| Method | DetachDgnDefinition | Detaches the specified DGN definition from the drawing. |
| Method | DetachExternalReference | Detaches the specified external reference from the drawing. |
| Method | DetachImageDefinition | Detaches the specified image definition from the drawing. |
| Method | DetachPdfDefinition | Detaches the specified PDF definition from the drawing. |
| Method | DetachReferenceImage | Detaches the specified Referenced image from the drawing. |
| Method | ExplodeEntities | Explodes a complex object comprised of the specified entities. |
| Method | ExtendEntities | Extends the specified sketch entities. |
| Method | ExtrudeEntitiesToSolidByHeight | Extrudes the specified entities into a solid with the specified height and the specified angle of taper. |
| Method | ExtrudeEntitiesToSolidByPath | Extrudes the specified entities into a solid using the specified path entity and the specified angle of taper. |
| Method | ExtrudeEntitiesToSurfaceByHeight | Extrudes the specified entities into a surface with the specified height and the specified angle of taper. |
| Method | ExtrudeEntitiesToSurfaceByPath | Extrudes the specified entities into a surface using the specified path entity, the specified height, and the specified angle of taper. |
| Method | FilletEntities | Connects two entities with a fillet arc that is tangent to both entities. |
| Method | FilletPolyLine | Fillets the specified 2D PolyLine. |
| Method | FlatShotByExportToFile | Saves a 2D flattened representation of the current view's 3D solid objects and Regions to an external drawing file. |
| Method | FlatShotByInsertAsBlock | Inserts a 2D flattened representation of the current view's 3D solid objects and Regions to the specified Block in the graphics area. |
| Method | FlatShotByReplaceExistingBlock | Replaces an existing Block in the drawing with a new Block containing the 2D flattened representation of the current view's 3D solid objects and Regions. |
| Method | GetBoundingBox | Gets the bounding box enclosing the sketch entity. |
| Method | GetEntities | Get the specified entities and their types. |
| Method | GetObjectLayer | Gets the name of the Layer where the specified sketch entity resides. |
| Method | InsertAlignedDimension | Inserts an aligned linear Dimension. |
| Method | InsertAngularDimension2Line | Inserts an angular Dimension formed by two lines. |
| Method | InsertAngularDimension3Point | Inserts an angular Dimension formed by three points. |
| Method | InsertAngularDimensionArc | Inserts an angular Dimension formed by the two end points of an Arc. |
| Method | InsertArc | Constructs an Arc. |
| Method | InsertArcBy3Points | Constructs an Arc using the specified three points. |
| Method | InsertArcByCenter2Points | Obsolete. Superseded by ISketchManager::InsertArcByCenter2Points . |
| Method | InsertArcByCenter2Points2 | Constructs an Arc using the specified center, start, and end points. |
| Method | InsertArcLengthDimension | Gets access to an arc length Dimension. |
| Method | InsertArcLengthDimensionPartial | Gets access to a partial arc length Dimension. |
| Method | InsertAttributeDefinition | Obsolete. Superseded by ISketchManager::InsertAttributeDefinition2 . |
| Method | InsertAttributeDefinition2 | Creates a BlockAttribute definition. |
| Method | InsertBlock | Obsolete. Superseded by ISketchManager::InsertBlock2 . |
| Method | InsertBlock2 | Inserts a Block instance. |
| Method | InsertCircle | Constructs a Circle. |
| Method | InsertCircleBy3Points | Constructs a Circle using the specified three points. |
| Method | InsertCircleByDiameter | Constructs a Circle using the specified center point and diameter. |
| Method | InsertCurvedText | Inserts the specified text along the curve of the specified Arc. |
| Method | InsertDgn | Inserts a DGN image. |
| Method | InsertDiameterDimensionArc | Inserts a diameter dimension for an Arc. |
| Method | InsertDiameterDimensionCircle | Inserts a diameter dimension for a Circle. |
| Method | InsertEllipseArcDistanceToOtherAxis | Constructs an elliptical Arc using the specified axes end points, radius of the perpendicular axis, and start and end angles. |
| Method | InsertEllipseArcRotation | Constructs an elliptical Arc using the specified axes end points, angle of rotation, and start and end angles. |
| Method | InsertEllipseDistanceToOtherAxis | Constructs an Ellipse using the specified axes end points and the radius of the perpendicular axis. |
| Method | InsertEllipseRotation | Constructs an Ellipse using the specified axes end points and the angle of rotation. |
| Method | InsertEmbeddedObjectFromFile | Adds an embedded object to the document based on the specified file. |
| Method | InsertExternalReference | Inserts an external reference to a Block instance. |
| Method | InsertExternalReferenceWithReferenceType | Inserts an external reference to a Block instance with the specified reference type. |
| Method | InsertFace | Inserts a Face. |
| Method | InsertHatchByBoundary | Inserts a Hatch with the specified pattern, scale, angle, and boundary loop. |
| Method | InsertHatchByEntities | Inserts a Hatch with the specified pattern, scale, angle, and boundary defined by the specified entities. |
| Method | InsertHatchByInternalPoints | Inserts a Hatch with the specified pattern, scale, and angle in the enclosed areas defined by the specified internal points. |
| Method | InsertInfiniteLine | Constructs an InfiniteLine. |
| Method | InsertJoggedDimensionArc | Inserts a jogged Dimension for an Arc. |
| Method | InsertJoggedDimensionCircle | Inserts a jogged Dimension for an Circle. |
| Method | InsertLeader | Inserts a Leader. |
| Method | InsertLine | Constructs a Line. |
| Method | InsertLinearDimension | Inserts a linear Dimension. |
| Method | InsertMLeaderWithBlockContentType | Inserts an MLeader in the specified location with the specified Block name. |
| Method | InsertMLeaderWithNoneContentType | Inserts an MLeader in the specified location. |
| Method | InsertMLeaderWithNoteContentType | Inserts an MLeader in the specified location with the specified Note content. |
| Method | InsertMLeaderWithToleranceContentType | Inserts an MLeader in the specified location with the specified Tolerance content and attachment. |
| Method | InsertNote | Inserts a Note. |
| Method | InsertNoteWithParameters | Inserts and formats the Note as specified. |
| Method | InsertOrdinateDimension | Inserts an ordinate Dimension. |
| Method | InsertPdf | Inserts page images from a PDF. |
| Method | InsertPicture | Inserts a raster Referenced image. |
| Method | InsertPoint | Inserts a point. |
| Method | InsertPolyFaceMesh | Inserts a polygon face mesh. |
| Method | InsertPolygonMesh | Inserts a PolygonMesh with the specified MxN vertices at the specified coordinates. |
| Method | InsertPolyline2D | Constructs a 2D PolyLine. |
| Method | InsertPolyline3D | Constructs a 3D PolyLine. |
| Method | InsertRadialDimensionArc | Inserts a radius Dimension for an Arc. |
| Method | InsertRadialDimensionCircle | Inserts a radius Dimension for a Circle. |
| Method | InsertRay | Inserts a Ray. |
| Method | InsertRegion | Constructs a Region for each selected entity. |
| Method | InsertRichLine | Constructs a RichLine. |
| Method | InsertRotatedDimension | Inserts a rotated Dimension. |
| Method | InsertShape | Inserts a shape. |
| Method | InsertSimpleNote | Inserts a SimpleNote. |
| Method | InsertSolid | Inserts a 2D Solid, which are solid filled planes that have straight line borders, at the specified location. |
| Method | InsertSpline | Constructs a Spline. |
| Method | InsertTable | Inserts a Table. |
| Method | InsertTolerance | Inserts a geometric Tolerance. |
| Method | InsertTrace | Inserts a Trace, which is a 2D solid Line. |
| Method | IntersectEntities | Intersects the specified regions or 3D solids to create new regions or 3D solids. |
| Method | IsObjectErased | Gets whether the specified sketch entity is erased. |
| Method | IsObjectVisible | Gets whether the specified sketch entity is visible. |
| Method | LoftEntitiesToSolidByGuides | Creates a new Loft using the specified closed entities, profile guide lines, draft angles, and draft curvatures. |
| Method | LoftEntitiesToSolidByPath | Creates a new Loft using the specified closed entities, path curves, draft angles, and draft curvatures. |
| Method | LoftEntitiesToSurfaceByGuides | Creates a new lofted surface using the specified entities, profile guide lines, draft angles, and draft curvatures. |
| Method | LoftEntitiesToSurfaceByPath | Creates a new lofted surface using the specified entities, path curves, draft angles, and draft curvatures. |
| Method | Mirror3DEntities | Creates a mirror image of the specified entities in a 3D plane around a 3D axis. |
| Method | MirrorEntities | Mirrors the specified entities onto the opposite side of the specified mirror line. |
| Method | MoveEntities | Moves the specified sketch entities to the specified relative location. |
| Method | OffsetEntityByDistance | Copies the specified entity to a location at the specified distance. |
| Method | OffsetEntityByThroughPoint | Copies the specified entity through the specified point. |
| Method | Pattern3DCircular | Creates a pattern of the specified entities in 3D space in a circular alignment about a rotation axis. |
| Method | Pattern3DLinear | Creates a pattern of the specified entities in 3D space in a matrix of rows, columns, and levels. |
| Method | PatternCircular | Creates a circular pattern of the specified entities. |
| Method | PatternLinear | Creates a linear pattern of the specified entities |
| Method | PolysolidByCoordinates | Creates a PolySolid using the specified vertices, height, and width. |
| Method | PolysolidByEntities | Creates a PolySolid using the specified 2D entities, height, and width. |
| Method | PushPullEntities | Extrudes selected 2D open entities into surfaces or selected 2D closed entities into 3D solids. |
| Method | RevolveEntitiesToSolidByAxis | Revolves the specified entities into a solid using the specified axis and angle of revolution. |
| Method | RevolveEntitiesToSolidByObject | Revolves the specified entities into a solid using the specified axis and angle of revolution. |
| Method | RevolveEntitiesToSolidByXAxis | Revolves the specified entities into a solid using the specified X-axis and angle of revolution. |
| Method | RevolveEntitiesToSurfaceByAxis | Revolves the specified entities into a surface using the specified axis and angle of revolution. |
| Method | RevolveEntitiesToSurfaceByObject | Revolves the specified entities into a surface using the specified axis and angle of revolution. |
| Method | RevolveEntitiesToSurfaceByXAxis | Revolves the specified entities into a surface using the specified X-axis and angle of revolution. |
| Method | Rotate3DEntities | Rotates the specified entities in 3D space. |
| Method | RotateEntities | Rotates the specified entities. |
| Method | ScaleEntities | Scales the specified entities while keeping their proportions the same. |
| Method | SendToBackEntities | Moves the specified entities to the bottom of the drawing order. |
| Method | SendToUnderEntities | Moves the specified entities under the specified reference entities. |
| Method | SetObjectErased | Sets whether the specified sketch entity is erased. |
| Method | SetObjectLayer | Sets the specified Layer of the specified sketch entity. |
| Method | SetObjectVisible | Sets whether the specified sketch entity is visible. |
| Method | SliceEntitiesBy3Points | Slices the specified 3D entities using the plane defined by the three specified points. |
| Method | SliceEntitiesByPlanarEntity | Slices the specified 3D entities using the specified planar entity. |
| Method | SliceEntitiesBySurface | Slices the specified 3D entities using the specified surface entity. |
| Method | SliceEntitiesByView | Slices the specified 3D entities using the active view plane that contains the specified point. |
| Method | SliceEntitiesByXY | Slices the specified 3D entities using the XY plane that contains the specified point. |
| Method | SliceEntitiesByYZ | Slices the specified 3D entities using the YZ plane that contains the specified point. |
| Method | SliceEntitiesByZAxis | Slices the specified 3D entities using the section plane that contains the specified point and whose normal contain the specified point on the Z-axis. |
| Method | SliceEntitiesByZX | Slices the specified 3D entities using the ZX plane that contains the specified point. |
| Method | StartUndoRecord | Starts the undo recording of a set of sketch operations. |
| Method | StopUndoRecord | Stops the undo recording of a set of sketch operations. |
| Method | StretchEntities | Changes the relative positions of a sketch entity's nodes, retaining their relations to other nodes in the entity. |
| Method | SubtractEntities | Subtracts the specified Regions or 3D solids from other specified Regions or 3D solids to create a composite Region or a 3D solid. |
| Method | SweepEntitiesToSolid | Creates a swept solid using the specified 2D entities, closed sweep path, base point, scale, banking, and twist angle. |
| Method | SweepEntitiesToSurface | Creates a swept surface using the specified 2D entities, open sweep path, base point, scale, banking, and twist angle. |
| Method | TrimEntities | Trims the specified sketch entities. |
| Method | UnionEntities | Unites the specified Regions or 3D solids to create a composite Region or a 3D solid. |

[Top](#topBookmark)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
