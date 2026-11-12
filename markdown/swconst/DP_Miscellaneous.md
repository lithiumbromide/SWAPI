---
title: "Document Properties > Miscellaneous"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_Miscellaneous.htm"
---

# Document Properties > Miscellaneous

Some document-level enumerators exist that do not correspond to any of the controls shown on the SOLIDWORKS **Tools > Options > Document Properties** dialogs. Click the links to jump to the tables in this Help topic or to the Help topics containing these miscellaneous document-level enumerators.

See [System Options and Document Properties](sldworksapiprogguide.chm::/Overview/System_Options_and_Document_Properties.htm) for details about system options and document properties.

| Miscellaneous Document-level Enumerators |  |  |
| --- | --- | --- |
| SOLIDWORKS | SOLIDWORKS Routing |  |
| Related to categories on Document Properties tab | Not related to categories on Document Properties tab |  |
| Annotations - Notes Dimensions - Hole Callout DimXpert Detailing Grid/Snap Material Properties Plane Display Configurations | Annotations folder shortcut menu Dimensions - Drafting Standard PropertyManager View menu Bounding Box Pdf | Route Properties PropertyManager page Twisted Pair Parameters |

Annotations folder shortcut menu

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swShowAnnotationInAnnotationViews | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowAnnotationInAnnotationViews, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowAnnotationInAnnotationViews, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to enable annotation view visibility; corresponds to Annotations' folder shortcut menu item, Enable Annotation View Visibility |

Detailing

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDetailingAngularDimLeaderStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingAngularDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingAngularDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDisplayDimensionLeaderText_e.< Value >) | See swDisplayDimensionLeaderText_e for valid options | Specifies the style of text placement for angular leaders |
| swDetailingAngularToleranceStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingAngularDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingAngularDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swTolType_e.< Value >) | See swTolType_e for valid options | Specifies the angular tolerance style |
| swDetailingChamferDimTextStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingChamferDimTextStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingChamferDimTextStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingChamferDimLeaderTextStyle_e.< Value >) | See swDetailingChamferDimLeaderTextStyle_e for valid options | Specifies how to display text relative to the leader |
| swDetailingCenterMarkShowLines | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterMarkShowLines, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterMarkShowLines, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display center mark lines |
| swDetailingCenterMarkUseCenterline | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterMarkUseCenterline, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingCenterMarkUseCenterline, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether lines in center mark use font specified for centerlines |
| swDetailingDimFontHeight | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingDimFontHeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingDimFontHeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies height of dimensions |
| swDetailingDisplayWithBrokenLeaders | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDisplayWithBrokenLeaders, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDisplayWithBrokenLeaders, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For ANSI dimensioning standard only; specifies whether to display broken leaders |
| swDetailingLinearDimLeaderStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingLinearDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingLinearDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDisplayDimensionLeaderText_e.< Value >) | See swDisplayDimensionLeaderText_e for valid options | Specifies the style of text placement for linear leaders |
| swDetailingLinearToleranceStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingLinearToleranceStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingLinearToleranceStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swTolType_e.< Value >) | See swTolType_e for valid options | Specifies the linear tolerance style |
| swDetailingMaxAngularToleranceValue | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxAngularToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxAngularToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies the maximum variation for the type of angular tolerance selected |
| swDetailingMaxLinearToleranceValue | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxLinearToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxLinearToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies maximum variation for type of linear tolerance selected |
| swDetailingMaxWitnessLineLength | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxWitnessLineLength, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMaxWitnessLineLength, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies maximum length for a witness line |
| swDetailingMinAngularToleranceValue | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMinAngularToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMinAngularToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies minimum variation for type of angular tolerance selected |
| swDetailingMinLinearToleranceValue | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMinLinearToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingMinLinearToleranceValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies minimum variation for type of linear tolerance selected |
| swDetailingNoteFontHeight | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingNoteFontHeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swDetailingNoteFontHeight, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value in meters | Specifies height of notes |
| swDetailingRadialDimLeaderStyle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingRadialDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingRadialDimLeaderStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDisplayDimensionLeaderText_e.< Value >) | See swDisplayDimensionLeaderText_e for valid options | Specifies the style of text placement for radial leaders |
| swDetailingToleranceFitToDisplayAngular | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingToleranceFitToDisplayAngular, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingToleranceFitToDisplayAngular, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swFitTolDisplay_e.< Value >) | If swTolType_e set to swTolFIT, swTolFITWITHTOL, or swTolFITTOLONLY, then see swFitTolDisplay_e for valid options |  |
| swDetailingToleranceFitToDisplayLinear | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingToleranceFitToDisplayLinear, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingToleranceFitToDisplayLinear, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swFitTolDisplay_e.< Value >) | If swTolType_e set to swTolFIT, swTolFITWITHTOL, or swTolFITTOLONLY, then see swFitTolDisplay_e for valid options |  |

[Back to top](#Top)

Dimensions - Drafting Standard

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDetailingAutoInsertDimsMarkedForDrawing | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDimsMarkedForDrawing, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingAutoInsertDimsMarkedForDrawing, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to automatically insert dimensions marked for the drawing in new drawing views; see IDisplayDimension::MarkedForDrawing for details about marking dimensions for drawings |
| swDetailingDimensionsAngularToleranceUseParentheses | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsAngularToleranceUseParentheses, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimensionsAngularToleranceUseParentheses, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For bilateral, symmetric, or fit-with-tolerance types only; specifies whether to show parentheses around angular tolerances |
| swDetailingDimensionStandardName | IModelDocExtension::GetUserPreferenceString (swUserPreferenceString_e.swDetailingDimensionStandardName, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceString (swUserPreferenceString_e.swDetailingDimensionStandardName, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Valid string values: ANSI ISO DIN JIS BSI GOST GB | Detailing standard |
| swDetailingDimLeaderOverrideStandard | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimLeaderOverrideStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimLeaderOverrideStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to override standard's leader display |
| swDetailingDimOffsetText | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimOffsetText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimOffsetText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to offset dimension text or not |
| swDetailingDimsFollowDimXpertLayout | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimsFollowDimXpertLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimsFollowDimXpertLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to follow DimXpert dimension/annotation layout |
| swDetailingDimsSnapTextToGrid | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimsSnapTextToGrid, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingDimsSnapTextToGrid, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to snap dimension text to grid in drawings or sketches |
| swDetailingShowHaloAroundAnnotation | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingShowHaloAroundAnnotation, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingShowHaloAroundAnnotation, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display a halo of space around dimensions or annotations that belong to the drawing view or a sketch and are on top of an area hatch |

[Back to top](#Top)

Dimensions - Hole Callout

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDetailingDualDimPosition | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingDualDimPosition, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDetailingDualDimPosition, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingDualDimPosition_e.< Value >) | See swDetailingDualDimPosition_e for valid options | Allows the display of dimensions in two kinds of units |

[Back to top](#Top)

DimXpert

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDisplayComponentDimXpertAnnotations | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayComponentDimXpertAnnotations, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayComponentDimXpertAnnotations, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value |  |

[Back to top](#Top)

Grid/Snap

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swSnapOnlyIfGridDisplayed | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapOnlyIfGridDisplayed, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapOnlyIfGridDisplayed, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to snap to grid if swGridDisplay is turned on |
| swSnapToAngle | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapToAngle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapToAngle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether sketched lines snap to predefined angle |
| swSnapToAngleValue | IModelDocExtension::GetUserPreferenceDouble (swUserPreferenceDouble_e.swSnapToAngleValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceDouble (swUserPreferenceDouble_e.swSnapToAngleValue, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Double value | Specifies angle to which sketched lines should snap |
| swSnapToPoints | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapToPoints, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSnapToPoints, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether points snap to grid |

[Back to top](#Top)

Material Properties

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swMaterialPropertySolidFill | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swMaterialPropertySolidFill, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swMaterialPropertySolidFill, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | For parts only; specifies whether to set the fill for area hatch or solid |

[Back to top](#Top)

Notes

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDetailingNotesDisplayWithBentLeader | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingNotesDisplayWithBentLeader, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDetailingNotesDisplayWithBentLeader, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display notes using bent leaders |

[Back to top](#Top)

Plane Display

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swPlaneDisplayShowEdges | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPlaneDisplayShowEdges, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPlaneDisplayShowEdges, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Edges of planes take the same color as the front and back faces, are not transparent, and are always displayed |

[Back to top](#Top)

Configurations

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDefaultConfigSortOrder | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swDefaultConfigSortOrder, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swDefaultConfigSortOrder, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swConfigTreeSortType_e.< Value >) | Values as defined in swConfigTreeSortType_e | ConfigurationManager RMB menu |

[Back to top](#Top)

PropertyManager

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swPropertyManagerColorActiveClosedDivider | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorActiveClosedDivider, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorActiveClosedDivider, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorBackground | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorBackground, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorBackground, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColor_Divider | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColor_Divider, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColor_Divider, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorEditBox | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorEditBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorEditBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColor_EditText | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColor_EditText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColor_EditText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorImportantMessage | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorImportantMessage, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorImportantMessage, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorInnerBorder | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorInnerBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorInnerBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorLabelAndIcon | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorLabelAndIcon, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorLabelAndIcon, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorTitle | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorTitle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorTitle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorOuterBorder | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorOuterBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorOuterBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorTopBorder | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorTopBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorTopBorder, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |
| swPropertyManagerColorDivider | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorDivider, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceInteger_e.swPropertyManagerColorDivider, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Read-only integer value for RGB color in use |  |

[Back to top](#Top)

View menu

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swDisplayCameraFOVBox | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayCameraFOVBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayCameraFOVBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value | Specifies whether to display Field of View (FOV) box in the graphics area when viewing through a camera |

[Back to top](#Top)

Bounding Box

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swViewDispGlobalBBox | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewDispGlobalBBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewDispGlobalBBox, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value |  |

[Back to top](#Top)

Pdf

| Enumerator | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| swPdfIncludeBookmarks | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPdfIncludeBookmarks, swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPdfIncludeBookmarks, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | Boolean value |  |

[Back to top](#Top)
