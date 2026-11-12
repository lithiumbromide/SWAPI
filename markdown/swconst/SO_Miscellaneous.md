---
title: "System Options > Miscellaneous"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Miscellaneous.htm"
---

# System Options > Miscellaneous

Some system-level enumerators exist in the SOLIDWORKS API that do not correspond to any of the options shown on the SOLIDWORKS Tools > Options > System Options dialogs. Click the links to jump to the tables in this topic containing these miscellaneous system-level enumerators.

NOTE: Unlinked text does not have any miscellaneous system-level enumerators. Unlinked text is shown to help you more easily map these miscellaneous system-level enumerators with the system options shown on the Tools > Options > System Options tab.

See [System Options and Document Properties](sldworksapiprogguide.chm::/Overview/System_Options_and_Document_Properties.htm) for details about system options and document properties.

| Miscellaneous System-level Enumerators |  |
| --- | --- |
| Related to categories on System Options tab | Not related to categories on System Options tab |
| General Drawings - Display Style - Area Hatch/Fill - Performance Colors Sketch - Relations/Snaps Display Selection Performance Assemblies External References Default Templates File Locations FeatureManager Spin Box Increments View Backup/Recover Hole Wizard/Toolbox File Explorer Search Collaboration Messages/Errors/Warnings Import Export | Bill of Materials Detailing Display States Large Assembly Mode PropertyManager Quick Tips Reference Triad Shaded Sketch Contours Viewpoint My SOLIDWORKS |

General

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swEditDesignTableInSeparateWindow | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEditDesignTableInSeparateWindow) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEditDesignTableInSeparateWindow, < OnFlag >) | Boolean value | Specifies whether to open Excel worksheet in Excel window or in SOLIDWORKS graphics view |
| swNotifySNLNotObtainedForEDrawingsSave | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swNotifySNLNotObtainedForEDrawingsSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swNotifySNLNotObtainedForEDrawingsSave, < OnFlag >) | Boolean value | Specifies whether to display message box each time eDrawings file saved |
| swUndoStepsMaximum | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUndoStepsMaximum) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUndoStepsMaximum, < Value >) | Integer value | Specifies the maximum number of Undo steps allowed; the higher the number, the more memory used |

[Back to top](#Top)

Drawings

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swAutomaticDrawingViewUpdateForceOff | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticDrawingViewUpdateForceOff) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticDrawingViewUpdateForceOff, < OnFlag >) | Boolean value | Specifies whether to automatically update drawing views |
| swDrawingAutomaticModelDimPlacement | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingAutomaticModelDimPlacement) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingAutomaticModelDimPlacement, < OnFlag >) | Boolean value | Specifies whether inserted dimensions are automatically placed at appropriate distance from geometry in view |
| swDrawingDefaultSheetScaleDenominator | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDefaultSheetScaleDenominator) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDefaultSheetScaleDenominator, < Value > ) | Double value | Specifies denominator for default drawing sheet scale |
| swDrawingDefaultSheetScaleNumerator | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDefaultSheetScaleNumerator) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingDefaultSheetScaleNumerator, < Value >) | Double value | Specifies numerator for default drawing sheet scale |
| swDrawingDisplayViewBorders | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayViewBorders) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingDisplayViewBorders, < OnFlag >) | Boolean value | Specifies whether borders are displayed around individual drawing views |
| swDynamicDrawingViewActivation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDynamicDrawingViewActivation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDynamicDrawingViewActivation, < OnFlag >) | Boolean value | Specifies whether the view closest to pointer is automatically activated |
| swDrawingPrintCrosshatchOutOfDateViews | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingPrintCrosshatchOutOfDateViews) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingPrintCrosshatchOutOfDateViews, swPromptAlwaysNever_e.< Value >) | See swPromptAlwaysNever_e for valid options | Specifies what happens when a drawing with out-of-date views is printed or print-previewed |
| swDrawingViewSmoothDynamicMotion | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewSmoothDynamicMotion) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingViewSmoothDynamicMotion, < OnFlag >) | Boolean value | Specifies whether dynamic operations, such as panning and zooming, display smoothly |

[Back to top](#Top)

Colors

NOTE: The input or output value is the corresponding [IColorTable](sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable.html) value unless otherwise specified.

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swSystemColorsActiveSelectionListBox | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsActiveSelectionListBox) ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsActiveSelectionListBox, <Value>) | Integer value | RGB value |
| swSystemColorsCrossHair | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsCrossHair) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsCrossHair, < Value >) | Integer value | RGB value |
| swSystemColorsDrawingsLockedFocus | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsLockedFocus) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsLockedFocus, < Value >) | Integer value | Border color; RGB value |
| swSystemColorsDrawingsSheetBorder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsSheetBorder) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsSheetBorder, < Value >) | Integer value | Drawing sheet border color; RGB value |
| swSystemColorsDrawingsViewBorder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsViewBorder) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsViewBorder, < Value >) | Integer value | View border color; RGB value |
| swSystemColorsNoteEditHandle | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNoteEditHandle) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNoteEditHandle, < Value >) | Integer value | RGB value |
| swSystemColorsNoteHandle | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNoteHandle) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNoteHandle, < Value >) | Integer value | RGB value |
| swSystemColorsTemporarySketchDragging | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporarySketchDragging) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporarySketchDragging, < Value >) | Integer value | RGB value |
| swSystemColorsTreeViewBackground | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTreeViewBackground) | Integer value | Read-only RGB value |
| swSystemColorsWeldPathSelection | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsWeldPathSelection) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsWeldPathSelection, < Value >) | Integer value | RGB value |

[Back to top](#Top)

Sketch

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Display virtual sharps | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayVirtualSharps) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayVirtualSharps, < OnFlag >) | Boolean value | Specifies whether to create sketch point at the virtual intersection point of two sketch entities |

[Back to top](#Top)

Display

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swDisplayMissingRefsWhenEditFeature | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayMissingRefsWhenEditFeature) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayMissingRefsWhenEditFeature, < OnFlag >) | Boolean value | Specifies whether to display missing references when editing features |
| swEdgesShadedEdgesDifferentColor | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesShadedEdgesDifferentColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesShadedEdgesDifferentColor, < OnFlag >) | Boolean value | Specifies whether to apply specified color to model edges when model is in Shaded With Edges mode |

[Back to top](#Top)

Performance

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swPerformanceDynamicUpdateOnMove | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceDynamicUpdateOnMove) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceDynamicUpdateOnMove, < OnFlag >) | Boolean value | Specifies whether to display feature preview while dragging entities of sketch |
| swPerformanceWin95ZoomClipping | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceWin95ZoomClipping) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPerformanceWin95ZoomClipping, < OnFlag >) | Boolean value | Valid for Windows ME only; specifies whether selected portion of model can be zoomed in on |
| swPerformanceViewsToDraftQuality | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceViewsToDraftQuality) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceViewsToDraftQuality, < Value >) | 0 = Prompt 1 = Always 2 = Never | Specifies whether to automatically convert drawing views to draft quality when unloading components |
| swRebuildOnActivation | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRebuildOnActivation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRebuildOnActivation, swRebuildOnActivation_e.< Value >) | See swRebuildOnActivation_e for valid options. |  |

[Back to top](#Top)

Assemblies

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swClearanceShowIgnored | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceShowIgnored) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceShowIgnored, < OnFlag >) | Boolean value | Specifies whether to show ignored clearances |
| swClearanceIgnoreEqual | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceIgnoreEqual) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceIgnoreEqual, < OnFlag >) | Boolean value | Specifies whether to ignore clearance equal to specified value |
| swClearanceSubAssyAsComp | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceSubAssyAsComp) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceSubAssyAsComp, < OnFlag >) | Boolean value | Specifies whether to treat subassemblies as components |
| swClearanceFasteners | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceFasteners) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceFasteners, < OnFlag >) | Boolean value | Specifies whether to create fasteners folder |
| swClearanceDisplayOption | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceDisplayOption) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swClearanceDisplayOption, < OnFlag >) | Boolean value | Specifies whether to make parts under study transparent |
| swIncontextFeatureHolderVisibility | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIncontextFeatureHolderVisibility) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIncontextFeatureHolderVisibility, < OnFlag >) | Boolean value | Specifies whether to hide or show all of the in-context icons |

[Back to top](#Top)

External References

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swWarnSavingReferencedDoc | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swWarnSavingReferencedDoc) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swWarnSavingReferencedDoc, < OnFlag >) | Boolean value | Specifies whether to display a warning when saving an assembly that references models that have been modified |

[Back to top](#Top)

File Locations

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swFileLocationsRouteCableLibrary | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteCableLibrary) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteCableLibrary, < Value >) | String value |  |
| swFileLocationsRouteComponentLibary | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteComponentLibary) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteComponentLibary, < Value >) | String value |  |
| swFileLocationsRouteCoveringLibrary | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteCoveringLibrary) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swFileLocationsRouteCoveringLibrary, < Value >) | String value |  |

[Back to top](#Top)

FeatureManager

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swFeatureManagerConfigTableFolderVisibility | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerConfigTableFolderVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerConfigTableFolderVisibility, swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| swFeatureManagerLightVisibility | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerLightVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerLightFolderVisibility, swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |

[Back to top](#Top)

View

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swInsertViewForNewDrawing | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swInsertViewForNewDrawing) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swInsertViewForNewDrawing, < OnFlag >) | Boolean value | Controls whether the Model View PropertyManager is automatically displayed when the user opens a new drawing |
| swViewShowAnnotationLinkErrors | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewShowAnnotationLinkErrors) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewShowAnnotationLinkErrors, < OnFlag >) | Boolean value | Specifies whether to show annotation link errors |
| swViewShowAnnotationLinkVariables | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewShowAnnotationLinkVariables) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewShowAnnotationLinkVariables, < OnFlag >) | Boolean value | Specifies whether to show annotation link variables |

[Back to top](#Top)

File Explorer

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swLockRecentDocumentsList | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLockRecentDocumentsList) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLockRecentDocumentsList, < OnFlag >) | Boolean value | Specifies whether to lock the recent documents list to prevent opened documents from being added to it |

[Back to top](#Top)

Collaboration

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swCollabTopDocsNoPromptOrSave | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabTopDocsNoPromptOrSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabTopDocsNoPromptOrSave, < OnFlag >) | Boolean value | Specifies to not prompt to save read-only referenced documents |

[Back to top](#Top)

Bill of Materials

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swBomConfigurationAlignBottom | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationAlignBottom) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationAlignBottom, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether to add new items to BOM by extending top border of table |
| swBOMConfigurationAnchorType | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMConfigurationAnchorType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMConfigurationAnchorType, swBOMConfigurationAnchorType_e.< Value >) | See swBOMConfigurationAnchorType_e for valid options |  |
| swBomConfigurationUseDocumentFont | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationUseDocumentFont) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationUseDocumentFont, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether to use document's note font when creating BOM |
| swBomConfigurationUseSummaryInfo | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationUseSummaryInfo) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBomConfigurationUseSummaryInfo, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether to use part identifier number in the title box of the Summary Info for the part number in the bill of materials |
| swBOMConfigurationWhatToShow | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMConfigurationWhatToShow) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMConfigurationWhatToShow, swBOMConfigurationWhatToShow_e.< Value >) | See See swBOMConfigurationWhatToShow_e for valid options for valid options |  |
| swBOMContentsDisplayAtTop | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMContentsDisplayAtTop) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMContentsDisplayAtTop, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether to show column headers at top of table |
| swBOMControlIDFromAssembly | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlIDFromAssembly) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlIDFromAssembly, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether row numbers follow assembly ordering |
| swBOMControlMissingRowDisplay | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMControlMissingRowDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMControlMissingRowDisplay, swBOMControlMissingRowDisplay_e.< Value >) | See swBOMControlMissingRowDisplay_e for valid options |  |
| swBOMControlMissingRows | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlMissingRows) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlMissingRows, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether rows for removed components are deleted from the table or displayed |
| swBOMControlSplitDirection | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMControlSplitDirection) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBOMControlSplitDirection, swBOMControlSplitDirection_e.< Value >) | See swBOMControlSplitDirection_e for valid options |  |
| swBOMControlSplitHeight | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swBOMControlSplitHeight) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swBOMControlSplitHeight, < Value >) | Double value | Specifies BOM table height before splitting it; applies to Excel-based BOM tables only |
| swBOMControlSplitTable | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlMissingRows) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBOMControlMissingRows, < OnFlag >) | Boolean value | For Excel-based BOMs only; specifies whether BOM table can be split as indicated by swUserPreferenceIntegerValue_e.swBOMControlSplitDirection and swUserPreferenceDoubleValue_e.swBOMControlSplitHeight |

[Back to top](#Top)

Detailing

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDetailingDimFontHeight | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDetailingDimFontHeight) | Double value in meters | Read-only; specifies height of dimensions |
| swDetailingNoteFontHeight | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.wDetailingNoteFontHeight) | Double value in meters | Read-only; specifies height of notes |

[Back to top](#Top)

Display States

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDisplayStateCreationChoice | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swDisplayStateCreationChoice ) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e. swDisplayStateCreationChoice , swDisplayStateCreationChoices_e.< Value >) | See swDisplayStateCreationChoices_e for valid options | Specifies which display states to preserve for documents that: have both SOLIDWORKS colors and PhotoWorks material display states were saved in SOLIDWORKS 2009 or earlier |

[Back to top](#Top)

Large Assembly Mode

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swLargeAsmModeAlwaysGenerateCurvature | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAlwaysGenerateCurvature) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAlwaysGenerateCurvature, < OnFlag >) | Boolean value | Specifies whether to always display curvatures for all shaded models |
| swLargeAsmModeAntiAliasEdgesFastMode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAntiAliasEdgesFastMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAntiAliasEdgesFastMode, < OnFlag >) | Boolean value | Specifies whether to set HLR edges in shaded and fast HLR/HLV modes to anti-alias |
| swLargeAsmModeAutoActvate | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeAutoActvate) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeAutoActvate, < Value >) | 0 = Prompt 1 = Always 2 = Never | In SOLIDWORKS 2006 and later, Prompt = Always |
| swLargeAsmModeAutoHideCompsDrawViewCreation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAutoHideCompsDrawViewCreation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeAutoHideCompsDrawViewCreation, < Value >) | Boolean value | Specifies whether to automatically hide components on view creation |
| swLargeAsmModeAutoRecoverCount | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeAutoRecoverCount) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeAutoRecoverCount, < Value >) | Integer value |  |
| swLargeAsmModeCheckOutOfDateLightweight | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeCheckOutOfDateLightweight) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeCheckOutOfDateLightweight, < Value >) | 0 = Do not check 1 = Indicate 2 = Always resolve |  |
| swLargeAsmModeDisplayModeForNewDrawViews | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeDisplayModeForNewDrawViews) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLargeAsmModeDisplayModeForNewDrawViews, < Value >) | 0 = Wireframe 1 = Hidden Lines Visible 2 = Hidden Lines Removed 3 = Shaded | To set new drawing views to shaded with edges when in large assembly mode, set this enumerator to Shaded and set ISldWorks::SetUserPreferenceToggle swUserPreferenceToggle_e.swLargeAsmModeDrawingHLREdgesWhenShaded to true. |
| swLargeAsmModeDrawingAutoLoadModels | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDrawingAutoLoadModels) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDrawingAutoLoadModels, < Value >) | Boolean value | Specifies whether to automatically load models for detached drawings |
| swLargeAsmModeDrawingHLREdgesWhenShaded | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDrawingHLREdgesWhenShaded) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDrawingHLREdgesWhenShaded, < Value >) | Boolean value | Specifies whether default display style is shaded with edges. NOTE : To set new drawing views to shaded with edges when in large assembly mode, set this enumerator to true and set ISldWorks::SetUserPreferenceIntegerValue swUserPreferenceIntegerValue_e.swLargeAsmModeDisplayModeForNewDrawViews to shaded. |
| swLargeAsmModeDynHighlightFeatureMgr | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDynHighlightFeatureMgr) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDynHighlightFeatureMgr, < Value >) | Boolean value | Specifies whether entities in graphics area are highlighted when moving pointer over them in FeatureManager design tree |
| swLargeAsmModeDynHighlightGraphicsView | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDynHighlightGraphicsView) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeDynHighlightGraphicsView, < Value >) | Boolean value | Specifies whether entities in the graphics area are highlighted when pointer is over them in graphics area |
| swLargeAsmModePreviewInsertComponents | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModePreviewInsertComponents) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModePreviewInsertComponents, < Value >) | Boolean value | Specifies whether to preview the assembly when inserting new components |
| swLargeAsmModeRemoveDetail | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeRemoveDetail) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeRemoveDetail, < Value >) | Boolean value | Specifies whether to remove details during zoom operations |
| swLargeAsmModeShadowsShadedMode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeShadowsShadedMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeShadowsShadedMode, < Value >) | Boolean value | Specifies whether to show shadows in shaded mode |
| swLargeAsmModeShowContentsDragDrawView | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeShowContentsDragDrawView) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeShowContentsDragDrawView, < Value >) | Boolean value | Specifies whether to show contents or view boundary while dragging drawing view |
| swLargeAsmModeSmoothDynamicMotionDrawView | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeSmoothDynamicMotionDrawView) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeSmoothDynamicMotionDrawView, < Value >) | Boolean value | Specifies whether to smoothly pan and zoom dynamic operations in drawing views |
| swLargeAsmModeTransparencyDynamicViewMode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeTransparencyDynamicViewMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeTransparencyDynamicViewMode, < Value >) | Boolean value | Specifies whether to use high quality transparency for dynamic view mode |
| swLargeAsmModeTransparencyNormalViewMode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeTransparencyNormalViewMode) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeTransparencyNormalViewMode, < Value >) | Boolean value | Specifies whether to use high quality transparency for normal view mode |
| swLargeAsmModeUpdateMassPropsOnSave | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeUpdateMassPropsOnSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLargeAsmModeUpdateMassPropsOnSave, < Value >) | Boolean value | Specifies whether to update mass properties when saving large assembly document |

[Back to top](#Top)

PropertyManager

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swPropertyManagerColorActiveClosedDivider | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorActiveClosedDivider) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorBackground | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorBackground) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColor_Divider | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColor_Divider) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorEditBox | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorEditBox) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColor_EditText | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColor_EditText) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorImportantMessage | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorImportantMessage) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorInnerBorder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorInnerBorder) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorLabelAndIcon | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorLabelAndIcon) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorTitle | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorTitle) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorOuterBorder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorOuterBorder) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorTopBorder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorTopBorder) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorDivider | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyManagerColorDivider) | Read-only integer value for RGB color in use |  |
| swPropertyMgrDockingState | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceInteger_e.swPropertyMgrDockingState) | See swPMContainer_e for valid options |  |

[Back to top](#Top)

Quick Tips

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swQuickTipsAssembly | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsAssembly) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsAssembly, < OnFlag >) | Boolean value | Specifies whether to enable or disable Quick Tips in assembly documents |
| swQuickTipsDrawing | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsDrawing) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsDrawing, < OnFlag >) | Boolean value | Specifies whether to enable or disable Quick Tips in drawing documents |
| swQuickTipsPart | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsPart) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swQuickTipsPart, < OnFlag >) | Boolean value | Specifies whether to enable or disable Quick Tips in part documents |

[Back to top](#Top)

Reference Triad

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swReferenceTriadUseAlternateLabel | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceTriadUseAlternateLabel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceTriadUseAlternateLabel, < OnFlag >) | Boolean value | Indicates whether alternate text should replace the reference triad's standard text of X , Y , and Z ; whenever you change this value, you must redraw the window to see the new text; use ISldWorks::SetUserPreferenceStringValue swUserPreferenceStringValue_e.swReferenceTriadXlabel, swUserPreferenceStringValue_e.swReferenceTriadYLabel, and swUserPreferenceStringValue_e.swReferenceTriadZLabel to specify the alternate text |
| swReferenceTriadXLabel | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadXLabel) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadXLabel, < Value >) | String value | Alternate text for the reference triad's standard text of X |
| swReferenceTriadYLabel | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadYLabel) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadYLabel, < Value >) | String value | Alternate text for the reference triad's standard text of Y |
| swReferenceTriadZLabel | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadZLabel) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swReferenceTriadZLabel, < Value >) | String value | Alternate text for the reference triad's standard text of Z |

NOTE: Use [ISldWorks::SetUserPreferenceToggle](sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)(swUserPreferenceToggle_e.swReferenceTriadUseAlternateLabels, <OnFlag> to indicate whether alternate text should replace the reference triad's standard text of X, Y, or Z. If swUserPreferenceToggle_e.swReferenceTriadUseAlernateLabels is true and swReferenceTriadXLabel, swReferenceTriadYLabel, or swReferenceTriadZLabel is blank, then the corresponding default text of X, Y, or Z is displayed.

[Back to top](#Top)

Shaded Sketch Contours

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swShadedSketchContours | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShadedSketchContours) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShadedSketchContours, < OnFlag >) | Boolean value | True to shade closed sketch contour areas, false to not |

[Back to top](#Top)

Viewpoint

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swViewpointPreserveNormals | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewpointPreserveNormals) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewpointPreserveNormals, < OnFlag >) | Boolean value | Specifies whether to preserve normals when saving document as Viewpoint file |

[Back to top](#Top)

My SolidWorks

| Enumerator | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swMySldSettings | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swMySldSettings) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swMySldSettings, < Value >) | String value |  |

[Back to top](#Top)
