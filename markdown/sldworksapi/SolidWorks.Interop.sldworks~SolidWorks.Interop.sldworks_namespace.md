---
title: "SolidWorks.Interop.sldworks Namespace"
project: "SOLIDWORKS API Help"
interface: "SolidWorks.Interop.sldworks"
member: ""
kind: "namespace"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html"
---

# SolidWorks.Interop.sldworks Namespace

SOLIDWORKS API

## Interfaces

| Interface | Description |
| --- | --- |
| IAdvancedHoleElementData | Allows access to Advanced Hole element data. |
| IAdvancedHoleFeatureData | Allows access to the Advanced Hole feature data. |
| IAdvancedSaveAsOptions | Allows access to all File > Save As options when saving a SOLIDWORKS Part, Assembly, or Drawing. |
| IAdvancedSelectionCriteria | Allows access to advanced component selection criteria for an assembly. |
| IAngleMateFeatureData | Allows access to an angle mate or a limit angle mate feature. |
| IAnimation | This interface is: obsolete and has not been superseded. nonfunctional in SOLIDWORKS 2008 and later. Use the interfaces related to motion studies introduced in SOLIDWORKS 2008 to access animation and simulation. |
| IAnnotation | Allows access to notes, weld symbols, datum tags, display dimensions, blocks, cosmetic threads, center marks, centerlines, and other annotation types. |
| IAnnotationView | Allows access to annotation views in parts and assemblies. |
| IAppearanceSetting | Allows access to visual property settings. |
| IAssemblyDoc | Allows access to functions that perform assembly operations; for example, adding new components, adding mate conditions, hiding, and exploding components. |
| IAttribute | Allows access to an attribute's values. |
| IAttributeDef | Allows access to an attribute definition. |
| IAutoBalloonOptions | Allows access to auto balloon options. |
| IBalloonOptions | Allows access to balloon options. |
| IBalloonStack | Allows access to the properties that apply to a balloon stack, such as the direction of the stack. |
| IBaseFlangeFeatureData | Allows access to a sheet metal base flange feature. |
| IBeltChainFeatureData | Allows access to a Belt/Chain assembly feature. |
| IBendsFeatureData | Allows access to a Flatten-Bends/Process-Bends feature. |
| IBendTable | Allows access to a bend table feature. |
| IBendTableAnnotation | Allows access to a bend table annotation. |
| IBlockDefinition | Obsolete. Superseded by ISketchBlockDefinition . |
| IBlockInstance | Obsolete. Superseded by ISketchBlockInstance . |
| IBody | Obsolete. Superseded by IBody2 . |
| IBody2 | Allows access to the faces on a body and the ability to create surfaces for sewing into a body object. |
| IBodyFolder | Allows access to the bodies in solid, surface, and various weldment folders. |
| IBomFeature | Allows access to the BOM table feature. |
| IBomTable | Allows access to BOM table information and values. IMPORTANT: You can no longer insert IBomTable objects; you can now only insert IBomTableAnnotation objects. IBomTable objects are not and cannot be converted to IBomTableAnnotation objects. Use the IBomTable APIs for legacy BOM tables only. |
| IBomTableAnnotation | Allows access to the IBomFeature object for this table annotation. |
| IBomTableSortData | Allows access to the sort data of an IBomTableAnnotation . |
| IBoundaryBossFeatureData | Allows access to a boundary feature that is a boss or base. |
| IBoundingBoxFeatureData | Allows access to a bounding box feature. |
| IBreakCornerFeatureData | Allows access to a break corner feature. |
| IBreakLine | Allows access to information about a break line in a drawing view . |
| IBrokenOutSectionFeatureData | Allows access to the broken-out section feature data of a drawing view. |
| IBSurfParamData | Allows access to the parameterization data of a B-spline surface. |
| ICallout | Allows add-in applications to manipulate single and multi-row callouts. |
| ICalloutAngleVariable | Allows access to an angle variable in a hole callout. |
| ICalloutLengthVariable | Allows access to a length variable in a hole callout. |
| ICalloutStringVariable | Allows access to a string variable in a hole callout. |
| ICalloutVariable | Allows access to a hole callout. |
| ICamera | Allows access to the camera feature. |
| ICamFollowerMateFeatureData | Allows access to a cam-follower mate feature. |
| ICavityFeatureData | Allows access to a cavity feature. |
| ICenterLine | Allows access to a centerline. |
| ICenterMark | Allows access to a center mark or center mark set in a drawing view . |
| ICenterOfMass | Allows access to the centers of mass in a drawing view . |
| IChainPatternFeatureData | Allows access to a chain component pattern feature. |
| IChamferFeatureData | Obsolete. Superseded by IChamferFeatureData2 . |
| IChamferFeatureData2 | Allows access to a chamfer feature. |
| ICircularPatternFeatureData | Allows access to a circular pattern feature. |
| IClearanceResult | Allows you to access the results of clearance verfication . |
| IClearanceVerificationMgr | Allows you to check the clearance between selected components and/or faces in assemblies. |
| IClosedCornerFeatureData | Allows access to a closed corner feature. |
| ICoEdge | Allows access to the underlying edge and loop as well as various coedge data. |
| ICoincidentMateFeatureData | Allows access to a coincident mate feature. |
| ICollision | Allows access to collision data. |
| ICollisionDetectionGroup | Allows access to collision detection groups. |
| ICollisionDetectionManager | Allows access to the collision detection manager. |
| IColorTable | Allows access to the color definitions used in SOLIDWORKS. |
| ICombineBodiesFeatureData | Allows access to a combine feature. |
| ICommandGroup | Allows add-in applications to create toolbars and menu items, including flyout toolbars and submenus, and add them to the ICommandManager. |
| ICommandManager | Allows add-in applications to add and remove CommandGroups (menus and toolbars) to the CommandManager. |
| ICommandTab | Allows add-in applications to create tabs and add them to the CommandManager . The add-in application must create and clean up its own tabs. |
| ICommandTabBox | Allows add-in applications to create CommandManager tab boxes and add them to a CommandManager tab. The add-in application must
create and clean-up its own tab boxes. |
| IComment | Allows access to the comments in the Comment folder in the FeatureManager design tree. |
| ICommentFolder | Allows access to the Comment folder in the FeatureManager design tree. |
| IComplexCornerTreatmentFeatureData | Allows access to a complex corner treatment feature of a structure system. |
| IComponent | Obsolete. Superseded by IComponent2 . |
| IComponent2 | Allows access to the components within assemblies. |
| ICompositeCurveFeatureData | Allows access to a composite curve feature. |
| IConcentricMateFeatureData | Allows access to a concentric mate feature. |
| IConfiguration | Allows you to manage different part or assembly states. |
| IConfigurationManager | Allows access to a configuration in a model. |
| IConnectionPointFeatureData | Allows access to a connection point feature. |
| IConvertSolidFeatureData | Allows access to a convert solid feature. |
| ICoordinateSystemElement | Allows access to a coordinate system element. |
| ICoordinateSystemFeatureData | Allows access to a coordinate system feature. |
| ICoreFeatureData | Allows access to a core feature. |
| ICornerManagementFolder | Allows access to a corner management folder in a structure system. |
| ICornerMember | Allows access to a corner member of a complex or two member structure system corner treatment feature. |
| ICornerReliefFeatureData | Allows access to sheet metal corner relief feature data. |
| ICornerTreatmentFeatureData | Allows access to a corner treatment feature of a structure system. |
| ICornerTreatmentGroupFolder | Allows access to a corner treatment group folder of a structure system. |
| ICosmeticThreadFeatureData | Allows access to a cosmetic thread feature. |
| ICosmeticWeldBeadFeatureData | Allows access to a cosmetic weld bead feature. |
| ICosmeticWeldBeadFolder | Allows access to the properties of cosmetic weld beads. |
| ICounterboreElementData | Allows access to the data of a counterbore hole element in an Advanced Hole. |
| ICountersinkElementData | Allows access to the data of a countersink hole element in an Advanced Hole. |
| ICrossBreakFeatureData | Gets or sets cross break feature data. |
| ICThread | Allows access to a cosmetic thread. |
| ICurve | Allows access to a curve and its parameters in their native form or in terms of b-curve data. |
| ICurveDrivenPatternFeatureData | Allows access to a curve-driven pattern feature. |
| ICurveParamData | Allows access to curve parameterization data. |
| ICustomBendAllowance | Allows access to the custom bend allowance of a feature. |
| ICustomPropertyManager | Allows access to the custom properties. |
| ICustomSymbol | Obsolete. Superseded by ISketchBlockDefinition and ISketchBlockInstance . |
| ICutListItem | Allows access to a configuration-specific cut list folder. |
| ICutListSortOptions | Allows access to cut list sorting options. |
| IDatumOrigin | Allows access to datum origin annotations. |
| IDatumTag | Allows access to display information for datum tags. |
| IDatumTargetSym | Allows access to display information for datum target symbol annotations. |
| IDecal | Allows access to the decals in models. |
| IDeleteBodyFeatureData | Allows access to a Body-Delete/Keep feature. |
| IDeleteFaceFeatureData | Allows access to a DeleteFace feature. |
| IDerivedPartFeatureData | Allows access to a derived part feature. |
| IDerivedPatternFeatureData | Allows access to a derived pattern feature. |
| IDesignTable | Allows access to design table information and values. |
| IDetailCircle | Allows access to a detail circle. |
| IDiagnoseResult | Get the gaps and coedges in each gap on this body. |
| IDimension | Allows you to get and set dimension values and tolerances. |
| IDimensionSensorData | Allows access to a Measurement (dimension) sensor feature. |
| IDimensionTolerance | Allows you to get and set dimension tolerances. |
| IDimPatternFeatureData | Allows access to a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances. |
| IDimXpertManager | Allows you to get the DimXpert schema for a configuration. |
| IDisplayData | Allows access to display information for certain items, including reference planes and reference axes shown in a drawing view. |
| IDisplayDimension | Represents instances of dimensions displayed in parts , assemblies , drawings and sensors . |
| IDisplayStateSetting | Allows access to display state settings. |
| IDistanceMateFeatureData | Allows access to a distance mate or a limit distance mate feature. |
| IDocumentSpecification | Allows you to specify how to open a model document. Use this interface's properties before calling ISldWorks::OpenDoc7 to specify how you want to open a model document. |
| IDomeFeatureData | Obsolete. Superseded by IDomeFeatureData2 . |
| IDomeFeatureData2 | Allows access to a dome feature. |
| IDowelSymbol | Allows access to a dowel symbol. |
| IDraftFeatureData | Obsolete. Superseded by IDraftFeatureData2 . |
| IDraftFeatureData2 | Allows access to a draft feature. |
| IDragArrowManipulator | Allows access to drag arrows, which are called handles in the SOLIDWORKS user interface. |
| IDragOperator | Allows access to settings for the Move Components command in the SOLIDWORKS user-interface. |
| IDrawingComponent | Represents the referenced component in a drawing view. |
| IDrawingDoc | Allows access to functions that perform drawing operations. |
| IDrSection | Allows access to a section view in a drawing. |
| IEdge | Allows access to its defining coedge, and adjacent faces, and its underlying curve and vertices as well as edge data. |
| IEdgeFlangeFeatureData | Allows access to a sheet metal edge flange feature. |
| IEdgePoint | Allows access to a midpoint on an edge or an endpoint or midpoint on a reference curve . |
| IEndCapFeatureData | Allows access to an end-cap feature. |
| IEntity | Allows access to an attribute instance that is stored on an entity. |
| IEnumBodies | Obsolete. Superseded by IEnumBodies2 . |
| IEnumBodies2 | Allows access to bodies enumeration. |
| IEnumCoEdges | Allows access to a coedges enumeration. |
| IEnumComponents | Obsolete. Superseded by IEnumComponents2 . |
| IEnumComponents2 | Allows access to a components enumeration. |
| IEnumDisplayDimensions | Allows access to a display dimensions enumeration. |
| IEnumDocuments | Obsolete. Superseded by IEnumDocuments2 . |
| IEnumDocuments2 | Allows access to a documents enumeration. |
| IEnumDrSections | Allows access to a section views enumeration. |
| IEnumEdges | Allows access to an edges enumeration. |
| IEnumFaces | Obsolete. Superseded by IEnumFaces2 . |
| IEnumFaces2 | Allows access to a faces enumeration. |
| IEnumLoops | Obsolete. Superseded by IEnumLoops2 . |
| IEnumLoops2 | Allows access to a loops enumeration. |
| IEnumModelViews | Allows access to a model views enumeration. |
| IEnumSketchHatches | Allows access to a sketch hatches enumeration. |
| IEnumSketchPoints | Allows access to a sketch points enumeration. |
| IEnumSketchSegments | Allows access to the sketch segments enumeration. |
| IEnvironment | Allows you to analyze the text and geometry used to create a geometric tolerance symbol. |
| IEquationMgr | Maintains a list of all of the existing equations in a model. |
| IExplodeStep | Allows access to an explode step in the explode view of the active assembly configuration. |
| IExportPdfData | Allows access to the PDF export data interface, which allows you to save: one or more drawing sheets to PDF. parts and assemblies to 3D PDF. |
| IExtrudeFeatureData | Obsolete. Superseded by IExtrudeFeatureData2 . |
| IExtrudeFeatureData2 | Allows access to an extrusion feature. |
| IFace | Obsolete. Superseded by IFace2 . |
| IFace2 | Allows access to the underlying edge, loop, and surface to the owning body or feature, and to face tessellation, trim data. |
| IFaceDecalProperties | Allow access to the properties of decals applied to faces in models. |
| IFaceHatch | Represents a cross-hatch, which is automatically added by SOLIDWORKS when you create a section view , aligned section view, break view, or detail view . |
| IFacet | Allows access to a triangular facet of a mesh or graphics body. |
| IFaultEntity | Identifies entities with faults and types of faults. |
| IFeatMgrView | Allows access to a view (tab) in the FeatureManager design tree. |
| IFeature | Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree. |
| IFeatureFolder | Allows access to the contents of feature folders in the FeatureManager design tree. |
| IFeatureManager | Allows you to create features. |
| IFeatureStatistics | Allows access to the feature statistics in a part document. |
| IFillPatternFeatureData | Allows access to a fill pattern feature. |
| IFillSurfaceFeatureData | Allows access to a fill-surface feature. |
| IFlatPatternFeatureData | Allows access to a Flat-Pattern feature. |
| IFlatPatternFolder | Allows access to the flat-pattern folder in the FeatureManager design tree. |
| IFlyoutGroup | Allows access to a flyout menu. |
| IFoldsFeatureData | Allows access to a fold feature. |
| IFrame | Allows access to SOLIDWORKS frames, including model windows, menus, and toolbars. |
| IFreePointCurveFeatureData | Allows access to a curve created using X, Y, Z coordinates for the points. |
| IGearMateFeatureData | Allows access to gear mate features. |
| IGeneralTableAnnotation | Allows access to the general table annotation. |
| IGeneralTableFeature | Allows access to the general table feature. |
| IGeneralToleranceTableAnnotation | Allows access to the general tolerance table annotation. |
| IGeneralToleranceTableFeature | Allows access to the general tolerance table feature. |
| IGraphicsBody | Allows access to a graphics body. |
| IGroundPlaneFeatureData | Allows access to a ground plane feature. |
| IGtol | Allows you to get and set geometric tolerance (GTol) parameters. |
| IGtolFrame | Allows access to indicators and XML strings for symbols in a Gtol feature control frame. |
| IGussetFeatureData | Allows access to a weldment gusset feature. |
| IHealEdgesFeatureData | Allows access to a heal edges feature. |
| IHelixFeatureData | Allows access to a helix feature. |
| IHemFeatureData | Allows access to a hem feature. |
| IHingeMateFeatureData | Allows access to a hinge mate feature. |
| IHoleDataTable | Allows access to Hole Wizard fastener tables. |
| IHoleSeriesFeatureData | Obsolete. Superseded by IHoleSeriesFeatureData2 . |
| IHoleSeriesFeatureData2 | Allows access to the data that defines a hole series feature. |
| IHoleStandardsData | Allows access to Hole Wizard standards data. |
| IHoleTable | Allows access to a hole table feature in a drawing document. |
| IHoleTableAnnotation | Accesses the hole table annotation. |
| IImport3DInterconnectData | Allows access to 3D Interconnect feature data. |
| IImportDxfDwgData | Allows you to specify values when importing or inserting DXF/DWG data. |
| IImportedCurveFeatureData | Allows access to an imported curve feature. |
| IImportIgesData | Allows you to specify levels and values when importing IGES data. |
| IImportStepData | Allows you to specify values when importing STEP data. |
| IIndentFeatureData | Allows access to an indent feature. |
| IInstanceToVaryOptions | Allows access to options for varying the dimensions and locations of instances in patterns for parts. |
| IInterference | Allows access to the components that interfere when interference detection is calculated. |
| IInterferenceDetectionMgr | Allows you to run interference detection on an assembly to determine whether components interfere with each other. |
| IIntersectFeatureData | Allows access to an intersect feature. |
| IJogFeatureData | Allows access to a jog feature. |
| IJoinFeatureData | Allows access to a join feature. |
| ILayer | Allows access to the properties and items on a layer, including the color, width, name, etc., used to define the layer. |
| ILayerMgr | Allows you to manage a drawing document's layers. |
| ILibraryFeatureData | Allows access to library feature data. |
| ILibraryFormToolFeatureData | Allows access to library forming tool feature data. |
| ILight | Allows access to the light feature. |
| ILightDialog | Obtained from a LightingDialogCreateNotify event. |
| ILinearCouplerMateFeatureData | Allows access to linear/linear coupler mate feature data. |
| ILinearPatternFeatureData | Allows access to a linear pattern feature. |
| ILocalCircularPatternFeatureData | Allows access to a circular component pattern feature in an assembly. |
| ILocalCurvePatternFeatureData | Allows access to a curve-driven component pattern feature in an assembly. |
| ILocalLinearPatternFeatureData | Allows access to a linear component pattern feature in an assembly. |
| ILocalSketchPatternFeatureData | Allows access to a sketch-driven component pattern feature in an assembly. |
| ILockMateFeatureData | Allows access to lock mate features. |
| ILoftedBendsFeatureData | Allows access to display information for a lofted bends feature. |
| ILoftFeatureData | Allows access to a loft feature. |
| ILoop | Obsolete. Superseded by ILoop2 . |
| ILoop2 | Allows access to the owning face and to the list of edges and coedges contained in the loop. |
| IMacroFeatureData | Allows access to the data that defines a macro feature. |
| IMagneticLine | Allows access to a magnetic line. |
| IManipulator | Allows access to a manipulator, which is similar to the triad or the drag arrow (also called a handle), in a SOLIDWORKS part or assembly document. |
| IMassProperty | Obsolete. Superseded by IMassProperty2 . |
| IMassProperty2 | Allows access to individual mass properties as found in the Mass Properties dialog box. |
| IMassPropertyOverrideOptions | Allows access to mass property override options. |
| IMate | Obsolete. Superseded by IMate2 . |
| IMate2 | Allows access to various assembly mate parameters. |
| IMateControllerFeatureData | Allows access to a mate controller feature. |
| IMateEntity | Obsolete. Superseded by IMateEntity2 . |
| IMateEntity2 | Allows access to mated entities and the assembly mate definition. |
| IMateFeatureData | Allows access to mate feature data. |
| IMateInPlace | Allows access to an Inplace (coincident) mate, which is created when you insert a component in the context of an assembly. |
| IMateLoadReference | Allows access to mate load references. |
| IMateReference | Allows access to a mate reference, which specifies one or more entities of a component to use for automatic mating. |
| IMaterialVisualPropertiesData | Allows access to a material on a part. |
| IMathPoint | Provides a simplified interface for manipulating math-point objects' data and ways to create other math objects. |
| IMathTransform | Provides a simplified interface for manipulating transformation matrix data. |
| IMathUtility | Provides access to the SOLIDWORKS math objects. These objects can simplify commonly used math calculations used with many API functions. |
| IMathVector | Provides a simplified interface for manipulating math vectors. |
| IMBD3DPdfData | Gains access to the details for publishing a SOLIDWORKS MBD 3D PDF. |
| IMeasure | Allows access to the measure tool. |
| IMeshBody | Allows access to a mesh body. |
| IMessageBarDefinition | Allows access to a message bar in an add-in. |
| IMidSurface | Obsolete. Superseded by IMidSurface3 . |
| IMidSurface2 | Obsolete. Superseded by IMidSurface3 . |
| IMidSurface3 | Allows access to a midsurface feature. |
| IMirrorComponentFeatureData | Allows access to a mirror component feature. |
| IMirrorPartFeatureData | Allows access to a mirror part feature. |
| IMirrorPatternFeatureData | Allows access to a mirror pattern feature. |
| IMirrorSolidFeatureData | Allows access to a mirror solid feature. |
| IMiterFlangeFeatureData | Allows access to a miter flange feature. |
| IModelDoc | Obsolete. Superseded by IModelDoc2 . |
| IModelDoc2 | Allows access to SOLIDWORKS documents: parts, assemblies, and drawings. |
| IModelDocExtension | Allows access to the model. |
| IModeler | Provides an interface to temporary body objects. |
| IModelView | Allows you access to the model view's orientation, translation, and the Microsoft handle to the window. |
| IModelViewManager | Allows access to the model view. |
| IModelWindow | Allows access to SOLIDWORKS model windows. |
| IMotionPlotAxisFeatureData | Allows access to a plot's x- and y-axis feature data. |
| IMotionPlotFeatureData | Allows access to a plot's feature data. |
| IMouse | Allows access to the mouse in a model view. |
| IMoveCopyBodyFeatureData | Allows access to a move/copy body feature. |
| IMoveFaceFeatureData | Allows access to Move Face features. |
| IMultiJogLeader | Allows access to display information for multi-jog leaders. |
| INote | Allows you to get standard note information. |
| IOneBendFeatureData | Allows access to a bend feature (sharp bend, round bend, or flat bend). |
| IPackAndGo | Allows access to Pack and Go. |
| IPageSetup | Allows access to a number of properties related to printer and page setup, including page header and footer information. |
| IParagraphs | Allows access to paragraphs in note annotations. |
| IParallelMateFeatureData | Allows access to a parallel mate feature. |
| IParameter | Allows you to get and set values in an attribute. |
| IPartDoc | Provides access to functions that perform operations on parts in part documents. |
| IPartExplodeStep | Allows access to the explode step of an explode view of a multibody part. |
| IPartialEdgeFilletData | Allows access to partial fillet/chamfer properties. |
| IPartingLineFeatureData | Allows access to a parting line feature. |
| IPartingSurfaceFeatureData | Allows access to a parting surface feature. |
| IPerpendicularMateFeatureData | Allows access to a perpendicular mate feature. |
| IPlaneManipulator | Allows access to a plane that has a manipulator. |
| IPLMObjectSpecification | Allows access to a SOLIDWORKS Connected document specification. |
| IPMIDatumData | Allows access to the Product and Manufacturing Information (PMI) for a datum annotation in a STEP 242 model. |
| IPMIDatumFeature | Allows access to a Product and Manufacturing Information (PMI) datum feature. |
| IPMIDatumTarget | Allows access to a Product and Manufacturing Information (PMI) datum target. |
| IPMIDimensionData | Allows access to the Product and Manufacturing Information (PMI) for a dimension annotation in a STEP 242 model. |
| IPMIDimensionItem | Allows access to a Product and Manufacturing Information (PMI) dimension item. |
| IPMIFrameData | Allows access to a Product and Manufacturing Information (PMI) Gtol frame. |
| IPMIGtolBoxData | Allows access to a Product and Manufacturing Information (PMI) Gtol tolerance box. |
| IPMIGtolData | Allows access to the Product and Manufacturing Information (PMI) for a Gtol annotation in a STEP 242 model. |
| IPMIGtolFrameDatum | Allows access to a Product and Manufacturing Information (PMI) Gtol datum box. |
| IPrimaryMemberFacePlaneIntersectionFeatureData | Allows access to a structure system member created along the intersection of a face or surface with a plane. |
| IPrimaryMemberPathSegmentFeatureData | Allows access to a structure system member created along path segments in a sketch. |
| IPrimaryMemberPointLengthFeatureData | Allows access to a structure system member originating at a point and extending to a specified end condition. |
| IPrimaryMemberRefPlaneFeatureData | Allows access to a structure system member created along the intersection of two or more planes. |
| IPrimaryStructuralMemberFeatureData | Allows access to a primary structure system member. |
| IPrint3DDialog | Allows access to the Print 3D dialog. |
| IPrintSpecification | Allows access to a document's printing specification. |
| IProfileCenterMateFeatureData | Allows access to profile center mate feature data. |
| IProfileGroupFolder | Allows access to a structure system profile group folder. |
| IProjectionArrow | Allows access to a projection arrow. |
| IProjectionCurveFeatureData | Allows access to a projection curve feature. |
| IPropertyManagerPage | Obsolete. Superseded by IPropertyManagerPage2 . |
| IPropertyManagerPage2 | Provides add-in applications the ability to display and use views that have the look and feel of SOLIDWORKS
PropertyManager pages. |
| IPropertyManagerPageActiveX | Allows you to access a PropertyManager page ActiveX control. |
| IPropertyManagerPageBitmap | Allows you to access a PropertyManager page bitmap. |
| IPropertyManagerPageBitmapButton | Allows you to access a PropertyManager page bitmap button control. |
| IPropertyManagerPageButton | Allows you to access a PropertyManager page button control. |
| IPropertyManagerPageCheckbox | Allows you to access a PropertyManager page check box. |
| IPropertyManagerPageCombobox | Allows you to access a PropertyManager page combo box control. |
| IPropertyManagerPageControl | Provides a set of methods and properties common to all PropertyManager page controls. |
| IPropertyManagerPageGroup | Allows you to access a PropertyManager page group control. |
| IPropertyManagerPageLabel | Allows you to access a PropertyManager page label control. |
| IPropertyManagerPageListbox | Allows you to access a PropertyManager page list box control. |
| IPropertyManagerPageNumberbox | Allows you to access a PropertyManager page number box control. |
| IPropertyManagerPageOption | Allows you to access to a PropertyManager page radio button control. |
| IPropertyManagerPageSelectionbox | Allows you to access a PropertyManager page selection box control. |
| IPropertyManagerPageSlider | Allows you to access a PropertyManager page slider control. |
| IPropertyManagerPageTab | Allows you to access a PropertyManager page tab control. |
| IPropertyManagerPageTextbox | Allows you to access a PropertyManager page text box control. |
| IPropertyManagerPageWindowFromHandle | Allows you to access a PropertyManager page .NET control. |
| IPunchTable | Allows access to punch table information and values. |
| IPunchTableAnnotation | Allows access to a punch table annotation. |
| IRackPinionMateFeatureData | Allows access to a rack and pinion mate feature. |
| IRayTraceRenderer | Allows access to ray-trace rendering engines. |
| IRayTraceRendererOptions | Allows access to a ray-trace rendering engine's options. |
| IRefAxis | Allows access to reference axis definitions. |
| IRefAxisFeatureData | Allows access to reference axis feature data. |
| IReferenceCurve | Allows access to reference curves. |
| IReferencePointCurveFeatureData | Allows access to reference-point curve feature data. |
| IRefPlane | Allows access to reference plane definitions. |
| IRefPlaneFeatureData | Allows access to reference plane feature data. |
| IRefPoint | Allows access to reference points. |
| IRefPointFeatureData | Allows access to reference point feature data. |
| IRenamedDocumentReferences | Allows you to update references to a renamed file in unopened documents. |
| IRenderMaterial | Use to apply appearances to models. NOTE: In SOLIDWORKS 2008 and later, materials are called appearances. RealView Graphics must be enabled to see any applied appearances. |
| IReplaceFaceFeatureData | Allows access to Replace Face feature data. |
| IRevisionCloud | Allows access to a revision cloud annotation. |
| IRevisionTableAnnotation | Accesses the revision table annotation. |
| IRevisionTableFeature | Allows access to the revision table feature. |
| IRevolveFeatureData | Obsolete. Superseded by IRevolveFeatureData2 . |
| IRevolveFeatureData2 | Allows access to a revolve feature. |
| IRibFeatureData | Obsolete. Superseded by IRibFeatureData2 . |
| IRibFeatureData2 | Allows access to a rib feature. |
| IRipFeatureData | Allows access to a rip feature. |
| IRoutingSettings | Allows access to various routing settings including those specified in Tools > Options > System Options > Routing . |
| IRuledSurfaceFeatureData | Allows access to a ruled-surface feature. |
| ISafeArrayUtility | Access the ISafeArrayUtility interface, which can: get an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type and return a packed Variant SafeArray to use in methods that requires passing a packed Variant SafeArray. get a packed Variant SafeArray and return an unpacked array of native SOLIDWORKS Dispatch-based objects of the same data type. get a Variant SafeArray and return the number of SafeArray objects in the Variant SafeArray and their data type. get and put a value in a Variant SafeArray of the same data type. |
| ISaveBodyFeatureData | Allows access to a Save Bodies feature. |
| ISaveTo3DExperienceOptions | Allows access to options for saving a document in SOLIDWORKS Connected . |
| IScaleFeatureData | Allows access to a scale feature. |
| IScrewMateFeatureData | Allows access to a screw mate feature. |
| ISecondaryMemberBetweenPointsFeatureData | Allows access to a secondary structure system member that is created between the end points on primary structure system member pairs. |
| ISecondaryMemberSupportPlaneFeatureData | Allows access to a secondary structure system member that is created on a plane between primary structure system member pairs. |
| ISecondaryMemberUpToMembersFeatureData | Allows access to a secondary structure system up-to member that is created between a selected point and one or more primary structure system members or between one or more point-member pairs. |
| ISecondaryStructuralMemberFeatureData | Allows access to a secondary structure system member. |
| ISectionViewData | Allows you to create and access section views in parts and assemblies. |
| ISelectData | Allows you to select objects. |
| ISelectionMgr | Allows you to get information about selected objects, obtain API objects representing the selected item, and get your selection coordinates interpreted in model or sketch space. |
| ISelectionSet | Allows access to a selection set. |
| ISelectionSetFolder | Allows access to the Selection Sets folder. |
| ISelectionSetItem | Allows access to a selection set item. |
| ISensor | Allows access to a sensor, which can monitor selected properties of parts and assemblies and alert you when the sensor's values deviate from the specified limits. |
| ISFSymbol | Allows access to display information for surface finish symbols. |
| ISheet | Allows access to a sheet and objects on the sheet such as BOM tables . |
| ISheetMetalFeatureData | Allows access to a sheet metal feature. |
| ISheetMetalFolder | Allows access to a sheet metal folder feature in the FeatureManager design tree. |
| ISheetMetalGaugeTableParameters | Allows access to sheet metal gauge table parameters. |
| IShellFeatureData | Allows access to a shell feature. |
| IShutOffSurfaceFeatureData | Allows access to a shut-off surface feature. |
| ISilhouetteEdge | Allows you to access silhouette edges in drawing documents. |
| ISimpleCornerTreatmentFeatureData | Allows access to a simple corner treatment feature of a structure system. |
| ISimpleFilletFeatureData | Obsolete. Superseded by ISimpleFilletFeatureData2 . |
| ISimpleFilletFeatureData2 | Allows access to a simple fillet feature. |
| ISimpleHoleFeatureData | Obsolete. Superseded by ISimpleHoleFeatureData2 . |
| ISimpleHoleFeatureData2 | Allows access to a simple hole feature. |
| ISimulation | This interface is: obsolete and has not been superseded. nonfunctional in SOLIDWORKS 2008 and later. Use the interfaces related to motion studies introduced in SOLIDWORKS 2008 to access animation and simulation. |
| ISimulation3DContactFeatureData | Allows access to a 3D Contact feature in SOLIDWORKS Motion studies. |
| ISimulationDamperFeatureData | Allows access to a damper feature in SOLIDWORKS Motion studies. |
| ISimulationForceFeatureData | Allows access to a force or torque feature in SOLIDWORKS Motion studies. |
| ISimulationGravityFeatureData | Allows access to a gravity feature in SOLIDWORKS Motion studies. |
| ISimulationLinearSpringFeatureData | Obsolete. Superseded by ISimulationSpringFeatureData . |
| ISimulationMotorFeatureData | Allows access to the data that defines linear or rotary motors in SOLIDWORKS Motion studies. |
| ISimulationSpringFeatureData | Allows access to the data that defines a simulation spring feature in SOLIDWORKS Motion studies. |
| ISketch | Allows access to sketch entities and to extract information about sketch elements, the sketch orientation, and so on. |
| ISketchArc | Provides access to properties and methods for sketched arc entities. |
| ISketchBlockDefinition | Allows access to information about a block definition. |
| ISketchBlockInstance | Allows access to block instances. |
| ISketchContour | Provides access to sketch contours. |
| ISketchedBendFeatureData | Allows access to a sheet metal sketched bend feature. |
| ISketchEllipse | Provides access to sketched ellipse entities. |
| ISketchHatch | Represents an area hatch, which is inserted into a SOLIDWORKS drawing polygon or component face when you click Insert > Annotations > Area Hatch/Fill in a SOLIDWORKS drawing. |
| ISketchLine | Provides access to sketched line entities. |
| ISketchManager | Provides access to sketch-creation routines. |
| ISketchParabola | Provides access to sketched parabolas. |
| ISketchPath | Provides access to the methods and properties for paths in sketches. |
| ISketchPatternFeatureData | Allows access to a sketch-driven pattern feature in a part. |
| ISketchPicture | Provides access to pictures on sketches (i.e., . bmp , . gif , . jpg , . jpeg , . tif , and . wmf ). |
| ISketchPoint | Provides access to sketch point entities. |
| ISketchRegion | Provides access to sketch regions. |
| ISketchRelation | Provides access to the entities for a sketch relation. |
| ISketchRelationManager | Provides access to all sketch relations. |
| ISketchSegment | Provides access to functions that are common among sketch entities. |
| ISketchSlot | Accesses a sketch slot. |
| ISketchSpline | Provides access to sketched spline entities. |
| ISketchText | Provides access to sketched text entities. |
| ISldWorks | Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API. |
| ISlicingData | Allows access to slicing tool data. |
| ISlotMateFeatureData | Allows access to a slot mate feature. |
| ISmartComponentFeatureData | Allows access to a Smart Component. |
| ISMCornerReliefData | Allows access to sheet metal corner relief data. |
| ISMGussetFeatureData | Allows access to a sheet metal gusset feature. |
| ISMNormalCutFeatureData | Obsolete. Superseded by ISMNormalCutFeatureData2 . |
| ISMNormalCutFeatureData2 | Allows access to a sheet metal normal cut feature. |
| ISMNormalCutGroupData | Allows access to a sheet metal normal cut feature's cut-extrude face group. |
| ISnapShot | Allows access to the snapshot of the graphics area of an assembly opened in Large Design Review mode. |
| ISplineHandle | Provides access to spline handles. |
| ISplineParamData | Allows access to the parameterization data of a spline. |
| ISplitBodyFeatureData | Allows access to a Split feature. |
| ISplitLineFeatureData | Allows access to a split line feature. |
| ISpring | Allows access to the geometry of a spring. |
| IStackedBalloonOptions | Allows access to stacked balloon options. |
| IStatusBarPane | Controls user-created status bar panes in the lower-right corner of the SOLIDWORKS status bar. |
| IStraightElementData | Allows access to the data of a simple hole element in an Advanced Hole. |
| IStraightTapElementData | Allows access to the data of a straight tap hole element in an Advanced Hole. |
| IStructuralMemberFeatureData | Allows access to a structural member. |
| IStructuralMemberGroup | Allows access to a weldment structural-member group. |
| IStructureSystemFolder | Allows access to a structure system folder. |
| IStructureSystemMemberFeatureData | Allows access to a structure system member. |
| IStructureSystemMemberProfile | Allows access to a structure system member profile. |
| IStructureSystemSplitMember | Allows access to a structure system split member. |
| ISurface | Used as the underlying definition of a face. |
| ISurfaceCutFeatureData | Allows access to a surface-cut feature. |
| ISurfaceExtendFeatureData | Allows access to a surface-extend feature. |
| ISurfaceFlattenFeatureData | Allows access to a surface-flatten feature. |
| ISurfaceKnitFeatureData | Allows access to a Surface-Knit feature. |
| ISurfaceOffsetFeatureData | Allows access to a surface offset feature. |
| ISurfaceParameterizationData | Allows access to the parameterization data of a surface. |
| ISurfacePlanarFeatureData | Allows access to a planar surface feature. |
| ISurfaceRadiateFeatureData | Allows access to a surface radiate feature. |
| ISurfaceTrimFeatureData | Allows access to a surface trim feature. |
| ISurfExtrudeFeatureData | Allows access to an extruded surface feature. |
| ISurfRevolveFeatureData | Allows access to a surface revolve feature. |
| ISweepFeatureData | Allows access to a sweep feature. |
| ISweptFlangeFeatureData | Allows access to a sheet metal swept flange feature. |
| ISwOLEObject | Allows access to an OLE object. |
| ISwPEClassFactory | Allows access to the callback object used by ISwPEManager to send a license key back to SOLIDWORKS for SOLIDWORKS Partner entitlement verification. |
| ISwPEToken | * For future use* |
| ISWPropertySheet | Allows applications to add pages to certain property sheets that are exported by the SOLIDWORKS application. |
| ISwScene | Allows access to the scene of a model. |
| ISymmetricMateFeatureData | Allows access to symmetry mate feature data. |
| ITabAndSlotFeatureData | Allows access to a tab and slot feature. |
| ITabAndSlotGroupData | Allows access to a tab and slot feature group. |
| ITableAnchor | Allows access to the data that defines a table anchor feature. |
| ITableAnnotation | Provides access to table annotations. |
| ITablePatternFeatureData | Allows access to a table-driven pattern feature. |
| ITangentMateFeatureData | Allows access to a tangent mate feature. |
| ITaperedTapElementData | Allows access to the data of a tapered tap hole element in an Advanced Hole. |
| ITaskpaneView | Provides access to an application-level Task Pane. |
| ITessellation | Used to gather tessellation information from a SOLIDWORKS body. |
| ITextAndCustomProperty | Gains access to the text and custom properties in a theme of a SOLIDWORKS MBD 3D PDF . |
| ITextFormat | Allows access to and control of the formatting of text used in annotations. |
| ITexture | Use to apply 2D textures to part and assembly documents for a more realistic finish. |
| IThickenFeatureData | Allows access to a thicken feature. |
| IThreadFeatureData | Allows access to a thread feature. |
| ITitleBlock | Allows access to the title block in this sheet. |
| ITitleBlockTableAnnotation | Provides access to title block table annotations. |
| ITitleBlockTableFeature | Provides access to title block table features. |
| IToolingSplitFeatureData | Allows access to a tooling-split feature. |
| ITreeControlItem | Allows you to traverse items in the FeatureManager design tree exactly as they appear in the FeatureManager design tree. |
| ITriadManipulator | Allows access to triad manipulators, which are: Similar to the SOLIDWORKS triad. Used to move and rotate assembly components, move/copy bodies, and so on. |
| ITwoMemberCornerTreatmentFeatureData | Allows access to a two member corner treatment feature of a structure system. |
| IUniversalJointMateFeatureData | Allows access to a universal joint mate feature. |
| IUserNotificationDefinition | Allows access to a user notification of an add-in. |
| IUserProgressBar | Allows access to a progress indicator that indicates how much longer a SOLIDWORKS operation will take. |
| IUserUnit | Allows you to manage units. |
| IVariableFilletFeatureData | Obsolete. Superseded by IVariableFilletFeatureData2 . |
| IVariableFilletFeatureData2 | Allows access to a variable radius fillet feature. |
| IVertex | Represents the start or end of an edge . |
| IView | Represents drawing views found in a drawing document. |
| IView3D | Allows access to a 3D View of a part or assembly. |
| IWeldBead | Allows access to weld bead annotations. |
| IWeldmentBeadFeatureData | Allows access to a weldment bead feature. |
| IWeldmentCutListAnnotation | Allows access to the annotations in a weldment cut list table. |
| IWeldmentCutListFeature | Allows access to a weldment cut list feature. |
| IWeldmentTrimExtendFeatureData | Allows access to the data that defines a weldment trim extend feature. |
| IWeldSymbol | Allows access to weld symbols. |
| IWidthMateFeatureData | Allows access to width mate feature data. |
| IWizardHoleFeatureData | Obsolete. Superseded by IWizardHoleFeatureData2 . |
| IWizardHoleFeatureData2 | Allows access to Hole Wizard hole or slot feature data. |
| IWrapSketchFeatureData | Allows access to a wrap feature. |

## Delegates

| Delegate | Description |
| --- | --- |
| DAssemblyDocEvents_ActiveAnnotationViewChangeNotifyEventHandler | Fired when the user changes the annotation view. |
| DAssemblyDocEvents_ActiveConfigChangeNotifyEventHandler | Fired when the user switches to a different configuration. |
| DAssemblyDocEvents_ActiveConfigChangePostNotifyEventHandler | Post-notifies the user program when the user has switched to a different configuration. |
| DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler | Fired after the display state of a configuration is changed or after a configuration is changed. |
| DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler | Fired before the display state of a configuration is changed or before a configuration is changed. |
| DAssemblyDocEvents_ActiveViewChangeNotifyEventHandler | Fired when the active view changes. |
| DAssemblyDocEvents_AddCustomPropertyNotifyEventHandler | Post-notifies the user program when the user adds a custom property. |
| DAssemblyDocEvents_AddItemNotifyEventHandler | Notifies the user when a component is added to the FeatureManager design tree. |
| DAssemblyDocEvents_AddMatePostNotify2EventHandler | Fired after one or more mates are created in an assembly. |
| DAssemblyDocEvents_AddMatePostNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_AddMatePostNotify2EventHandler . |
| DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler | Fired when the SOLIDWORKS software updates the electrical data. |
| DAssemblyDocEvents_AutoSaveNotifyEventHandler | Fired when the assembly document is automatically saved. |
| DAssemblyDocEvents_AutoSaveToStorageNotifyEventHandler | Fired when the assembly document is automatically saved to third-party IStream storage. |
| DAssemblyDocEvents_AutoSaveToStorageStoreNotifyEventHandler | Fired when the assembly document is automatically saved to third-party IStorage storage. |
| DAssemblyDocEvents_BeginInContextEditNotifyEventHandler | Notifies the application that the user is starting to edit an assembly component within the context of the assembly (inside the assembly document window). |
| DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler | Notifies the application that the visible state of a body within this assembly has changed. |
| DAssemblyDocEvents_ChangeCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has changed a custom property. |
| DAssemblyDocEvents_ClearSelectionsNotifyEventHandler | Notifies the user program when selections are cleared using Clear Selections . |
| DAssemblyDocEvents_CloseDesignTableNotifyEventHandler | Pre-notifies your application that a design table that was being edited is about to be closed. |
| DAssemblyDocEvents_CommandManagerTabActivatedPreNotifyEventHandler | Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated. |
| DAssemblyDocEvents_ComponentConfigurationChangeNotifyEventHandler | Fired when a reference component's configuration is being changed in an assembly. |
| DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler | Fired after a reference component's display mode is changed in an assembly. |
| DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler | Fired before a reference component's display mode is changed in an assembly. |
| DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler | Fired when the display state, such as shaded, wireframe, and so on, of a component is changed. |
| DAssemblyDocEvents_ComponentMoveNotify2EventHandler | Post-notification that is sent when a user releases the mouse button indicating that the components have been moved to the desired destination. |
| DAssemblyDocEvents_ComponentMoveNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_ComponentMoveNotifyEventHandler2 . |
| DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler | Fired when a component's referenced display state changes. |
| DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler | Fired when one or more components are reorganized in an assembly or sub-assembly. |
| DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler | Obsolete. Superseded by DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler . |
| DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler | Fired whenever the state of a component within this assembly changes. |
| DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler . |
| DAssemblyDocEvents_ComponentVisibleChangeNotifyEventHandler | Fired when a component is changed to hidden or shown. |
| DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler | Fired when a visual property, such as color, transparency, and so on, of a component is changed. |
| DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler | Gets information about an object or feature that has had one of its configurable parameters changed. |
| DAssemblyDocEvents_DeleteCustomPropertyNotifyEventHandler | Post-notifies the user program when the user deletes a custom property. |
| DAssemblyDocEvents_DeleteItemNotifyEventHandler | Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree). |
| DAssemblyDocEvents_DeleteItemPreNotifyEventHandler | Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the
ConfigurationManager tree). |
| DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler | Pre-notifies the user program when the selection is deleted. |
| DAssemblyDocEvents_DestroyNotify2EventHandler | Pre-notifies the user program when an assembly document is about to be destroyed. |
| DAssemblyDocEvents_DestroyNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_DestroyNotify2EventHandler . |
| DAssemblyDocEvents_DimensionChangeNotifyEventHandler | Fired when a dimension is changed through the Dimension dialog. |
| DAssemblyDocEvents_DisplayPaneCollapseNotifyEventHandler | Fired when the display pane collapses in this assembly. |
| DAssemblyDocEvents_DisplayPaneExpandNotifyEventHandler | Fired when the display pane expands in this assembly. |
| DAssemblyDocEvents_DragStateChangeNotifyEventHandler | Fired when starting or stopping the dragging of an Instant3D manipulator. |
| DAssemblyDocEvents_DynamicHighlightNotifyEventHandler | Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa. |
| DAssemblyDocEvents_EndInContextEditNotifyEventHandler | Notifies the application that the user is done editing an assembly component within the context of the assembly (inside the assembly document window). |
| DAssemblyDocEvents_EquationEditorPostNotifyEventHandler | Notifies your application that the equation editor is being destroyed. |
| DAssemblyDocEvents_EquationEditorPreNotifyEventHandler | Notifies your application that the equation editor has been constructed. |
| DAssemblyDocEvents_FeatureEditPreNotifyEventHandler | Pre-notifies the user program when the user edits the definition of a selected feature. |
| DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler | Fired when text is typed in the FeatureManager design tree filter or IModelDocExtension::FeatureManagerFilterString is called. |
| DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler | Fired when the active tab in the Manager Pane changes. |
| DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler | Fired before the active tab in the Manager Pane changes. |
| DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler | Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt. |
| DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler | Pre-notifies the user program when the user edits the definition of a sketch. |
| DAssemblyDocEvents_FileDropNotifyEventHandler | Fired when a part is dropped from File Explorer into an assembly. |
| DAssemblyDocEvents_FileDropPostNotifyEventHandler | Post-notifies user applications when a part is dropped from File Explorer into an assembly. |
| DAssemblyDocEvents_FileDropPreNotifyEventHandler | Pre-notifies user applications before a part is dropped from File Explorer into an assembly document. |
| DAssemblyDocEvents_FileReloadCancelNotifyEventHandler | Fired if the IAssembly event FileReloadNotify is canceled. |
| DAssemblyDocEvents_FileReloadNotifyEventHandler | Post-notifies the user program when an assembly document is reloaded. |
| DAssemblyDocEvents_FileReloadPreNotifyEventHandler | Pre-notifies the user program when an assembly document is reloaded. |
| DAssemblyDocEvents_FileSaveAsNotify2EventHandler | Pre-notifies the user program when a file is about to be saved with a new name and passes the new document name. This event is sent before SOLIDWORKS displays the File Save dialog. |
| DAssemblyDocEvents_FileSaveAsNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_FileSaveAsNotify2EventHandler . |
| DAssemblyDocEvents_FileSaveNotifyEventHandler | Pre-notifies the user program when a file is about to be saved and passes the current document name. |
| DAssemblyDocEvents_FileSavePostCancelNotifyEventHandler | Fired if FileSavePostNotify is not fired. |
| DAssemblyDocEvents_FileSavePostNotifyEventHandler | Post-notifies the user program when a file is saved in SOLIDWORKS. |
| DAssemblyDocEvents_FlipLoopNotifyEventHandler | Notifies your program when a loop flips. |
| DAssemblyDocEvents_InsertTableNotifyEventHandler | Notifies your program when a table has been inserted in an assembly. |
| DAssemblyDocEvents_InterferenceNotifyEventHandler | Notifies your program about an interference between parts in the assembly during the Move/Rotate Component command. |
| DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler | Fired when the Large Design Review state changes in this assembly. |
| DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler | Fired when a lighting dialog has been opened by the user. |
| DAssemblyDocEvents_LoadFromStorageNotifyEventHandler | Fired when it is safe to load data from third-party IStream storage. |
| DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler | Fired when it is safe to load data from third-party IStorage storage. |
| DAssemblyDocEvents_ModifyNotifyEventHandler | Fired when a document is marked dirty for the first time. |
| DAssemblyDocEvents_ModifyTableNotifyEventHandler | Notifies your program when a table has been modified in an assembly. |
| DAssemblyDocEvents_NewSelectionNotifyEventHandler | Post-notifies the user program when the selection list has changed. |
| DAssemblyDocEvents_OpenDesignTableNotifyEventHandler | Post-notifies your application that a design table has been opened for editing. |
| DAssemblyDocEvents_PreRenameItemNotifyEventHandler | Fired when a component document in an assembly is about to be renamed. |
| DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler | Generated when a body is cut into multiple bodies. |
| DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler | Fired when publishing an assembly document to SOLIDWORKS MBD 3D PDF. |
| DAssemblyDocEvents_RedoPostNotifyEventHandler | Fired after a Redo operation occurs in an assembly document. |
| DAssemblyDocEvents_RedoPreNotifyEventHandler | Fired before a Redo operation occurs in an assembly document. |
| DAssemblyDocEvents_RegenNotifyEventHandler | Pre-notifies the user program when an assembly document is about to be rebuilt. |
| DAssemblyDocEvents_RegenPostNotify2EventHandler | Post-notifies the user program when an assembly document is rebuilt. |
| DAssemblyDocEvents_RegenPostNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents RegenPostNotify2EventHandler . |
| DAssemblyDocEvents_RenamedDocumentNotifyEventHandler | Fired when saving an assembly document in which a renamed component file is referenced by other assembly documents. |
| DAssemblyDocEvents_RenameDisplayTitleNotifyEventHandler | Fired when the display title changes for an item in the FeatureManager design tree. |
| DAssemblyDocEvents_RenameItemNotifyEventHandler | Fired when an item is renamed in one of the SOLIDWORKS tree structures, such as the FeatureManager design tree or the ConfigurationManager tree. |
| DAssemblyDocEvents_SaveToStorageNotifyEventHandler | Fired when it is safe to save data to third-party IStream storage. |
| DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler | Fired when it is safe to save data to third-party IStorage storage. |
| DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler | Post-notifies the user program when assembly components are selected for Quick View/Selective Open. |
| DAssemblyDocEvents_SensorAlertPreNotifyEventHandler | Fired before a sensor's value deviates from its limits in an assembly document. |
| DAssemblyDocEvents_SketchSolveNotifyEventHandler | Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. |
| DAssemblyDocEvents_SuppressionStateChangeNotifyEventHandler | Fired when the suppression state of a feature changes. |
| DAssemblyDocEvents_UndoPostNotifyEventHandler | Fired after an Undo operation occurs in an assembly document. |
| DAssemblyDocEvents_UndoPreNotifyEventHandler | Fired before an Undo operation occurs in an assembly document. |
| DAssemblyDocEvents_UnitsChangeNotifyEventHandler | Fired when the document units change. |
| DAssemblyDocEvents_UserSelectionPostNotifyEventHandler | Fired after an entity is selected in an assembly document. |
| DAssemblyDocEvents_UserSelectionPreNotifyEventHandler | Fired when an interactive user moves the cursor over or clicks a model view in an assembly document. |
| DAssemblyDocEvents_ViewNewNotify2EventHandler | Post-notifies the user program when a new view model window has been created. |
| DAssemblyDocEvents_ViewNewNotifyEventHandler | Obsolete. Superseded by DAssemblyDocEvents_ViewNewNotify2EventHandler . |
| DDrawingDocEvents_ActivateSheetPostNotifyEventHandler | Notifies the user program after activating the drawing sheet. |
| DDrawingDocEvents_ActivateSheetPreNotifyEventHandler | Notifies the user program before activating the drawing sheet. |
| DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler | Pre-notifies the user program when the user is about to switch to a different configuration. |
| DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler | Post-notifies the user program when the user has switched to a different configuration. |
| DDrawingDocEvents_AddCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has added a custom property. |
| DDrawingDocEvents_AddItemNotifyEventHandler | Notifies the user program when an item is added to one of the SOLIDWORKS tree structures (for example, FeatureManager design tree, ConfigurationManager tree, and so on). |
| DDrawingDocEvents_AutoSaveNotifyEventHandler | Fired when the drawing document is automatically saved. |
| DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler | Fired when the drawing document is automatically saved to third-party IStream storage. |
| DDrawingDocEvents_AutoSaveToStorageStoreNotifyEventHandler | Fired when the drawing document is automatically saved to third-party IStorage storage. |
| DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has changed a custom property. |
| DDrawingDocEvents_ClearSelectionsNotifyEventHandler | Notifies the user program when selections are cleared using Clear Selections . |
| DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler | Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated. |
| DDrawingDocEvents_DeleteCustomPropertyNotifyEventHandler | Post-notifies the user program when the user deletes a custom property. |
| DDrawingDocEvents_DeleteItemNotifyEventHandler | Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree). |
| DDrawingDocEvents_DeleteItemPreNotifyEventHandler | Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree). |
| DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler | Pre-notifies the user program when the selection is deleted. |
| DDrawingDocEvents_DestroyNotify2EventHandler | Pre-notifies the user program when a drawing document is about to be destroyed. |
| DDrawingDocEvents_DestroyNotifyEventHandler | Obsolete. Superseded by DDrawingDocEvents_DestroyNotify2EventHandler . |
| DDrawingDocEvents_DimensionChangeNotifyEventHandler | Fired when a dimension is changed through the Dimension dialog. |
| DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler | Fired when a display pane is collapsed in this drawing. |
| DDrawingDocEvents_DisplayPaneExpandNotifyEventHandler | Fired when a display pane is expanded in this drawing. |
| DDrawingDocEvents_DrawingStateChangeNotifyEventHandler | Fired when a drawing's state changes. |
| DDrawingDocEvents_DynamicHighlightNotifyEventHandler | Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa. |
| DDrawingDocEvents_EquationEditorPostNotifyEventHandler | Notifies your application that the equation editor is being destroyed. |
| DDrawingDocEvents_EquationEditorPreNotifyEventHandler | Notifies your application that an the equation editor has been constructed. |
| DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler | Fired when the active tab in the Manager Pane changes. |
| DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler | Fired before the active tab in the Manager Pane changes. |
| DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler | Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt. |
| DDrawingDocEvents_FileReloadPreNotifyEventHandler | Pre-notifies the user application when a drawing document is reloaded. |
| DDrawingDocEvents_FileSaveAsNotify2EventHandler | Sends pre-notification before displaying the File, Save dialog. |
| DDrawingDocEvents_FileSaveAsNotifyEventHandler | Obsolete. Superseded by DDrawingDocEvents_FileSaveAsNotify2EventHandler . |
| DDrawingDocEvents_FileSaveNotifyEventHandler | Pre-notifies the user program when a file is about to be saved and passes the current document name. |
| DDrawingDocEvents_FileSavePostCancelNotifyEventHandler | Fired if FileSavePostNotify is not fired. |
| DDrawingDocEvents_FileSavePostNotifyEventHandler | Post-notifies the user program when a drawing is saved in SOLIDWORKS. |
| DDrawingDocEvents_InsertTableNotifyEventHandler | Notifies your program when a table has been inserted in a drawing. |
| DDrawingDocEvents_LoadFromStorageNotifyEventHandler | Fired when it is safe to load data from third-party IStream storage. |
| DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler | Fired when it is safe to load data from third-party IStorage storage. |
| DDrawingDocEvents_ModifyNotifyEventHandler | Fired when a document is marked as dirty for the first time. |
| DDrawingDocEvents_ModifyTableNotifyEventHandler | Notifies your program when a table has been modified in a drawing. |
| DDrawingDocEvents_NewSelectionNotifyEventHandler | Post-notifies the user program when the selection list has changed. |
| DDrawingDocEvents_RedoPostNotifyEventHandler | Fired after a Redo operation occurs in a drawing document. |
| DDrawingDocEvents_RedoPreNotifyEventHandler | Fired before a Redo operation occurs in a drawing document. |
| DDrawingDocEvents_RegenNotifyEventHandler | Pre-notifies the user program when a drawing document is about to be regenerated. |
| DDrawingDocEvents_RegenPostNotifyEventHandler | Post-notifies the user program when a drawing document has been regenerated. |
| DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler | Notifies the user program when the display title changes for an item in the FeatureManager design tree. |
| DDrawingDocEvents_RenameItemNotifyEventHandler | Notifies the user program when an item is renamed in one of the SOLIDWORKS tree structures (for example, such as the FeatureManager design tree or the ConfigurationManager tree). |
| DDrawingDocEvents_SaveToStorageNotifyEventHandler | Fired when it is safe to save data to third-party IStream storage. |
| DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler | Fired when it is safe to save data to third-party IStorage storage. |
| DDrawingDocEvents_SketchSolveNotifyEventHandler | Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated. |
| DDrawingDocEvents_UndoPostNotifyEventHandler | Fired after an Undo action occurs in a drawing document. |
| DDrawingDocEvents_UndoPreNotifyEventHandler | Fired before an Undo action occurs in a drawing document. |
| DDrawingDocEvents_UnitsChangeNotifyEventHandler | Raised when document units change. |
| DDrawingDocEvents_UserSelectionPostNotifyEventHandler | Fired after an entity is selected in a drawing document. |
| DDrawingDocEvents_UserSelectionPreNotifyEventHandler | Fired when an interactive user moves the cursor over or clicks a drawing view in a drawing document. |
| DDrawingDocEvents_ViewCreatePreNotifyEventHandler | Pre-notifies the user application when a drawing view is about to be created. |
| DDrawingDocEvents_ViewNewNotify2EventHandler | Post-notifies the user program when a new view window is created. |
| DDrawingDocEvents_ViewNewNotifyEventHandler | Obsolete. Superseded by DDrawingDocEvents_ViewNewNotify2EventHandler . |
| DFeatMgrViewEvents_ActivateNotifyEventHandler | Post-notifies the user program once a FeatureManager design tree view is activated and returns the view handle. |
| DFeatMgrViewEvents_DeactivateNotifyEventHandler | Post-notifies the user program once a FeatureManager design tree view is deactivated and returns the view handle. |
| DFeatMgrViewEvents_DestroyNotifyEventHandler | Pre-notifies the user program when a FeatureManager design tree view is about to be destroyed and returns the view handle. |
| DModelViewEvents_BufferSwapNotifyEventHandler | Fired from the model view immediately before the buffers are swapped when rendering shaded graphics in OpenGL. |
| DModelViewEvents_DestroyNotify2EventHandler | Pre-notifies the user program when a model view is about to be destroyed. |
| DModelViewEvents_DestroyNotifyEventHandler | Obsolete. Superseded by DModelViewEvents_DestroyNotify2EventHandler . |
| DModelViewEvents_DisplayModeChangePostNotifyEventHandler | Post-notifies the user program when a model view display mode is changed. |
| DModelViewEvents_DisplayModeChangePreNotifyEventHandler | Pre-notifies the user program when a model view display mode is about to be changed. |
| DModelViewEvents_GraphicsRenderPostNotifyEventHandler | Fired after all SOLIDWORKS graphics are drawn, including SOLIDWORKS model, sketch, dimension, and annotation graphics. |
| DModelViewEvents_PerspectiveViewNotifyEventHandler | Post-notifies the user program when the perspective view is changed (for example, if the user rotates the perspective view). |
| DModelViewEvents_PrintNotify2EventHandler | Notifies the user program when a document is printed. |
| DModelViewEvents_PrintNotifyEventHandler | Obsolete. Superseded by DModelViewEvents_PrintNotify2EventHandler . |
| DModelViewEvents_RenderLayer0NotifyEventHandler | Fired whenever SOLIDWORKS renders to Layer0. |
| DModelViewEvents_RepaintNotifyEventHandler | Pre-notifies the user program when a view is about to be repainted and returns the paint type. |
| DModelViewEvents_RepaintPostNotifyEventHandler | Post-notifies the user program when a view has been repainted. |
| DModelViewEvents_UserClearSelectionsNotifyEventHandler | Fired when a user: Clicks the right-mouse button when the pointer is over a selection box on a PropertyManager page. Selects Clear Selections on the short-cut menu. |
| DModelViewEvents_ViewChangeNotifyEventHandler | Post-notifies the user program when a view is altered and returns the new transform matrix of the view. |
| DMouseEvents_MouseLBtnDblClkNotifyEventHandler | Fired when the left-mouse button is double-clicked. |
| DMouseEvents_MouseLBtnDownNotifyEventHandler | Fired when the left-mouse button is pressed down. |
| DMouseEvents_MouseLBtnUpNotifyEventHandler | Fired when the left-mouse button is released after being pressed. |
| DMouseEvents_MouseMBtnDblClkNotifyEventHandler | Fired when the middle-mouse button is double-clicked. |
| DMouseEvents_MouseMBtnDownNotifyEventHandler | Fired when the middle-mouse button is pressed down. |
| DMouseEvents_MouseMBtnUpNotifyEventHandler | Fired when the middle-mouse button is released after being pressed. |
| DMouseEvents_MouseMoveNotifyEventHandler | Fired when the mouse pointer is moved. |
| DMouseEvents_MouseNotifyEventHandler | Fired whenever a mouse event occurs. |
| DMouseEvents_MouseRBtnDblClkNotifyEventHandler | Fired when the right-mouse button is double-clicked. |
| DMouseEvents_MouseRBtnDownNotifyEventHandler | Fired when the right-mouse button is pressed down. |
| DMouseEvents_MouseRBtnUpNotifyEventHandler | Fired when the right-mouse button is released after being pressed down. |
| DMouseEvents_MouseSelectNotifyEventHandler | Fired when the user makes a selection in the model view using the mouse. |
| DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler | Fired when the user changes the annotation view. |
| DPartDocEvents_ActiveConfigChangeNotifyEventHandler | Fired with the user switches to a different configuration. |
| DPartDocEvents_ActiveConfigChangePostNotifyEventHandler | Post-notifies the user program when the user has switched to a different configuration. |
| DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler | Fired after the display state of a configuration is changed or after a configuration is changed. |
| DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler | Fired before the display state of a configuration is changed or before a configuration is changed. |
| DPartDocEvents_ActiveViewChangeNotifyEventHandler | Fired when the active view changes. |
| DPartDocEvents_AddCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has added a custom property. |
| DPartDocEvents_AddItemNotifyEventHandler | Fired when an item is added to one of the SOLIDWORKS tree structures such as the FeatureManager design tree and the ConfigurationManager. |
| DPartDocEvents_AutoSaveNotifyEventHandler | Fired when the part document is automatically saved. |
| DPartDocEvents_AutoSaveToStorageNotifyEventHandler | Fired when the part document is automatically saved to third-party IStream storage. |
| DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler | Fired when the part document is automatically saved to third-party IStorage storage. |
| DPartDocEvents_BodyVisibleChangeNotifyEventHandler | Fired whenever the visible state of a body within this part changes. |
| DPartDocEvents_ChangeCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has changed a custom property. |
| DPartDocEvents_ClearSelectionsNotifyEventHandler | Notifies the user program when selections are cleared using Clear Selections . |
| DPartDocEvents_CloseDesignTableNotifyEventHandler | Pre-notifies your application that a design table that was opened for editing is about to be closed. |
| DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler | Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated. |
| DPartDocEvents_ConfigurationChangeNotifyEventHandler | Gets information about an object or feature that has had one if its configurable parameters changed. |
| DPartDocEvents_ConvertToBodiesPostNotifyEventHandler | Fired after the Convert to Bodies dialog closes. |
| DPartDocEvents_ConvertToBodiesPreNotifyEventHandler | Fired before the Convert to Bodies dialog opens. |
| DPartDocEvents_DeleteCustomPropertyNotifyEventHandler | Post-notifies the user program when the user has deleted a custom property. |
| DPartDocEvents_DeleteItemNotifyEventHandler | Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager. |
| DPartDocEvents_DeleteItemPreNotifyEventHandler | Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager. |
| DPartDocEvents_DeleteSelectionPreNotifyEventHandler | Pre-notifies the user when the selection is deleted. |
| DPartDocEvents_DestroyNotify2EventHandler | Pre-notifies the user program when a part document is about to be destroyed. |
| DPartDocEvents_DestroyNotifyEventHandler | Obsolete. Superseded by DPartDocEvents_DestroyNotify2EventHandler . |
| DPartDocEvents_DimensionChangeNotifyEventHandler | Fired when a dimension is changed through the Dimension dialog. |
| DPartDocEvents_DisplayPaneCollapseNotifyEventHandler | Fired when the Display Pane collapses in this part. |
| DPartDocEvents_DisplayPaneExpandNotifyEventHandler | Fired when the Display Pane expands in this part. |
| DPartDocEvents_DragStateChangeNotifyEventHandler | Fired when starting or stopping the dragging of an Instant3D manipulator. |
| DPartDocEvents_DynamicHighlightNotifyEventHandler | Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa. |
| DPartDocEvents_EquationEditorPostNotifyEventHandler | Notifies your application that the equation editor is being destroyed. |
| DPartDocEvents_EquationEditorPreNotifyEventHandler | Notifies your application that an the equation editor has been constructed. |
| DPartDocEvents_FeatureEditPreNotifyEventHandler | Pre-notifies the user program when the user edits the definition of a selected feature. |
| DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler | Fired when text is typed in the FeatureManager design tree filter or IModelDocExtension::FeatureManagerFilterString is called. |
| DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler | Fired when the active tab changes in the Manager Pane. |
| DPartDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler | Fired before the active tab in the Manager Pane changes. |
| DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler | Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt. |
| DPartDocEvents_FeatureSketchEditPreNotifyEventHandler | Pre-notifies the user program when the user edits the definition of a sketch. |
| DPartDocEvents_FileDropPostNotifyEventHandler | Post-notifies user applications when a part is dropped from File Explorer into a part document. |
| DPartDocEvents_FileDropPreNotifyEventHandler | Pre-notifies user applications before a part is dropped from File Explorer into a part document. |
| DPartDocEvents_FileReloadCancelNotifyEventHandler | Fired if FileReloadNotify is canceled. |
| DPartDocEvents_FileReloadNotifyEventHandler | Post-notifies the user program when a part document is reloaded. |
| DPartDocEvents_FileReloadPreNotifyEventHandler | Pre-notifies the user program when an part document is reloaded |
| DPartDocEvents_FileSaveAsNotify2EventHandler | Sends pre-notification before displaying the File, Save dialog. |
| DPartDocEvents_FileSaveAsNotifyEventHandler | Obsolete. Superseded by DPartDocEvents_FileSaveAsNotify2EventHandler . |
| DPartDocEvents_FileSaveNotifyEventHandler | Pre-notifies the user program when a file is about to be saved and passes the current document name. |
| DPartDocEvents_FileSavePostCancelNotifyEventHandler | Fired if FileSavePostNotify is not fired. |
| DPartDocEvents_FileSavePostNotifyEventHandler | Post-notifies the user program when a part document is saved. |
| DPartDocEvents_FlipLoopNotifyEventHandler | Fired when a loop is flipped. |
| DPartDocEvents_InsertTableNotifyEventHandler | Notifies your program when a table has been inserted in a part. |
| DPartDocEvents_LightingDialogCreateNotifyEventHandler | Fired when a lighting dialog has been opened by the user. |
| DPartDocEvents_LoadFromStorageNotifyEventHandler | Fired when it is safe to load data from third-party IStream storage. |
| DPartDocEvents_LoadFromStorageStoreNotifyEventHandler | Fired when it is safe to load data from third-party IStorage storage. |
| DPartDocEvents_ModifyNotifyEventHandler | Notifies the user program when a document is marked as dirty for the first time. |
| DPartDocEvents_ModifyTableNotifyEventHandler | Notifies your program when a table has been modified in a part. |
| DPartDocEvents_NewSelectionNotifyEventHandler | Post-notifies the user program when the selection list has changed. |
| DPartDocEvents_OpenDesignTableNotifyEventHandler | Post-notifies your application that a design table has been opened for editing. |
| DPartDocEvents_PreRenameItemNotifyEventHandler | Fired when a part document referenced by other documents is about to be renamed. |
| DPartDocEvents_PromptBodiesToKeepNotifyEventHandler | Generated when a body is cut into multiple bodies. |
| DPartDocEvents_PublishTo3DPDFNotifyEventHandler | Fired when publishing a part document to SOLIDWORKS MBD 3D PDF. |
| DPartDocEvents_RedoPostNotifyEventHandler | Fired after a Redo operation occurs in a part document. |
| DPartDocEvents_RedoPreNotifyEventHandler | Fired before a Redo operation occurs in a part document. |
| DPartDocEvents_RegenNotifyEventHandler | Pre-notifies the user program when a part document is about to be rebuilt. |
| DPartDocEvents_RegenPostNotify2EventHandler | Post-notifies the user program when a part document has been rebuilt or rolled back. |
| DPartDocEvents_RegenPostNotifyEventHandler | Obsolete. Superseded by DPartDocEvents_RegenPostNotify2EventHandler . |
| DPartDocEvents_RenamedDocumentNotifyEventHandler | Fired when saving a document in which a renamed part file is referenced by other documents. |
| DPartDocEvents_RenameDisplayTitleNotifyEventHandler | Fired when the display title is changed for an item in the FeatureManager design tree. |
| DPartDocEvents_RenameItemNotifyEventHandler | Fired when an item is renamed in one of the SOLIDWORKS tree structures, such as the FeatureManager design tree or the ConfigurationManager. |
| DPartDocEvents_SaveToStorageNotifyEventHandler | Fired when it is safe to save data to third-party IStream storage. |
| DPartDocEvents_SaveToStorageStoreNotifyEventHandler | Fired when it is safe to save data to third-party IStorage storage. |
| DPartDocEvents_SensorAlertPreNotifyEventHandler | Fired before a sensor's value deviates from its limits in a part document. |
| DPartDocEvents_SketchSolveNotifyEventHandler | Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated. |
| DPartDocEvents_SuppressionStateChangeNotifyEventHandler | Fired when the suppression state of a feature changes. |
| DPartDocEvents_UndoPostNotifyEventHandler | Fired after an Undo action occurs in a part document. |
| DPartDocEvents_UndoPreNotifyEventHandler | Fired before an Undo operation occurs in a part document. |
| DPartDocEvents_UnitsChangeNotifyEventHandler | Generated when document units change. |
| DPartDocEvents_UserSelectionPostNotifyEventHandler | Fired after an entity is selected in a part document. |
| DPartDocEvents_UserSelectionPreNotifyEventHandler | Fired when an interactive user moves the cursor over or clicks a model view in a part document. |
| DPartDocEvents_ViewNewNotify2EventHandler | Post-notifies the user program when a new model view window is created. For example, this event is sent for each new model view created by the window split bar. |
| DPartDocEvents_ViewNewNotifyEventHandler | Obsolete. Superseded by DPartDocEvents_ViewNewNotify2EventHandler . |
| DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler | Post-notifies the user program when the weldment cut list in this part is updated. |
| DSldWorksEvents_ActiveDocChangeNotifyEventHandler | Post-notifies the user program when the active window has changed. This change can be between windows of the same document or between windows of different documents. |
| DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler | Post-notifies the user program when the active IModelDoc2 object has changed. |
| DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler | Notifies the user program when background processing has ended. |
| DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler | Notifies the user program when background processing has started. |
| DSldWorksEvents_Begin3DInterconnectTranslationNotifyEventHandler | Notifies the user program when the SOLIDWORKS application starts to import or export a third-party native CAD file. |
| DSldWorksEvents_BeginRecordNotifyEventHandler | Notifies the user program when a macro recording has started. |
| DSldWorksEvents_BeginTranslationNotifyEventHandler | Notifies the user program when the SOLIDWORKS applications starts to import a file. |
| DSldWorksEvents_CommandCloseNotifyEventHandler | Fired when a command, including a PropertyManager page, is okay'd or canceled by a user. |
| DSldWorksEvents_CommandOpenPreNotifyEventHandler | Fired before a command, including a PropertyManager page, executes or opens. |
| DSldWorksEvents_DestroyNotifyEventHandler | Sent to an MFC-based or a COM-based DLL add-in when SOLIDWORKS is about to be destroyed. |
| DSldWorksEvents_DisplayPaneActivationNotifyEventHandler | Fired when the Display Pane is activated. |
| DSldWorksEvents_DocumentConversionNotifyEventHandler | Post-notifies the user program that a file has been converted from an older version of SOLIDWORKS during the open operation. |
| DSldWorksEvents_DocumentLoadNotify2EventHandler | Post-notifies the user program when a SOLIDWORKS document is loaded. |
| DSldWorksEvents_DocumentLoadNotifyEventHandler | Obsolete. Superseded by DSldWorksEvetns_DocumentLoadNotify2EventHandler . |
| DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler | Notifies the user program when the SOLIDWORKS application is finished importing or exporting a third-party native CAD file. |
| DSldWorksEvents_EndRecordNotifyEventHandler | Notifies the user program when a macro recording has ended, including if the user cancels the recording (i.e., the user cancels out of the Save As dialog and says No to the SOLIDWORKS Continue recording? dialog). |
| DSldWorksEvents_EndTranslationNotifyEventHandler | Notifies the user program when the SOLIDWORKS application is finished importing a file. |
| DSldWorksEvents_FileCloseNotifyEventHandler | Notifies the user program when SOLIDWORKS is finished closing a file. |
| DSldWorksEvents_FileNewNotify2EventHandler | Post-notifies the user program when a new file is created. |
| DSldWorksEvents_FileNewNotifyEventHandler | Obsolete. Superseded by DSldWorksEvents_FileNewNotify2EventHandler . |
| DSldWorksEvents_FileNewPreNotifyEventHandler | Fired before a new document is created either using the SOLIDWORKS API or the SOLIDWORKS user-interface. |
| DSldWorksEvents_FileOpenNotify2EventHandler | Post-notifies the user program when an existing file has been opened. |
| DSldWorksEvents_FileOpenNotifyEventHandler | Obsolete. Superseded by DSldWorksEvents_FileOpenNotify2EventHandler . |
| DSldWorksEvents_FileOpenPostNotifyEventHandler | Post-notifies the user program when a file has been opened. |
| DSldWorksEvents_FileOpenPreNotifyEventHandler | Pre-notifies the user program of a FileOpenNotify2 event. |
| DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler | Notifies an add-in when the SOLIDWORKS background changes. |
| DSldWorksEvents_LightSheetCreateNotifyEventHandler | Fired when a lighting sheet has been created. |
| DSldWorksEvents_NonNativeFileOpenNotifyEventHandler | Fired when non-native SOLIDWORKS files are opened. |
| DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler | Fired when 3DExperience changes state. |
| DSldWorksEvents_OnIdleNotifyEventHandler | Fired after all of the messages have been processed, included posted repaints; therefore, eliminating the need to call IModelDoc2::GraphicsRedraw2 . |
| DSldWorksEvents_PromptForFilenameNotifyEventHandler | Fired when a dependent document is missing from the file being opened. |
| DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler | Fired when any dependent documents are missing from the file being opened. |
| DSldWorksEvents_PropertySheetCreateNotifyEventHandler | Notifies the user program when an exported ISWPropertySheet is created so that the application can add pages to it. |
| DSldWorksEvents_ReferencedFilePreNotify2EventHandler | Notifies the user program before SOLIDWORKS opens the specified file with the specified status. |
| DSldWorksEvents_ReferencedFilePreNotifyEventHandler | Obsolete. Superseded by DSldWorksEvents_ReferencedFilePreNotify2EventHandler . |
| DSldWorksEvents_ReferenceNotFoundNotifyEventHandler | Notifies the user program before the SOLIDWORKS software displays a dialog box prompting the end-user to browse for the referenced file. |
| DSldWorksEvents_TaskPaneCollapseNotifyEventHandler | Fired when the Task Pane collapses. |
| DSldWorksEvents_TaskPaneExpandNotifyEventHandler | Fired when the Task Pane expands. |
| DSldWorksEvents_TaskPaneHideNotifyEventHandler | Fired when the Task Pane hides. |
| DSldWorksEvents_TaskPanePinnedNotifyEventHandler | Fired when the Task Pane is pinned. |
| DSldWorksEvents_TaskPaneShowNotifyEventHandler | Fired when the Task Pane displays. |
| DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler | Fired when the Task Pane is unpinned. |
| DSWPropertySheetEvents_CreateControlNotifyEventHandler | Fired when the ActiveX control is created on the property page. |
| DSWPropertySheetEvents_DestroyNotifyEventHandler | Fired when the property sheet is in the process of being destroyed. |
| DSWPropertySheetEvents_HelpNotifyEventHandler | Fired when the Help button is clicked on a property sheet. |
| DSWPropertySheetEvents_OnCancelNotifyEventHandler | Fired when the Cancel button on the property sheet is clicked. Your add-in can perform clean-up activities in this event. |
| DSWPropertySheetEvents_OnOKNotifyEventHandler | Fired when the OK button on the property sheet is clicked. |
| DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler | Post-notifies the user program when an application-level Task Pane view is activated. |
| DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler | Post-notifies the user program when an application-level Task Pane view is deactivated. |
| DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler | Pre-notifies the user program when an application-level Task Pane view is about to be destroyed. |
| DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler | Fired when a toolbar button on the Task Pane is clicked. |

## See Also

[SolidWorks.Interop.sldworks Assembly](SolidWorks.Interop.sldworks.html)
