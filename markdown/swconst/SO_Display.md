---
title: "System Options > Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Display.htm"
---

# System Options > Display

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Hidden edges displayed as - Solid | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesHiddenEdgeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesHiddenEdgeDisplay, swEdgesHiddenEdgeDisplay_e.swEdgesHiddenEdgeDisplaySolid) | swEdgesHiddenEdgeDisplay_e .swEdgesHiddenEdgeDisplaySolid |  |
| Hidden edges displayed as - Dashed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesHiddenEdgeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesHiddenEdgeDisplay, swEdgesHiddenEdgeDisplay_e.swEdgesHiddenEdgeDisplayDashed) | swEdgesHiddenEdgeDisplay_e .swEdgesHiddenEdgeDisplayDashed |  |
| Part/Assembly tangent edge display - As visible | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay, swEdgesTangentEdgeDisplay_e.swEdgesTangentEdgeDisplayVisible) | swEdgesTangentEdgeDisplay_e .swEdgesTangentEdgeDisplayVisible |  |
| Part/Assembly tangent edge display - As phantom | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay, swEdgesTangentEdgeDisplay_e.swEdgesTangentEdgeDisplayPhantom) | swEdgesTangentEdgeDisplay_e .swEdgesTangentEdgeDisplayPhantom |  |
| Part/Assembly tangent edge display - Removed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesTangentEdgeDisplay, swEdgesTangentEdgeDisplay_e.swEdgesTangentEdgeDisplayRemoved) | swEdgesTangentEdgeDisplay_e .swEdgesTangentEdgeDisplayRemoved |  |
| Edge display in shaded with edges mode - HLR | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesShadedModeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesShadedModeDisplay, swEdgesShadedModeDisplay_e.swEdgesShadedModeDisplayHLR) | swEdgesShadedModeDisplay_e .swEdgesShadedModeDisplayHLR |  |
| Edge display in shaded with edges mode - HLR - Optimize for thin parts | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesShadedModeDisplayOptimizeForThinParts) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesShadedModeDisplayOptimizeForThinParts, < OnFlag >) | Boolean value | True to optimize for thin parts; valid only if Edge display in shaded with edges mode - HLR is set |
| Edge display in shaded with edges mode - Wireframe | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesShadedModeDisplay) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesShadedModeDisplay, swEdgesShadedModeDisplay_e.swEdgesShadedModeDisplayWireframe) | swEdgesShadedModeDisplay_e .swEdgesShadedModeDisplayWireframe) |  |
| Assembly transparency for in context edit - < selection box> | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesInContextEditTransparencyType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesInContextEditTransparencyType, swInContextEditTransparencyType_e.< Value >) | See swInContextEditTransparencyType_e for valid options |  |
| Assembly transparency for in context edit - < slider> | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesInContextEditTransparency) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swEdgesInContextEditTransparency, < Value >) | Integer value between 0 and 100 indicating transparency |  |
| Anti-aliasing | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemOptionDisplayAntiAliasing) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swSystemOptionDisplayAntiAliasing, < Value >) | See swSystemOptionDisplayAntiAliasing_e for valid options | S pecifies whether to smooth out jagged edges in Shaded With Edges, Wireframe, Hidden Lines Removed, and Hidden Lines Visible modes |
| Appearance Visual Style - DSPBR or Legacy Appearances | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDspbrAppearances) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDspbrAppearances, < OnFlag >) | Boolean value | Valid only if Enhanced Graphics Performance is enabled; True to select Dassault Standard Physically Based Rendering (DSPBR), false for Legacy Appearances |
| Use shaded face highlighting | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedFaceHighlight) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedFaceHighlight, < OnFlag >) | Boolean value |  |
| Highlight all edges of features selected in graphics view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHighlightFeatureEdges) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHighlightFeatureEdges, < OnFlag >) | Boolean value | Specifies whether all edges on selected feature are highlighted when feature selected |
| Dynamic highlight from graphics view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDynamicHighlight) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDynamicHighlight, < OnFlag >) | Boolean value | Specifies whether to highlight edges, faces, vertices, dimensions, annotations, and so on, in the graphics area when pointer moves across them |
| Display temporary axes upon hover over cylindrical faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayTempAxesOnMouseHover) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayTempAxesOnMouseHover, < OnFlag >) | Boolean value |  |
| Show open edges of surfaces in different color | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesOpenEdgesDifferentColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesOpenEdgesDifferentColor, < OnFlag >) | Boolean value | Specifies whether to differentiate between open edges of surface and any tangent edges or silhouette |
| Display shaded planes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDisplayShadedPlanes) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDisplayShadedPlanes, < OnFlag >) | Boolean value | Specifies whether to display transparent shaded planes with a wireframe edge that have different front and back colors |
| Display dimensions flat to screen | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDimensionsFlatToScreen) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayDimensionsFlatToScreen, < OnFlag >) | Boolean value | Specifies whether to display dimensions flat to screen |
| Display DimXpert dimensions on top of model | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDispDimXpertDimOnTopOfModel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDispDimXpertDimOnTopOfModel, < OnFlag >) | Boolean value |  |
| Display notes flat to screen | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayNotesFlatToScreen) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayNotesFlatToScreen, < OnFlag >) | Boolean value | Specifies whether to display notes flat to screen |
| Display reference triad | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayReferenceTriad) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayReferenceTriad, < OnFlag >) | Boolean value |  |
| Display scrollbars in graphics view for parts and assemblies | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayScrollbarsInGraphicsViewPartsAndAssemblies) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayScrollbarsInGraphicsViewPartsAndAssemblies, < OnFlag >) | Boolean value |  |
| Display scrollbars in graphics view for drawings | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayScrollbarsInGraphicsViewDrawings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayScrollbarsInGraphicsViewDrawings, < OnFlag >) | Boolean value |  |
| Display draft quality ambient occlusion | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftQualityAmbientOcclusion) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDraftQualityAmbientOcclusion, < OnFlag >) | Boolean value | Specifies whether to use global lighting that adds realism to models by controlling the attenuation of ambient light due to occluded areas; available in all scenes when you use RealView graphics |
| Display Speedpak graphics circle | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplaySpeedpakGraphicsCircle) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplaySpeedpakGraphicsCircle, < OnFlag >) | Boolean value | Specifies whether to display Speedpak graphics circle |
| Display pattern information tooltips | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayPatternInformationToolTips) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayPatternInformationToolTips, < OnFlag >) | Boolean value | Specifies whether to display pattern information tooltips |
| Breadcrumbs - Show breadcrumbs on selection | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowBreadcrumbsOnSelection) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowBreadcrumbsOnSelection, < OnFlag >) | Boolean value | Specifies whether to show breadcrumbs on selection |
| Breadcrumbs - Show breadcrumbs at mouse pointer | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowBreadcrumbsAtMousePointer) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowBreadcrumbsAtMousePointer, < OnFlag >) | Boolean value | Specifies whether to show breadcrumbs at the mouse pointer; valid only if Show breadcrumbs on selection is selected |
| Display facet fins in Mesh BREP bodies | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayMeshBREPFacetFins) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayMeshBREPFacetFins, < OnFlag >) | Boolean value |  |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swDisplayEquationIds | Obsolete |
| swFourViewportProjectionType | Obsolete |
| swDisplayGraphicsComponents | Obsolete |
| swDisplayReferenceGeometryForXYZOrientation | Obsolete |
| swEdgesAntiAlias | Obsolete |
| swEdgesHighQualityDisplay | Obsolete |
| swEdgesRepaintAfterSelectionInHLR | Obsolete |
