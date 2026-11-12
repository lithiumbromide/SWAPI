# Drawing entities
Entities are created through a sketch manager (`IModel.GetSketchManager` for model space, `ISheet.GetSketchManager` for a layout) and changed through their own properties or through `IEntityHelper`, which works on any entity object. Units, angles, arrays and layer rules are in [correctness-rules.md](correctness-rules.md); this file maps tasks to members.
## Contents
- [Creating entities](#creating-entities)
- [Reading and changing entities](#reading-and-changing-entities)
- [Layers, colors, line styles and text styles](#layers-colors-line-styles-and-text-styles)
- [Blocks and attributes](#blocks-and-attributes)
- [Dimensions, hatches and tables](#dimensions-hatches-and-tables)
- [Selection and prompts](#selection-and-prompts)
- [Custom data and dictionaries](#custom-data-and-dictionaries)
- [3D entities](#3d-entities)
## Creating entities
| Entity | Member |
| --- | --- |
| Line, ray, infinite line, point | `ISketchManager.InsertLine`, `InsertRay`, `InsertInfiniteLine`, `InsertPoint` |
| Circle | `InsertCircle` (center and radius), `InsertCircleBy3Points`, `InsertCircleByDiameter` |
| Arc | `InsertArc` (center, radius, start and end angle in radians), `InsertArcBy3Points`, `InsertArcByCenter2Points2` |
| Ellipse and elliptical arc | `InsertEllipseDistanceToOtherAxis`, `InsertEllipseRotation`, `InsertEllipseArcDistanceToOtherAxis`, `InsertEllipseArcRotation` |
| 2D and 3D polyline | `InsertPolyline2D(CoordinateDblArray, Closed)` with `x1, y1, x2, y2, ...`; `InsertPolyline3D` with triples |
| Spline, rich line, trace, region | `InsertSpline`, `InsertRichLine`, `InsertTrace`, `InsertRegion` |
| Multi-line text (the MTEXT equivalent) | `InsertNote(X1, Y1, Z1, X2, Y2, Z2, StrArray)`; `InsertNoteWithParameters` sets style and size in one call |
| Single-line text | `InsertSimpleNote(StartX, StartY, StartZ, Height, Angle, Value)` |
| Leader and multileader | `InsertLeader`; `InsertMLeaderWithNoteContentType`, `InsertMLeaderWithBlockContentType` (2024 SP4) |
| Picture, PDF, DGN, external reference | `InsertPicture`, `InsertPdf`, `InsertDgn`, `InsertExternalReference` |

Each `Insert*` returns the new entity (`Line`, `Circle`, `PolyLine`, `Note`) or Nothing; set `Layer`, `Color`, `LineStyle` and `LineWeight` on the returned object. Find any other entity with `swapi.py find Insert --kind m` or `members ISketchManager --grep Insert`.
## Reading and changing entities
- All entities of a space: `ISketchManager.GetEntities(Filter, LayerNamesStrArray, out EntityTypeLongArray, out EntitiesArray)`. Pass the names of every layer to search (the examples collect them from `ILayerManager.GetLayers` and each `ILayer.Name`) and either Nothing for all types or a filter from `IDocument.GetSelectionManager().GetSelectionFilter()` after `Clear`, `AddEntityType(dsObjectType_e)` for each wanted type and `Active = True`. Cast each element by its `dsObjectType_e` (`dsLineType` to `Line`, `dsCircleType` to `Circle`).
- Geometry is read through the entity: `ICircle.GetCenter`, `ICircle.Radius`, `ILine.GetFirstPoint` and `GetSecondPoint`, `IPolyLine.GetVertexCoordinate` per vertex; check `members ICircle` for the rest.
- Move, copy, rotate, scale and mirror many entities at once: `ISketchManager.MoveEntities`, `CopyEntities2`, `RotateEntities`, `ScaleEntities`, `MirrorEntities`; the type and entity arrays must have the same length and order.
- Delete: set the entity's `Erased` property to True, or call `ISketchManager.SetObjectErased(Obj, True)` or `IEntityHelper.SetErased`.
- Generic access for any entity object: `IApplication.GetEntityHelper()` gives `GetLayer` and `SetLayer`, `GetColor` and `SetColor`, `GetErased` and `SetErased`, `GetVisible` and `SetVisible`, and `GetCustomData`.
- Bounding box of a whole space: `ISketchManager.GetBoundingBox`; of entities, their own `GetBoundingBox` members where they exist.
## Layers, colors, line styles and text styles
- Layers: `IDocument.GetLayerManager()`, then `GetLayer(Name)` or `CreateLayer(Name, out Layer, out dsCreateObjectResult_e)`, `GetLayers()` for all and `GetActiveLayer()` for the current one. `ILayer` has `Name` (read-only; use `Rename`), `Color`, `LineStyle`, `LineWeight`, `Frozen`, `Locked`, `Shown`, `Printable` and `Activate()`. Layer states: `IDocument.GetLayerStateManager` (2018).
- Colors: `IApplication.GetNamedColor(dsNamedColor_e)`, `GetColorByIndex(Index)` for an index in the standard colors, `GetRGBColor(Red, Green, Blue)`; assign the returned `Color` object. ByLayer and ByBlock are named colors in `dsNamedColor_e`.
- Line styles: `IDocument.GetLineStyleManager()`, `LoadLineStyle(Name, FileName, out LineStyle)` from a `.lin` file before assigning the name; `IApplication.GetLineStyleListFromFile` lists a file's styles.
- Text styles and dimension styles: `IDocument.GetTextStyleManager()` (`CreateTextStyle`, `GetTextStyle`), `IDocument.GetDimensionStyleManager()`; table styles through `GetTableStyleManager`.
## Blocks and attributes
- Define: `IDocument.CreateBlockDefinition(BlockName, Description, BasePointX, BasePointY, BasePointZ, EntityTypeLongArray, EntitiesArray, dsBlockDefinitionEntities_e)`; attribute definitions with `ISketchManager.InsertAttributeDefinition2`.
- Insert: `ISketchManager.InsertBlock2(BlockName, InsertX, InsertY, InsertZ, ScaleX, ScaleY, ScaleZ, Rotation)`; check `IDocument.HasBlockDefinition` first, because the block must exist in the drawing.
- Read: `IDocument.GetBlockDefinitions`, `GetBlockDefinition(Name)`; `IBlockInstance.GetBlockDefinition`, `GetAttributeInstances` then `IAttributeInstance.GetName` and `Value` to read or set title-block fields.
- Dynamic blocks: `swapi.py example "Modify Dynamic Block Instance Properties Example (C#)"`.
## Dimensions, hatches and tables
- Dimensions: `InsertAlignedDimension`, `InsertLinearDimension` (returns a rotated dimension), `InsertRotatedDimension`, `InsertAngularDimension2Line`, `InsertAngularDimension3Point`, `InsertRadialDimensionCircle`, `InsertDiameterDimensionCircle`, `InsertOrdinateDimension`, `InsertArcLengthDimension`, `InsertJoggedDimensionCircle`; each point is a `DblArray` triple (x, y, z), radial and diameter dimensions take the `Circle` or `CircleArc` itself, and every member takes a `DimensionTextOverride` string (empty for the measured value). Tolerances: `InsertTolerance`.
- Hatches: `InsertHatchByEntities(EntitiesArray, PatternName, PatternScale, PatternAngle)`, `InsertHatchByInternalPoints`, `InsertHatchByBoundary`; pattern names are those in the pattern file (`ANSI31`, `SOLID`).
- Tables: `ISketchManager.InsertTable(Left, Top, Rows, Columns, RowHeight, ColumnWidth, dsTableCellType_e, dsTableCellType_e, dsTableCellType_e)`, then `ITable.SetText` and the cell members of `ITable`.
## Selection and prompts
- Interactive selection: `IApplication.GetCommandMessage().PromptForSelection(SingleSelection, Prompt, ErrorMsg)`. It returns True when the prompt ran; the entities the user picked are then in the previous selection set, so read `ISelectionManager.GetSelectedObjectCount(dsSelectionSetType_Previous)` and `GetSelectedObject(dsSelectionSetType_Previous, index, out ObjType)` as the shipped Rotate and Copy Entities examples do. Indexes start at 0.
- What the user selected before running the macro: `dsSelectionSetType_Current`.
- Points, distances, strings and keywords: `PromptForPoint2`, `PromptForDistance`, `PromptForString`, `PromptForKeyword2`, `PromptForMouseOrKeyword2`; they return False (or a `dsPromptResultType_e`) when the user cancels, so stop cleanly.
- Feedback in the command window: `ICommandMessage.PrintLine`.
- Highlight without selecting: `IDocument.CreateHighlightSet`; rubber-band previews: `IApplication.CreateTracker` and `IDocument.AddPermanentTracker`.
## Custom data and dictionaries
- Extended entity data: get the entity's `ICustomData` with its `GetCustomData(ApplicationName)` (or `IEntityHelper.GetCustomData(Obj, ApplicationName)` for any object), change it, and write it back with the entity's `SetCustomData(ApplicationName, CustomData)`; see `swapi.py example "Add, Modify, and Remove Custom Data Example (C#)"`. `IDocument.GetRegisteredApplications` lists the application names in use.
- Drawing-level data: `IDocument.GetNamedObjectsDictionary()` returns the root `IDictionary`; nested dictionaries hold objects keyed by name (`swapi.py topic Dictionaries`).
- Document properties (title, author, custom properties): `IDocument.GetDrawingProperties()` and `IDrawingProperties.GetCustomProperty` and `SetCustomProperty`.
## 3D entities
Extrude, revolve, sweep, loft, slice, section, push-pull, boolean and polysolid members on `ISketchManager` (2020 and later) need DraftSight Premium or Enterprise Plus, as the Getting Started topic notes for 3D modeling. Each has a shipped example (`swapi.py examples Extruding`, `examples Revolving`). Entities passed to them are `DispatchWrapper[]` in .NET.
