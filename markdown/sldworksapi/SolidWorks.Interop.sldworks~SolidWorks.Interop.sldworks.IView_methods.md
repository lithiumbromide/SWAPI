---
title: "IView Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IView_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_methods.html"
---

# IView Interface Methods

For a list of all members of this type, see[IView members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AlignDrawingView | Specifies the alignment of this auxiliary drawing view. |
| Method | AlignWithView | Sets view alignment. |
| Method | AutoInsertCenterMarks | Obsolete. Superseded by IView::AutoInsertCenterMarks2 . |
| Method | AutoInsertCenterMarks2 | Automatically inserts the specified center marks in this view. |
| Method | Crop | Obsolete. Superseded by IView::Crop2 . |
| Method | Crop2 | Crops this view using the selected closed sketch profile. |
| Method | EnumHiddenComponents | Obsolete. Superseded by IView::EnumHiddenComponents2 . |
| Method | EnumHiddenComponents2 | Gets the hidden components enumeration in this drawing view. |
| Method | EnumSectionLines | Obsolete. Superseded by IView::EnumSectionLines2 . |
| Method | EnumSectionLines2 | Gets the section lines enumeration in the view. |
| Method | GetAlignment | Gets the alignment information of this view. |
| Method | GetAnnotationCount | Gets the number of annotations in this view. |
| Method | GetAnnotations | Gets the annotations in this view. |
| Method | GetAnnotationsByType | Gets the annotations of the specified type in this view. |
| Method | GetArcCount | Gets the number of arcs in this view. |
| Method | GetArcs | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | GetArcs2 | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | GetArcs3 | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | GetArcs4 | Gets all of the information for all of the arcs added by a user in this drawing view. |
| Method | GetBaseView | Gets the base (parent) view used to create this view. |
| Method | GetBendLineCount | Gets the number of bendlines in a flat-pattern drawing view . |
| Method | GetBendLines | Gets the bendlines in a flat-pattern drawing view . |
| Method | GetBendNoteAttributeString | Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part. |
| Method | GetBendNoteTextFormat | Gets the text format of all bend notes in this drawing view of a sheet metal part. |
| Method | GetBodiesCount | Gets the number of bodies of a multibody part in the drawing view. |
| Method | GetBomTable | Gets the BOM table found in this drawing view. |
| Method | GetBreakLineCount | Obsolete. Superseded by IView::GetBreakLineCount2 . |
| Method | GetBreakLineCount2 | Gets the number of breaks lines and breaks in this view. |
| Method | GetBreakLineInfo | Obsolete. Superseded by IView::GetBreakLineInfo2 . |
| Method | GetBreakLineInfo2 | Gets information for all of the break lines in this view. |
| Method | GetBreakLines | Gets the all of the breaks in this view. |
| Method | GetBreakOutSectionCount | Gets the number of broken-out sections in this view. |
| Method | GetBreakOutSections | Gets all of the broken-out sections in this view. |
| Method | GetCenterLineCount | Gets the number of centerlines on this drawing view. |
| Method | GetCenterLines | Gets all of the centerline annotations on this drawing view. |
| Method | GetCenterLineSketch | Gets the sketch that contains all of the centerline information for this view. |
| Method | GetCenterMarkCount | Obsolete. Superseded by IView::GetCenterMarkCount2 . |
| Method | GetCenterMarkCount2 | Gets the number of center marks that are features in the view. |
| Method | GetCenterMarkInfo | Gets information about each center mark that is a feature in the view. |
| Method | GetCenterMarks | Gets all of the center marks that are features in the view. |
| Method | GetCorresponding | Gets the object in this drawing view that corresponds to the specified part or assembly object. |
| Method | GetCorrespondingEntity | Gets the entity in this drawing view that corresponds to the specified part or assembly entity. |
| Method | GetCThreadCount | Gets the number of cosmetic threads in this drawing view. |
| Method | GetCThreadQuality | Gets the cosmetic thread display quality in this view. |
| Method | GetCThreads | Gets all of the cosmetic threads on this drawing view. |
| Method | GetDatumOriginCount | Gets the number of datum origins on this drawing view. |
| Method | GetDatumOrigins | Gets all of the datum origins on this drawing view. |
| Method | GetDatumPoints | Obsolete. Superseded by IView::GetDatumPoints2 and IView::IGetDatumPoints2 . |
| Method | GetDatumPoints2 | Gets all of the information about all the datum points in this view. |
| Method | GetDatumPointsCount | Gets the number of datum points in this view. |
| Method | GetDatumTagCount | Gets the number of datum tags on this drawing view. |
| Method | GetDatumTags | Gets all of the datum tags on this drawing view. |
| Method | GetDatumTargetSymCount | Gets the number of datum target symbols on this drawing view. |
| Method | GetDatumTargetSyms | Gets all of the datum target symbols on this drawing view. |
| Method | GetDependentViewCount | Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view. |
| Method | GetDependentViews | Gets either all, or only the specified, dependent views in this view. |
| Method | GetDesignTableExtent | Gets the size and location of the design table associated with this drawing view. |
| Method | GetDetail | Gets the detail circle for this detail view. |
| Method | GetDetailCircleCount | Obsolete. Superseded by IView::GetDetailCircleCount2 . |
| Method | GetDetailCircleCount2 | Gets the number of detail circles in the drawing view. |
| Method | GetDetailCircleInfo | Obsolete. Superseded by IView::GetDetailCircleInfo2 and IView::IGetDetailCircleInfo2 . |
| Method | GetDetailCircleInfo2 | Gets all of the information about each detail circle in the view. |
| Method | GetDetailCircles | Gets the detail circles in this view. |
| Method | GetDetailCircleStrings | Gets an array of strings; each string represents the text label for a detail circle in this view. |
| Method | GetDimensionCount | Obsolete. Superseded by IView::GetDimensionCount4 . |
| Method | GetDimensionCount2 | Obsolete. Superseded by IView::GetDimensionCount4 . |
| Method | GetDimensionCount3 | Obsolete. Superseded by IView::GetDimensionCount4 . |
| Method | GetDimensionCount4 | Gets the number of display dimensions in the current drawing sheet or the current drawing view. |
| Method | GetDimensionDisplayInfo | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | GetDimensionDisplayInfo2 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | GetDimensionDisplayInfo3 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | GetDimensionDisplayInfo4 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | GetDimensionDisplayInfo5 | Gets the display dimension information for the current drawing sheet or the current drawing view. |
| Method | GetDimensionDisplayInfoSize | Obsolete. Superseded by IView::GetDimensionDisplayInfoSize2 . |
| Method | GetDimensionDisplayInfoSize2 | Gets the number of the dimension lines n the current drawing sheet or the current drawing view. |
| Method | GetDimensionDisplayString | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | GetDimensionDisplayString2 | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | GetDimensionDisplayString3 | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | GetDimensionDisplayString4 | Obsolete. Superseded by IView::GetDimensionDisplayString5 . |
| Method | GetDimensionDisplayString5 | Gets all of the dimension text in the current drawing sheet or the current drawing view. |
| Method | GetDimensionIds | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | GetDimensionIds2 | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | GetDimensionIds3 | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | GetDimensionIds4 | Gets the dimension names from the current drawing sheet or the current drawing view. |
| Method | GetDimensionInfo | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | GetDimensionInfo2 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | GetDimensionInfo3 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | GetDimensionInfo4 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | GetDimensionInfo5 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | GetDimensionInfo6 | Obsolete. Superseded by IView::GetDimensionInfo7 . |
| Method | GetDimensionInfo7 | Gets all of the dimension information in the current drawing sheet or the current drawing view. |
| Method | GetDimensionString | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | GetDimensionString2 | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | GetDimensionString3 | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | GetDimensionString4 | Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view. |
| Method | GetDisplayData | Obsolete. Superseded by IView::GetDisplayData3 and IView::IGetDisplayData3 . |
| Method | GetDisplayData2 | Obsolete. Superseded by IView::GetDisplayData3 and IView::IGetDisplayData3 . |
| Method | GetDisplayData3 | Obsolete. Superseded by IView::GetDisplayData4 . |
| Method | GetDisplayData4 | Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view. |
| Method | GetDisplayDimensionCount | Gets the number of display dimensions in this drawing view. |
| Method | GetDisplayDimensions | Gets all of the display dimension on this drawing view. |
| Method | GetDisplayEdgesInShadedMode | Gets whether to display the edges in this when the drawing view is in shaded mode. |
| Method | GetDisplayMode | Obsolete. Superseded by IView::GetDisplayMode2 . |
| Method | GetDisplayMode2 | Gets the current display mode of the view. |
| Method | GetDisplayTangentEdges | Obsolete. Superseded by IView::GetDisplayTangentEdges2 . |
| Method | GetDisplayTangentEdges2 | Gets the current tangent edge display mode of the drawing view. |
| Method | GetDowelSymbolCount | Gets the number of dowel symbols in this drawing view. |
| Method | GetDowelSymbols | Gets all of the dowel symbols on this drawing view. |
| Method | GetEllipseCount | Gets the number of ellipses in the view. |
| Method | GetEllipses | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | GetEllipses2 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | GetEllipses3 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | GetEllipses4 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | GetEllipses5 | Gets all of the ellipses added by a user in this drawing view. |
| Method | GetFaceHatchCount | Gets the number of face hatches in the view. |
| Method | GetFaceHatches | Gets the face hatches in the view. |
| Method | GetFacettedHlrDisplay | Gets whether HLR/HLV (Hidden Lines Removed/Hidden Lines Visible) edges should be displayed faceted in the view. |
| Method | GetFirstAnnotation | Obsolete. Superseded by IView::GetFirstAnnotation3 . |
| Method | GetFirstAnnotation2 | Obsolete. Superseded by IView::GetFirstAnnotation3 . |
| Method | GetFirstAnnotation3 | Gets the first annotation in this drawing view. |
| Method | GetFirstBlockInstance | Obsolete. Not superseded. |
| Method | GetFirstCenterLine | Gets the first centerline in this view. |
| Method | GetFirstCenterMark | Obsolete. Superseded by IView::GetFirstCenterMark2 . |
| Method | GetFirstCenterMark2 | Gets the first center mark in the view. |
| Method | GetFirstCenterOfMass | Gets the first center of mass in this view. |
| Method | GetFirstCThread | Gets the first cosmetic thread in the view. |
| Method | GetFirstCustomSymbol | Obsolete. Not superseded. |
| Method | GetFirstDatumOrigin | Gets the first datum origin in this drawing view. |
| Method | GetFirstDatumTag | Gets the first datum tag in the view. |
| Method | GetFirstDatumTargetSym | Gets the first datum target symbol in the view. |
| Method | GetFirstDisplayDimension | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | GetFirstDisplayDimension2 | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | GetFirstDisplayDimension3 | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | GetFirstDisplayDimension4 | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | GetFirstDisplayDimension5 | Obsolete. Superseded by IView::GetFirstDisplayDimension6 . |
| Method | GetFirstDisplayDimension6 | Gets the first display dimension in this drawing view. |
| Method | GetFirstDowelSymbol | Gets the first dowel symbol in the view. |
| Method | GetFirstGTOL | Gets the first geometric tolerance in this view. |
| Method | GetFirstMultiJogLeader | Obsolete. Superseded by IView::GetFirstMultiJogLeader2 . |
| Method | GetFirstMultiJogLeader2 | Gets the first multi-jog leader in the view. |
| Method | GetFirstNote | Obsolete. Superseded by IView::GetFirstNote2 . |
| Method | GetFirstNote2 | Gets the first note in the view. |
| Method | GetFirstRevisionCloud | Obsolete. Superseded by IView::GetFirstRevisionCloud2 . |
| Method | GetFirstRevisionCloud2 | Gets the first revision cloud annotation in this view. |
| Method | GetFirstSFSymbol | Gets the first surface-finish symbols in the view. |
| Method | GetFirstTableAnnotation | Obsolete. Superseded by IView::GetFirstTableAnnotation2 . |
| Method | GetFirstTableAnnotation2 | Gets the first table annotation in this view. |
| Method | GetFirstWeldBead | Gets the first weld bead annotation in this view. |
| Method | GetFirstWeldSymbol | Gets the first weld symbol in the view. |
| Method | GetGTolCount | Gets the number of geometric tolerances in this drawing view. |
| Method | GetGTols | Gets all of the geometric tolerances on this drawing view. |
| Method | GetHiddenComponents | Gets the hidden components in this drawing view. |
| Method | GetKeepLinkedToBOM | Gets whether this drawing view is linked to a BOM or weldment cut-list table. |
| Method | GetKeepLinkedToBOMName | Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked. |
| Method | GetLineCount | Obsolete. Superseded by IView::GetLineCount2 . |
| Method | GetLineCount2 | Gets the number of lines in this view with an option to include or exclude crosshatch lines. |
| Method | GetLines | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | GetLines2 | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | GetLines3 | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | GetLines4 | Gets all of the lines in the view with an option to include or exclude crosshatch lines. |
| Method | GetMirrorViewOrientation | Gets whether this view is mirrored. |
| Method | GetMultiJogLeaderCount | Gets the number of multi-jog leaders on this drawing view. |
| Method | GetMultiJogLeaders | Gets all of the multi-jog leaders in this drawing view. |
| Method | GetName2 | Gets the name of this drawing view displayed in the FeatureManager design tree. |
| Method | GetNextView | Gets the next drawing view in the drawing. |
| Method | GetNoteCount | Gets the number notes in this drawing view. |
| Method | GetNotes | Gets the notes in this drawing view. |
| Method | GetOrientationName | Gets the predefined name of this view. |
| Method | GetOutline | Gets the bounding box for a view (sheet or drawing) in meters on the drawing page. |
| Method | GetParabolaCount | Gets the number of parabolas in the view. |
| Method | GetParabolas | Obsolete. Superseded by IView::GetParabolas2 and IView::IGetParabolas2 . |
| Method | GetParabolas2 | Gets all of the information about all of the parabolas in this view. |
| Method | GetPolyLineCount | Obsolete. Superseded by IView::GetPolyLineCount5 . |
| Method | GetPolyLineCount2 | Obsolete. Superseded by IView::GetPolyLineCount5 . |
| Method | GetPolyLineCount3 | Obsolete. Superseded by IView::GetPolyLineCount5 . |
| Method | GetPolyLineCount4 | Obsolete. Superseded by IView::GetPolyLineCount5 . |
| Method | GetPolyLineCount5 | Gets the number of polylines in this view with an option to include or exclude crosshatch lines. |
| Method | GetPolylines | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | GetPolylines2 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | GetPolylines3 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | GetPolylines4 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | GetPolylines5 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | GetPolylines6 | Obsolete. Superseded by IView::GetPolylines7 . |
| Method | GetPolylines7 | Gets all of the polylines in the view with an option to include or exclude crosshatch lines. |
| Method | GetPolyLinesAndCurves | Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines. |
| Method | GetPolyLinesAndCurvesCount | Gets the number of lines, including arcs, ellipses, splines, and polylines, in the view with the option to include or exclude cross hatch lines. |
| Method | GetProjectionArrow | Gets the projection arrow for this projected view. |
| Method | GetProjectionLineCount | Gets the number of projection lines (arrows) in this drawing view. |
| Method | GetProjectionLines | Gets the projection lines (arrows) in this drawing view. |
| Method | GetReferencedModelName | Gets the name of the model that is referenced in the drawing view. |
| Method | GetRelatedTangentEdgeCount | Gets the number of visible tangent edges for the specified bendline in a flat-pattern drawing view . |
| Method | GetRelatedTangentEdges | Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view . |
| Method | GetRevisionCloudCount | Gets the number of revision cloud annotations in this view. |
| Method | GetRevisionClouds | Gets all of the revision cloud annotations in this view. |
| Method | GetSection | Gets the section for this section view. |
| Method | GetSectionLineCount | Obsolete. Superseded by IView::GetSectionLineCount2 . |
| Method | GetSectionLineCount2 | Gets the number of section lines in the view. |
| Method | GetSectionLineInfo | Obsolete. Superseded by IView::GetSectionLineInfo2 and IView::GetSectionLineInfo2 . |
| Method | GetSectionLineInfo2 | Gets all of the information about the section lines in the view. |
| Method | GetSectionLines | Gets the section lines in the view. |
| Method | GetSectionLineStrings | Gets an array of strings; each string represents the text label for a section line in this view. |
| Method | GetSFSymbolCount | Gets the number of surface finish symbols on this drawing view. |
| Method | GetSFSymbols | Gets all of the surface finish symbols in this drawing view. |
| Method | GetSketch | Gets the sketch used by this view. |
| Method | GetSketchPictureCount | Gets the number of sketch pictures imported to this view when a drawing is created from a part. |
| Method | GetSketchPictures | Gets all of the sketch pictures imported to this view when a drawing is created from a part. |
| Method | GetSMBoundaryBoxDisplayData | Obsolete. Superseded by IVew::GetSMBoundaryBoxDisplayData2 . |
| Method | GetSMBoundaryBoxDisplayData2 | Gets the boundary-box sketch display data of a flat-pattern drawing view. |
| Method | GetSolidHatchCount | Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data. |
| Method | GetSolidHatchInfo | Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view. |
| Method | GetSplineCount | Gets the number of splines in the view. |
| Method | GetSplines | Obsolete. Superseded by IView::GetSplines3 and IView::IGetSplines3 . |
| Method | GetSplines2 | Obsolete. Superseded by IView::GetSplines3 and IView::IGetSplines3 . |
| Method | GetSplines3 | Gets all of the splines added by a user in the drawing view. |
| Method | GetTableAnnotationCount | Gets the number of table annotations in this drawing view. |
| Method | GetTableAnnotations | Gets all of the table annotations on this drawing view. |
| Method | GetTemporaryAxes | Gets the information of the temporary axes displayed in this view. |
| Method | GetTemporaryAxesCount | Gets the number of temporary axes in this view. |
| Method | GetUniqueName | Gets the unique name of this section view. |
| Method | GetUseParentDisplayMode | Gets whether the view is using its parent settings or if it is using its own local settings. |
| Method | GetUserPoints | Obsolete. Superseded by IView::GetUserPoints2 and IView::IGetUserPoints2 . |
| Method | GetUserPoints2 | Gets all of the information about all of the user points in this view. |
| Method | GetUserPointsCount | Gets the number of user points in the view. |
| Method | GetViewXform | Gets the transform from model space origin to drawing space origin. |
| Method | GetVisible | Gets the visibility of this drawing view. |
| Method | GetVisibleComponentCount | Gets the number of visible components in this drawing view. |
| Method | GetVisibleComponents | Gets the visible components in this drawing view. |
| Method | GetVisibleDrawingComponents | Gets all of the unobscured drawing components in this drawing view of an assembly drawing. |
| Method | GetVisibleEntities | Obsolete. Superseded by IView::GetVisibleEntities2 . |
| Method | GetVisibleEntities2 | Gets the visible entities of the specified type for the specified component in this drawing view. |
| Method | GetVisibleEntityCount | Obsolete. Superseded by IView::GetVisibleEntityCount2 . |
| Method | GetVisibleEntityCount2 | Gets the number of visible entities of the specified type for the specified component in this drawing view. |
| Method | GetWeldBeadCount | Gets the number of weld beads on this drawing view. |
| Method | GetWeldBeads | Gets all of the weld beads on this drawing view. |
| Method | GetWeldSymbolCount | Gets the number of weld symbols on this drawing view. |
| Method | GetWeldSymbols | Gets all of the weld symbols on this drawing view. |
| Method | GetWitnessEntitiesCount | Gets the number of virtual sharp witness lines in this drawing view. |
| Method | GetWitnessGeomInfo | Gets the geometry data for all of the virtual sharp witness lines in this drawing view. |
| Method | GetXform | Gets the matrix used for displaying this drawing view. |
| Method | HasDesignTable | Gets whether this drawing view has a design table associated with it. |
| Method | IGetAnnotations | Gets the annotations in this view. |
| Method | IGetArcs | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | IGetArcs2 | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | IGetArcs3 | Obsolete. Superseded by IView::GetArcs4 and IView::IGetArcs4 . |
| Method | IGetArcs4 | Gets all of the information for all of the arcs added by a user in this drawing view. |
| Method | IGetBaseView | Gets the base (parent) view used to create this view. |
| Method | IGetBendLines | Gets the bendlines in a flat-pattern drawing view . |
| Method | IGetBodies | Gets the bodies of a multibody part in the drawing view. |
| Method | IGetBomTable | Gets the BOM table found in this drawing view. |
| Method | IGetBreakLineInfo | Obsolete. Superseded by IView::IGetBreakLineInfo2 . |
| Method | IGetBreakLineInfo2 | Gets information for all of the break lines in this view. |
| Method | IGetBreakLines | Gets the all of the breaks in this view. |
| Method | IGetBreakOutSections | Gets all of the broken-out sections in this view. |
| Method | IGetCenterLines | Gets all of the centerlines on this drawing view. |
| Method | IGetCenterMarkInfo | Gets information about each center mark that is a feature in the view. |
| Method | IGetCenterMarks | Gets all of the center marks that are features in the view. |
| Method | IGetCThreads | Gets all of the cosmetic threads on this drawing view. |
| Method | IGetDatumOrigins | Gets all of the datum origins on this drawing view. |
| Method | IGetDatumPoints | Obsolete. Superseded by IView::GetDatumPoints2 and IView::IGetDatumPoints2 . |
| Method | IGetDatumPoints2 | Gets all of the information about all the datum points in this view. |
| Method | IGetDatumTags | Gets all the datum tags on this drawing view. |
| Method | IGetDatumTargetSyms | Gets all of the datum target symbols on this drawing view. |
| Method | IGetDependentViews | Gets either all, or only the specified, dependent views in this view. |
| Method | IGetDesignTableExtent | Gets the size and location of the design table associated with this drawing view. |
| Method | IGetDetail | Gets the detail circle for this detail view. |
| Method | IGetDetailCircleInfo | Obsolete. Superseded by IView::GetDetailCircleInfo2 and IView::IGetDetailCircleInfo2 . |
| Method | IGetDetailCircleInfo2 | Gets all of the information about each detail circle in the view. |
| Method | IGetDetailCircles | Gets the detail circles in this view. |
| Method | IGetDetailCircleStrings | Gets an array of strings; each string represents the text label for a detail circle in this view. |
| Method | IGetDimensionDisplayInfo | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | IGetDimensionDisplayInfo2 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | IGetDimensionDisplayInfo3 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | IGetDimensionDisplayInfo4 | Obsolete. Superseded by IView::GetDimensionDisplayInfo5 and IView::IGetDimensionDisplayInfo5 . |
| Method | IGetDimensionDisplayInfo5 | Gets the display dimension information for the current drawing sheet or the current drawing view. |
| Method | IGetDimensionDisplayString | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | IGetDimensionDisplayString2 | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | IGetDimensionDisplayString3 | Obsolete. Superseded by IView::GetDimensionDisplayString4 and IView::IGetDimensionDisplayString4 . |
| Method | IGetDimensionDisplayString4 | Gets all of the dimension text in the current drawing sheet or the current drawing view. |
| Method | IGetDimensionIds | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | IGetDimensionIds2 | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | IGetDimensionIds3 | Obsolete. Superseded by IView::GetDimensionIds4 and IView::IGetDimensionIds4 . |
| Method | IGetDimensionIds4 | Gets the dimension names from the current drawing sheet or the current drawing view. |
| Method | IGetDimensionInfo | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | IGetDimensionInfo2 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | IGetDimensionInfo3 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | IGetDimensionInfo4 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | IGetDimensionInfo5 | Obsolete. Superseded by IView::GetDimensionInfo6 and IView::IGetDimensionInfo6 . |
| Method | IGetDimensionInfo6 | Obsolete. Superseded by IView::GetDimensionInfo7 . |
| Method | IGetDimensionString | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | IGetDimensionString2 | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | IGetDimensionString3 | Obsolete. Superseded by IView::GetDimensionString4 and IView::IGetDimensionString4 . |
| Method | IGetDimensionString4 | Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view. |
| Method | IGetDisplayData | Obsolete. Superseded by IView::GetDisplayData3 and IView::IGetDisplayData3 . |
| Method | IGetDisplayData2 | Obsolete. Superseded by IView::GetDisplayData3 and IView::IGetDisplayData3 . |
| Method | IGetDisplayData3 | Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view. |
| Method | IGetDisplayDimensions | Gets all of the display dimensions on this drawing view. |
| Method | IGetDowelSymbols | Gets all of the dowel symbols on this drawing view. |
| Method | IGetEllipses | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | IGetEllipses2 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | IGetEllipses3 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | IGetEllipses4 | Obsolete. Superseded by IView::GetEllipses5 and IView::IGetEllipses5 . |
| Method | IGetEllipses5 | Gets all of the ellipses added by a user in this drawing view. |
| Method | IGetFaceHatches | Gets the face hatches in the view. |
| Method | IGetFirstAnnotation | Obsolete. Superseded by IView::GetFirstAnnotation3 . |
| Method | IGetFirstAnnotation2 | Obsolete. Superseded by IView::GetFirstAnnotation3 . |
| Method | IGetFirstCenterOfMass | Gets the first center of mass in this view. |
| Method | IGetFirstCThread | Gets the first cosmetic thread in the view. |
| Method | IGetFirstCustomSymbol | Obsolete. Not superseded. |
| Method | IGetFirstDatumTag | Gets the first datum tag in the view. |
| Method | IGetFirstDatumTargetSym | Gets the first datum target symbol in the view. |
| Method | IGetFirstDisplayDimension | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | IGetFirstDisplayDimension2 | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | IGetFirstDisplayDimension3 | Obsolete. Superseded by IView::GetFirstDisplayDimension5 . |
| Method | IGetFirstDowelSymbol | Gets the first dowel symbol in the view. |
| Method | IGetFirstGTOL | Gets the first geometric tolerance in this view. |
| Method | IGetFirstMultiJogLeader | Gets the first multi-jog leader in the view. |
| Method | IGetFirstNote | Gets the first note in the view. |
| Method | IGetFirstRevisionCloud | Gets the first revision cloud annotation in this view. |
| Method | IGetFirstSFSymbol | Gets the first surface-finish symbols in the view. |
| Method | IGetFirstWeldSymbol | Gets the first weld symbol in the view. |
| Method | IGetGTols | Gets all of the geometric tolerances on this drawing view. |
| Method | IGetLines | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | IGetLines2 | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | IGetLines3 | Obsolete. Superseded by IView::GetLines4 and IView::IGetLines4 . |
| Method | IGetLines4 | Gets all of the lines in the view with an option to include or exclude crosshatch lines. |
| Method | IGetMultiJogLeaders | Gets all of the multi-jog leaders in this drawing view. |
| Method | IGetNextView | Gets the next drawing view in the drawing. |
| Method | IGetNotes | Gets the notes in this drawing view. |
| Method | IGetOutline | Gets the bounding box for a view (sheet or drawing) in meters on the drawing page. |
| Method | IGetParabolas | Obsolete. Superseded by IView::GetParabolas2 and IView::IGetParabolas2 . |
| Method | IGetParabolas2 | Gets all of the information about all of the parabolas in this view. |
| Method | IGetPolylines | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | IGetPolylines2 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | IGetPolylines3 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | IGetPolylines4 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | IGetPolylines5 | Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6 . |
| Method | IGetPolylines6 | Obsolete. Superseded by IView::IGetPolylines7 . |
| Method | IGetPolylines7 | Gets all of the polylines in the view with an option to include or exclude crosshatch lines |
| Method | IGetPolyLinesAndCurves | Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines. |
| Method | IGetProjectionArrow | Gets the projection arrow for this projected view. |
| Method | IGetProjectionLines | Gets the projection lines (arrows) in this drawing view. |
| Method | IGetRelatedTangentEdges | Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view . |
| Method | IGetRevisionClouds | Gets all of the revision cloud annotations in this view. |
| Method | IGetSection | Gets the section for this section view. |
| Method | IGetSectionLineInfo | Obsolete. Superseded by IView::GetSectionLineInfo2 and IView::GetSectionLineInfo2 . |
| Method | IGetSectionLineInfo2 | Gets all of the information about the section lines in the view. |
| Method | IGetSectionLines | Gets the section lines in the view. |
| Method | IGetSectionLineStrings | Gets an array of strings; each string represents the text label for a section line in this view. |
| Method | IGetSFSymbols | Gets all of the surface finish symbols in this drawing view. |
| Method | IGetSketch | Gets the sketch used by this view. |
| Method | IGetSketchPictures | Gets all of the sketch pictures imported to this view when a drawing is created from a part. |
| Method | IGetSMBoundaryBoxDisplayData | Gets the boundary-box sketch display data of a flat-pattern drawing view. |
| Method | IGetSolidHatchInfo | Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view. |
| Method | IGetSplines | Obsolete. Superseded by IView::GetSplines3 and IView::IGetSplines3 . |
| Method | IGetSplines2 | Obsolete. Superseded by IView::GetSplines3 and IView::IGetSplines3 . |
| Method | IGetSplines3 | Gets all of the splines added by a user in the drawing view. |
| Method | IGetTableAnnotations | Gets all of the table annotations in this drawing view. |
| Method | IGetTemporaryAxes | Gets the information of the temporary axes displayed in this view. |
| Method | IGetUserPoints | Obsolete. Superseded by IView::GetUserPoints2 and IView::IGetUserPoints2 . |
| Method | IGetUserPoints2 | Gets all of the information about all of the user points in this view. |
| Method | IGetViewXform | Gets the transform from model space origin to drawing space origin. |
| Method | IGetVisibleComponents | Gets the visible components in this drawing view. |
| Method | IGetVisibleEntities | Obsolete. Superseded by IView::IGetVisibleEntities2 . |
| Method | IGetVisibleEntities2 | Gets the visible entities of the specified type for the specified component in this drawing view. |
| Method | IGetWeldBeads | Gets all of the weld beads on this drawing view. |
| Method | IGetWeldSymbols | Gets all of the weld symbols on this drawing view. |
| Method | IGetWitnessGeomInfo | Gets the geometry data for all of the virtual sharp witness lines in this drawing view. |
| Method | IGetXform | Gets the matrix used for displaying this drawing view. |
| Method | IInsertBomTable | Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel. |
| Method | ImportAnnotations | Imports the specified annotations into this drawing view. |
| Method | InsertAlternateView | Inserts an Alternate Position View of the currently selected drawing view. |
| Method | InsertBendTable | Inserts a bend table for this drawing view. |
| Method | InsertBomTable | Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel. |
| Method | InsertBomTable2 | Obsolete. Superseded by IView::InsertBomTable3 . |
| Method | InsertBomTable3 | Obsolete. Superseded by IView::InsertBomTable4 . |
| Method | InsertBomTable4 | Obsolete. Superseded by IView::InsertBomTable5 . |
| Method | InsertBomTable5 | Obsolete. Superseded by IView::InsertBomTable6 . |
| Method | InsertBomTable6 | Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality. |
| Method | InsertBreak | Obsolete. Superseded by IView::InsertBreak2 . |
| Method | InsertBreak2 | Obsolete. Superseded by IView::InsertBreak3 . |
| Method | InsertBreak3 | Inserts the specified type of break at the specified location in this drawing view. |
| Method | InsertCutListPropertyNote | Inserts a note that contains all of the cut list item properties of a sheet metal part. |
| Method | InsertHoleTable | Obsolete. Superseded by IView::InsertHoleTable2 . |
| Method | InsertHoleTable2 | Obsolete. Superseded by IView::InsertHoleTable3 . |
| Method | InsertHoleTable3 | Inserts a hole table in this drawing view. |
| Method | InsertPunchTable | Inserts a punch table in the flat pattern drawing view of a sheet metal part. |
| Method | InsertViewAsBlock | Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet. |
| Method | InsertWeldmentTable | Inserts a weldment cut-list table into this drawing view. |
| Method | InsertWeldTable | Inserts a weld table into this drawing view. |
| Method | IsBroken | Gets whether the drawing view is displayed with a break. |
| Method | IsCropped | Get whether this drawing view is cropped. |
| Method | ISelectEntity | Selects an entity in this drawing view. |
| Method | ISetBodies | Sets the bodies of a multibody part to include in the view. |
| Method | ISetXform | Sets the matrix used for display of this drawing view. |
| Method | IsExploded | Gets whether the drawing view is currently showing the assembly as exploded or collasped. |
| Method | IsFlatPatternView | Gets whether a drawing view is a flat-pattern drawing view. |
| Method | IsLightweight | Gets whether the drawing view is lightweight. |
| Method | IsModelBreakState | Gets whether this drawing view is a Model Break View. |
| Method | IsModelLoaded | Gets whether the model is loaded in this drawing view. |
| Method | IsModelOutOfDate | Gets whether the model in this drawing view is up-to-date with the current model. |
| Method | IsPerspectiveView | Gets whether this drawing view is showing a perspective view of the model. |
| Method | LoadModel | Loads the model if the model has not already been loaded for this drawing view. |
| Method | MergeBendTags | Merges or unmerges bend tags in drawings of sheet metal parts. |
| Method | RemoveAlignment | Removes the alignment from this drawing view. |
| Method | ReplaceViewWithBlock | Converts this view into a sketch block with the specified manipulator location. |
| Method | ReplaceViewWithSketch | Converts this view into a sketch. |
| Method | ResetSketchVisibility | Resets the visibility of the sketches in the drawing view so that the drawing view reflects the model. |
| Method | SelectEntity | Selects an entity in this drawing view. |
| Method | SetBendNoteTextFormat | Sets the text format of all bend notes in this drawing view of a sheet metal part. |
| Method | SetDisplayMode | Obsolete. Superseded by IView::SetDisplayMode3 . |
| Method | SetDisplayMode2 | Obsolete. Superseded by IView::SetDisplayMode3 . |
| Method | SetDisplayMode3 | Obsolete. Superseded by IView::SetDisplayMode4 . |
| Method | SetDisplayMode4 | Sets the display mode of this drawing view. |
| Method | SetDisplayTangentEdges | Obsolete. Superseded by IView::SetDisplayTangentEdges2 . |
| Method | SetDisplayTangentEdges2 | Sets the tangent edge display mode of the drawing view. |
| Method | SetKeepLinkedToBOM | Sets whether this drawing view is linked to the specified BOM or weldment cut-list table. |
| Method | SetLightweightToResolved | Changes the drawing view from lightweight to resolved. |
| Method | SetMirrorViewOrientation | Sets whether to mirror this view. |
| Method | SetName2 | Sets the name of this drawing view, as displayed in the FeatureManager design tree. |
| Method | SetResolvedToLightweight | Changes the drawing view from resolved to lightweight. |
| Method | SetVisible | Sets the visibility of this drawing view. |
| Method | SetXform | Sets the matrix used for display of this drawing view. |
| Method | ShowExploded | Shows an exploded assembly in this drawing view. |
| Method | ShowModelBreakState | Sets whether to display the specified Model Break View. |
| Method | UpdateViewDisplayGeometry | Updates the displayed geometry for a drawing view. |
| Method | UseDefaultAlignment | Restores the default alignment for this drawing view. |

[Top](#topBookmark)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
