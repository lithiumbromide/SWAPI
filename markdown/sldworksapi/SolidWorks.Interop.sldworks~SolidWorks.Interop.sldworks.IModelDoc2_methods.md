---
title: "IModelDoc2 Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_methods.html"
---

# IModelDoc2 Interface Methods

For a list of all members of this type, see [IModelDoc2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateFeatureMgrView | Obsolete. Superseded by IFeatureMgrView::ActivateView or IModelDocExtension::ActivateFeatureMgrViewx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. |
| Method | ActivateSelectedFeature | Activates the selected feature for editing. |
| Method | AddConfiguration | Obsolete. Superseded by IModelDoc2::AddConfiguration3 . |
| Method | AddConfiguration2 | Obsolete. Superseded by IModelDoc2::AddConfiguration3 . |
| Method | AddConfiguration3 | Adds a new configuration to this model document. |
| Method | AddCustomInfo | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | AddCustomInfo2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | AddCustomInfo3 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | AddDiameterDimension | Obsolete. Superseded by IModelDoc2::AddDiameterDimension2 . |
| Method | AddDiameterDimension2 | Adds a diameter dimension at the specified location for the selected item. |
| Method | AddDimension | Obsolete. Superseded by IModelDoc2::AddDimension2 . |
| Method | AddDimension2 | Creates a display dimension at the specified location for selected entities. |
| Method | AddFeatureMgrView | Obsolete. Superseded by IModelDocExtension::AddFeatureMgrView3x64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. |
| Method | AddFeatureMgrView2 | Obsolete. Superseded by IModelDocExtension::AddFeatureMgrView3x64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. |
| Method | AddFeatureMgrView3 | Obsolete. Superseded by IModelDocExtension::AddFeatureMgrView3x64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Adds the specified tab to the FeatureManager design tree view. |
| Method | AddHorizontalDimension | Obsolete. Superseded by IModelDoc2::AddHorizontalDimension2 . |
| Method | AddHorizontalDimension2 | Creates a horizontal dimension for the currently selected entities at the specified location. |
| Method | AddIns | Displays the Add-In Manager dialog box. |
| Method | AddLightSource | Adds a type of light source to a scene with the specified names. |
| Method | AddLightSourceExtProperty | Stores a float, string, or integer value for the light source. |
| Method | AddLightToScene | Adds a light source to a scene. |
| Method | AddLoftSection | Adds a loft section to a blend feature. |
| Method | AddOrEditConfiguration | Obsolete. Superseded by IConfiguraiton::GetParameters , IConfiguration::IGetParameters , IConfiguration::ISetParameters , and IConfiguration::SetParameters . |
| Method | AddPropertyExtension | Adds a property extension to this model. |
| Method | AddRadialDimension | Obsolete. Superseded by IModelDoc2::AddRadialDimension2 . |
| Method | AddRadialDimension2 | Adds a radial dimension at the specified location for the selected item. |
| Method | AddRelation | Obsolete. Superseded by IEquationMgr::Add . |
| Method | AddSceneExtProperty | Stores a float, string, or integer value for a scene. |
| Method | AddVerticalDimension | Obsolete. Superseded by IModelDoc2::AddVerticalDimension2 . |
| Method | AddVerticalDimension2 | Creates a vertical dimension for the currently selected entities at the specified location. |
| Method | AlignDimensions | Obsolete. Superseded by IModelDocExtension::AlignDimensions . |
| Method | AlignOrdinate | Aligns the selected group of ordinate dimensions. |
| Method | AlignParallelDimensions | Aligns the selected linear dimensions in a parallel fashion. |
| Method | AndSelect | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | AndSelectByID | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | AndSelectByMark | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | AutoInferToggle | Obsolete. Superseded by ISketchManager::AutoInference . |
| Method | AutoSolveToggle | Obsolete. Superseded by ISketchManager::AutoSolve . |
| Method | BlankRefGeom | Hides the selected reference geometry in the graphics window. |
| Method | BlankSketch | Hides the selected sketches. |
| Method | BreakAllExternalReferences | Obsolete. Superseded by IModelDocExtension::BreakAllExternalReferences2 . |
| Method | BreakDimensionAlignment | Breaks the association of any selected dimensions belonging to an alignment group (parallel or collinear). |
| Method | ChangeSketchPlane | Obsolete. Superseded by IModelDocExtension::ChangeSketchPlane . |
| Method | ClearSelection | Obsolete. Superseded by IModelDoc2::ClearSelection2 . |
| Method | ClearSelection2 | Clears the selection list. |
| Method | ClearUndoList | Clears the undo list for this model document. |
| Method | Close | Not implemented. Use ISldWorks::CloseDoc . |
| Method | CloseFamilyTable | Closes the design table currently being edited. |
| Method | ClosePrintPreview | Closes the currently displayed Print Preview page for this document. |
| Method | ClosestDistance | Calculates the minimum distance between the specified geometric objects. |
| Method | Create3PointArc | Obsolete. Superseded by ISketchManager::Create3PointArc . |
| Method | CreateArc | Obsolete. Superseded by IModelDoc2::CreateArc2 . |
| Method | CreateArc2 | Obsolete. Superseded by ISketchManager::CreateArc . |
| Method | CreateArcByCenter | Creates an arc by center in this model document. |
| Method | CreateArcDB | Obsolete. Superseded by IModelDoc2::CreateArc2 . |
| Method | CreateArcVB | Obsolete. Superseded by IModelDoc2::CreateArc2 . |
| Method | CreateCenterLine | Obsolete. Superseded by ISketchManager::CreateCenterLine . |
| Method | CreateCenterLineVB | Creates a center line from P1 to P2 and can be used in Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays. |
| Method | CreateCircle | Obsolete. Superseded by IModelDoc2::CreateCircle2 . |
| Method | CreateCircle2 | Obsolete. Superseded by SketchManager::CreateCircle . |
| Method | CreateCircleByRadius | Obsolete. Superseded by IModelDoc2::CreateCircleByRadius2 . |
| Method | CreateCircleByRadius2 | Obsolete. Superseded by SketchManager::CreateCircleByRadius . |
| Method | CreateCircleDB | Obsolete. Superseded by IModelDoc2::CreateCircle2 . |
| Method | CreateCircleVB | Obsolete. Superseded by IModelDoc2::CreateCircle2 . |
| Method | CreateCircularSketchStepAndRepeat | Obsolete. Superseded by ISketchManager::CreateCircularSketchStepAndRepeat . |
| Method | CreateClippedSplines | Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch. |
| Method | CreateEllipse | Obsolete. Superseded by IModelDoc2::CreateEllipse2 . |
| Method | CreateEllipse2 | Obsolete. Superseded by ISketchManager::CreateEllipse . |
| Method | CreateEllipseVB | Obsolete. Superseded by IModelDoc2::CreateEllipse2 . |
| Method | CreateEllipticalArc2 | Obsolete. Superseded by SketchManager::CreateEllipticalArc . |
| Method | CreateEllipticalArcByCenter | Obsolete. Superseded by SketchManager::CreateEllipticalArc . |
| Method | CreateEllipticalArcByCenterVB | Obsolete. Superseded by SketchManager::CreateEllipticalArc . |
| Method | CreateFeatureMgrView | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | CreateFeatureMgrView2 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | CreateFeatureMgrView3 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | CreateGroup | Creates an annotation group from the currently selected annotations. |
| Method | CreateLine | Obsolete. Superseded by IModelDoc2::CreateLine2 . |
| Method | CreateLine2 | Obsolete. Superseded by SketchManager::CreateLine . |
| Method | CreateLinearSketchStepAndRepeat | Obsolete. Superseded by ISketchManager::CreateLinearSketchStepAndRepeat . |
| Method | CreateLineDB | Obsolete. Superseded by IModelDoc2::CreateLine2 . |
| Method | CreateLineVB | Obsolete. Superseded by IModelDoc2::CreateLine2 . |
| Method | CreatePlaneAtAngle | Obsolete. Superseded by IModelDoc2::CreatePlaneAtAngle3 . |
| Method | CreatePlaneAtAngle2 | Obsolete. Superseded by IModelDoc2::CreatePlaneAtAngle3 . |
| Method | CreatePlaneAtAngle3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneAtOffset | Obsolete. Superseded by IModelDoc2::CreatePlaneAtOffset3 . |
| Method | CreatePlaneAtOffset2 | Obsolete. Superseded by IModelDoc2::CreatePlaneAtOffset3 . |
| Method | CreatePlaneAtOffset3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneAtSurface | Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface3 . |
| Method | CreatePlaneAtSurface2 | Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface3 . |
| Method | CreatePlaneAtSurface3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneFixed | Obsolete. Superseded by IModelDoc2::CreatePlaneFixed2 . |
| Method | CreatePlaneFixed2 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlanePerCurveAndPassPoint | Obsolete. Superseded by IModelDoc2::CreatePlanePerCurveAndPassPoint3 . |
| Method | CreatePlanePerCurveAndPassPoint2 | Obsolete. Superseded by IModelDoc2::CreatePlanePerCurveAndPassPoint3 . |
| Method | CreatePlanePerCurveAndPassPoint3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneThru3Points | Obsolete. Superseded by IModelDoc2::CreatePlaneThru3Points3 . |
| Method | CreatePlaneThru3Points2 | Obsolete. Superseded by IModelDoc2::CreatePlaneThru3Points3 . |
| Method | CreatePlaneThru3Points3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneThruLineAndPt | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePlaneThruPtParallelToPlane | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | CreatePoint | Obsolete. Superseded by IModelDoc2::CreatePoint2 . |
| Method | CreatePoint2 | Obsolete. Superseded by ISketchManager::CreatePoint . |
| Method | CreatePointDB | Obsolete. Superseded by IModelDoc2::CreatePoint2 and IModelDoc2::ICreatePoint2 . |
| Method | CreateSpline | Obsolete. Superseded by ISketchManager::CreateSpline . |
| Method | CreateSplineByEqnParams | Obsolete. Superseded by ISketchManager::CreateSplineByEqnParams . |
| Method | CreateSplinesByEqnParams | Obsolete. Superseded by ISketchManager::CreateSplinesByEqnParams . |
| Method | CreateTangentArc | Obsolete. Superseded by IModelDoc2::CreateTangentArc2 . |
| Method | CreateTangentArc2 | Obsolete. Superseded by ISketchManager::CreateTangentArc . |
| Method | DeActivateFeatureMgrView | Deactivates a tab in the FeatureManager design tree view. |
| Method | DebugCheckIgesGeom | Dumps a IGES geometry check. |
| Method | DeleteAllRelations | Deletes all existing relations. |
| Method | DeleteBendTable | Deletes a bend table. |
| Method | DeleteBkgImage | Deletes any background image. |
| Method | DeleteConfiguration | Obsolete. Superseded by IModelDoc2::DeleteConfiguration2 . |
| Method | DeleteConfiguration2 | Deletes a configuration. |
| Method | DeleteCustomInfo | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | DeleteCustomInfo2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | DeleteDesignTable | Deletes the design table for this document, if one exists. |
| Method | DeleteFeatureMgrView | Obsolete. Superseded by IModelDocExtension::DeleteFeatureMgrViewx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Removes the specified tab in the FeatureManager design tree. |
| Method | DeleteLightSource | Deletes a light source. |
| Method | DeleteNamedView | Deletes the specified model view. |
| Method | DeleteSelection | Obsolete. Superseded by IModelDocExtension::DeleteSelection2 . |
| Method | DeriveSketch | Creates a derived sketch. |
| Method | DeSelectByID | Removes the selected object from the selection list. |
| Method | DimPreferences | Sets dimension preferences. |
| Method | DissolveLibraryFeature | Dissolves the selected library features. |
| Method | DissolveSketchText | Dissolves sketch text. |
| Method | DragTo | Drags the specified end point. |
| Method | DrawLightIcons | Draws any visible light icons. |
| Method | EditBalloonProperties | Obsolete. Superseded by INote::SetBalloon and INote::SetBomBalloonText . |
| Method | EditClearAll | Obsolete. Superseded by IModelDoc2::ClearSelection2 . |
| Method | EditConfiguration | Obsolete. Superseded by IModelDoc2::EditConfiguration3 . |
| Method | EditConfiguration2 | Obsolete. Superseded by IModelDoc2::EditConfiguration3 . |
| Method | EditConfiguration3 | Edits the specified configuration. |
| Method | EditCopy | Copies the currently selected items and places them in the clipboard. |
| Method | EditCut | Cuts the currently selected items and places them on the Microsoft Windows Clipboard. |
| Method | EditDatumTargetSymbol | Edits a datum target symbol. |
| Method | EditDelete | Deletes the selected items. |
| Method | EditDimensionProperties | Obsolete. Superseded by IModelDoc2::EditDimensionProperties3 . |
| Method | EditDimensionProperties2 | Obsolete. Superseded by IModelDoc2::EditDimensionProperties3 . |
| Method | EditDimensionProperties3 | Obsolete. Superseded by IModelDocExtension::EditDimensionProperties . |
| Method | EditOrdinate | Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group. |
| Method | EditRebuild3 | Rebuilds only those features that need to be rebuilt in the active configuration in the model. |
| Method | EditRedo | Obsolete. Superseded by IModelDoc2::EditRedo2 . |
| Method | EditRedo2 | Repeats the specified number of actions in this SOLIDWORKS Design session. |
| Method | EditRollback | Obsolete. Superseded by IFeatureManager::EditRollback . |
| Method | EditRollback2 | Obsolete. Superseded by IFeatureManager::EditRollback . |
| Method | EditRoute | Makes the last selected route the active route. |
| Method | EditSeedFeat | Gets the pattern seed feature, based on the selected face, and displays the Edit Definition dialog for that feature. |
| Method | EditSketch | Allows the currently selected sketch to be edited. |
| Method | EditSketchOrSingleSketchFeature | Edits a selected sketch or feature sketch. |
| Method | EditSuppress | Obsolete. Superseded IModelDoc2::EditSuppress2 . |
| Method | EditSuppress2 | Suppresses the selected feature, the selected component, or the owning feature of the selected face. |
| Method | EditUndo | Obsolete. Superseded by IModelDoc2::EditUndo2 . |
| Method | EditUndo2 | Undoes the specified number of actions in the active SOLIDWORKS Design session. |
| Method | EditUnsuppress | Obsolete. Superseded by IModelDoc2::EditUnsuppress2 . |
| Method | EditUnsuppress2 | Unsuppresses the selected feature or component. |
| Method | EditUnsuppressDependent | Obsolete. Superseded by IModelDoc2::EditUnsuppressDependent2 . |
| Method | EditUnsuppressDependent2 | Unsuppresses the selected feature or component and their dependents. |
| Method | EntityProperties | Displays the Properties dialog for the selected edge or face. |
| Method | EnumModelViews | Gets the model views enumeration in this document. |
| Method | FeatEdit | Puts the current feature into edit mode. |
| Method | FeatEditDef | Displays the Feature Definition dialog and lets the user edit the values. |
| Method | FeatureBoss | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureBoss2 | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureBossThicken | Obsolete. Superseded by IFeatureManager::FeatureBossThicken . |
| Method | FeatureBossThicken2 | Obsolete. Superseded by IFeatureManager::FeatureBossThicken . |
| Method | FeatureBossThin | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureBossThin2 | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureByPositionReverse | Gets the n th from last feature in the document. |
| Method | FeatureChamfer | Creates a chamfer feature. |
| Method | FeatureChamferType | Obsolete. Superseded by IFeatureManager::InsertFeatureChamfer . |
| Method | FeatureCirPattern | Obsolete. Superseded by IFeatureManager::FeatureCircularPattern2 . |
| Method | FeatureCurvePattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks of ICurveDrivenPatternFeatureData . |
| Method | FeatureCut | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | FeatureCut2 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | FeatureCut3 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | FeatureCut4 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | FeatureCut5 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | FeatureCutThicken | Obsolete. Superseded by IFeatureManager::FeatureCutThicken . |
| Method | FeatureCutThicken2 | Obsolete. Superseded by IFeatureManager::FeatureCutThicken . |
| Method | FeatureCutThin | Obsolete. Superseded by IFeatureManager::FeatureCutThin . |
| Method | FeatureCutThin2 | Obsolete. Superseded by IFeatureManager::FeatureCutThin . |
| Method | FeatureExtruRefSurface | Obsolete. Superseded by IModelDoc2::FeatureExtruRefSurface2 . |
| Method | FeatureExtruRefSurface2 | Obsolete. Superseded by IFeatureManager::FeatureExtruRefSurface . |
| Method | FeatureFillet | Obsolete. Superseded by IFeatureManager::FeatureFillet . |
| Method | FeatureFillet2 | Obsolete. Superseded by IFeatureManager::FeatureFillet . |
| Method | FeatureFillet3 | Obsolete. Superseded by IFeatureManager::FeatureFillet . |
| Method | FeatureFillet4 | Obsolete. Superseded by IFeatureManager::FeatureFillet . |
| Method | FeatureFillet5 | Obsolete. Superseded by IFeatureManager::FeatureFillet . |
| Method | FeatureLinearPattern | Obsolete. Superseded by IFeatureManager::FeatureLinearPattern2 . |
| Method | FeatureReferenceCurve | Creates a reference curve feature from an array of curves. |
| Method | FeatureRevolve2 | Obsolete. Superseded by IFeatureManager::FeatureRevolve . |
| Method | FeatureRevolveCut2 | Obsolete. Superseded by IFeatureManager::FeatureRevolveCut . |
| Method | FeatureSketchDrivenPattern | Obsolete. Superseded by IFeatureManager::FeatureSketchDrivenPattern . |
| Method | FileReload | Obsolete. Superseded by IModelDoc2::ReloadOrReplace . |
| Method | FileSummaryInfo | Displays the File Summary Information dialog box for this file. |
| Method | FirstFeature | Gets the first feature in the document. |
| Method | FontBold | Enables or disables bold font style in the selected notes, dimensions, and GTols. |
| Method | FontFace | Changes the font face in the selected notes, dimensions, and GTols. |
| Method | FontItalic | Enables or disables italic font style in the selected notes, dimensions, and GTols. |
| Method | FontPoints | Changes the font height (specified in points) in the selected notes, dimensions, and GTols. |
| Method | FontUnderline | Enables or disables underlining the selected notes, dimensions, and GTols. |
| Method | FontUnits | Changes font height (specified in current system units) in the selected notes, dimensions, and GTols. |
| Method | ForceRebuild3 | Forces a rebuild of all features in the active configuration in the model. |
| Method | ForceReleaseLocks | Releases the locks that a file system places on a file when it is opened and detaches that file from the file system. |
| Method | GetActiveConfiguration | Obsolete. Superseded by IConfigurationManager::ActiveConfiguration . |
| Method | GetActiveSketch | Obsolete. Superseded by IModelDoc2::GetActiveSketch2 . |
| Method | GetActiveSketch2 | Obsolete. Superseded by SketchManager::ActiveSketch . |
| Method | GetAddToDB | Gets whether entities are added directly to the SOLIDWORKS database. |
| Method | GetAmbientLightProperties | Gets the ambient light properties for this model document. |
| Method | GetAngularUnits | Gets the current angular unit settings. |
| Method | GetArcCentersDisplayed | Gets whether the arc centers are displayed. |
| Method | GetBendState | Gets the current bend state of a sheet metal part. |
| Method | GetBlockingState | Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState . |
| Method | GetColorTable | Obsolete. Superseded by ISldWorks::GetColorTable . |
| Method | GetConfigurationByName | Gets the specified configuration. |
| Method | GetConfigurationCount | Gets the number of configurations. |
| Method | GetConfigurationNames | Gets the names of the configurations in this document. |
| Method | GetConsiderLeadersAsLines | Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document. |
| Method | GetCoordinateSystemXformByName | Obsolete. Superseded by IModelDocExtension::GetCoordinateSystemTransformByName . |
| Method | GetCurrentCoordinateSystemName | Gets the name of the current coordinate system or an empty string for the default coordinate system. |
| Method | GetCustomInfoCount | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoCount2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoNames | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoNames2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoType | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoType2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoType3 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetCustomInfoValue | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | GetDefaultTextHeight | Gets the default text height in use for this document. |
| Method | GetDependencies | Obsolete. Superseded by IModelDoc2::GetDependencies2 . |
| Method | GetDependencies2 | Obsolete. Superseded by IModelDocExtension::GetDependencies . |
| Method | GetDesignTable | Gets the design table associated with this part or assembly document. |
| Method | GetDetailingDefaults | Obsolete. Superseded by IModelDoc2::GetUserPreferenceTextFormat and IModelDoc2::SetUserPreferenceTextFormat . |
| Method | GetDirectionLightProperties | Gets the directional light properties. |
| Method | GetDisplayWhenAdded | Gets whether new sketch entities are displayed when created. |
| Method | GetEntityName | Gets the name of the specified face, edge, or vertex. |
| Method | GetEquationMgr | Gets the equation manager. |
| Method | GetExternalReferenceName | Gets the name of the externally referenced document (in the case of a join or mirrored part). |
| Method | GetFeatureCount | Gets the number of features in this document. |
| Method | GetFeatureManagerWidth | Gets the width of the FeatureManager design tree. |
| Method | GetFirstAnnotation | Obsolete. Superseded by IModelDoc2::GetFirstAnnotation2 . |
| Method | GetFirstAnnotation2 | Gets the first annotation in the model. |
| Method | GetFirstModelView | Gets the first view in a model document. |
| Method | GetGridSettings | Gets the current grid settings. |
| Method | GetInferenceMode | Obsolete. Superseded by SketchManager::InferenceMode . |
| Method | GetLayerManager | Gets the layer manager for the current drawing document. |
| Method | GetLightSourceCount | Gets the number of light sources. |
| Method | GetLightSourceExtProperty | Gets a float, string, or integer value stored for the light source. |
| Method | GetLightSourceIdFromName | Gets the ID of the specified light source. |
| Method | GetLightSourceName | Gets the name of a light source used internally by the SOLIDWORKS Design application. |
| Method | GetLineCount | Gets the number of lines in the current sketch. |
| Method | GetLines | Gets all of the lines in the current sketch. |
| Method | GetMassProperties | Obsolete. Superseded by IModelDocExtension::GetMassProperties and IModelDocExtension::IGetMassProperties . |
| Method | GetMassProperties2 | Obsolete. Superseded by IModelDocExtension::GetMassProperties and IModelDocExtension::IGetMassProperties . |
| Method | GetModelViewCount | Obsolete. Superseded by IModelDocExtension::GetModelViewCount . |
| Method | GetModelViewNames | Gets a list containing the names of each model view in this document. |
| Method | GetNext | Gets the next document opened in the current SOLIDWORKS Design session. |
| Method | GetNumDependencies | Gets the number of strings returned by IModelDoc2::GetDependencies2 . |
| Method | GetPathName | Gets the full path name for this document, including the file name. |
| Method | GetPointLightProperties | Gets point light properties. |
| Method | GetPopupMenuMode | Gets the current pop-up menu mode. |
| Method | GetPropertyExtension | Gets the specified property extension on this model. |
| Method | GetPropertyManagerPage | Obsolete. Superseded by ISldWorks::CreatePropertyManagerPage and ISldWorks::ICreatePropertyManagerPage . |
| Method | GetRayIntersectionsPoints | Gets the intersection point information generated by IModelDoc2::RayIntersections . |
| Method | GetRayIntersectionsTopology | Gets the topology intersections generated by IModelDoc2::RayIntersections . |
| Method | GetSaveFlag | Gets whether the document is currently dirty and needs to be saved. |
| Method | GetSceneBkgDIB | Obsolete. Superseded by IModelDocExtension::GetSceneBkgDIBx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets background image as a LPDIBSECTION. |
| Method | GetSceneExtProperty | Gets a float, string, or integer value stored for the scene. |
| Method | GetSpotlightProperties | Gets the spotlight properties. |
| Method | GetStandardViewRotation | Gets the specified view orientation matrix with respect to the Front view. |
| Method | GetTessellationQuality | Gets the shaded-display image quality number for the current document. |
| Method | GetTitle | Gets the title of the document that appears in the active window's title bar. |
| Method | GetToolbarVisibility | Gets the visibility of a toolbar. |
| Method | GetType | Gets the type of the document. |
| Method | GetUnits | Gets the current unit settings, fraction base, fraction value, and significant digits. |
| Method | GetUpdateStamp | Gets the current update stamp for this document. |
| Method | GetUserPreferenceDoubleValue | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceDouble . |
| Method | GetUserPreferenceIntegerValue | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceInteger . |
| Method | GetUserPreferenceStringValue | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceString . |
| Method | GetUserPreferenceTextFormat | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceTextFormat . |
| Method | GetUserPreferenceToggle | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceToggle . |
| Method | GetUserUnit | Gets this document's units settings. |
| Method | GetVisibilityOfConstructPlanes | Gets whether construction (reference) planes are currently visible. |
| Method | GetZebraStripeData | Gets zebra line data. |
| Method | GraphicsRedraw | Obsolete. Superseded by IModelDoc2::GraphicsRedraw2 . |
| Method | GraphicsRedraw2 | Obsolete. Superseded by IModelView::GraphicsRedraw and IModelView::IGraphicsRedraw . |
| Method | GridOptions | Obsolete. Superseded by ISketchManager::SetGridOptions . |
| Method | HideComponent2 | Hides the selected component. |
| Method | HideCosmeticThread | Hides the selected cosmetic thread. |
| Method | HideDimension | Hides the selected dimension in this document. |
| Method | HideFeatureDimensions | Obsolete. Superseded by IModelDoc2::GetUserPreferenceToggle or IModelDoc2::SetUserPreferenceToggle and swDisplayFeatureDimensions. |
| Method | HideShowBodies | Sets whether to hide or show the bodies in the model. |
| Method | HideSolidBody | Hides the currently selected solid body. |
| Method | HoleWizard | Obsolete. Superseded by IFeatureManager::HoleWizard2 . |
| Method | IAddConfiguration3 | Adds a new configuration to this model document. |
| Method | IAddDiameterDimension2 | Adds a diameter dimension at the specified location for the selected item. |
| Method | IAddDimension2 | Obsolete. Superseded by IModelDocExtension::AddDimension . |
| Method | IAddHorizontalDimension2 | Creates a horizontal dimension for the current selected entities at the specified location. |
| Method | IAddOrEditConfiguration | Obsolete. Superseded by IConfiguraiton::GetParameters , IConfiguration::IGetParameters , IConfiguration::ISetParameters , and IConfiguration::SetParameters . |
| Method | IAddRadialDimension2 | Adds a radial dimension at the specified location for the selected item. |
| Method | IAddVerticalDimension2 | Creates a vertical dimension for the currently selected entities at the specified location. |
| Method | IClosestDistance | Calculates the distance and closest points between two geometric objects. |
| Method | ICreateArc | Obsolete. Superseded by IModelDoc2::ICreateArc2 . |
| Method | ICreateArc2 | Creates an arc based on a center point, a start, an end point, and a direction. |
| Method | ICreateCenterLine | Creates a center line from P1 to P2. |
| Method | ICreateCircle2 | Creates a circle based on a center point and a point on the circle. |
| Method | ICreateCircleByRadius | Obsolete. Superseded by IModelDoc2::ICreateCircleByRadius2 . |
| Method | ICreateCircleByRadius2 | Creates a circle based on a center point and a specified radius. |
| Method | ICreateClippedSplines | Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch. |
| Method | ICreateEllipse | Obsolete. Superseded by IModelDoc2::ICreateEllipse2 . |
| Method | ICreateEllipse2 | Creates an ellipse using the specified center point and points. |
| Method | ICreateEllipticalArc2 | Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points. |
| Method | ICreateEllipticalArcByCenter | Creates an elliptical arc trimmed between two points. |
| Method | ICreateFeatureMgrView | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | ICreateFeatureMgrView2 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | ICreateFeatureMgrView3 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | ICreateLine | Obsolete. Superseded by IModelDoc2::ICreateLine2 . |
| Method | ICreateLine2 | Creates a sketch line in the currently active 2D or 3D sketch. |
| Method | ICreatePlaneAtAngle2 | Obsolete. Superseded by IModelDoc2::ICreatePlaneAtAngle3 . |
| Method | ICreatePlaneAtAngle3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneAtOffset2 | Obsolete. Superseded by IModelDoc2::ICreatePlaneAtOffset3 . |
| Method | ICreatePlaneAtOffset3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneAtSurface2 | Obsolete. Superseded by IModelDoc2::ICreatePlaneAtSurface3 . |
| Method | ICreatePlaneAtSurface3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneFixed | Obs olete. Superseded by IModelDoc2::ICreatePlaneFixed2 . |
| Method | ICreatePlaneFixed2 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlanePerCurveAndPassPoint2 | Obsolete. Superseded by IModelDoc2::ICreatePlanePerCurveAndPassPoint3 . |
| Method | ICreatePlanePerCurveAndPassPoint3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneThru3Points2 | Obsolete. Superseded by IModelDoc2::ICreatePlaneThru3Points3 . |
| Method | ICreatePlaneThru3Points3 | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneThruLineAndPt | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePlaneThruPtParallelToPlane | Obsolete. Superseded by IFeatureManager::InsertRefPlane . |
| Method | ICreatePoint2 | Obsolete. Superseded by ISketchManager::CreatePoint . |
| Method | ICreateSpline | Obsolete. Superseded by ISketchManager::ICreateSpline . |
| Method | ICreateSplineByEqnParams | Obsolete. Superseded by ISketchManager::ICreateSplineByEqnParams . |
| Method | ICreateSplinesByEqnParams | Obsolete. Superseded by ISketchManager::ICreateSplinesByEqnParams . |
| Method | IEditDimensionProperties3 | Obsolete. Superseded by IModelDocExtension::IEditDimensionProperties . |
| Method | IFeatureByPositionReverse | Gets the n th from last feature in the document. |
| Method | IFeatureFillet2 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | IFeatureFillet3 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | IFeatureFillet4 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | IFeatureFillet5 | Obsolete. Superseded by IFeatureManager::FeatureCut . |
| Method | IFeatureReferenceCurve | Creates a reference curve feature from an array of curves. |
| Method | IFirstFeature | Gets the first feature in the document. |
| Method | IGet3rdPartyStorage | Gets the IStream interface to the specified third-party stream inside this SOLIDWORKS Design document. |
| Method | IGetActiveConfiguration | Obsolete. Superseded by IConfigurationManager::ActiveConfiguration . |
| Method | IGetActiveSketch | Obsolete. Superseded by IModelDoc2::IGetActiveSketch2 . |
| Method | IGetActiveSketch2 | Gets the active sketch. |
| Method | IGetAngularUnits | Gets the current angular unit settings. |
| Method | IGetColorTable | Obsolete. Superseded by ISldWorks::IGetColorTable . |
| Method | IGetConfigurationByName | Gets the specified configuration. |
| Method | IGetConfigurationNames | Gets the names of the configurations in this document. |
| Method | IGetCoordinateSystemXformByName | Obsolete. Superseded by IModelDocExtension::GetCoordinateSystemTransformByName . |
| Method | IGetCustomInfoNames | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | IGetCustomInfoNames2 | Obsolete. Superseded by IModelDocExtension::CustomPropertyManager . |
| Method | IGetDependencies | Obsolete. Superseded by IModelDoc2::GetDependencies2 . |
| Method | IGetDependencies2 | Gets all of the model's dependencies. |
| Method | IGetDesignTable | Gets the design table associated with this part or assembly document. |
| Method | IGetDetailingDefaults | Obsolete. Superseded by IModelDoc2::GetUserPreferenceTextFormat and IModelDoc2::SetUserPreferenceTextFormat . |
| Method | IGetEntityName | Gets the name of the specified face, edge, or vertex. |
| Method | IGetFirstAnnotation | Obsolete. Superseded by IModelDoc2::IGetFirstAnnotation2 . |
| Method | IGetFirstAnnotation2 | Gets the first annotation in the model. |
| Method | IGetFirstModelView | Gets the first view in a model document. |
| Method | IGetLayerManager | Gets the layer manager ofr the current drawing document. |
| Method | IGetLines | Gets all of the lines in the current sketch. |
| Method | IGetMassProperties | Obsolete. Superseded by IModelDocExtension::IGetMassProperties . |
| Method | IGetMassProperties2 | Obsolete. Superseded by IModelDocExtension::IGetMassProperties . |
| Method | IGetModelViewNames | Gets a list containing the names of each model view in this document. |
| Method | IGetNext | Gets the next document opened in the current SOLIDWORKS Design session. |
| Method | IGetNumDependencies | Obsolete. Superseded by IModelDoc2::IGetNumDependencies2 . |
| Method | IGetNumDependencies2 | Gets the number of strings returned by IModelDoc2::IGetDependencies2 . |
| Method | IGetRayIntersectionsPoints | Gets the intersection point information generated by IModelDoc2::IRayIntersections . |
| Method | IGetRayIntersectionsTopology | Gets the topology intersections generated by IModelDoc2::IRayIntersections . |
| Method | IGetStandardViewRotation | Gets the specified view orientation matrix with respect to the Front view. |
| Method | IGetUnits | Gets the current unit settings, fraction base, fraction value, and significant digits. |
| Method | IGetUserPreferenceTextFormat | Obsolete. Superseded by IModelDocExtension::GetUserPreferenceTextFormat . |
| Method | IGetUserUnit | Gets this document's units settings. |
| Method | IGetVersionHistoryCount | Gets the size of the array required to hold data returend by IModleDoc2::IVersionHistory . |
| Method | IInsertBOMBalloon2 | Obsolete. Superseded by IModelDocExtension::InsertBOMBalloon . |
| Method | IInsertDatumTag2 | Inserts a datum tag symbol at the selected location. |
| Method | IInsertGtol | Creates a new geometric tolerance symbol (GTol) in this document. |
| Method | IInsertMacroFeature | Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3 . |
| Method | IInsertMidSurfaceExt | Obsolete. Superseded by IFeatureManager::IInsertMidSurface . |
| Method | IInsertNote | Inserts a note in this document. |
| Method | IInsertProjectedSketch2 | Projects the selected sketch items from the current sketch onto a selected surface. |
| Method | IInsertSheetMetalEdgeFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2 . |
| Method | IInsertSketchForEdgeFlange | Inserts a sketch for IFeatureManager::InsertSheetMetalEdgeFlange2 in this sheet metal part. |
| Method | IInsertSketchText | Obsolete. Superseded by IModelDoc2::InsertSketchText . |
| Method | IInsertWeldSymbol3 | Inserts a weld symbol into the model. |
| Method | IListAuxiliaryExternalFileReferences | Gets the names of auxiliary external file references for this model. |
| Method | IListExternalFileReferences | Obsolete. Superseded by IModelDocExtension::ListExternalReferences . |
| Method | IListExternalFileReferences2 | Obsolete. Superseded by IModelDocExtension::ListExternalReferences . |
| Method | IMultiSelectByRay | Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius. |
| Method | Insert3DSketch | Obsolete. Superseded by IModelDoc2::Insert3DSketch2 . |
| Method | Insert3DSketch2 | Obsolete. Superseded by ISketchManager::Insert3DSketch . |
| Method | Insert3DSplineCurve | Inserts a 3D-spline curve through the selected reference points. |
| Method | InsertAxis | Obsolete. Superseded by IModelDoc2::InsertAxis2 . |
| Method | InsertAxis2 | Inserts a reference axis based on the currently selected items with an option to automatically size the axis. |
| Method | InsertBendTableEdit | Inserts a bend table and puts the bend table into its edit state. |
| Method | InsertBendTableNew | Inserts a new bend table into the model document. |
| Method | InsertBendTableOpen | Inserts an existing bend table from a file into this model document. |
| Method | InsertBkgImage | Inserts the scene background image. |
| Method | InsertBOMBalloon | Obsolete. Superseded by IModelDoc2::InsertBOMBalloon2 . |
| Method | InsertBOMBalloon2 | Obsolete. Superseded by IModelDocExtension::InsertBOMBalloon . |
| Method | InsertCompositeCurve | Inserts a composite curve based on selections. |
| Method | InsertConnectionPoint | Adds a connection point based on the selected point and selected planar item. |
| Method | InsertCoordinateSystem | Obsolete. Superseded by IFeatureManager::InsertCoordinateSystem . |
| Method | InsertCosmeticThread | Obsolete. Superseded by IFeatureManager::InsertCosmeticThread2 . |
| Method | InsertCurveFile | Creates a curve. |
| Method | InsertCurveFileBegin | Creates a curve. |
| Method | InsertCurveFileEnd | Creates a curve. |
| Method | InsertCurveFilePoint | Creates a point for a curve. |
| Method | InsertCutBlend | Obsolete. Superseded by IFeatureManager::InsertCutBlend . |
| Method | InsertCutBlend2 | Obsolete. Superseded by IFeatureManager::InsertCutBlend . |
| Method | InsertCutBlend3 | Obsolete. Superseded by IFeatureManager::InsertCutBlend . |
| Method | InsertCutBlend4 | Obsolete. Superseded by IFeatureManager::InsertCutBlend . |
| Method | InsertCutSurface | Obsolete. Superseded by IFeatureManager::InsertCutSurface . |
| Method | InsertCutSwept | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertCutSwept2 | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertCutSwept3 | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertCutSwept4 | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertDatumTag2 | Inserts a datum tag symbol at a selected location. |
| Method | InsertDatumTargetSymbol | Obsolete. Superseded by IModelDocExtension::InsertDatumTargetSymbol2 . |
| Method | InsertDeleteFace | Obsolete. Supserseded by IModelDoc2::InsertDeleteFace2 . |
| Method | InsertDeleteFace2 | Obsolete. Superseded by IModelDocExtension::InsertDeleteFace . |
| Method | InsertDeleteHole | Obsolete. Supserseded by IFeatureManager::InsertDeleteHoleForSurface . |
| Method | InsertDome | Inserts a dome. |
| Method | InsertExtendSurface | Extends a surface along the selected faces or edges. |
| Method | InsertFamilyTableEdit | Edits an open design table from Microsoft Excel. |
| Method | InsertFamilyTableNew | Inserts an existing design table from the model into the selected drawing view. |
| Method | InsertFamilyTableOpen | Inserts the specified Microsoft Excel design table. |
| Method | InsertFeatureReplaceFace | Creates a Replace Face feature. |
| Method | InsertFeatureShell | Creates a shell feature. |
| Method | InsertFeatureShellAddThickness | Adds thickness to a face in a multi-thickness shell feature. |
| Method | InsertFramePoint | Obsolete. Not superseded. |
| Method | InsertGtol | Creates a new geometric tolerance symbol (GTol) in this document. |
| Method | InsertHatchedFace | Hatches the selected faces or closed sketch segments in a drawing. |
| Method | InsertHelix | Creates a constant-pitch helix or spiral. |
| Method | InsertLibraryFeature | Obsolete . See Remarks . |
| Method | InsertLoftRefSurface | Obsolete. Superseded by IModelDoc2::InsertLoftRefSurface2 . |
| Method | InsertLoftRefSurface2 | Creates a loft surface from the selected profiles, centerline, and guide curves. |
| Method | InsertMacroFeature | Obsolete. Superseded by IFeatureManager::InsertMacroFeature3 . |
| Method | InsertMfDraft | Obsolete. Superseded by IFeatureManager::InsertMultifaceDraft . |
| Method | InsertMfDraft2 | Obsolete. Superseded by IFeatureManager::InsertMultifaceDraft . |
| Method | InsertMidSurfaceExt | Obsolete. Superseded by IFeatureManager::InsertMidSurface . |
| Method | InsertNewNote3 | Creates a new note. |
| Method | InsertNote | Inserts a note in this document. |
| Method | InsertObject | Activates the Microsoft Insert Object dialog. |
| Method | InsertObjectFromFile | Obsolete. Superseded by IModelDocExtension::InsertObjectFromFile . |
| Method | InsertOffsetSurface | Inserts an offset surface. |
| Method | InsertPlanarRefSurface | Inserts a planar reference surface. |
| Method | InsertPoint | Inserts a point in this model document. |
| Method | InsertProjectedSketch | Obsolete. Superseded by IModelDoc2::InsertProjectedSketch2 . |
| Method | InsertProjectedSketch2 | Obsolete. See IProjectionCurveFeatureData and IFeatureManager::CreateDefinition . |
| Method | InsertProtrusionBlend | Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend . |
| Method | InsertProtrusionBlend2 | Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend . |
| Method | InsertProtrusionBlend3 | Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend . |
| Method | InsertProtrusionBlend4 | Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend . |
| Method | InsertProtrusionSwept | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertProtrusionSwept2 | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertProtrusionSwept3 | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertProtrusionSwept4 | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertRadiateSurface | Creates a radiate surface based on the selections. |
| Method | InsertRefPoint | Inserts a reference point based on the current selections. |
| Method | InsertRevolvedRefSurface | Obsolete. Superseded by IFeatureManager::InsertRevolvedRefSurface . |
| Method | InsertRib | Obsolete. Superseded by IModelDoc2::InsertRib2 . |
| Method | InsertRib2 | Obsolete. Superseded by IFeatureManager::InsertRib . |
| Method | InsertRip | Creates a rip feature. |
| Method | InsertRoutePoint | Adds a route point based on the selected point. |
| Method | InsertScale | Obsolete. Superseded by IFeatureManager::InsertScale . |
| Method | InsertSewRefSurface | Obsolete. Superseded by IFeatureManager::InsertSewRefSurface . |
| Method | InsertSheetMetal3dBend | Obsolete. Superseded by IFeatureManager::InsertSheetMetal3dBend . |
| Method | InsertSheetMetalBaseFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalBaseFlange . |
| Method | InsertSheetMetalBreakCorner | Inserts a break corner into a sheet metal part. |
| Method | InsertSheetMetalClosedCorner | Inserts a sheet metal closed corner into this model document. |
| Method | InsertSheetMetalEdgeFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2 . |
| Method | InsertSheetMetalFold | Inserts a fold feature at the selected objects. |
| Method | InsertSheetMetalHem | Obsolete. Superseded by IFeatureManager::InsertSheetMetalHem . |
| Method | InsertSheetMetalJog | Inserts a sheet metal jog in the current model document. |
| Method | InsertSheetMetalMiterFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalMiterFlange . |
| Method | InsertSheetMetalUnfold | Inserts an unfold feature at the selected objects. |
| Method | InsertSketch | Obsolete. Superseded by ISketchManager::InsertSketch . |
| Method | InsertSketch2 | Obsolete. Superseded by ISketchManager::InsertSketch . |
| Method | InsertSketchForEdgeFlange | Inserts a profile sketch of an edge flange in this sheet metal part. |
| Method | InsertSketchPicture | Inserts a picture into the current sketch. |
| Method | InsertSketchPictureData | Obsolete. Superseded by IModelDoc2::InsertSketchPictureDatax64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Inserts a picture into the current sketch. |
| Method | InsertSketchPictureDatax64 | Inserts a picture into the current sketch in 64-bit applications. |
| Method | InsertSketchText | Inserts sketch text. |
| Method | InsertSplinePoint | Inserts a spline point. |
| Method | InsertSplitLineProject | Splits a face by projecting sketch lines onto the face. |
| Method | InsertSplitLineSil | Splits a face by creating split lines along the silhouette of the selected faces. |
| Method | InsertStackedBalloon | Obsolete. Superseded by IModelDocExtension::InsertStackedBalloon . |
| Method | InsertSurfaceFinishSymbol2 | Obsolete. Superseded by IModelDocExtension::InsertSurfaceFinishSymbol3 . |
| Method | InsertSweepRefSurface | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertSweepRefSurface2 | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept3 . |
| Method | InsertWeldSymbol2 | Obsolete. Superseded by IModelDoc2::InsertWeldSymbol3 . |
| Method | InsertWeldSymbol3 | Inserts a weld symbol into the model. |
| Method | InspectCurvature | Adds curvature combs to the selected sketch segment. |
| Method | IParameter | Gets the specified parameter. |
| Method | IRayIntersections | Obsolete. Superseded by IModelDocExtension::RayIntersections . |
| Method | IRelease3rdPartyStorage | Releases the specified third-party stream. |
| Method | IsActive | Gets whether the specified assembly component is shown or hidden in this model document. |
| Method | IsEditingSelf | Gets whether this model is being edited in the context of another document. |
| Method | ISelectByRay | Obsolete. Superseded by IModelDocExtension::SelectByRay . |
| Method | ISetAngularUnits | Sets the current angular units. |
| Method | ISetNextSelectionGroupId | Sets the group ID for all remaining selections. |
| Method | ISetUserPreferenceTextFormat | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceTextFormat . |
| Method | IsExploded | Obsolete. Superseded by IModelDocExtension::IsExploded . |
| Method | ISketchSplineByEqnParams | Creates a spline on the active 2D sketch using the specified b-curve parameters. |
| Method | IsLightLockedToModel | Gets whether the specified light is fixed. |
| Method | IsOpenedReadOnly | Gets whether a SOLIDWORKS document is open in read-only mode. |
| Method | IsOpenedViewOnly | Gets whether a SOLIDWORKS document is open in view-only mode. |
| Method | IsTessellationValid | Gets whether the current set of facets is valid. |
| Method | IVersionHistory | Gets an array of strings indicating the versions in which this model document was saved, including the SOLIDWORKS Design version in which the model document is currently opened and which is the last value returned in the array. |
| Method | LBDownAt | Generates a left mouse button press (down) event. |
| Method | LBUpAt | Generates a left-mouse button release (up) event. |
| Method | Lights | Obsolete. Not superseded. |
| Method | ListAuxiliaryExternalFileReferences | Gets the names of auxiliary external file references for this model. |
| Method | ListAuxiliaryExternalFileReferencesCount | Gets the number of auxiliary external file references for this model. |
| Method | ListExternalFileReferences | Obsolete. Superseded by IModelDocExtension::ListExternalReferences . |
| Method | ListExternalFileReferences2 | Obsolete. Superseded by IModelDocExtension::ListExternalReferences . |
| Method | ListExternalFileReferencesCount | Obsolete. Superseded by IModelDocExtension::ListExternalFileReferenceCount . |
| Method | ListExternalFileReferencesCount2 | Obsolete. Superseded by IModelDocExtension::ListExternalFileReferenceCount . |
| Method | Lock | Blocks the modifying commands in the user interface, effectively locking the application. |
| Method | LockAllExternalReferences | Locks all external references. |
| Method | LockFramePoint | Obsolete. Not superseded. |
| Method | LockLightToModel | Locks or unlocks the specified light. |
| Method | MoldDraftAnalysis | Performs a mold draft analysis. |
| Method | MultiSelectByRay | Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius. |
| Method | NameView | Creates a named view using the current view. |
| Method | ObjectDisplayAsIcon | Shows the current OLE object as an icon. |
| Method | ObjectDisplayContent | Shows the current OLE object's content. |
| Method | ObjectResetsize | Sets the size of the current OLE object to the default. |
| Method | Parameter | Gets the specified parameter. |
| Method | ParentChildRelationship | Shows the Parent/Child Relationships dialog for the selected feature. |
| Method | Paste | Pastes the contents of the Microsoft Windows Clipboard at the current insertion point. |
| Method | PostTrimSurface | Obsolete. Superseded by IFeatureManager::PostTrimSurface . |
| Method | PreTrimSurface | Obsolete. Superseded by IFeatureManager::PreTrimSurface . |
| Method | PrintDirect | Prints the current document to the default printer. |
| Method | PrintOut | Obsolete. Superseded by IModelDocExtension::PrintOut2 and IModelDocExtension::IPrintOut2 . |
| Method | PrintOut2 | Obsolete. Superseded by IModelDocExtension::PrintOut2 and IModelDocExtension::IPrintOut2 . |
| Method | PrintPreview | Displays the Print Preview page for the current document. |
| Method | PropertySheet | Displays the the selected object's property sheet. |
| Method | Quit | Closes the active document without saving changes (see Remarks ). |
| Method | RayIntersections | Obsolete. Superseded by IModelDocExtension::RayIntersections . |
| Method | ReattachOrdinate | Reattaches an ordinate dimension to a different entity. |
| Method | Rebuild | Obsolete. Superseded by IModelDocExtension::Rebuild . |
| Method | ReloadOrReplace | Obsolete. Superseded by IModelDocExtension::ReloadOrReplace . |
| Method | RemoveGroups | Removes any annotation groups in the current selection. |
| Method | RemoveInspectCurvature | Removes curvature combs from the selected curved sketch segment. |
| Method | RemoveItemsFromGroup | Removes the selected annotations from their annotation groups. |
| Method | ResetBlockingState | Resets the blocking state for the SOLIDWORKS menus. |
| Method | ResetLightSourceExtProperty | Resets the properties for a light source. |
| Method | ResetPropertyExtension | Clears all values stored in the property extension. |
| Method | ResetSceneExtProperty | Resets the extension property for a scene. |
| Method | Save | Obsolete. Superseded by IModelDoc2::Save3 . |
| Method | Save2 | Obsolete. Superseded by IModelDoc2::Save3 . |
| Method | Save3 | Saves the current document. |
| Method | SaveAs | Obsolete. Superseded by IModelDocExtension::SaveAs . |
| Method | SaveAs2 | Obsolete. Superseded by IModelDocExtension::SaveAs . |
| Method | SaveAs3 | Obsolete. Superseded by IModelDocExtension::SaveAs . |
| Method | SaveAs4 | Obsolete. Superseded by IModelDocExtension::SaveAs . |
| Method | SaveAsSilent | Obsolete. Superseded by IModelDocExtension::SaveAs . |
| Method | SaveBMP | Saves the current view as a bitmap (BMP) file. |
| Method | SaveSilent | Obsolete. Superseded by IModelDoc2::Save3 . |
| Method | Scale | Scales the part. |
| Method | ScreenRotate | Switches between model and screen center rotation. |
| Method | Select | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectAt | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectByID | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectByMark | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectByName | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectByRay | Obsolete. Superseded by IModelDocExtension::SelectByRay . |
| Method | SelectedEdgeProperties | Sets the property values of the selected edge. |
| Method | SelectedFaceProperties | Sets the material property values of the selected face. |
| Method | SelectedFeatureProperties | Sets the property values of the selected feature. |
| Method | SelectLoop | Selects the loop that corresponds to the selected edge. |
| Method | SelectMidpoint | Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected. |
| Method | SelectSketchArc | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectSketchItem | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectSketchLine | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectSketchPoint | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectSketchSpline | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectTangency | Selects all faces tangent to the selected face. |
| Method | SetAddToDB | Obsolete. Superseded by ISketchManager::AddToDB . |
| Method | SetAmbientLightProperties | Sets ambient light properties. |
| Method | SetAngularUnits | Sets the current angular units. |
| Method | SetArcCentersDisplayed | Sets the current arc centers displayed setting. |
| Method | SetBendState | Sets the bend state of a sheet metal part. |
| Method | SetBlockingState | Sets the blocking state for the SOLIDWORKS menus. |
| Method | SetConsiderLeadersAsLines | Sets a flag on the document that indicates whether the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document. |
| Method | SetDirectionLightProperties | Sets direction light properties. |
| Method | SetDisplayWhenAdded | Obsolete. Superseded by ISketchManager::DisplayWhenAdded . |
| Method | SetFeatureManagerWidth | Sets the width of the FeatureManager design tree. |
| Method | SetInferenceMode | Obsolete. Superseded by SketchManager::InferenceMode . |
| Method | SetLightSourceName | Sets the light source name used internally by the SOLIDWORKS Design software. |
| Method | SetLightSourcePropertyValuesVB | Sets the light source property values. |
| Method | SetParamValue | Sets the value of selected dimension (or parameter). |
| Method | SetPickMode | Returns the user to the default selection mode. |
| Method | SetPointLightProperties | Sets point light properties. |
| Method | SetPopupMenuMode | Sets the pop-up menu mode. |
| Method | SetReadOnlyState | Sets whether this document is read-only or read-write. |
| Method | SetSaveAsFileName | Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog. |
| Method | SetSaveFlag | Flags the document as dirty. |
| Method | SetSceneBkgDIB | Obsolete. Superseded by IModelDocExtension::SetSceneBkgDIBx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Sets background image described by DIBSECTION data. |
| Method | SetSpotlightProperties | Sets the spotlight properties. |
| Method | SetTessellationQuality | Sets the shaded-display image quality number for the current document. |
| Method | SetTitle2 | Sets the title of a new document. |
| Method | SetToolbarVisibility | Sets the visibility of a toolbar. |
| Method | SetUnits | Sets the units used by the end-user for the model. |
| Method | SetUserPreferenceDoubleValue | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceDouble . |
| Method | SetUserPreferenceIntegerValue | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceInteger . |
| Method | SetUserPreferenceStringValue | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceString . |
| Method | SetUserPreferenceTextFormat | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceTextFormat . |
| Method | SetUserPreferenceToggle | Obsolete. Superseded by IModelDocExtension::SetUserPreferenceToggle . |
| Method | SetZebraStripeData | Sets the zebra-line data. |
| Method | ShowComponent2 | Shows the selected component. |
| Method | ShowConfiguration | Obsolete. Superseded by IModelDoc2::ShowConfiguration2 . |
| Method | ShowConfiguration2 | Shows the named configuration by switching to that configuration and making it the active configuration. |
| Method | ShowCosmeticThread | Shows the selected cosmetic thread. |
| Method | ShowFeatureDimensions | Obsolete. Superseded by IModelDoc2::GetUserPreferenceToggle and IModelDoc2::SetUserPreferenceToggle and swDisplayFeatureDimensions. |
| Method | ShowNamedView | Obsolete. Superseded by IModelDoc2::ShowNameView2 . |
| Method | ShowNamedView2 | Shows the specified view. |
| Method | ShowSolidBody | Shows the selected solid body. |
| Method | SimpleHole | Obsolete. Superseded by IFeatureManager::SimpleHole . |
| Method | SimpleHole2 | Obsolete. Superseded by IFeatureManager::SimpleHole . |
| Method | SimpleHole3 | Obsolete. Superseded by IFeatureManager::SimpleHole . |
| Method | SimplifySpline | Obsolete. Superseded by ISketchSpline::Simplify . |
| Method | Sketch3DIntersections | Creates new sketch segments based on the selected surfaces. |
| Method | SketchAddConstraints | Adds the specified constraint to the selected entities. |
| Method | SketchAlign | Aligns the selected sketch entities. |
| Method | SketchArc | Creates an arc in the current model document. |
| Method | SketchCenterline | Adds a centerline to the current model document. |
| Method | SketchChamfer | Obsolete. Superseded by ISketchManager::CreateChamfer . |
| Method | SketchCircle | Obsolete. Superseded by IModelDoc2::CreateCircle2 . |
| Method | SketchConstrainCoincident | Makes the selected sketch entities coincident. |
| Method | SketchConstrainConcentric | Makes the selected sketch entities concentric. |
| Method | SketchConstrainParallel | Makes the selected sketch entities parallel. |
| Method | SketchConstrainPerp | Makes the selected sketch entities perpendicular. |
| Method | SketchConstrainTangent | Makes the selected entities tangent. |
| Method | SketchConstraintsDel | Deletes the specified relationship (constraint) on the currently selected sketch item. |
| Method | SketchConstraintsDelAll | Deletes all of the constraints on the currently selected sketch segment. |
| Method | SketchConvertIsoCurves | Converts ISO-parametric curves on a selected surface into a sketch entity. |
| Method | SketchFillet | Obsolete. Superseded by IModelDoc2::SketchFillet2 . |
| Method | SketchFillet1 | Obsolete. Superseded by IModelDoc2::SketchFillet2 . |
| Method | SketchFillet2 | Obsolete. Superseded by ISketchManager::CreateFillet . |
| Method | SketchMirror | Creates new entities that are mirror images of the selected entities. |
| Method | SketchModifyFlip | Flips the the active or selected sketch about the specified coordinate system axis. |
| Method | SketchModifyRotate | Rotates the coordinate system of the active or selected sketch. |
| Method | SketchModifyScale | Scales the active or selected sketch. |
| Method | SketchModifyTranslate | Translates the coordinate system of the active or selected sketch. |
| Method | SketchOffset | Obsolete. Superseded by IModelDoc2::SketchOffset2 . |
| Method | SketchOffset2 | Obsolete. Superseded by ISketchManager::SketchOffset . |
| Method | SketchOffsetEdges | Offsets the edges of the selected entities. |
| Method | SketchOffsetEntities | Obsolete. Superseded by IModelDoc2::SketchOffsetEntities2 . |
| Method | SketchOffsetEntities2 | Generates entities in the active sketch by offsetting the selected geometry by the specified amount. |
| Method | SketchParabola | Obsolete. Superseded by ISketchManager::CreateParabola . |
| Method | SketchPoint | Obsolete. Superseded by IModelDoc2::CreatePoint2 and IModelDoc2::ICreatePoint2 . |
| Method | SketchPolygon | Obsolete. Superseded by ISketchManager::CreatePolygon . |
| Method | SketchRectangle | Obsolete. Superseded by ISketchManager::CreateCornerRectangle . |
| Method | SketchRectangleAtAnyAngle | Obsolete. Superseded by ISketchManager::Create3PointCornerRectangle . |
| Method | SketchSpline | Starts a spline, or continues one, using the specified point. |
| Method | SketchSplineByEqnParams | Obsolete. Superseded by IModelDoc2::ISketchSplineByEqnParams2 . |
| Method | SketchSplineByEqnParams2 | Obsolete. Superseded by ISketchManager::CreateSplineByEqnParams . |
| Method | SketchTangentArc | Creates a tangent arc in the current model document. |
| Method | SketchTrim | Obsolete. Superseded by ISketchManager::SketchExtend and ISketchManager::SketchTrim . |
| Method | SketchUndo | Undoes the last sketch command. |
| Method | SketchUseEdge | Obsolete. Superseded by ISketchManager::SketchUseEdge . |
| Method | SketchUseEdge2 | Obsolete. Superseded by ISketchManager::SketchUseEdge . |
| Method | SketchUseEdgeCtrline | Uses this centerline in sketch. |
| Method | SkToolsAutoConstr | Automatically constrains the active sketch. |
| Method | SplitClosedSegment | Obsolete. Superseded by ISketchManager::SplitClosedSegment . |
| Method | SplitOpenSegment | Obsolete. Superseded by ISketchManager::SplitOpenSegment . |
| Method | Toolbars | Turns the specified SOLIDWORKS toolbars on and off. |
| Method | ToolsDistance | Computes distance. |
| Method | ToolsGrid | Shows and hides the grid in this model document. |
| Method | ToolsMacro | Not implemented. |
| Method | ToolsMassProps | Calculates the mass propert ies. |
| Method | ToolsSketchScale | Scales a sketch. |
| Method | ToolsSketchTranslate | Translates a sketch. |
| Method | UnBlankRefGeom | Shows the selected, hidden reference geometry in the graphics window. |
| Method | UnblankSketch | Shows a hidden sketch. |
| Method | UnderiveSketch | Changes a sketch to underived. |
| Method | UnLock | Reverses IModelDoc2::Lock and changes the status bar message to Process Complete . |
| Method | UnlockAllExternalReferences | Unlocks all external references. |
| Method | UnlockFramePoint | Obsolete. Not superseded. |
| Method | UserFavors | Specifies whether geometric relations are automatically created as you add sketch entities. |
| Method | UserPreferences | Obsolete. The See Also section of this topic contains links to the methods that supersede this method. |
| Method | VersionHistory | Gets an array of strings indicating the versions in which this document was saved, including the SOLIDWORKS Design version in which the model document is currently opened and which is the last value returned in the array. |
| Method | ViewConstraint | Shows the constraints for the current model document. |
| Method | ViewDispCoordinateSystems | Toggles the display of coordinate systems on and off. |
| Method | ViewDisplayCurvature | Toggles the display of surface curvature on and off. |
| Method | ViewDisplayFaceted | Sets the current display mode to show the facets that make up a shaded picture of STL output. |
| Method | ViewDisplayHiddengreyed | Sets the current display mode to Hidden Lines Visible . |
| Method | ViewDisplayHiddenremoved | Sets the current display mode to Hidden Lines Removed . |
| Method | ViewDisplayShaded | Sets the current display mode to Shaded . |
| Method | ViewDisplayWireframe | Sets the current display mode to Wireframe . |
| Method | ViewDispOrigins | Toggles the display of origins off and on. |
| Method | ViewDispRefaxes | Toggles the display of reference axis on and off. |
| Method | ViewDispRefplanes | Toggles the display of reference planes on and off. |
| Method | ViewDispRefPoints | Shows and hides the reference points for the current model document. |
| Method | ViewDispTempRefaxes | Toggles the display of temporary reference axes on and off. |
| Method | ViewOglShading | Sets the current display subsystem to use OpenGL. |
| Method | ViewOrientationUndo | Undoes previous view orientation changes that were made interactively by the user. |
| Method | ViewRotate | Rotates the view of the current model. |
| Method | ViewRotateminusx | Dynamically rotates the view around x in a negative direction with the current increment. |
| Method | ViewRotateminusy | Dynamically rotates the view around y in a negative direction with the current increment. |
| Method | ViewRotateminusz | Dynamically rotates the view around z in a negative direction with the current increment. |
| Method | ViewRotateplusx | Rotates the view around x in a positive direction with the current increment. |
| Method | ViewRotateplusy | Rotates the view around y in a positive direction with the current increment. |
| Method | ViewRotateplusz | Rotates the view around z in a positive direction with the current increment. |
| Method | ViewRotXMinusNinety | Dynamically rotates the view by negative 90 about x. |
| Method | ViewRotXPlusNinety | Dynamically rotates the view by 90 about x. |
| Method | ViewRotYMinusNinety | Dynamically rotates the view by negative 90 about y. |
| Method | ViewRotYPlusNinety | Dynamically rotates the view by 90 about y. |
| Method | ViewRwShading | Sets the current display subsystem to use renderware. |
| Method | ViewTranslate | Translates the view. |
| Method | ViewTranslateminusx | Dynamically shifts the view left. |
| Method | ViewTranslateminusy | Dynamically shifts the view down. |
| Method | ViewTranslateplusx | Dynamically shifts the view right. |
| Method | ViewTranslateplusy | Dynamically shifts the view up. |
| Method | ViewZoomin | Zooms the current view in by a factor of 20%. |
| Method | ViewZoomout | Zooms the current view out by a factor of 20%. |
| Method | ViewZoomto | Zooms the view to the selected box. |
| Method | ViewZoomTo2 | Zooms to the specified region. |
| Method | ViewZoomtofit | Obsolete. Superseded by IModelDoc2::ViewZoomtofit2 . |
| Method | ViewZoomtofit2 | Zooms the currently active view to fit the screen. |
| Method | ViewZoomToSelection | Zooms the display to the selection. |
| Method | WindowRedraw | Redraws the current window. |

[Top](#topBookmark)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
