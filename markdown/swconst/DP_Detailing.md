---
title: "Document Properties > Detailing"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Detailing.htm"
---

# Document Properties > Detailing

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

For drawings:

For parts and assemblies:

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Display filter - Cosmetic threads | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayCosmeticThreads,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayCosmeticThreads,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display cosmetic threads. Depends on swDisplayAnnotations
setting |
| Display filter - Datums | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDatums,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDatums,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display datums. Depends on swDisplayAnnotations
setting |
| Display filter - Datum targets | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDatumTargets,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDatumTargets,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display datum targets. Depends on swDisplayAnnotations
setting |
| Display filter - Feature dimensions | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayFeatureDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayFeatureDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display feature dimensions. Depends on swDisplayAnnotations
setting |
| Display filter - Reference dimensions | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayReferenceDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayReferenceDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display reference dimensions. Depends on swDisplayAnnotations
setting |
| Display filter - DimXpert dimensions | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDimXpertDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDimXpertDimensions,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to show DimXpert dimensions |
| Display filter - Shaded cosmetic threads | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayShadedCosmeticThreads,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayShadedCosmeticThreads,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display cosmetic threads shaded or not |
| Display filter - Geometric tolerances | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayGeometricTolerances,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayGeometricTolerances,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display geometric tolerances. Depends on swDisplayAnnotations
setting |
| Display filter - Notes | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayNotes,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayNotes,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display notes. Depends on swDisplayAnnotations
setting |
| Display filter - Surface finish | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplaySurfaceFinishSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplaySurfaceFinishSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display surface-finish symbols. Depends on swDisplayAnnotations
setting |
| Display filter - Welds | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayWeldSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayWeldSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display weld symbols. Depends on swDisplayAnnotations
setting |
| Display filter - Display all types | See Comments | See Comments | Not currently available in SOLIDWORKS API |
| Point, Axis, and Coordinate System - Hide names | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPointAxisCoordSystemHideNames,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPointAxisCoordSystemHideNames,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to hide names of points, axes, and coordinate systems
(parts and assemblies only) |
| Point, Axis, and Coordinate System - Name font | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swPointAxisCoordSystemNameFontTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swPointAxisCoordSystemNameFontTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for valid font options | To set font property values, implement ITextFormat, set the appropriate
ITextFormat member values, and pass the ITextFormat object in the API
set method (parts and assemblies only) |
| Point, Axis, and Coordinate System - Label font | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swPointAxisCoordSystemLabelFontTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swPointAxisCoordSystemLabelFontTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for valid font options | To set font property values, implement ITextFormat, set the appropriate
ITextFormat member values, and pass the ITextFormat object in the API
set method (parts and assemblies only) |
| Text scale - numerator | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swAnnotationTextScaleNumerator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swAnnotationTextScaleNumerator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies numerator for annotation text scale |
| Text scale - denominator | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swAnnotationTextScaleDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swAnnotationTextScaleDenominator,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies denominator for annotation text scale |
| Always display text at the same size | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayTextAtSameSizeAlways,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayTextAtSameSizeAlways,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display all annotations and dimensions at same
size regardless of zoom. Drawings have this option disabled and always
zoom the text height |
| Display items only in the view in which they are created | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayOnlyInViewOfCreation,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayOnlyInViewOfCreation,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to only display an annotation when model is viewed
in same orientation as when annotation was added |
| Display annotations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayAnnotations,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayAnnotations,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display annotations |
| Use assembly setting for all components | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayAnnotationsUseAssemblySettings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayAnnotationsUseAssemblySettings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For assemblies only. Specifies whether to display all annotations for
the assembly document, regardless of the setting in the individual part
documents |
| Hide dangling dimensions and annotations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAnnotationDisplayHideDanglingDim,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAnnotationDisplayHideDanglingDim,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to hide dangling dimensions and annotations in drawings |
| Highlight associated elements on reference dimension selection | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingHighlightElements,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingHighlightElements,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to highlight elements associated with selected
reference dimensions (for parts and assemblies only) |
| Use model color for HLR/HLV in
drawings | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseModelColorInDrawings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseModelColorInDrawings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use model color
for hidden lines that are removed/visible |
| Use model color for HLR/HLV with
SpeedPak configurations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseSpeedpakModelColorInDrawings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseSpeedpakModelColorInDrawings,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to use model color
for HLR/HLV with SpeedPak configurations; only
available when a drawing of an assembly is open |
| See through transparent components in HRL/HLV | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSeeThroughTransparentComponents,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSeeThroughTransparentComponents,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only |
| Link child view to parent view
configuration | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingLinkParentViewConfiguration,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingLinkParentViewConfiguration,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to link the child view
to parent view configurations |
| Hatch density limit | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingHatchDensityLimit,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingHatchDensityLimit,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For drawings only |
| Import annotations - From entire assembly | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingImportEntireAssemblyAnnotations,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingImportEntireAssemblyAnnotations,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to import annotations from the entire assembly |
| Auto insert on view creation - Center marks-holes -part | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForHoles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForHoles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for holes in parts |
| Auto insert on view creation - Center marks-fillets -part | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForFillets,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForFillets,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for fillets in parts |
| Auto insert on view creation - Center marks-slots -part | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForSlots,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForSlots,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for slots in parts |
| Auto insert on view creation - Cosmetic Threads - assembly (may affect
performance) | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCosmeticThreadForHolesAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCosmeticThreadForHolesAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For assemblies, specifies whether to automatically insert cosmetic threads |
| Auto insert on view creation - Dowel symbols -part | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDowelSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDowelSymbols,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert dowel symbols in parts |
| Auto insert on view creation -
Center marks-holes -assembly | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForHolesAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForHolesAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for holes
in assemblies |
| Auto insert on view creation -
Center marks-fillets -assembly | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForFilletsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForFilletsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for fillets
in assemblies |
| Auto insert on view creation -
Center marks-slots -assembly | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForSlotsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterMarksForSlotsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert center marks for slots
in assemblies |
| Auto insert on view creation - Dowel Symbols -assembly | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDowelSymbolsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDowelSymbolsAsm,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert dowel symbols in assemblies |
| Auto insert on view creation - Connection Lines to hole patterns with center
marks | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingConnectionLinesHolePatternsCenterMarks,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingConnectionLinesHolePatternsCenterMarks,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert connection lines to hole patterns with
center marks |
| Auto insert on view creation - Centerlines | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterLines,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertCenterLines,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically add centerlines to model faces with
parallel edges |
| Auto insert on view creation - Balloons | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertBalloons,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertBalloons,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert balloons in new drawing views |
| Auto insert on view creation - Dimensions marked for drawing | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDimsMarkedForDrawing,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDimsMarkedForDrawing,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to add dimensions to models, without duplicates in
multiple views |
| Cosmetic thread display - High quality | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCThreadDisplayHighQuality,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCThreadDisplayHighQuality,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to hide or show cosmetic threads |
| Area hatch display - Show halo around annotations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingShowHaloAroundAnnotation,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingShowHaloAroundAnnotation,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display a halo of space around dimensions or annotations
that belong to the drawing view or a sketch and are on top of an area
hatch |
| View break lines - Gap | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBreakLineGap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBreakLineGap,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies size of the gap between break lines in a broken view in a
drawing |
| View break lines - Extension | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBreakLineExtension,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingBreakLineExtension,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies length of the break lines beyond the model geometry |
| View break lines - Scale by view scale for Jagged Style | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingScaleForJaggedStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingScaleForJaggedStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to scale the view break lines by the view scale for the
Jagged Style |
| Center of mass - Symbol size | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingCenterOfMassSize,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swDetailingCenterOfMassSize,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies size of center of mass |
| Center of mass - Scale by view scale | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterOfMassScaleByView,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterOfMassScaleByView,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to to scale the
center of mass symbol by the view scale |
