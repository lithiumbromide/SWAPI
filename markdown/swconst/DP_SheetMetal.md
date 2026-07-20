---
title: "Document Properties > Sheet Metal"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_SheetMetal.htm"
---

# Document Properties > Sheet Metal

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

For drawings:

For assemblies:

For parts:

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Flat pattern colors - Bend Lines - Up Direction | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesUp,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesUp,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Bend Lines - Down Direction | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesDown,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesDown,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Form Feature | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorFormFeature,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorFormFeature,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Bend Lines - Hems | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesHems,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBendLinesHems,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Model Edges | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorModelEdges,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorModelEdges,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Flat Pattern Sketch Color | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorFlatPatternSketch,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorFlatPatternSketch,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Flat pattern colors - Bounding box | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBoundingBox,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalColorBoundingBox,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Integer RGB value | For drawings only |
| Bend notes - Display sheet metal bend notes | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowSheetMetalBendNotes,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowSheetMetalBendNotes,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only Specifies whether to show sheet metal bend notes |
| Bend notes - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swBendNoteStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swBendNoteStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBendNoteStyle_e.< Value >) | See swBendNoteStyle_e for valid options | For drawings only Specifies where to place note with respect to bend lines |
| Bend notes - Leader style - Line style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderLineStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineStyles_e.< Value >) | See swLineStyles_e for valid options | For drawings only |
| Bend notes - Leader style - Line thickness | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderLineThickness,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLineWeights_e.< Value >) | See swLineWeights_e for valid options | For drawings only If set to Custom Size , you must also
set Leader style - Line thickness - Custom Size |
| Bend notes - Leader style - Line thickness - Custom Size | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesLeaderLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesLeaderLineThicknessCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For drawings only Specifies a custom thickness for leader lines in sheet
metal drawings |
| Bend notes - Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swSheetMetalBendNotesTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swSheetMetalBendNotesTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | For drawings only To set font property values, implement ITextFormat, set the appropriate
ITextFormat member values, and pass the ITextFormat object in this API's
set method |
| Bend notes - Text - Text alignment | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesTextAlignment,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesTextAlignment,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swTextJustification_e.< Value >) | See swTextJustification_e for valid options; None is not a valid option | For drawings only |
| Bend notes - Leader anchor | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderAnchor,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderAnchor,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLeaderSide_e.< Value >) | See swLeaderSide_e for valid options | For drawings only |
| Bend notes - Leader display | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesLeaderDisplay,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swLeaderStyle_e.< Value >) | See swLeaderStyle_e for valid options | For drawings only |
| Bend notes - Leader display - Use document leader length | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBendNotesUseDocLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBendNotesUseDocLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only |
| Bend notes - Leader display - Leader length | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesLeaderLength,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For drawings only |
| Bend notes - Leader display - Leader justification snapping | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBendNotesLeaderJustificationSnapping,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalBendNotesLeaderJustificationSnapping,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only |
| Bend notes - Layer | IModelDocExtension::GetUserPreferenceString (swUserPreferenceStringValue_e.swSheetMetalBendNotesLayer,
swUserPreferenceOption_e. swDetailingNoOptionSpecified ) IModelDocExtension::SetUserPreferenceString (swUserPreferenceStringValue_e.swSheetMetalBendNotesLayer,
swUserPreferenceOption_e. swDetailingNoOptionSpecified , < Value >) | Valid Options: "Border" "Dimensions" "Notes" "BOM" "FORMAT" | For drawings only |
| Bend notes - Border - Style | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesBorderStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesBorderStyle,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonStyle_e.< Value >) | See swBalloonStyle_e for valid options; swBS_SplitCir and swBS_Underline are not valid options | For drawings only |
| Bend notes - Border - Size | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesBorderSize,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swSheetMetalBendNotesBorderSize,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, swSheetMetalBendNotesBorderSize_e.< Value >) | See swSheetMetalBendNotesBorderSize_e for valid options | For drawings only If set to swSheetMetalBendNotesBorderSizeUserDefined ,
you must also set Bend notes - Border - Size - Custom Size |
| Bend notes - Border - Size - Custom Size | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesBorderSizeCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDoubleValue_e.swSheetMetalBendNotesBorderSizeCustom,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | For drawings only |
| Show fixed face | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowFixedFace,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowFixedFace,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only |
| Show grain direction | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowGrainDirection,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowGrainDirection,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For drawings only |
| Flat pattern options - Simplify
bends | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_SimplifyBends,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_SimplifyBends,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For assemblies only |
| Flat pattern options - Corner
treatment | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_CornerTreatment,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_CornerTreatment,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For assemblies only |
| Flat pattern options - Create
multiple flat patterns whenever a feature creates multiple sheet metal bodies | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_DisableSplitters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_DisableSplitters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For assemblies only |
| Flat pattern options - Show form
tool punches when flattened | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowPunches,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowPunches,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| Flat pattern options - Show form
tool profiles when flattened | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowProfiles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowProfiles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| Flat pattern options - Show form
tool centers when flattened | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowCenters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_ShowCenters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| Flat pattern options - Show sheet metal gusset profiles when flattened | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_WhenFlattenedShowGussetProfiles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_WhenFlattenedShowGussetProfiles,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| Flat pattern options - Show sheet metal gusset centers when flattened | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_WhenFlattenedShowGussetCenters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFlatPatternOpt_WhenFlattenedShowGussetCenters,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| New Sheet Metal Bodies - Override default parameters | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateParam,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateParam,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| New Sheet Metal Bodies - Override bend allowance parameters | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateAllowance,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateAllowance,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| New Sheet Metal Bodies - Override auto relief parameters | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateRelief,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalOverrideTemplateRelief,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| New Sheet Metal Bodies - Use sheet metal parameters from material | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalUseMaterial,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetMetalUseMaterial,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
| Edge Flange Options - Automatically add Flange Length dimension to flange
profiles | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetDimensionFlangeSketch,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSheetDimensionFlangeSketch,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only |
