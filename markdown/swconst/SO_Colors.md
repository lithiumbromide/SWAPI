---
title: "System Options > Colors"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Colors.htm"
---

# System Options > Colors

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the

  dialog
  corresponds to the settings on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on
  the dialog but are now obsolete.

NOTE: The input or output value
is the corresponding[IColorTable](sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable.html)value unless otherwise specified.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Icon color (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsIconColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsIconColor,
swSystemColorsIconColor_e.< Value >) | See swSystemColorsIconColor_e for valid options |  |
| Background | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsBackground) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsBackground,
swInterfaceBrightnessTheme_e.< Value >) | See swInterfaceBrightnessTheme_e for valid options |  |
| Current color scheme | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsCurrentColorScheme) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsCurrentColorScheme,
swSystemColorsCurrentColorScheme_e.< Value >) | See swSystemColorsCurrentColorScheme_e for valid options |  |
| Color scheme settings - Viewport Background | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsViewportBackground) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsViewportBackground,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Top Gradient Color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTopGradientColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTopGradientColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Bottom Gradient Color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsBottomGradientColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsBottomGradientColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dynamic Highlight | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDynamicHighlight) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDynamicHighlight,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Highlight | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsHighlight) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsHighlight,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 1 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem1) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem1,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 2 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem2) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem2,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 3 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem3) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem3,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 4 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem4) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem4,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 5 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem5) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem5,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item 6 | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem6) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedItem6,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color Scheme settings - Measure
Highlight | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMeasureSelection) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMeasureSelection,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Item Missing Reference | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGhostSelColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGhostSelColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Selected Face, Shaded | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedFaceShaded) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSelectedFaceShaded,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Paper Color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsPaper) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsPaper,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable ; sheet color |
| Color scheme settings - Drawings, Background | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsBackground) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsBackground,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable ; drawing background color |
| Color scheme settings - Drawings, Visible Model Edges | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsVisibleModelEdge) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsVisibleModelEdge,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Hidden Model Edges | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsHiddenModelEdge) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsHiddenModelEdge,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Model Edges (SpeedPak) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsSpeedPakModelEdge) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsSpeedPakModelEdge,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Model Tangent Edges | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsModelTangentEdges) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsModelTangentEdges,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings,
Changed dimensions | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsChangedDimensions) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDrawingsChangedDimensions,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Modified Cells (BOM) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBomOverriddenCellValueColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBomOverriddenCellValueColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Drawings, Overridden Dimensions | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDimOverriddenCellValueColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDimOverriddenCellValueColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dimensions, Imported (Driving) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedDrivingAnnotation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedDrivingAnnotation,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dimensions, Non Imported (Driven) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedDrivenAnnotation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedDrivenAnnotation,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dimensions, Dangling | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDanglingDimension) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDanglingDimension,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dimensions, Not Marked for Drawing | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDimsNotMarkedForDrawing) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDimsNotMarkedForDrawing,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dimensions, Controlled by Design Table | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDTDim) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsDTDim,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Graphical Annotations | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swGraphicalAnnotationsColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swGraphicalAnnotationsColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Text | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsText) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsText,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Over Defined | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchOverDefined) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchOverDefined,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Fully Defined | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchFullyDefined) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchFullyDefined,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Under Defined | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchUnderDefined) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchUnderDefined,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Invalid Geometry | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchInvalidGeometry) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchInvalidGeometry,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Not Solved | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchNotSolved) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchNotSolved,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Inactive | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchInactive) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSketchInactive,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Shaded Contours | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swShadedSketchContourColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swShadedSketchContourColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sketch, Exploded | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSketchExplodedColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSketchExplodedColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Grid Lines, Minor | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGridLinesMinor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGridLinesMinor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Grid Lines, Major | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGridLinesMajor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsGridLinesMajor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Construction Geometry | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsConstructionGeometry) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsConstructionGeometry,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly, Edit Part | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyEditPart) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyEditPart,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly, Hidden Lines of Edit Part | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyEditPartHiddenLines) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyEditPartHiddenLines,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly, Non-Edit Parts | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyNonEditPart) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAssemblyNonEditPart,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Inactive Entities | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsInactiveEntity) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsInactiveEntity,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Inactive Handles | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsInactiveHandles) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsInactiveHandles,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Temporary Graphics | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporaryGraphics) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporaryGraphics,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Temporary Graphics, Shaded | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporaryGraphicsShaded) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTemporaryGraphicsShaded,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Temporary Graphics - Add Material | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTempGraphicsAddMaterialColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTempGraphicsAddMaterialColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Temporary Graphics - Remove Material | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTempGraphicsRemoveMaterialColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTempGraphicsRemoveMaterialColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Sheet Metal
Temporary Graphics color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSheetMetalTemporaryGraphics) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSheetMetalTemporaryGraphics,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Surfaces, Open Edges | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSurfacesOpenEdge) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSurfacesOpenEdge,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Edges in Shaded With Edges Mode | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsShadedEdge) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsShadedEdge,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - FeatureManager Design Tree Text | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTreeItemNormal) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsTreeItemNormal,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Flyout FeatureManager Design Tree Text | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swGraphicsTreeItemNormalColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swGraphicsTreeItemNormalColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Annotations, Imported | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedAnnotation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsImportedAnnotation,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Annotations, Non Imported | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNonImportedAnnotation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsNonImportedAnnotation,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly Interference Volume | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAsmInterferenceVolume) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsAsmInterferenceVolume,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Hidden Edge Selection Show Color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsHiddenEdgeSelectionShow) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsHiddenEdgeSelectionShow,
< Value >) | Integer value | Read-only COLORREF value in SOLIDWORKS IColorTable ; although it appears that you have set it, the SOLIDWORKS
software ignores your setting |
| Color scheme settings - Mate Callout, Healthy | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutHealthy) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutHealthy,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Mate Callout, Warning | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutWarning) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutWarning,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings -Mate Callout,
Error | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutError) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsMateCalloutError,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Envelope
Components | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEnvelopeComponentColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEnvelopeComponentColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization First | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor1) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.sswAssemblyVisualizationComponentColor1,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization Second | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor2) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor2,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization Third | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor3) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor3,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization Fourth | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor4) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor4,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization Fifth | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor5) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor5,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Assembly
Visualization Sixth | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor6) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAssemblyVisualizationComponentColor6,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Manipulator connection point color | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swManipConnectionPointColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swManipConnectionPointColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Annotations, DimXpert | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftAnnotations) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftAnnotations,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - DimXpert, Under Constrained | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftUnderConstrained) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftUnderConstrained,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - DimXpert, Fully Constrained | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftFullyConstrained) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftFullyConstrained,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - DimXpert, Over Constrained | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftOverConstrained) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsSwiftOverConstrained,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Annotations, TolAnalyst Dimension | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsToleranceAnalysisDim) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsToleranceAnalysisDim,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Zone row/column lines | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swZoneLineColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swZoneLineColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Recognized mesh face | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRecognizedMeshFaceColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRecognizedMeshFaceColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Unrecognized mesh face | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUnrecognizedMeshFaceColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swUnrecognizedMeshFaceColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dynamic Reference Visualization (Parent) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRefVisualizationParentColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRefVisualizationParentColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Dynamic Reference Visualization (Child) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRefVisualizationChildrenColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRefVisualizationChildrenColor,
< Value >) | Integer value | COLORREF value in SOLIDWORKS IColorTable |
| Color scheme settings - Background appearance: Use
document scene background | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance,
swColorsBackgroundAppearance_e.swColorsBackgroundAppearance_DocumentScene) | See swColorsBackgroundAppearance_e for valid options |  |
| Color scheme settings - Background appearance: Plain
(Viewport Background color above) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance,
swColorsBackgroundAppearance_e.swColorsBackgroundAppearance_Plain) | See swColorsBackgroundAppearance_e for valid options |  |
| Color scheme settings - Background appearance: Gradient
(Top/Bottom Gradient colors above) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance,
swColorsBackgroundAppearance_e.swColorsBackgroundAppearance_Gradient) | See swColorsBackgroundAppearance_e for valid options |  |
| Color scheme settings - Background appearance: Image File | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance,
swColorsBackgroundAppearance_e.swColorsBackgroundAppearance_Image) and ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swColorsBackgroundImageFile) ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swColorsBackgroundImageFile,
< Value >) | Integer value: See swColorsBackgroundAppearance_e for valid options String value: Path and file name of the file to use as the background for the SOLIDWORKS
graphics window NOTE: If you omit the path,
then the default image folder in the SOLIDWORKS install folder is assumed: \data\Images\textures\background You can also use ISldWorks::GetDataFolder to get the data folder |  |
| Use specified color for drawings paper color | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetBackgroundAsPicture) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDrawingSheetBackgroundAsPicture,
< OnFlag >) | Boolean value |  |
| Use specified color for Shaded With Edges mode | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swColorsUseShadedEdgeColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swColorsUseShadedEdgeColor,
< OnFlag >) | Boolean value | Specifies whether to use specified colors for Shaded With Edges mode |
| Use specified colors when editing parts in assemblies | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swColorsUseSpecifiedEditColors) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swColorsUseSpecifiedEditColors,
< OnFlag >) | Boolean value | Specifies whether to use specified colors when editing assemblies |
| Use specified color for changed
drawing dimensions on open | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseChangedDimensions) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseChangedDimensions,
< OnFlag >) | Boolean value | Specifies whether to highlight
changed dimensions in a specified color after a drawing document is opened |
| Envelopes | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsEnvelopes) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemColorsEnvelopes,
swSystemColorsEnvelopes_e.< Value >) | See swSystemColorsEnvelopes_e for valid options |  |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swColorsGradientPartBackground | Obsolete ; used swColorsBackgroundAppearance_e |
| swColorsMatchViewAndFeatureManagerBackground | Obsolete |
| swSystemColorsDrawingsPaperBorder | Obsolete |
| swSystemColorsDrawingsPaperShadow | Obsolete |
| swSystemColorsPropertyManagerColor | Obsolete ; used swPropertyManagerColorScheme_e |
| swSystemColorsRefTriadX | Obsolete |
| swSystemColorsRefTriadY | Obsolete |
| swSystemColorsRefTriadZ | Obsolete |
| swSystemColorsTreeItemSelected | Obsolete |
