---
title: "IFeatureManager Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_methods.html"
---

# IFeatureManager Interface Methods

For a list of all members of this type, see[IFeatureManager members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddCornerReliefCorner | Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief. |
| Method | AddCornerReliefType | Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body. |
| Method | AddSMNormalCut | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ISMNormalCutGroupData , and ISMNormalCutFeatureData2 . |
| Method | AddSMNormalCutType | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ISMNormalCutGroupData , and ISMNormalCutFeatureData2 . |
| Method | AddVariablePitchHelixFirstPitchAndDiameter | Adds the first segment to a variable-pitch helix. |
| Method | AddVariablePitchHelixSegment | Adds a segment to a variable-pitch helix. |
| Method | AdvancedHole | Obsolete. Superseded by IFeatureManager::AdvancedHole2 . |
| Method | AdvancedHole2 | Creates an Advanced Hole feature. |
| Method | CreateCoordinateSystem | Creates a coordinate system feature using the specified entities. |
| Method | CreateCoordinateSystemUsingNumericalValues | Creates a coordinate system feature using the specified numerical values for position and orientation with respect to the global coordinate system. |
| Method | CreateCustomBendAllowance | Creates a custom bend allowance to use when creating a sheet metal feature. |
| Method | CreateDefinition | Creates a feature data object of the specified type. |
| Method | CreateFeature | Creates the specified feature. |
| Method | CreateFormTool | Obsolete. Superseded by IFeatureManager::CreateFormTool2 . |
| Method | CreateFormTool2 | Creates a forming tool feature with the specified point of insertion in a sheet metal part. |
| Method | CreateSaveBodyFeature | Creates a Save Bodies feature and creates part and assembly documents of the save bodies. |
| Method | CreateStructuralMemberGroup | Creates a weldment structural-member group. |
| Method | CutListFolderLocation | Gets the parent folder of the specified solid body / cut list item / body folder. |
| Method | DraftXpertChange | Changes the parameters on the selected drafted faces, regardless of whether the drafted faces were created manually or with DraftXpert, provided that DraftXpert can process them. |
| Method | DraftXpertRemove | Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it. |
| Method | EditDeleteFace | Edits a DeleteFace feature. |
| Method | EditFreeze | Obsolete. Superseded by IFeatureManager::EditFreeze2 . |
| Method | EditFreeze2 | Moves the freeze bar to the specified location in the FeatureManager design tree. |
| Method | EditReferencePoint | Edits the selected reference points. |
| Method | EditRollback | Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree. |
| Method | EndVariablePitchHelix | Ends and inserts a variable-pitch helix. |
| Method | ExpandFeature | Expands the specified component in the specified FeatureManager design tree pane. |
| Method | FeatureAdvancedTableDrivenPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in IDimPatternFeatureData . |
| Method | FeatureBossThicken | Thickens the selected reference surface, and then generates a boss. |
| Method | FeatureChainPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in IChainPatternFeatureData . |
| Method | FeatureCircularPattern | Obsolete. Superseded by IFeatureManager::FeatureCircularPattern2 . |
| Method | FeatureCircularPattern2 | Obsolete. Superseded by IFeatureManager::FeatureCircularPattern3 . |
| Method | FeatureCircularPattern3 | Obsolete. Superseded by IFeatureManager::FeatureCircularPattern4 . |
| Method | FeatureCircularPattern4 | Obsolete. Superseded by IFeatureManager::FeatureCircularPattern5 . |
| Method | FeatureCircularPattern5 | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ICircularPatternFeatureData and ILocalCircularPatternFeatureData . |
| Method | FeatureCut | Obsolete. Superseded by IFeatureManager::FeatureCut2 . |
| Method | FeatureCut2 | Obsolete. Superseded by IFeatureManager::FeatureCut3 . |
| Method | FeatureCut3 | Obsolete. Superseded by IFeatureManager::FeatureCut4 . |
| Method | FeatureCut4 | Creates a cut extrude feature. |
| Method | FeatureCutThicken | Thickens the selected reference surface feature, and then generates a cut. |
| Method | FeatureCutThin | Obsolete. Superseded by IFeatureManager::FeatureCutThin2 . |
| Method | FeatureCutThin2 | Inserts a thin cut extrude feature. |
| Method | FeatureDimensionPattern | Not implemented. |
| Method | FeatureExtruRefSurface | Obsolete. Superseded by IFeatureManager::FeatureExtruRefSurface2 . |
| Method | FeatureExtruRefSurface2 | Obsolete. Superseded by IFeatureManager::FeatureExtruRefSurface3 . |
| Method | FeatureExtruRefSurface3 | Inserts an extruded surface. |
| Method | FeatureExtrusion | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureExtrusion2 | Obsolete. Superseded by IFeatureManager::FeatureExtrusion3 . |
| Method | FeatureExtrusion3 | Creates an extruded feature. |
| Method | FeatureExtrusionThin | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureExtrusionThin2 | Creates an extruded thin feature. |
| Method | FeatureFillet | Obsolete. Superseded by IFeatureManager::FeatureFillet2 . |
| Method | FeatureFillet2 | Obsolete. Superseded by IFeatureManager::FeatureFillet3 . |
| Method | FeatureFillet3 | Creates a fillet feature for selected edges and control point references. |
| Method | FeatureFillPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in IFillPatternFeatureData . |
| Method | FeatureFolderLocation | Gets the folder feature for the specified feature. |
| Method | FeatureLinearPattern | Obsolete. Superseded by IFeatureManager::FeatureLinearPattern2 . |
| Method | FeatureLinearPattern2 | Obsolete. Superseded by IFeatureManager::FeatureLinearPattern3 . |
| Method | FeatureLinearPattern3 | Obsolete. Superseded by IFeatureManager::FeatureLinearPattern4 . |
| Method | FeatureLinearPattern4 | Obsolete. Superseded by IFeatureManager::FeatureLinearPattern5 . |
| Method | FeatureLinearPattern5 | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ILinearPatternFeatureData and ILocalLinearPatternFeatureData . |
| Method | FeatureLocalCurveDrivenPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ILocalCurvePatternFeatureData . |
| Method | FeatureLocalSketchDrivenPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ILocalSketchPatternFeatureData . |
| Method | FeatureRevolve | Obsolete. Superseded by IFeatureManager::FeatureRevolve2 . |
| Method | FeatureRevolve2 | Creates a base-, boss-, or cut-revolve feature. |
| Method | FeatureRevolveCut | Obsolete. Superseded by IFeatureManager::FeatureRevolveCut2 . |
| Method | FeatureRevolveCut2 | Obsolete. Superseded by IFeatureManager::FeatureRevolve2 . |
| Method | FeatureRevolveThin | Obsolete. Superseded by IFeatureManager::FeatureRevolve2 . |
| Method | FeatureRevolveThinCut | Obsolete. Superseded by IFeatureManager::FeatureRevolve2 . |
| Method | FeatureSketchDrivenPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ISketchPatternFeatureData . |
| Method | FilletXpertChange | Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them. |
| Method | FilletXpertMakeCorner | Creates or changes a fillet corner feature. |
| Method | FilletXpertRemove | Deletes the fillets on the selected faces. |
| Method | FinishCornerRelief | Creates a sheet metal corner relief feature. |
| Method | FinishSMNormalCut | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ISMNormalCutGroupData , and ISMNormalCutFeatureData2 . |
| Method | GetCornerManagementFolders | Gets the structure system corner management folders. |
| Method | GetCreateFeatureErrors | Gets the errors that occurred during the last call to IFeatureManager::CreateFeature . |
| Method | GetFeatureCount | Gets the number of features in this document. |
| Method | GetFeatures | Gets the features in this document. |
| Method | GetFeatureTreeRootItem | Obsolete. Superseded by IFeatureManager::GetFeatureTreeRootItem2 . |
| Method | GetFeatureTreeRootItem2 | Gets the root item of the FeatureManager design tree in the specified pane. |
| Method | GetFlatPatternFolder | Gets the interface to the flat-pattern folder feature in the FeatureManager design tree. |
| Method | GetFreezeLocation | Gets the location of the freeze bar in the FeatureManager design tree. |
| Method | GetPreTrimmedBodies | Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by IFeatureManager::PreTrimSurface . |
| Method | GetSelectionSetFolder | Gets the Selection Sets folder. |
| Method | GetSheetMetalFolder | Gets the interface to the sheet metal folder feature in the FeatureManager design tree. |
| Method | GetSlicingData | Gets a new slicing data object with default parameter values. |
| Method | GetStructureSystemFolders | Gets the structure system folders. |
| Method | HideBodies | Hides both solid and surface bodies in the model. |
| Method | HoleWizard | Obsolete. Superseded by IFeatureManager::HoleWizard2 . |
| Method | HoleWizard2 | Obsolete. Superseded by IFeatureManager::HoleWizard3 . |
| Method | HoleWizard3 | Obsolete. Superseded by IFeatureManager::HoleWizard4 . |
| Method | HoleWizard4 | Obsolete. Superseded by IFeatureManager::HoleWizard5 . |
| Method | HoleWizard5 | Creates customized holes of various kinds. |
| Method | IFeatureFillet | Obsolete. Superseded by IFeatureManager::IFeatureFillet2 . |
| Method | IFeatureFillet2 | Obsolete. Superseded by IFeatureManager::FeatureFillet3 . |
| Method | IGetFeatures | Gets the features in this document. |
| Method | IInsertCombineFeature | Combines the specified bodies in the multibody part to create a combine feature. |
| Method | IInsertMacroFeature | Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3 . |
| Method | IInsertMacroFeature2 | Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3 . |
| Method | IInsertMacroFeature3 | Inserts a macro feature in this model. |
| Method | IInsertMoveFace2 | Obsolete. Superseded by IFeatureManager::InsertMoveFace3 . |
| Method | IInsertReferencePoint | Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry. |
| Method | IInsertSheetMetalEdgeFlange2 | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | IInsertTableDrivenPattern | Obsolete. Superseded by IFeatureManager::InsertTableDrivenPattern2 . |
| Method | InsertCenterOfMass | Inserts a Center of Mass feature. |
| Method | InsertCenterOfMassReferencePoint | Inserts a Center of Mass Reference Point feature. |
| Method | InsertCombineFeature | Combines the specified bodies in the multibody part to create a combine feature. |
| Method | InsertConnectionPoint | Adds a connection point based on the selected entities. |
| Method | InsertConvertToSheetMetal | Obsolete. Superseded by IFeatureManager::InsertConvertToSheetMetal2 . |
| Method | InsertConvertToSheetMetal2 | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | InsertCoordinateSystem | Inserts a coordinate system feature. |
| Method | InsertCosmeticThread | Obsolete. Superseded by IFeatureManager::InsertCosmeticThread2 . |
| Method | InsertCosmeticThread2 | Obsolete. Superseded by IFeatureManager::InsertCosmeticThread3 . |
| Method | InsertCosmeticThread3 | Inserts a cosmetic thread. |
| Method | InsertCosmeticWeldBead | Obsolete. Superseded by IFeatureManager::InsertCosmeticWeldBead2 . |
| Method | InsertCosmeticWeldBead2 | Inserts a cosmetic weld bead using either weld geometry or a weld path. |
| Method | InsertCrossBreak | Inserts a cross break feature on the selected face in a sheet metal part. |
| Method | InsertCutBlend | Inserts a lofted cut based on the selected profiles, centerline, and guide curves. |
| Method | InsertCutSurface | Inserts a surface-cut feature using the preselected surface or plane. |
| Method | InsertCutSwept | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertCutSwept2 | Obsolete. Superseded by IFeatureManager::InsertCutSwept3 . |
| Method | InsertCutSwept3 | Obsolete. Superseded by IFeatureManager::InsertCutSwept4 . |
| Method | InsertCutSwept4 | Obsolete. Superseded by IFeatureManager::InsertCutSwept5 . |
| Method | InsertCutSwept5 | Obsolete . See Remarks . |
| Method | InsertDeleteBody | Obsolete. Superseded by IFeatureManager::InsertDeleteBody2 . |
| Method | InsertDeleteBody2 | Inserts a Body-Delete/Keep feature. |
| Method | InsertDeleteHoleForSurface | Inserts a Delete Hole feature for one or more selected hole edges on a surface. |
| Method | InsertDerivedPattern | Obsolete. Superseded by IFeatureManager::InsertDerivedPattern2 . |
| Method | InsertDerivedPattern2 | Obsolete. See IFeatureManager::CreateFeature and the Remarks in IDerivedPatternFeatureData . |
| Method | InsertDwgOrDxfFile | Obsolete. Superseded by IFeatureManager::InsertDwgOrDxfFile2 . |
| Method | InsertDwgOrDxfFile2 | Inserts a DXF/DWG image feature. |
| Method | InsertEdgeMerge | Merges multiple edges into a single edge using the selected faces when importing data. |
| Method | InsertEndCapFeature | Obsolete. Superseded by IFeatureManager::InsertEndCapFeature3 . |
| Method | InsertEndCapFeature2 | Inserts an end cap feature using the specified end faces of a structural member. |
| Method | InsertEndCapFeature3 | Inserts an end cap feature for one or more pre-selected open ends of a structural member. |
| Method | InsertFeatureChamfer | Inserts a chamfer. |
| Method | InsertFeatureLock | Locks or freezes a selected feature. |
| Method | InsertFeatureTreeFolder | Obsolete. Superseded by IFeatureManager::InsertFeatureTreeFolder2 . |
| Method | InsertFeatureTreeFolder2 | Inserts a folder in the FeatureManager design tree for pre-selected features or components. |
| Method | InsertFilletBeadFeature | Obsolete. Superseded by IFeatureManager::InsertFilletBeadFeature2 . |
| Method | InsertFilletBeadFeature2 | Inserts a fillet weld bead feature and also fills the gap between the pre-selected part bodies, if any. |
| Method | InsertFilletBeadFeature3 | Inserts fillet weld bead features for the specified face sets. |
| Method | InsertFillSurface | Obsolete. Superseded by IFeatureManager::InsertFillSurface2 . |
| Method | InsertFillSurface2 | Inserts a fill-surface feature in the model. |
| Method | InsertFlattenSurface | Obsolete. Superseded by IFeatureManager::InsertFlattenSurface2 . |
| Method | InsertFlattenSurface2 | Inserts a surface-flatten feature in the model. |
| Method | InsertFlexFeature | Inserts a Flex feature using the selected solid or surface body. |
| Method | InsertFormToolFeature | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | InsertFreeform | Ob solete. Superseded by IFeatureManager::InsertFreeform2 . |
| Method | InsertFreeform2 | Inserts a Freeform feature. |
| Method | InsertGlobalBoundingBox | Obsolete. See IFeatureManager::CreateDefinition and IBoundingBoxFeatureData . |
| Method | InsertGridFeature | Inserts a Grid System feature. |
| Method | InsertGroundPlane | Obsolete. See IFeatureManager::CreateDefinition and IGroundPlaneFeatureData . |
| Method | InsertGussetFeature | Obsolete. Superseded by IFeatureManager::InsertGussetFeature3 . |
| Method | InsertGussetFeature2 | Inserts a gusset feature for the specified faces. |
| Method | InsertGussetFeature3 | Inserts a gusset feature for pre-selected faces of a weldment. |
| Method | InsertIndent | Inserts an indent feature using a selected target body and tool body regions. |
| Method | InsertLiveSectionPlane | Inserts a Live Section Plane using the selected plane or planar face. |
| Method | InsertMacroFeature | Obsolete. Superseded by IFeatureManager::InsertMacroFeature3 . |
| Method | InsertMacroFeature2 | Obsolete. Superseded by IFeatureManager::InsertMacroFeature3 . |
| Method | InsertMacroFeature3 | Inserts a macro feature in this model. |
| Method | InsertMateReference | Obsolete. Superseded by IFeatureManager::InsertMateReference2 . |
| Method | InsertMateReference2 | Inserts a mate reference for a part or assembly document. |
| Method | InsertMidSurface | Inserts a midsurface feature. |
| Method | InsertMirrorFeature | Obsolete. Superseded by IFeatureManager::InsertMirrorFeature2 . |
| Method | InsertMirrorFeature2 | Mirrors selected features, faces, bodies, and structure systems about a selected plane or planar face. |
| Method | InsertMoldCoreCavitySolids | Creates a core/cavity solid feature. |
| Method | InsertMoldPartingLine | Inserts a mold parting line feature. |
| Method | InsertMoldPartingSurface | Inserts a mold parting surface feature. |
| Method | InsertMoldShutOffSurface | Inserts the mold shut-off surface feature. |
| Method | InsertMoveCopyBody | Obsolete. Superseded by IFeatureManager::InsertMoveCopyBody2 . |
| Method | InsertMoveCopyBody2 | Moves or makes copies of the selected solid bodies or surfaces. |
| Method | InsertMoveFace | Obsolete. Superseded by IFeatureManager::InsertMoveFace2 and IFeatureManager::IInsertMoveFace2 . |
| Method | InsertMoveFace2 | Obsolete. Superseded by IFeatureManager::InsertMoveFace3 . |
| Method | InsertMoveFace3 | Moves the selected faces on a solid or surface model. |
| Method | InsertMultiFaceDraft | Inserts a multiface draft feature. |
| Method | InsertNetBlend | Obsolete. Superseded by IFeatureManager::InsertNetBlend2 . |
| Method | InsertNetBlend2 | This method inserts a boundary feature or a boundary surface feature. |
| Method | InsertProtrusionBlend | Obsolete. Superseded by IFeatureManager::InsertProtrusionBlend2 . |
| Method | InsertProtrusionBlend2 | Creates a lofted body or boss from the selected profiles, centerline, and guide curves. |
| Method | InsertProtrusionSwept | Obsolete. Superseded by IFeatureManager::InsertProtusionSwept3 . |
| Method | InsertProtrusionSwept2 | Obsolete. Superseded by IFeatureManager::InsertProtusionSwept3 . |
| Method | InsertProtrusionSwept3 | Obsolete. Superseded by IFeatureManager::InsertProtrusionSwept4 . |
| Method | InsertProtrusionSwept4 | Obsolete . See Remarks . |
| Method | InsertReferencePoint | Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry. |
| Method | InsertRefPlane | Inserts a constraint-based reference plane using the selected reference entities. |
| Method | InsertRevolvedRefSurface | Creates a revolved reference surface by revolving a profile around a centerline. |
| Method | InsertRib | Inserts a rib. |
| Method | InsertRuledSurfaceFromEdge | Obsolete. Superseded by IFeatureManager::InsertRuledSurfaceFromEdge2 . |
| Method | InsertRuledSurfaceFromEdge2 | Inserts a ruled surface from the selected edge on this feature. |
| Method | InsertSaveOutBodies | Saves the selected surface bodies or solid bodies or sub-weldments to a file. |
| Method | InsertScale | Applies the specified scaling to either the current model or a selected graphic body. |
| Method | InsertSecurityNote | Inserts a note for the specified macro feature . |
| Method | InsertSewRefSurface | Creates a surface by knitting the selected surfaces together. |
| Method | InsertSheetMetal3dBend | Inserts a 3D bend in sheet metal part. |
| Method | InsertSheetMetalBaseFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalBaseFlange2 . |
| Method | InsertSheetMetalBaseFlange2 | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | InsertSheetMetalCornerTrim | Inserts a break corner trim in the sheet metal part. |
| Method | InsertSheetMetalEdgeFlange | Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2 . |
| Method | InsertSheetMetalEdgeFlange2 | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | InsertSheetMetalGussetFeature | Obsolete. Superseded by IFeatureManager::InsertSheetMetalGussetFeature3 . |
| Method | InsertSheetMetalGussetFeature2 | Obsolete. Superseded by IFeatureManager::InsertSheetMetalGussetFeature3 . |
| Method | InsertSheetMetalGussetFeature3 | Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature . |
| Method | InsertSheetMetalHem | Obsolete. Superseded by IFeatureManager::InsertSheetMetalHem2 . |
| Method | InsertSheetMetalHem2 | Inserts a hem of the specified relief type at the selected edges of the current sheet metal part. |
| Method | InsertSheetMetalLoftedBend | Obsolete. Superseded by IFeatureManager::InsertSheetMetalLoftedBend2 . |
| Method | InsertSheetMetalLoftedBend2 | Inserts a lofted bend in a sheet metal part. |
| Method | InsertSheetMetalMiterFlange | Inserts a meter flange in a sheet metal part. |
| Method | InsertSlicing | Creates and inserts slicing into the FeatureManager design tree. |
| Method | InsertSplitLineIntersect | Creates split lines using the selected intersecting tool and target entities. |
| Method | InsertStructuralWeldment | Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment2 . |
| Method | InsertStructuralWeldment2 | Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment3 . |
| Method | InsertStructuralWeldment3 | Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment4 . |
| Method | InsertStructuralWeldment4 | Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment5 . |
| Method | InsertStructuralWeldment5 | Inserts a structural weldment feature. |
| Method | InsertSubFolder | Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder. |
| Method | InsertSubWeldFolder | Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface. |
| Method | InsertSubWeldFolder2 | Creates a sub weld folder feature containing the specified weldment bodies. |
| Method | InsertSweepSurface | Obsolete. Superseded by IFeatureManager::InsertSweepSurface2 . |
| Method | InsertSweepSurface2 | Obsolete. Superseded by IFeatureManager::InsertSweepSurface3 . |
| Method | InsertSweepSurface3 | Obsolete. See Remarks . |
| Method | InsertTableDrivenPattern | Obsolete. Superseded by IFeatureManager::InsertTableDrivenPattern2 . |
| Method | InsertTableDrivenPattern2 | Obsolete. See IFeatureManager::CreateFeature and the Remarks in ITablePatternFeatureData . |
| Method | InsertUntrimSurface | Obsolete. Superseded by IFeatureManager::InsertUntrimSurface2 . |
| Method | InsertUntrimSurface2 | Extends a surface along its natural boundaries or fills interior surface holes, optionally trimming outside these boundaries or holes. |
| Method | InsertVariablePitchHelix | Starts a variable-pitch helix using the selected sketch containing an arc. |
| Method | InsertVaryInstanceIncrement | Obsolete. Superseded by IInstanceToVaryOptions . |
| Method | InsertVaryInstanceOverride | Obsolete. Superseded by IInstanceToVaryOptions . |
| Method | InsertWeldmentCutList | Inserts a cut-list-item folder feature containing pre-selected weldment bodies. |
| Method | InsertWeldmentCutList2 | Inserts a cut-list-item folder feature containing the specified weldment bodies. |
| Method | InsertWeldmentFeature | Inserts a weldment feature. |
| Method | InsertWeldmentTrimFeature | Inserts a weldment trim feature. |
| Method | InsertWeldmentTrimFeature2 | Inserts a weldment trim feature for the specified weldment bodies or faces. |
| Method | InsertWrapFeature | Obsolete. Superseded by IFeatureManager::InsertWrapFeature2 . |
| Method | InsertWrapFeature2 | Inserts a wrap feature. |
| Method | IsNameUsed | Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use. |
| Method | MakeStyledCurves | Obsolete. Superseded by IFeatureManager::MakeStyledCurves2 . |
| Method | MakeStyledCurves2 | Fits a spline to the preselected sketch segments to make a smooth edge on the model. |
| Method | MoldUndercutDetect | Obsolete. Superseded by IFeatureManager::MoldUndercutDetect2 . |
| Method | MoldUndercutDetect2 | Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold. |
| Method | MoveRotateLiveSectionPlane | Moves or rotates the selected Live Section Plane using the selected Live Section Plane and its manipulator. |
| Method | MoveToFolder | Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure. |
| Method | PostIntersect | Creates an intersect feature. |
| Method | PostSplitBody | Obsolete. Superseded by IFeatureManager::PostSplitBody2 . |
| Method | PostSplitBody2 | Creates a Split feature. |
| Method | PostTrimSurface | Sets whether to sew the resulting trimmed surfaces. |
| Method | PreIntersect | Obsolete. Superseded by IFeatureManager::PreIntersect2 . |
| Method | PreIntersect2 | Prepares an intersect feature. |
| Method | PreSplitBody | Obsolete. Superseded by IFeatureManager::PreSplitBody2 . |
| Method | PreSplitBody2 | Gets all of the bodies created by splitting a part. |
| Method | PreTrimSurface | Sets the trimming options before trimming a surface. |
| Method | SetComponentIdentifiers | Allows you to specify the primary, ( secondary ), and < tertiary > elements to display for the components in the FeatureManager design tree. |
| Method | SetFreeformBoundaryContinuity | Sets the boundary continuity for this Freeform feature. |
| Method | SetFreeformCurveData | Adds a curve to the pre-selected face for a Freeform feature. |
| Method | SetFreeformPointData | Adds a point to a curve for a Freeform feature. |
| Method | SetNetBlendCurveData | Sets the data for a curve for this boundary feature or boundary surface feature. |
| Method | SetNetBlendDirectionData | Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature. |
| Method | ShowBodies | Shows both hidden solid and surface bodies. |
| Method | SimpleHole | Obsolete. Superseded by IFeatureManager::SimpleHole2 . |
| Method | SimpleHole2 | Inserts a simple hole feature. |
| Method | UpdateFeatureTree | Updates the FeatureManager design tree. |

[Top](#topBookmark)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
