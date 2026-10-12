---
title: "IAnnotation Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IAnnotation_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_methods.html"
---

# IAnnotation Interface Methods

For a list of all members of this type, see [IAnnotation members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddOrUpdateStyle | Adds or updates the annotation linked to the specified style. |
| Method | ApplyDefaultStyleAttributes | Applies the default style attribute to this annotation. |
| Method | CanShowInAnnotationView | Gets whether this annotation can be shown in the specified annotation view . |
| Method | CanShowInMultipleAnnotationViews | Gets whether this annotation can be shown in multiple annotation views. |
| Method | CheckSpelling | Spell checks the text in this annotation. |
| Method | ConvertToMultiJog | Converts a note with a leader to a note with a multi-jog leader. |
| Method | DeleteStyle | Deletes the specified style. |
| Method | DeSelect | Deselects this annotation. |
| Method | GetArrowHeadCount | Gets the number of arrowheads on this symbol. |
| Method | GetArrowHeadSizeAtIndex | Gets the arrow head size of the specified leader on this annotation. |
| Method | GetArrowHeadStyleAtIndex | Gets the arrow head style of a specific leader on this annotation. |
| Method | GetAttachedEntities | Obsolete. Superseded by IAnnotation::GetAttachedEntities2 . |
| Method | GetAttachedEntities2 | Obsolete. Superseded by IAnnotation::GetAttachedEntities3 . |
| Method | GetAttachedEntities3 | Gets the entities to which this annotation is attached. |
| Method | GetAttachedEntityCount2 | Obsolete. Superseded by IAnnotation::GetAtatchedEntityCount3 . |
| Method | GetAttachedEntityCount3 | Gets the number of entities to which this annotation is attached. |
| Method | GetAttachedEntityTypes | Gets the types of entities attached to this annotation. |
| Method | GetBentLeader | Obsolete. Superseded by IAnnotation::GetLeaderStyle . |
| Method | GetDashedLeader | Gets whether this leader is a dashed line or a solid line. |
| Method | GetDimXpertFeature | Gets the DimXpert feature associated with this annotation. |
| Method | GetDimXpertName | Gets the DimXpert name for this annotation. |
| Method | GetDisplayData | Gets the display data for this annotation. |
| Method | GetFlipPlaneTransform | Gets the transformation matrix of the annotation plane in the opposite direction. |
| Method | GetLeader | Obsolete. Superseded by IAnnotation::GetLeaderStyle . |
| Method | GetLeaderAllAround | Gets the setting for all-around symbol display of this annotation. |
| Method | GetLeaderCount | Gets the number of leaders on this annotation. |
| Method | GetLeaderPerpendicular | Gets the perpendicular bent leader display setting for this annotation. |
| Method | GetLeaderPointsAtIndex | Gets coordinate information about a specified leader on this annotation. |
| Method | GetLeaderSide | Gets the leader attachment side setting for this annotation. |
| Method | GetLeaderStyle | Gets the style of this leader. |
| Method | GetMultiJogLeaderCount | Gets the number of multi-jog leaders on this annotation. |
| Method | GetMultiJogLeaders | Gets the multi-jog leaders on this annotation. |
| Method | GetName | Gets the name of this annotation. |
| Method | GetNext | Obsolete. Superseded by IAnnotation::GetNext3 . |
| Method | GetNext2 | Obsolete. Superseded by IAnnotation::GetNext3 . |
| Method | GetNext3 | Gets the next annotation. |
| Method | GetParagraphs | Gets the paragraphs in this note annotation. |
| Method | GetPlane | Gets the rotation matrix of the annotation relative to the X-Y plane of the model. |
| Method | GetPMIData | Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation. |
| Method | GetPMIType | Gets the type of Product and Manufacturing Information (PMI) associated with this STEP 242 annotation. |
| Method | GetPosition | Gets the position of this annotation. |
| Method | GetSmartArrowHeadStyle | Gets the setting for smart arrowhead style for this annotation. |
| Method | GetSpecificAnnotation | Gets the specific underlying object associated with this annotation. |
| Method | GetStyleName | Gets the name of the style applied to this annotation. |
| Method | GetTextFormat | Gets the text format for the specified text in this annotation. |
| Method | GetTextFormatCount | Gets the number of text formats for this annotation. |
| Method | GetType | Gets the type of the annotation. |
| Method | GetUseDocTextFormat | Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation. |
| Method | GetVisualProperties | Gets the visual properties of this annotation. |
| Method | IGetAttachedEntities | Obsolete. Superseded by IAnnotation::GetAttachedEntities2 . |
| Method | IGetAttachedEntityCount | Obsolete. Superseded by IAnnotation::GetAttachedEntityCount2 . |
| Method | IGetAttachedEntityTypes | Gets the types of all entities attached to this annotation. |
| Method | IGetDisplayData | Gets the display data for the annotation. |
| Method | IGetLeaderPointsAtIndex | Gets coordinate information about a specified leader on this annotation. |
| Method | IGetMultiJogLeaders | Gets the multi-jog leaders on this annotation. |
| Method | IGetNext | Obsolete. Superseded by IAnnotation::GetNext3 . |
| Method | IGetNext2 | Obsolete. Superseded by IAnnotation::GetNext3 . |
| Method | IGetPosition | Gets the position of this annotation. |
| Method | IGetSpecificAnnotation | Gets the specific underlying object associated with this annotation. |
| Method | IGetTextFormat | Gets the text format for the specified text in this annotation. |
| Method | IGetVisualProperties | Gets the visual properties of this annotation. |
| Method | IsDangling | Gets whether this annotation is dangling. |
| Method | IsDimXpert | Gets whether the annotation is a DimXpert annotation. |
| Method | ISetAttachedEntities | Attaches this annotation to the specified entities. |
| Method | ISetTextFormat | Sets the text format information for the specified text within this annotation. |
| Method | LoadStyle | Loads the specified style. |
| Method | SaveStyle | Saves the specified style. |
| Method | Select | Obsolete. Superseded by IAnnotation::Select3 . |
| Method | Select2 | Obsolete. Superseded by IAnnotation::Select3 . |
| Method | Select3 | Selects this annotation and marks it. |
| Method | SelectByMark | Obsolete. Superseded by IAnnotation::Select3 . |
| Method | SetArrowHeadSizeAtIndex | Sets the size of the arrow head of the specified leader on this annotation. |
| Method | SetArrowHeadStyleAtIndex | Sets the arrow head style of a specific leader on this annotation. |
| Method | SetAttachedEntities | Attaches this annotation to the specified entities. |
| Method | SetLeader | Obsolete. Superseded by IAnnotation::SetLeader3 . |
| Method | SetLeader2 | Obsolete. Superseded by IAnnotation::SetLeader3 . |
| Method | SetLeader3 | Sets the leader characteristics for this annotation. |
| Method | SetLeaderAttachmentPointAtIndex | Sets the specified attachment point of a leader for an annotation with the specified index. |
| Method | SetName | Sets the name of this annotation. |
| Method | SetPosition | Obsolete. Superseded by IAnnotation::SetPosition2 . |
| Method | SetPosition2 | Sets the position of this annotation. |
| Method | SetStyleName | Sets the style for this annotation. |
| Method | SetTextFormat | Sets the text format for the specified text in this annotation. |

[Top](#topBookmark)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::GetObjectId Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId.html)
