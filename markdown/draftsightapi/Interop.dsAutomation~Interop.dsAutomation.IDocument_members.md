---
title: "IDocument Interface Members"
project: ""
interface: "IDocument_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html"
---

# IDocument Interface Members

The following tables list the members exposed by [IDocument](Interop.dsAutomation~Interop.dsAutomation.IDocument.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoUpdateAttributeReferences | Gets or sets whether to update all existing block attribute references in the document with changes. |
| Property | DimensionScale | Gets or sets the scale factor based on the ratio between the current Viewport and the drawing Sheet. |
| Property | Is3DExperienceFile | Gets or sets whether this is a 3DEXPERIENCE file. |
| Property | ScaleUnit | Gets or sets the scale factor for DimensionStyle settings. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Activate | Activates the document. |
| Method | AddPermanentTracker | Adds a permanent tracker to this document. |
| Method | AllowVeto | Sets whether to abort a command operation. |
| Method | Clean | Purges this document of the objects that are defined or loaded but not used. |
| Method | CopySheet | Creates a new Sheet by copying the specified existing Sheet. |
| Method | CreateBlockDefinition | Creates a Block definition. |
| Method | CreateGroup | Creates an EntityGroup, which combines the specified entities into a group that you can manipulate in a single operation. |
| Method | CreateHighlightSet | Creates a highlight selection set containing the specified entities. |
| Method | CreateLispFunction | Creates a LISP function that can be called from LISP. |
| Method | CreateSheet | Creates a Sheet using the specified name. |
| Method | CreateSheetByTemplate | Creates a Sheet based on a Sheet in another file. |
| Method | ErrorCheck | Checks the integrity of this document and optionally corrects errors. |
| Method | GetAngleUnitExpression | Gets the type of angular unit and its precision for the document. |
| Method | GetBaseAngle | Gets the base angle for the document. |
| Method | GetBlockDefinition | Gets the specified Block definition for the document. |
| Method | GetBlockDefinitions | Gets the Block definitions for the document. |
| Method | GetCommandOptionBool | Gets the Boolean value of the specified command option for the document. |
| Method | GetCommandOptionDouble | Gets the double value of the specified command option for the document. |
| Method | GetCommandOptionInt16 | Gets the 16-bit signed integer, also called Int16, value of the specified command option for the document. |
| Method | GetCommandOptionInt32 | Gets the 32-bit signed integer, also called Int32, value of the specified command option for the document. |
| Method | GetCommandOptionInt8 | Gets the 8-bit signed integer, also called Int8, value of the specified command option for the document. |
| Method | GetCommandOptionPoint2D | Gets the 2D point's coordinates for the specified command option in the document. |
| Method | GetCommandOptionPoint3D | Gets the 3D point's coordinates for the specified command option in the document. |
| Method | GetCommandOptionString | Gets the string value for the specified command option in the document. |
| Method | GetCustomCoordinateSystemManager | Creates a new instance of the custom coordinate system manager. |
| Method | GetDimensionStyleManager | Gets the DimensionStyle Manager. |
| Method | GetDocumentExporter | Gets the export feature for the document. |
| Method | GetDrawingProperties | Gets access to the standard (i.e., author, keywords, title, and subject) and custom properties of a drawing document. |
| Method | GetExternalReferences | Gets all external references for this document. |
| Method | GetGroup | Gets the specified EntityGroup, which contains entities that have been combined into a group that you can manipulate in a single operation. |
| Method | GetGroups | Gets the specified EntityGroups. |
| Method | GetHandleFromObject | Gets the handle of the specified object. |
| Method | GetImmediateChildReferences | Gets the immediate child external references for this document. |
| Method | GetLayerManager | Gets the Layer Manager for the document. |
| Method | GetLayerStateManager | Accesses the Layer State Manager of this document. |
| Method | GetLengthUnitExpression | Gets the type of linear unit and its precision for the document. |
| Method | GetLineStyleManager | Gets the LineStyle Manager. |
| Method | GetModel | Gets the model for the document. |
| Method | GetNamedObjectsDictionary | Gets the named-objects dictionary for the drawing. |
| Method | GetObjectByHandle | Gets an object by its handle. |
| Method | GetPathName | Gets the path and file name of the document. |
| Method | GetRegisteredApplications | Gets the names of the registered applications for the document's custom data . |
| Method | GetRichLineStyleManager | Gets the RichLineStyle Manager. |
| Method | GetSelectionManager | Gets the interface for selecting entities, which makes the currently and previously selected entity available. |
| Method | GetShapeManager | Gets the Shape Manager. |
| Method | GetSheet | Gets the specified Sheet. |
| Method | GetSheets | Obsolete. Superseded by IDocument::GetSheets2 . |
| Method | GetSheets2 | Gets the Sheets for the document. |
| Method | GetTableStyleManager | Gets the TableStyle Manager. |
| Method | GetTextStyleManager | Gets the TextStyle Manager. |
| Method | GetViewManager | Gets the View Manager. |
| Method | GetWindow | Gets the DraftSight document window. |
| Method | HasBlockDefinition | Gets whether the specified Block definition is inserted in the document. |
| Method | HasSheet | Gets whether the document contains the specified Sheet . |
| Method | IsActive | Gets whether the document is active. |
| Method | IsDirty | Gets whether the document has been modified since it was opened and not saved. |
| Method | IsReadOnly | Gets whether the document is read only. |
| Method | Pan | Moves the visible portion of the drawing in the direction and distance defined through a vector. |
| Method | Rebuild | Rebuilds the document. |
| Method | RemoveLispFunction | Removes the specified LISP function so that it can no longer be called from LISP. |
| Method | RemovePermanentTracker | Removes the specified permanent tracker. |
| Method | RemoveSheet | Deletes the specified Sheet from the document. |
| Method | Save | Saves the document. |
| Method | SaveAs | Obsoleted. Superseded by IDocument::SaveAs2 . |
| Method | SaveAs2 | Saves the document as the specified file name and file type. |
| Method | SetAngleUnitExpression | Sets the type of angular unit and its precision for the document. |
| Method | SetBaseAngle | Sets the base angle for the document. |
| Method | SetCommandOptionBool | Sets the Boolean value for the specified command option for the document. |
| Method | SetCommandOptionDouble | Sets the double value for the specified command option for the document. |
| Method | SetCommandOptionInt16 | Sets the 16-bit signed integer, also called Int16, value for the specified command option for the document. |
| Method | SetCommandOptionInt32 | Sets the 32-bit signed integer, also called Int32, value for the specified command option for the document. |
| Method | SetCommandOptionInt8 | Sets the 8-bit signed integer, also called Int8, value for the specified command option for the document. |
| Method | SetCommandOptionPoint2D | Sets the command option for the specified 2D point in the document. |
| Method | SetCommandOptionPoint3D | Sets the command option for the specified 3D point in the document. |
| Method | SetCommandOptionString | Sets the string value for the specified command option in the document. |
| Method | SetDirty | Modifies this document so it can be saved. |
| Method | SetLengthUnitExpression | Sets the type of linear unit and its precision for the document. |
| Method | WriteBlockByAllEntities | Saves this entire drawing to a new drawing file. |
| Method | WriteBlockByName | Saves the specified Block in this drawing to a new drawing file. |
| Method | WriteBlockBySpecifiedEntities | Saves the specified entities in this drawing to a new drawing file. |

[Top](#topBookmark)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument Event DestroyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DestroyNotifyEventHandler.html)
[IDocument Event FileSavePostNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePostNotifyEventHandler.html)
[IDocument Event FileSavePreNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_FileSavePreNotifyEventHandler.html)
[IDocument Event ModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ModifyNotifyEventHandler.html)
