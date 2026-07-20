---
title: "swCommands_e Enumeration"
project: "SOLIDWORKS API Commands Enumeration"
interface: "swCommands_e"
member: ""
kind: "enum"
source: "swcommands/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html"
---

# swCommands_e Enumeration

SOLIDWORKS toolbar and menu commands.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCommands_e
   Inherits System.Enum
```

### C#

```csharp
public enum swCommands_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCommands_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCommand_Border_Editor | 3156; valid only for drawings in Edit Sheet Format mode (run swCommands_e.swCommands_Edit_Template before running this command); Sheet Format toolbar > Automatic Border |
| swCommand_Cartoon_Shading | 3170; valid only for assemblies and parts; View toolbar > View Settings > Cartoon |
| swCommand_ChildReferenceArrow | 3152; valid only for assemblies; Assembly toolbar > Dynamic Reference Visualization (Child) |
| swCommand_Component_Preview_Window | 3171; valid only for assemblies; Assembly toolbar > Component Preview Window |
| swCommand_Delete_Selected_BE | 3158; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; selects all items in Delete List |
| swCommand_Deselect_All_Selected_BE | 3160; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; deselects all selections in Delete List |
| swCommand_Hide_Show_Primary_Planes | 3169; valid only for parts; View toolbar > Hide / Show Primary Planes |
| swCommand_ReferenceArrow_PopUp | 3151; valid only for assemblies; Assembly toolbar > Dynamic Reference Visualization (Parent) |
| swCommand_Restore_Selected_BE | 3159; valid only for drawings in Edit Sheet Format mode while the Automatic Border PropertyManager page is open; restores the selected items in Delete List |
| swCommand_Sheet_Format | 3155; valid only for drawings; View menu > Toolbars > Sheet Format |
| swCommand_TemporaryFixGroup | 3162; valid only for assemblies; Assembly toolbar > Temporary Fix/Group |
| swCommands_2DTo3D | 509; alternative to swCommands_Toolbar_2dto3d; View menu > Toolbars > 2D to 3D |
| swCommands_2DTo3DCut | 394; valid only for parts with a single 2D sketch in edit mode; 2D to 3D toolbar > Convert to Cut |
| swCommands_2DTo3DMakeRefsketchBack | 378; valid only for parts with a single 2D sketch in edit mode; 2D to 3D toolbar > Add to Back Sketch |
| swCommands_2DTo3DMakeRefsketchBottom | 376; valid only for parts with a single 2D sketch in edit mode; 2D to 3D toolbar > Add to Bottom Sketch |
| swCommands_2DTo3DMakeRefsketchFront | 373; valid only for parts with a single 2D sketch in edit mode; 2D to 3D toolbar > Add to Front Sketch |
| swCommands_2DTo3DMakeRefsketchLeft | 377; valid only for parts with a 2D sketch in edit mode; 2D to 3D toolbar > Add to Left Sketch |
| swCommands_2DTo3DMakeRefsketchRight | 375; valid only for parts with a 2D sketch in edit mode; 2D to 3D toolbar > Add to Right Sketch |
| swCommands_2DTo3DMakeRefsketchTop | 374; valid only for parts with a 2D sketch in edit mode; 2D to 3D toolbar > Add to Top Sketch |
| swCommands_3DDrawingView | 548; valid only for drawings; View toolbar > 3D Drawing View |
| swCommands_3dExperienceDesignEngineer | 3288; launches 3DEXPERIENCE from SOLIDWORKS Simulation; Tools toolbar > 3DEXPERIENCE Simulation Connector |
| swCommands_3DPDF_ADD_ALL_3DVIEWS | 3401; MBD toolbar > Publish to 3D PDF > Include Primary Views > Select all views |
| swCommands_3dpmi | 3212; opens the 3D PMI Compare PropertyManager page; Tools menu > 3D PMI Compare Wizard |
| swCommands_3dPrintValidation | 3191; opens the 3-D Print Validation PropertyManager page; View toolbar > 3D Print Validation |
| swCommands_3DSketch | 89; Sketch toolbar > 3D Sketch |
| swCommands_3DSketchOnPlane | 567; valid only for pre-selected planes; Sketch toolbar > 3D Sketch On Plane |
| swCommands_3dTexturizeSolidSurface | 3333; converts solid and surface bodies to texturized graphics bodies; Features toolbar > Texturize Bodies |
| swCommands_3PointArc | 80; Sketch toolbar > 3 Point Arc |
| swCommands_Activate_And_Orient_Annotation_View | 2230; valid only for inactive annotation views that are oriented; in the FeatureManager design tree, Annotations > annotation_view RMB menu > Activate and Reorient |
| swCommands_Activate_Annotation_View | 2213; in the FeatureManager design tree, Annotations > annotation_view RMB menu > Activate |
| swCommands_Activate_Doc_Or_Journal | 2059; in the FeatureManager design tree, Design Binder > doc_name RMB menu > Open |
| swCommands_Activate_Sheet | 1206; valid for a selected drawing sheet that is not activated, current, or in edit mode; in the FeatureManager design tree, sheet RMB menu > Activate |
| swCommands_ActivateFlexiblePartComp | 3418; Assembly toolbar > Make Part Flexible |
| swCommands_Add_Bends | 2290; valid for SOLIDWORKS Electrical add-in and an open assembly with a selected route junction point, opens the Add Bends PropertyManager page; Electrical toolbar > Add Bends |
| swCommands_Add_Comment | 2062; in the FeatureManager design tree, component_feature_or_sheet RMB menu > Comment > Add Comment |
| swCommands_Add_Configuration | 1534; in the ConfigurationManager, configuration_name RMB menu > Add Configuration or Add Derived Configuration |
| swCommands_Add_Constraint_Alongx | 2204; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Along X ; when the Line Properties PropertyManager page is open for a selected line in the graphics area, sel_line RMB context menu > Make AlongX |
| swCommands_Add_Constraint_Alongy | 2205; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Along Y ; when the Line Properties PropertyManager page is open for a selected line in the graphics area, sel_line RMB context menu > Make AlongY |
| swCommands_Add_Constraint_Alongz | 2206; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Along Z ; when the Line Properties PropertyManager page is open for a selected line in the graphics area, sel_line RMB context menu > Make AlongZ |
| swCommands_Add_Constraint_Atinter | 1719; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Intersection |
| swCommands_Add_Constraint_Atmid | 1718; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Midpoint |
| swCommands_Add_Constraint_Atpierce | 1724; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Pierce |
| swCommands_Add_Constraint_Coinc | 1720; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Coincident |
| swCommands_Add_Constraint_Colinear | 1712; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Colinear |
| swCommands_Add_Constraint_Concent | 1717; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Concentric |
| swCommands_Add_Constraint_Coradial | 1713; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Coradial |
| swCommands_Add_Constraint_Equalcurvature | 1729; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Equal Curvature |
| swCommands_Add_Constraint_Equaltangent | 1730; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Equal tangent |
| swCommands_Add_Constraint_Fix | 1723; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Fix ; when the Line Properties PropertyManager page is open for a selected line in the graphics area, sel_line RMB context menu > Make Fixed |
| swCommands_Add_Constraint_G3Touch | 3425; valid only for part sketches in edit mode with a multi-selected arc and spline, adds a continuous curvature variation relation to the selected arc and spline; in the Properties PropertyManager page click Add Relations > Torsion Continuity ; in the pop-up constraints dialog, click Make Torsion Continuity |
| swCommands_Add_Constraint_Horiz | 1710; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Horizontal |
| swCommands_Add_Constraint_Merge | 1725; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Merge |
| swCommands_Add_Constraint_Normal | 1726; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Normal |
| swCommands_Add_Constraint_Onsurface | 2217; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > On Surface |
| swCommands_Add_Constraint_Parallel | 1715; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Parallel |
| swCommands_Add_Constraint_Parallelyz | 1727; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Parallel YZ |
| swCommands_Add_Constraint_Parallelzx | 1728; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Parallel ZX |
| swCommands_Add_Constraint_Perp | 1714; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Perpendicular |
| swCommands_Add_Constraint_Planar_Offset | 3003; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Offset |
| swCommands_Add_Constraint_SameCurvelen | 3153; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Equal Arc/Spline |
| swCommands_Add_Constraint_Samelen | 1721; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Equal |
| swCommands_Add_Constraint_Sym | 1722; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Symmetric |
| swCommands_Add_Constraint_Tanface | 1731; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Tangent to Face |
| swCommands_Add_Constraint_Tang | 1716; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Tangent |
| swCommands_Add_Constraint_Traction | 1732; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Traction |
| swCommands_Add_Constraint_Vert | 1711; accessible only for part sketches in edit mode where this relation is possible; click Sketch toolbar > Relations > Add Relation or Tools menu > Relations > Add ; select a sketch segment in the graphics area; in the Add Relations PropertyManager page click Add Relations > Vertical |
| swCommands_Add_Coverings | 2286; valid for the SOLIDWORKS Routing add-in and a selected route segment in an open routing assembly, opens the Covering PropertyManager page ; Routing Tools toolbar > Covering |
| swCommands_Add_Derived_Configuration | 2461; in the ConfigurationManager, configuration_name RMB menu > Add Derived Configuration |
| swCommands_Add_Feature_Dims | 1552; valid for dimensioned parts; in FeatureManager design tree, f eature_name RMB menu > Show All Dimensions |
| swCommands_Add_Fitting | 2285; valid for the SOLIDWORKS Routing add-in and a routing assembly ; Piping or Flexible Tubing or User Defined toolbar > Add Fitting |
| swCommands_Add_OverallDim_To_ChainDim | 3424; valid only if an overall chain dimension does not already exist for the chain dimension set, automatically adds an overall dimension between a selected dimension in the chain dimension set and the dimension(s) that are farthest from the selection, in both directions if applicable; RMB menu > Add Overall |
| swCommands_Add_Part_Block | 2823; valid for blocks created in assembly layouts; in the FeatureManager design tree, block_name RMB menu > Make Part from Block |
| swCommands_Add_Slope | 3103; valid for the SOLIDWORKS Routing add-in and a piping assembly, opens the Pipe Slope PropertyManager page ; Piping toolbar > Add Slope |
| swCommands_Add_Split_Feat_To_Asm | 1818; valid only for parts with a split feature; Insert menu > Features > Create Assembly |
| swCommands_Add_To_Bookmark | 3514; valid only in SOLIDWORKS Connected, adds the current file to the bookmark folder; Lifecycle and Collaboration toolbar > Bookmarks > Add to Bookmark |
| swCommands_Add_to_CMarkSet | 3131; valid only for drawings with a center mark set; in the graphics view, center_mark RMB menu >Add to Center Mark Set |
| swCommands_Add_To_Palette | 2171; valid for parts with a selected geometric tolerance symbol, opens the Add to Library PropertyManager page; in the graphics area, geo_tol RMB menu > Add to Library ; also valid for assemblies; in the FeatureManager design tree, component_name RMB menu > Add to Library |
| swCommands_Add_To_Recent_Bookmark | 3525; valid only in SOLIDWORKS Connected, adds selected files and components to your recent bookmarks; Lifecycle and Collaboration toolbar > Bookmarks > Add to Recent Bookmark |
| swCommands_AddCurvatureControl | 416; valid only for 2D spline sketches; Spline Tools toolbar > Add Curvature Control |
| swCommands_AddRelation | 71; valid for sketches in edit mode; Dimensions/Relations toolbar > Add Relation |
| swCommands_AddRemove | 515; valid for blocks in edit mode; Layout or Blocks toolbar >Add/Remove |
| swCommands_AddTangencyControl | 415; valid only for 2D and 3D spline sketches; Spline Tools toolbar > Add Tangency Control |
| swCommands_AddTo_Chain_Dimension | 3406; valid for a selected dimension in a chain dimension set; RMB menu > Add to Chain |
| swCommands_AdvancedHoleWizard | 3172; opens the Hole Specification PropertyManager page; Features toolbar > Advanced Hole Wizard |
| swCommands_AdvancedStructuralMember | 3335; creates a structural member feature by sweeping pre-defined profiles along user-defined paths; Structure System toolbar > Create Structure System |
| swCommands_Align | 474; alternative to swCommands_Toolbar_Align; View menu > Toolbars > Align |
| swCommands_Align_Horz | 1511; valid for drawing view items; in the graphics area, view_item RMB menu > Alignment > Align Horizontal by Origin |
| swCommands_Align_Horz_By_Center | 695; valid for drawing view items; in the graphics area, view_item RMB menu > Alignment > Align Horizontal by Center |
| swCommands_Align_Ordinate | 1505; valid for drawings of circles or arcs with angular running dimensions; in the graphics area, angular_running_dimensi on RMB menu > Display Options > Align Running Dimension |
| swCommands_Align_Vert | 1512; valid for drawing view items; in the graphics area, view_item RMB menu > Alignment > Align Vertical by Origin |
| swCommands_Align_Vert_By_Center | 694; valid for drawing view items; in the graphics area, view_item RMB menu > Alignment > Align Vertical by Center |
| swCommands_Align_With_Assy_Origin | 2274; valid in assemblies after component RMB menu > Move with Triad command; in the graphics area, triad_center_ball RMB menu > Align with Assembly Origin |
| swCommands_Align_With_Comp_Origin | 2273; valid in assemblies after component RMB menu > Move with Triad command; in the graphics area, triad_center_ball RMB menu > Align with Component Origin |
| swCommands_Align_With_Selection | 2279; valid after component RMB menu > Move with Triad command in assembly; in the graphics area, triad_ball_arrow RMB menu > Align with selection |
| swCommands_AlignBetweenLines | 579; valid in drawings where a dimension or annotation and two vertical or horizontal lines are selected; Align toolbar > Align Between Lines |
| swCommands_AlignBottom | 310; valid for multi-selected annotations or dimensions; Align toolbar > Align Bottom |
| swCommands_AlignCollinearRadial | 145; valid for multi-selected dimensions; Align toolbar > Align Collinear/Radial |
| swCommands_AlignedSectionView | 108; valid for parts and assemblies; in the Section View Assist PropertyManager page; Cutting Line > Aligned |
| swCommands_AlignHorizontal | 314; valid for multi-selected annotations or dimensions; Align toolbar > Align Horizontal |
| swCommands_AlignLeft | 389; valid for selected text; Formatting toolbar > Align Left |
| swCommands_AlignParallelConcentric | 146; valid for multi-selected dimensions; Align toolbar > Align Parallel/Concentric |
| swCommands_AlignRight | 388; valid for selected text; Formatting toolbar > Align Right |
| swCommands_AlignSketch | 379; valid for parts; 2D To 3D toolbar > Align Sketch or Tools > Sketch Tools > Align > Sketch |
| swCommands_AlignTop | 309; valid for multi-selected annotations or dimensions; Align toolbar > Align Top |
| swCommands_AlignVertical | 315; valid for multi-selected annotations or dimensions; Align toolbar > Align Vertical |
| swCommands_AlternatePositionView | 357; valid for a selected drawing sheet with alternate position views; Drawing toolbar > Alternate Position View |
| swCommands_AlternativeHandwrittenDim_0 | 3388; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the first of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_1 |
| swCommands_AlternativeHandwrittenDim_1 | 3389; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the second of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_2 |
| swCommands_AlternativeHandwrittenDim_2 | 3390; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the third of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_3 |
| swCommands_AlternativeHandwrittenDim_3 | 3391; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the fourth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_4 |
| swCommands_AlternativeHandwrittenDim_4 | 3392; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the fifth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_5 |
| swCommands_AlternativeHandwrittenDim_5 | 3393; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the sixth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_6 |
| swCommands_AlternativeHandwrittenDim_6 | 3394; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the seventh of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_7 |
| swCommands_AlternativeHandwrittenDim_7 | 3395; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the eighth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_8 |
| swCommands_AlternativeHandwrittenDim_8 | 3396; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the ninth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_9 |
| swCommands_AlternativeHandwrittenDim_9 | 3397; valid only on supporting pen/stylus hardware, updates a selected handwritten dimension with the tenth of ten alternative values that were calculated from InkAnalysis handwriting recognition; RMB dimension context menu > alternative_value_10 |
| swCommands_Ambient_Occlusion | 3030; valid only if RealView Graphics is enabled in parts and assemblies; View toolbar > View Settings > Ambient Occlusion |
| swCommands_AnalysistoolsDraftAnalysis | 2885; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Draft Analysis |
| swCommands_AnalysistoolsPartingLineAnalysis | 2887; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Parting Line Analysis |
| swCommands_AnalysistoolsUndercutAnalysis | 2886; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Undercut Analysis |
| swCommands_AngleSnap | 536; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > Angle Snap |
| swCommands_AngularOrdinateDimension | 3068; valid only for arcs in drawing views; Dimensions/Relations toolbar > Angular Running Dimension |
| swCommands_Anim_Custom_Msg_Display_Camera_By_Name | 2353; valid only in the context of Motion Studies for a selected Orientation and Camera View bar key; in the Motion Study gantt chart, orientation_and_camera_views_time_bar_key RMB menu > View Orientation > camera_view_name |
| swCommands_Anim_Custom_Msg_Display_Vw_By_Name | 2352; valid only in the context of Motion Studies for a selected Orientation and Camera View bar key; in the Motion Study gantt chart, orientation_and_camera_views_time_bar_key RMB menu > View Orientation > view_name |
| swCommands_Anim_Edit_Dim | 2798; valid only in the context of Motion Studies; in the MotionManager tree, MateGroup1 > mate_name > mate_dimension RMB menu > Edit Dimension |
| swCommands_Anim_Lock_Viewpoint | 2644; valid only in the context of Motion Studies; in the MotionManager tree, Orientation and Camera Views RMB menu > Disable View Key Creation |
| swCommands_Anim_Suppress_Viewpoint | 2643; valid only in the context of Motion Studies; in the MotionManager tree, Orientation and Camera Views RMB menu > Disable Playback of View Keys |
| swCommands_Anim_View_Back | 2344; valid only in the context of Motion Studies for a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Back |
| swCommands_Anim_View_Bottom | 2348 valid only in the context of Motion Studies for a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Bottom |
| swCommands_Anim_View_Camera | 2354; valid only in the context of Motion Studies with a camera view and for a selected Orientation and Camera View time bar; in the Motion Study gantt chart, orientation_and_camera_views_time_bar RMB > Camera View |
| swCommands_Anim_View_Dimetric | 2351; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Dimetric |
| swCommands_Anim_View_Front | 2343; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Front |
| swCommands_Anim_View_Isometric | 2349; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Isometric |
| swCommands_Anim_View_Left | 2345; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Left |
| swCommands_Anim_View_Right | 2346; valid only in the context of Motion Studies and a selected Orientation and Camera View row; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Right |
| swCommands_Anim_View_Top | 2347; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Top |
| swCommands_Anim_View_Trimetric | 2350; valid only in the context of Motion Studies and a selected Orientation and Camera View time bar; in the gantt chart, orientation_and_camera_views_time_bar RMB menu > View Orientation > Trimetric |
| swCommands_Animation_CancelSolver | 2929; Motion Study tab RMB menu > Cancel Solver Status |
| swCommands_Animation_Delete | 2144; Motion Study tab RMB menu > Delete |
| swCommands_Animation_Duplicate | 2827; Motion Study tab RMB menu > Duplicate |
| swCommands_Animation_Ff | 1962; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Fast Forward |
| swCommands_Animation_Goto_End | 1963; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, End |
| swCommands_Animation_Goto_Start | 1959; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Start |
| swCommands_Animation_MoveCurTime | 2918; valid only in the context of Motion Studies; opens the Edit Time dialog; in Motion Study gantt chart, RMB menu > Move Time Bar |
| swCommands_Animation_New | 2142; valid for assemblies; Assembly toolbar > New Motion Study |
| swCommands_Animation_Pause | 1964; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Pause |
| swCommands_Animation_Play | 1961; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Play |
| swCommands_Animation_Play_Fast | 1971; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Fast Play |
| swCommands_Animation_Play_From_Start | 657; MotionManager toolbar > Play from Start |
| swCommands_Animation_Play_Loop | 1968; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Playback Mode: Loop |
| swCommands_Animation_Play_Normal | 1967; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Playback Mode: Normal |
| swCommands_Animation_Play_Reciprocate | 1969; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Playback Mode: Reciprocate |
| swCommands_Animation_Play_Slow | 1970; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Slow Play |
| swCommands_Animation_Record | 1966; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Save Animation |
| swCommands_Animation_Rename | 2143; Motion Study tab RMB menu > Rename |
| swCommands_Animation_Rewind | 1960; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Rewind |
| swCommands_Animation_SolverStatus | 2930; Motion Study tab RMB menu > Show Solver Status |
| swCommands_Animation_Stop | 1965; valid only when exploding a view or collapsing an exploded view; Configurations tab > exploded_view_name RMB menu > Animate Explode/Collapse ; in Animation Controller Pop-Up Toolbar, Stop |
| swCommands_Animation_Wizard | 659; valid only in the context of Motion Studies, opens the Select an Animation Type dialog; in a Motion Study gantt chart, RMB menu > Animation Wizard; also available on the MotionManager toolbar |
| swCommands_AnimEditTime_Dlg_Cancel | 2920; valid only in the context of Motion Studies; in the Motion Study gantt chart RMB menu > Move Time Bar > Edit Time dialog > Cancel |
| swCommands_AnimEditTime_Dlg_Increment | 2923; valid only in the context of Motion Studies; in the Motion Study gantt chart RMB menu > Move Time Bar > Edit Time dialog > Spin Increment |
| swCommands_AnimEditTime_Dlg_Ok | 2919; valid only in the context of Motion Studies; in the Motion Study gantt chart RMB menu > Move Time Bar > Edit Time dialog > OK |
| swCommands_AnimEditTime_Dlg_SetOffset | 2922; valid only in the context of Motion Studies; in the Motion Study gantt chart RMB menu > Move Time Bar > Edit Time dialog > Offset |
| swCommands_AnimEditTime_Dlg_SetTime | 2921; valid only in the context of Motion Studies; in the Motion Study gantt chart RMB menu > Move Time Bar > Edit Time dialog > Exact Time |
| swCommands_Animkey_Clear | 2137; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, orientation_and_camera_views_time_bar_key RMB > Delete |
| swCommands_Animkey_Copy | 2135; valid only in the context of Motion Studies for a selected gantt chart time bar key; in Motion Study gantt chart, time_bar_key RMB menu > Copy |
| swCommands_Animkey_Cut | 2134; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, time_bar_key RMB menu > Cut |
| swCommands_Animkey_EditTime | 2917; valid only in the context of Motion Studies for a selected gantt chart time bar key, opens the Edit Time dialog; in the Motion Study gantt chart, time_bar_key RMB menu > Edit Key Point Time |
| swCommands_Animkey_Interp_Easein_Sin | 2161; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, time_bar_key_pos_B RMB menu > Interpolation mode > Ease in |
| swCommands_Animkey_Interp_Easeinout_Sin | 2163; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, time_bar_key_pos_B RMB menu > Interpolation mode > Ease in/Ease out |
| swCommands_Animkey_Interp_Easeout_Sin | 2162; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, time_bar_key_pos_B RMB menu > Interpolation mode > Ease out |
| swCommands_Animkey_Interp_Linear | 2157; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, time_bar_key_pos_B RMB menu > Interpolation mode > Linear |
| swCommands_Animkey_Interp_Step_End | 2156; valid only in the context of Motion Studies for a selected gantt chart time bar key at position B; in the Motion Study gantt chart, time_bar_key_pos_B RMB menu > Interpolation mode > Snap |
| swCommands_Animkey_Paste | 2136; valid only in the context of Motion Studies for a copied gantt chart time bar key; in the Motion Study gantt chart, time_bar_key RMB menu > Paste |
| swCommands_Animkey_Place | 2140; valid only in the context of Motion Studies; in the Motion Study gantt chart, RMB menu > Place Key |
| swCommands_Animkey_Replace | 2141; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, time_bar_key RMB menu > Replace Key |
| swCommands_Animkey_Reverse_Path | 2150; valid only in the context of Motion Studies for a selected assembly gantt chart time bar key; in the Motion Study gantt chart, time_bar_key RMB menu > Reverse Path |
| swCommands_Animkey_Select_All | 2138; valid only in the context of Motion Studies; in the Motion Study gantt chart, RMB menu > Select All |
| swCommands_Animkey_Suppress | 2155; valid only in the context of Motion Studies for a selected gantt chart time bar key; in the Motion Study gantt chart, time_bar_key RMB > Suppress Key |
| swCommands_AnimMateSuppress | 2932; valid only in the context of Motion Studies for a selected mate; in the Motion Study gantt chart, mate_line_gantt_time_bar RMB menu > Suppress |
| swCommands_AnimMateUnsuppress | 2933; valid only in the context of Motion Studies for a selected mate; in the Motion Study gantt chart, mate_line_gantt_time_bar RMB menu > Unsuppress |
| swCommands_Ann_Feat_Dim | 1550; in the FeatureManager design tree, Annotations folder RMB menu > Show Feature Dimensions |
| swCommands_Ann_Ref_Dim | 1551; in the FeatureManager design tree, Annotations folder RMB menu > Show Reference Dimensions |
| swCommands_Ann_Show | 1549; in the FeatureManager design tree, Annotations folder RMB menu > Display Annotations |
| swCommands_Annotation_View_Create | 2210; in the FeatureManager design tree, Annotations folder RMB menu > Insert Annotation View |
| swCommands_Annotation_View_Hide | 2233; in the FeatureManager design tree, Annotations > annotation_view RMB menu > Hide |
| swCommands_Annotation_View_Show | 2232; in the FeatureManager design tree, Annotations > annotation_view RMB menu > Show |
| swCommands_AnnotationAlignLeft | 307; valid for multi-selected annotations; Align toolbar > Align Left |
| swCommands_AnnotationAlignRight | 308; valid for multi-selected annotations; Align toolbar > Align Right |
| swCommands_Annotations | 475; alternative to swCommands_Toolbar_Annotation; View menu > Toolbars > Annotation |
| swCommands_Api_Help_Contents | 833; ? menu > API Help |
| swCommands_App_Exit | 2825; File menu > Exit |
| swCommands_App_Servicepacks | 1233; ? menu > Check for Updates |
| swCommands_Apply | 696; dialog resource Apply |
| swCommands_AreaHatchFill | 384; valid only for a selected face or closed sketch profile in a drawing; Annotations toolbar > Area Hatch/Fill |
| swCommands_Asm_Cir_Feat_Pattern | 1376; valid for a selected assembly hole or cut and a selected axis about which to create the circular pattern, opens the Circular Pattern PropertyManager page; Insert menu > Assembly Feature > Circular Pattern |
| swCommands_Asm_Feat_Chamfer | 2957; valid for a selected assembly feature, opens the Chamfer PropertyManager page; Insert menu > Assembly Feature > Chamfer |
| swCommands_Asm_Feat_Cut_Extr | 1001; valid for a selected location on an assembly, opens the Extrude PropertyManager page; Insert menu > Assembly Feature > Cut > Extrude |
| swCommands_Asm_Feat_Cut_Revolve | 1002; valid for a selected location on an assembly, opens the Revolve PropertyManager page; Insert menu > Assembly Feature > Cut > Revolve |
| swCommands_Asm_Feat_Cut_Sweep | 2958; valid for assemblies, opens the Cut-Sweep PropertyManager page; Insert menu > Assembly Feature > Cut > Sweep |
| swCommands_Asm_Feat_Fillet | 2956; valid for a selected assembly feature, opens the Fillet PropertyManager page; Insert menu > Assembly Feature > Fillet |
| swCommands_Asm_Feature_Hole | 1003; valid for a selected location on an assembly; Insert menu > Assembly Feature > Hole > Simple |
| swCommands_Asm_Lin_Feat_Pattern | 1375; valid for a selected assembly hole or cut and a selected axis for the pattern direction, opens the Linear Pattern PropertyManager page; Insert menu > Assembly Feature > Linear Pattern |
| swCommands_Asm_Sketch_Feat_Pattern | 1382; valid for a selected assembly hole or cut, opens the Sketch Driven Pattern PropertyManager page; Insert menu > Assembly Feature > Sketch Driven Pattern |
| swCommands_Asm_Table_Feat_Pattern | 1380; valid for a selected assembly hole or cut, opens the Table Driven Pattern dialog; Insert menu > Assembly Feature > Table Driven Pattern |
| swCommands_Assemblies | 476; alternative to swCommands_Toolbar_Assembly; View menu > Toolbars > Assembly |
| swCommands_Assembly_Stats | 1215; valid for assemblies; Assembly toolbar > Performance Evaluation |
| swCommands_AssemblyTransparency | 3; valid only for assemblies that have one or more components in edit mode; in the graphics area, click RMB menu > Assembly Transparency |
| swCommands_Asset_Publish | 3215; opens the Asset Publisher PropertyManager page; Tools menu or toolbar > Asset Publisher |
| swCommands_Assign_Smart_Fastener | 2452; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping, opens the Smart Fastener dialog; in the Smart Fasteners PropertyManager page, Results > Group1 > Series1 RMB menu > Change fastener type |
| swCommands_Attach_Dimensions | 986; valid only for drawings; Tools menu > Dimensions > Attach Dimensions |
| swCommands_Auto_Ann_View_Generate | 2223; in the FeatureManager design tree, Annotations folder RMB menu > Automatically Place into Annotation Views |
| swCommands_Auto_Dimension_Toggle | 3026; valid for an open sketch with an active sketch tool; Sketch toolbar > Add Dimension |
| swCommands_Auto_Jog | 639; valid for a selected ordinate dimension; in the graphics area, ord_dim RMB menu > Display Options > Re-Jog Ordinate |
| swCommands_Auto_Size | 1702; valid for a reference plane that is re-sized; in the graphics area ref_plane RMB menu > Autosize |
| swCommands_AutoArrangeDimension | 2976; valid for multi-selected annotations or dimensions; Align toolbar > Auto Arrange Dimensions |
| swCommands_AutoBalloon | 447; valid for drawings; Annotations toolbar > Auto Balloon |
| swCommands_AutoExplodeLine | 3296; valid for assemblies, opens Smart Explode Lines PropertyManager to insert or edit smart explode lines for a selected explode view; Assembly toolbar > Insert/Edit Smart Explode Lines |
| swCommands_AutoGenerateDrawing | 3536; valid for parts and assemblies, auto-generates a new drawing from the model; File menu > Auto-Generate Drawing |
| swCommands_Autoinfer_Toggle | 1301; valid for drawings; Tools menu > Sketch Settings > Enable Snapping |
| swCommands_Automatic_Cutlist | 2601; valid for a selected body folder or cut list folder; in the FeatureManager design tree, folder RMB menu > Create Cut Lists Automatically |
| swCommands_AutomaticRelations | 52; Dimensions/Relations toolbar > Automatic Relations |
| swCommands_AutomaticUpdateCutlists | 3122; valid for a cut list folder that has enabled Create Cut Lists Automatically; in the FeatureManager design tree, folder RMB menu > Update Automatically |
| swCommands_AutoRepair_Mates | 3510; Auto repairs mates in a model that is in resolved or lightweight mode; right-click on the Mates root folder and click Auto Repair. |
| swCommands_AutoRepair_Pattern | 3520; Auto repairs a missing Direction 1 or Direction 2 selection in a linear pattern; Right-click the pattern feature in the FeatureManager design tree and click Auto Repair in the pattern context menu |
| swCommands_Autosolve_Toggle | 997; valid for drawings; Tools menu > Sketch Settings > Automatic Solve |
| swCommands_Auxiliary | 391; valid for part documents with a single 2D sketch in edit mode; 2D to 3D toolbar > Auxiliary Sketch |
| swCommands_AuxiliaryView | 33; valid for drawings; Drawing toolbar > Auxiliary View |
| swCommands_Axis | 22; valid for parts; Reference Geometry toolbar > Axis or Features toolbar > Reference Geometry > Axis |
| swCommands_Back | 162; View toolbar > View Orientation > Back |
| swCommands_Backward | 1616; palette toolbar > Back |
| swCommands_Balloon | 37; Annotations toolbar > Balloon |
| swCommands_BaseFlangeTab | 320; valid for sheet metal parts; Sheet Metal toolbar > Base Flange/Tab |
| swCommands_BaselineDimension | 81; valid only for drawings; Dimensions/Relations toolbar > Baseline Dimension |
| swCommands_BendTable | 3010; valid only for selected flat-pattern views in drawings; Table toolbar > Bend Table or Insert > Tables > Bend Table |
| swCommands_BillOfMaterials | 88; valid for drawings; Table toolbar > Bill of Materials |
| swCommands_Blank_Atom_Body | 1026; in the FeatureManager design tree, click body_folder RMB context toolbar > Hide |
| swCommands_Blank_Atom_Body2 | 2730; valid for a part with a solid or surface body; in the FeatureManager design tree, body_folder > body RMB context toolbar > Hide |
| swCommands_Blank_Grid_Comp | 3000; valid for a part or assembly with the GridSystem PropertyManager page open and the grid feature component visible; in the graphics area, RMB menu > Hide |
| swCommands_Blank_Origin_Sketch | 2468; valid for a visible profile sketch; in the graphics area, prof_sketch RMB menu > Hide |
| swCommands_Blank_Part_Body | 901; valid for a selected face of an atom feature in an assembly; in the graphics area, sel_face RMB menu > Hide Solid Body |
| swCommands_Blank_Pic_Feat | 2485; valid for a selected visible picture feature object; in the graphics area, pic_feat RMB menu > Hide |
| swCommands_Blank_Refgeom | 895; valid for a selected reference geometry; in the FeatureManager design tree, ref_geom RMB menu > Hide |
| swCommands_Blank_Sketch | 954; valid for a selected drawing sketch; in the graphics area, sketch RMB menu > Hide |
| swCommands_Blocks | 557; alternative to swCommands_Toolbar_Sketch_Group; View menu > Toolbars > Blocks |
| swCommands_Body_Color | 648; in the FeatureManager design tree, body_folder RMB menu > Appearance > Sketch/Curve Color |
| swCommands_Body_Properties | 2519; in the FeatureManager design tree, body_name RMB menu > Body Properties |
| swCommands_Body_RV_Appearance | 2896; in the FeatureManager design tree, body_folder RMB menu > Appearance |
| swCommands_Body_Texture | 650; valid for a selected component in an assembly, opens the Texture PropertyManager page |
| swCommands_BodyComparison | 3411; valid for selected bodies, displays color comparison; View toolbar > Body Compare |
| swCommands_Bold | 147; valid for selected text; Formatting toolbar > Bold |
| swCommands_Bold_Menu_Title | 2359; adds the bold font style to a selected item in RMB menus |
| swCommands_Bom_Open_Comp_File | 2557; valid for a selected row in a drawing BOM table; BOM_table_row RMB menu > Open comp_file |
| swCommands_Bom_Open_Draw_File | 3502; valid for a selected row in a drawing BOM table; BOM_table_row RMB menu > Open Drawing |
| swCommands_Bom_Viewtable | 1302; valid for a drawing view Excel-based BOM; E xcel_based_bom RMB menu > Edit |
| swCommands_Bottom | 166; View toolbar > View Orientation > Bottom |
| swCommands_Bottom_Left | 933; valid for a selected Excel-based BOM in a drawing view; Excel_BOM RMB menu > Anchor > Bottom Left |
| swCommands_Bottom_Right | 930; valid for a selected Excel-based BOM in a drawing view; Excel_BOM RMB menu > Anchor > Bottom Right |
| swCommands_Break_Alignment | 1510; valid only for aligned drawing view items; view_item RMB menu > Alignment > Break Alignment |
| swCommands_Break_Dim_Align | 1562; valid for a selected drawing dimension to which Align Collinear/Radial has been applied; in the graphics area, aligned_dim RMB menu > Break Alignment |
| swCommands_Break_View | 1519; valid for a drawing view that was previously made a Break View; in the FeatureManager design tree, break_view RMB menu > Break View |
| swCommands_BreakCornerCornerTrim | 364; valid for sheet metal parts; Sheet Metal toolbar > Corners > Break-Corner/Corner-Trim |
| swCommands_BrokenOutSection | 328; valid for drawings; Drawing toolbar > Broken-out Section |
| swCommands_Browse | 795; dialog resource Browse |
| swCommands_Build_Doctor | 1743; valid when a selected feature, component, or mate group has errors; Tools menu > Evaluate > MateXpert |
| swCommands_Bullet | 533; valid for selected text; Formatting toolbar > Bullet |
| swCommands_CameraView | 127; valid for models with cameras; View toolbar > Camera View |
| swCommands_Cancel | 767; dialog resource button "Cancel" |
| swCommands_Cancel_Command | 3043; Standard toolbar > Cancel |
| swCommands_Cancel_Edit_Cntr | 849; virtual key Esc |
| swCommands_Cancel_Edit_Srvr | 850; virtual key Esc |
| swCommands_Capture_3dView | 3141; SOLIDWORKS MBD toolbar > Capture 3D View |
| swCommands_Capture_RenderSystem_ProfilingData | 3359; only valid on the DebugDotMenu in SOLIDWORKS debug builds; DotMenu > Display > Capture RenderSystem Profiling data |
| swCommands_Caterpillar | 516; valid for drawings; Annotations toolbar > Caterpillar |
| swCommands_Cavity | 93; for assemblies with a mold base and design parts; Mold Tools toolbar > Cavity |
| swCommands_Cd_Delete | 689; dialog resource Delete |
| swCommands_Cd_Deleteall | 691; dialog resource Delete All |
| swCommands_Cd_Edit | 716; Relations dialog Edit |
| swCommands_Cd_Undo | 706; dialog resource Undo |
| swCommands_Center | 390; valid for selected text; Formatting toolbar > Center |
| swCommands_Centerline | 49; valid for parts with a selected sketch; Sketch toolbar > Centerline |
| swCommands_CenterMark | 95; valid only for drawings; Annotation toolbar > Center Mark |
| swCommands_CenterpointArc | 44; valid for parts and drawings; Layout Tools toolbar > Arcs > Centerpoint Arc or Sketch toolbar > Arcs > Centerpoint Arc |
| swCommands_CenterPointSnap | 530; valid for sketches; Quick Snaps toolbar > Center Point Snap |
| swCommands_CentreRectangle | 2794; valid for parts with a selected sketch; Layout Tools toolbar > Rectangles > Center Rectangle or Sketch toolbar > Rectangles > Center Rectangle |
| swCommands_CentreRectangleAtAngle | 2795; valid for parts with a selected sketch; Layout Tools toolbar > Rectangles >3 Point Center Rectangle or Sketch toolbar > Rectangles > 3 Point Center Rectangle |
| swCommands_Chamfer | 11; valid for parts; Features toolbar > Chamfer |
| swCommands_ChamferDimension | 366; valid only for drawings; Dimensions/Relations toolbar > Chamfer Dimension |
| swCommands_Change_DrView_Reference | 3094; valid only for drawings; Drawing toolbar > Replace Model |
| swCommands_Change_Route_Dia | 2288; valid for the SOLIDWORKS Routing add-in and an open piping or flexible tubing assembly; Routing Tools toolbar > Change Route Diameter |
| swCommands_Change_Write_Access | 2120; valid for models in a multi-user environment (select Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment ; File menu > Get Write Access |
| swCommands_Change_Write_Access_Comp | 2119; valid for shared assemblies in a multi-user environment (select Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment ; in the FeatureManager design tree, comp RMB menu > Make Read-Only or Get Write Access |
| swCommands_ChangeDisplayState | 2926; valid for parts and assemblies; View > Change Display States |
| swCommands_ChangeLayer | 3056; valid for drawings; Line Format toolbar > Change Layer |
| swCommands_ChangeSuppressionState | 150; valid for assemblies with a selected component; Assembly toolbar > Change Suppression State |
| swCommands_ChangeTransparency | 120; valid for assemblies with a selected component; Assembly toolbar > Change Transparency |
| swCommands_Check | 133; Tools toolbar > Check |
| swCommands_Check_Sketch_For_Feature | 1138; valid for a part and an open sketch, opens the Check Sketch For Feature Usage dialog; Tools menu > Sketch Tools > Check Sketch for Feature |
| swCommands_CheckReadOnlyFiles | 541; valid only if Tools menu > Options > System Options > Collaboration > Enable Multi-user environment and Check if files opened read-only have been modified by other users are both checked; Standard > Check Read-only Files |
| swCommands_Circle | 46; for drawings, Layout Tools toolbar > Circle ; for parts with a selected sketch or assemblies with a selected planar face, Sketch toolbar > Circle |
| swCommands_CircuitWorks | 2893; SOLIDWORKS Add-ins toolbar > CircuitWorks |
| swCommands_CircularPattern | 73; valid for parts; Features toolbar > Circular Pattern |
| swCommands_CircularSketchPattern | 173; valid for parts with a sketch in edit mode; Sketch toolbar > Circular Sketch Pattern |
| swCommands_Clear_List_Box | 1734; valid in list boxes in dialogs and PropertyManager pages; list_box RMB menu > Clear Selections |
| swCommands_ClearAllFilters | 274; Selection Filter toolbar > Clear All Filters |
| swCommands_ClearanceVerification | 2848; valid for assemblies; Assembly toolbar > Clearance Verification |
| swCommands_ClickHereToSeeThePreview | 5; alternative to swCommands_Toolbar_Inference; View menu > Toolbars > Quick Snaps |
| swCommands_ClosedCorner | 360; valid for sheet metal parts; Sheet Metal toolbar > Corners > Closed Corner |
| swCommands_Cmark_Merge | 1893; valid for a drawing with two multi-selected center marks that are mergeable in the center mark set; in the graphics area, center_mark RMB menu > Merge Center Mark |
| swCommands_Cmark_Select | 1898; valid for a drawing with a selected center mark in a center mark set; in the graphics area, center_mark RMB menu > Select Center Mark Set |
| swCommands_Cmark_Setbase | 1873; valid for a drawing with a selected center mark in a center mark set; in the graphics area, center_mark RMB menu > Set as Base Center |
| swCommands_Collapse_Tree | 1977; accelerator key ctrl-C |
| swCommands_Collapseallitems_Tree | 2555; accelerator key shift-C |
| swCommands_Color | 531; valid for selected text; Formatting toolbar > Color |
| swCommands_ColorDisplayMode | 299; Line Format toolbar > Color Display Mode |
| swCommands_Combine | 407; valid for parts with two or more solid bodies; Features > Combine |
| swCommands_Command_Option_Toggle | 1635; valid during insertion of a line in an open sketch; in the graphics area, sketch_line RMB menu > Switch to arc (A) |
| swCommands_Comp_Config_Prop | 941; valid for assemblies; in the FeatureManager design tree, selected_component RMB menu toolbar > Component Properties |
| swCommands_Comp_Display_Hiddengreyed | 2563; valid for assemblies; in the FeatureManager design tree, selected_component RMB menu > Component Display > Hidden Lines Visible |
| swCommands_Comp_Display_Hiddengreyed_All | 2706; valid for a selected top-level-assembly; Edit menu > Component Display > Hidden Lines Visible > All Display States |
| swCommands_Comp_Display_Hiddengreyed_Specify | 2712; valid for a selected top-level-assembly, opens the Apply to Display States dialog; Edit menu > Component Display > Hidden Lines Visible > Specified Display States |
| swCommands_Comp_Display_Hiddenremoved | 2564; valid for assemblies; in the FeatureManager design tree, selected_component RMB menu > Component Display > Hidden Lines Removed |
| swCommands_Comp_Display_Hiddenremoved_All | 2707; valid for a selected top-level-assembly; Edit menu > Component Display > Hidden Lines Removed > All Display States |
| swCommands_Comp_Display_Hiddenremoved_Specify | 2713; valid for a selected top-level-assembly; Edit menu > Component Display > Hidden Lines Removed > Specified Display States |
| swCommands_Comp_Display_Shaded | 2566; valid for assemblies; in FeatureManager design tree, selected_component RMB menu > Component Display > Shaded |
| swCommands_Comp_Display_Shaded_All | 2709; valid for a selected top-level-assembly; Edit menu > Component Display > Shaded > All Display States |
| swCommands_Comp_Display_Shaded_Specify | 2715; valid for a selected top-level-assembly; Edit menu > Component Display > Shaded > Specified Display States |
| swCommands_Comp_Display_Shaded_With_Edges | 2565; valid for assemblies; in FeatureManager design tree, selected_component RMB menu > Component Display > Shaded With Edges |
| swCommands_Comp_Display_Shaded_With_Edges_All | 2708; valid for a selected top-level-assembly; Edit menu > Component Display > Shaded With Edges > All Display States |
| swCommands_Comp_Display_Shaded_With_Edges_Specify | 2714; valid for a selected top-level-assembly; Edit menu > Component Display > Shaded With Edges > Specified Display States |
| swCommands_Comp_Display_View_Default | 2567; valid for assemblies; in FeatureManager design tree, selected_component RMB menu > Component Display > Default Display |
| swCommands_Comp_Display_View_Default_All | 2710; valid for a selected top-level-assembly; Edit menu > Component Display > Default Display > All Display States |
| swCommands_Comp_Display_View_Default_Specify | 2716; valid for a selected top-level-assembly; Edit menu > Component Display > Default Display > Specified Display States |
| swCommands_Comp_Display_Wireframe | 2562; valid for assemblies; in FeatureManager design tree, selected_component RMB menu > Component Display > Wireframe |
| swCommands_Comp_Display_Wireframe_All | 2705; valid for a selected top-level-assembly; Edit menu > Component Display > Wireframe > All Display States |
| swCommands_Comp_Display_Wireframe_Specify | 2711; valid for a selected top-level-assembly; Edit menu > Component Display > Wireframe > Specified Display States |
| swCommands_Comp_Isolate | 2726; valid for assemblies; in the FeatureManager design tree, selected_component RMB menu > Isolate |
| swCommands_Comp_Isolate_Exit | 2732; Isolate dialog Exit |
| swCommands_Comp_Parent_Child_Rel | 2627; valid for assemblies and drawings; in the FeatureManager design tree, selected_component RMB menu > Parent/Child |
| swCommands_Component_Color | 653; alternative to swCommands_EditColor, valid for a selected component in an assembly, opens the Sketch/Curve Color PropertyManager page; Edit menu > Appearance > Sketch/Curve Color |
| swCommands_Component_Display | 2561; in the FeatureManager design tree, component_name RMB menu > Component Display submenu |
| swCommands_Component_Pattern | 1016; Insert menu > Component Pattern submenu |
| swCommands_Component_Pattern_Chain | 3126; valid for assemblies; Assembly toolbar > Chain Component Pattern |
| swCommands_Component_Pattern_Circular | 1942; valid for assemblies; Assembly toolbar > Circular Component Pattern |
| swCommands_Component_Pattern_Curve | 3109; valid for assemblies; Assembly toolbar > Curve Driven Component Pattern |
| swCommands_Component_Pattern_Feature | 1943; valid for assemblies; Assembly toolbar > Pattern Driven Component Pattern |
| swCommands_Component_Pattern_Linear | 1941; valid for assemblies; Assembly toolbar > Linear Component Pattern |
| swCommands_Component_Pattern_Sketch | 3108; valid for assemblies; Assembly toolbar > Sketch Driven Component Pattern |
| swCommands_Component_Properties | 864; valid for drawings, opens the Component Line Font dialog; in the FeatureManager design tree or drawing view, selected_component RMB menu > Component Line Font |
| swCommands_Component_Reload | 1527; valid for assemblies; in the FeatureManager design tree, selected_component RMB menu > Reload |
| swCommands_Component_RV_Appearance | 2898; in the FeatureManager design tree, component_name RMB context toolbar > Appearances > component_name |
| swCommands_Component_Texture | 654; valid for a selected component in an assembly, opens the Texture PropertyManager page |
| swCommands_CompositeCurve | 158; valid for parts; Features toolbar > Curves > Composite Curve or Curves toolbar > Composite Curve |
| swCommands_Conc_Dim_Show_Extn_Lines | 1995; valid for drawings; concentric_dimension_extension_line RMB menu > Show extension lines |
| swCommands_ConfigurationsToolbar | 3117; View menu > Toolbars > Configurations |
| swCommands_Conic | 3049; valid for parts with a selected sketch; Sketch toolbar > Conic |
| swCommands_ConstructionGeometry | 102; valid for parts with an open sketch and selected sketch entity; Sketch toolbar > Construction Geometry |
| swCommands_Convert_To_Bom98 | 1585; valid for a selected OLE item in a drawing view; in the graphics area, dr_view_OLE_item RMB menu > Convert to SOLIDWORKS 98 and later Format |
| swCommands_ConvertEntities | 57; valid for parts with an open sketch; Sketch toolbar > Convert Entities |
| swCommands_ConvertMeshBody2Classic | 3531; converts recognized mesh brep faces to standard BREP faces; Insert > Features > Convert Mesh to Standard... |
| swCommands_ConvertMeshSolidSurface | 3245; converts a selected solid or surface body to a Parasolid mesh body; Feature toolbar > ConvertMesh Bodies... |
| swCommands_ConvertTo_Base_Dimension | 3408; valid for a selected dimension in a chain dimension set, replaces all dimensions in the set with baseline dimensions; RMB menu > Convert To Base |
| swCommands_ConvertTo_Chain_Dimension | 3407; valid for a selected dimension in a baseline dimension set, replaces all dimensions in the set with chain dimensions; RMB menu > Convert To Chain |
| swCommands_ConvertToGeneric | 3364; converts the selected interpolating spline into a generic spline; Tools > Spline Tools > Convert to Generic Spline... |
| swCommands_ConvertToModif | 3124; valid for open sketches of a selected style spline; Spline Tools toolbar > Convert to Spline |
| swCommands_ConvertToStyle | 3123; valid for open sketches of a selected interpolating spline; Spline Tools toolbar > Convert to Style Spline |
| swCommands_CoordinateSystem | 154; valid for parts with a selected sketch; Features toolbar > Reference Geometry > Coordinate System |
| swCommands_Copy | 583; valid for a selection; Standard > Copy |
| swCommands_Copy_Appearance | 3053; valid for a model with an appearance; Render Tools or View toolbar > Copy Appearance |
| swCommands_Copy_Bookmark_Link | 3526; valid only in SOLIDWORKS Connected, copies the link of the bookmarked file location in bookmarks to the clipboard; Lifecycle and Collaboration toolbar > Bookmarks > Copy Bookmark Link |
| swCommands_Copy_Drw_To_Dwgeditor | 2202; valid for drawings; Edit menu > Copy to DWG format |
| swCommands_Copy_Swift_Schema | 2017; valid for parts with multiple configurations and a selected configuration to which to copy an existing tolerance scheme; DimXpert toolbar > Copy Scheme |
| swCommands_CopyEntities | 559; vald for parts with a sketch in edit mode; Sketch toolbar > Copy Entities |
| swCommands_Core | 514; valid for parts with a selected plane or planar face; Mold Tools toolbar > Core |
| swCommands_Corner_Relief | 3112; valid for sheet metal parts and multiple selected faces that define corners; Sheet Metal toolbar > Corner Relief |
| swCommands_CosmeticThread | 115; valid for parts with a selected circular edge; Annotation > Cosmetic Thread |
| swCommands_CosmeticWeld | 2991; valid for parts or assemblies with a selected assembly feature, opens the Weld Bead PropertyManager page; Weldments toolbar or Insert menu > Assembly Features > Weld Bead |
| swCommands_COSMOSFloXpress | 2834; Tools toolbar > FloXpress Analysis Wizard |
| swCommands_CosmosMotion | 621; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Motion |
| swCommands_CosmosworksDesigner | 565; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation |
| swCommands_CosmosxpressAnalysisWizard | 439; Tools toolbar > SimulationXpress Analysis Wizard |
| swCommands_Create_Cut_List_Folder | 2512; valid for weldment parts; in the FeatureManager design tree, solid_body RMB menu > Create Cut List Item |
| swCommands_Create_Empty_Folder | 1906; in the FeatureManager design tree, item_name RMB menu > Create New Folder |
| swCommands_Create_New_Configuration | 2022; in the FeatureManager design tree, component_name RMB menu > Add Configuration |
| swCommands_Create_Sub_Bodyfolder | 2570; in the FeatureManager design tree, solid_body_name RMB menu > Add to New Folder |
| swCommands_Create_Sub_LiveSectionFolder | 2884; valid for parts with a Live Section Plane; in the FeatureManager Design Tree, Live Section Planes folder RMB menu > Add to New Folder |
| swCommands_Create_Sub_Weldment | 2367; valid for weldment parts; in the FeatureManager design tree, Cutlist folder > item_name RMB menu > Create Sub-Weldment |
| swCommands_Create_Userdefined_Rt_By_Drag_Drop | 3163; valid for the SOLIDWORKS Routing add-in and a routing assembly; User Defined Route toolbar > Start by Drag/Drop |
| swCommands_Create_Userdefined_Rt_On_Fly | 3166; valid for the SOLIDWORKS Routing add-in and a routing assembly, opens the Connection Point PropertyManager page; User Defined Route toolbar > Start at Point |
| swCommands_CreateSketchFromSelections | 381; valid for parts, creates a new sketch from selected sketch entities; 2D To 3D toolbar > Create Sketch from Selections |
| swCommands_CropView | 311; valid for drawings with a closed sketch profile on a selected view; Drawing toolbar > Crop View |
| swCommands_Cull_Dynamic_Update | 1799; valid for assemblies; View menu > Display > Optimize Zoom/Pan/Rotate |
| swCommands_Curvature | 132; View toolbar > Curvature |
| swCommands_CurvatureHedgehog | 3130; View toolbar > Surface Curvature Combs |
| swCommands_CurveDrivenPattern | 362; valid for parts with a selected sketch; Features toolbar > Curve Driven Pattern |
| swCommands_Curves | 477; alternative to swCommands_Toolbar_Curve; View menu > Toolbars > Curves |
| swCommands_CurveThroughReferencePoints | 123; valid for parts with a selected sketch; Features toolbar > Curves > Curve Through Reference Points |
| swCommands_CurveThroughXYZPoints | 128; valid for parts with a selected sketch; Features toolbar > Curves > Curve Through XYZ Points |
| swCommands_Custom_Msg_Display_Camera_By_Name | 2239; alternative to swCommands_Anim_Custom_Msg_Display_Camera_By_Name; valid only in context of Motion Study gantt chart pop-up menus; In Motion Study gantt chart, orientation_and_camera_views_time_bar_key RMB menu > View Orientation > camera_view_name |
| swCommands_Custom_Msg_Display_Vw_By_Name | 2238; menu item valid only in context of view orientations |
| swCommands_Customization_And_More | 1938; File menu > Customize Menu and many RMB menu > Customize menu |
| swCommands_Cut | 584; Standard toolbar > Cut |
| swCommands_CutListSortingOptions | 3431; valid for a model with cut list items, opens the Cut List Sorting Options PropertyManager for the selected cut list folder; FeatureManager design tree cut list folder RMB menu > Cut List Sorting Options |
| swCommands_CutWithSurface | 101; Features toolbar > Cut With Surface |
| swCommands_CVSpline | 3099; Sketch toolbar > Style Spline |
| swCommands_DatumFeature | 114; Annotation toolbar > Datum Feature |
| swCommands_DatumTarget | 122; Annotation toolbar > Datum Feature |
| swCommands_DecimateMesh | 3429; simplifies facet counts for graphics and mesh BRP bodies; Features toolbar > Decimate Mesh Body |
| swCommands_DecreaseIndent | 543; valid for selected text; Formatting toolbar > Decrease indent |
| swCommands_Defeature | 3050; valid for parts or assembles with a selected Defeature item; RMB menu > Update Defeature |
| swCommands_Defer | 708; dialog resource Show preview |
| swCommands_DefineStructConnection | 3415; Structure System toolbar > Define Connection Element |
| swCommands_Deform | 454; valid for parts; Features toolbar > Deform |
| swCommands_Deform_Rmb_Add_Connector | 754; valid when the Deform or Loft PropertyManager page is open, the Deform Type is Curve to curve, and an entity is selected; in the graphics area, entity RMB menu > Add Connector |
| swCommands_Deform_Rmb_Delete_All_Connector | 2610; valid when the Loft PropertyManager page is open; in the graphics area, RMB menu > Delete all connectors |
| swCommands_Deform_Rmb_Delete_Connector | 2609; valid when the Deform or Loft PropertyManager page is open, and a connector is selected; in the graphics area, connector RMB menu > Delete Connector |
| swCommands_Deform_Rmb_Disp_Connectionlines | 756; valid when the Deform PropertyManager page is open, and Deform Type is Curve to curve; in the graphics area, RMB menu > Show Connection Lines |
| swCommands_Deform_Rmb_Set_Transparent | 751; valid when the Deform PropertyManager page is open; in the graphics area, RMB menu > Transparent Preview |
| swCommands_Deform_Rmb_Set_Zebra | 752; valid when the Deform PropertyManager page is open; in the graphics area, RMB menu > Zebra Stripes Preview |
| swCommands_Deform_Rmb_Show_Connector | 2608; valid when the Deform or Loft PropertyManager page is open, and a connector has been hidden; in the graphics area, connector RMB menu > Show Connector |
| swCommands_Deform_Rmb_Update_Display | 755; valid when the Deform PropertyManager page is open; in the graphics area, RMB menu > Show Preview |
| swCommands_Del_Equation | 1580; valid in the Equations, Global Vairables, and Dimensions dialog; row RMB menu > Delete Equation |
| swCommands_Delete | 16; deletes a selected item; Standard toolbar > Delete |
| swCommands_Delete_All_Constraints | 1763; valid only in specific dialogs involving sketch constraints, such as the Display/Delete Relations PropertyManager page; relations_list_box RMB menu > Delete All |
| swCommands_Delete_Annotation_View | 2215; valid for drawing annotation views; annotation_view RMB menu > Delete |
| swCommands_Delete_Comment | 2070; in the FeatureManager design tree, comment_name RMB menu > Delete Comment |
| swCommands_Delete_Constraints | 709; Move Confirmation or Copy Confirmation dialog resource Delete |
| swCommands_Delete_Cut_List | 2640; in the FeatureManager design tree, cut_list_folder RMB menu > Delete |
| swCommands_Delete_List_Box_Item | 1735; valid in dialog list boxes; RMB > Delete |
| swCommands_Delete_Pgm_Sketch_Offset | 2434; valid for an open sketch with one or more offset entities; sketch_offset_line RMB menu > Delete Offset |
| swCommands_Delete_Relation | 679; Equations dialog resource Delete |
| swCommands_Delete_Selected_Constraint | 1809; valid in specific dialogs involving sketch constraints, such as Display/Delete Relations PropertyManager page; relations_list_box RMB menu > Delete |
| swCommands_Delete_Smart_Fastener | 2457; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping; in the Smart Fasteners PropertyManager page, Results > Group1 > Series1 RMB menu > Delete |
| swCommands_Delete_Weldment | 2361; valid only for weldments; in the FeatureManager design tree, weldment_name RMB menu > Delete |
| swCommands_DeleteFace | 393; Surfaces toolbar > Delete Face |
| swCommands_DeleteHoleSurface | 3360; deletes inner cavity on surfaces; Surfaces toolbar > Delete Hole |
| swCommands_DeleteSolidSurface | 424; Feaures toolbar > Delete/Keep Body |
| swCommands_Derive_Sketch | 1009; valid for a multi-selected sketch and a face or a plane; Insert menu > Derived Sketch |
| swCommands_Design_Study | 2953; Tools toolbar > Design Study |
| swCommands_DesignChecker | 460; SOLIDWORKS Add-ins toolbar > Design Checker |
| swCommands_DesignStudy_Add_Parameters | 2955; valid for parts, opens the Parameters dialog; Insert menu > Design Study > Parameters |
| swCommands_DesignTable | 413; Tools toolbar > Design Table |
| swCommands_DetailView | 35; valid for drawings; Drawing toolbar > Detail View |
| swCommands_DeviationAnalysis | 411; valid for parts; Tools toolbar > Deviation Analysis |
| swCommands_DFMXpress | 2833; valid for parts; Tools toolbar > DFMXpress Analysis Wizard |
| swCommands_Dim_Center_Text | 1574; centers a selected dimension between extension lines; in the graphics area, dimension RMB menu > Display Options > Center Dimension |
| swCommands_Dim_Foreshort | 2645; valid for a selected dimension; in the graphics area, dimension RMB menu > Display Options > Foreshorten |
| swCommands_Dim_Inspection | 1342; valid for a selected dimension; in the graphics area, dimension RMB menu > Display Options > Show as Inspection |
| swCommands_Dim_Jog | 2839; valid for a selected dimension; in the graphics area, dimension_extension_line RMB menu > Display Options > Jog |
| swCommands_Dim_RadialDiametric_Toggle | 3470; Toggles display dimension from single distance to doubled distance and vice versa |
| swCommands_Dim_Restore_Original_Value | 3522; valid for a selected overridden dimension; in the graphics area, overridden_dimension RMB menu > Dimension > Restore Original Value |
| swCommands_Dim_Showpara | 1572; valid for a selected dimension; in the graphics area, dimension RMB menu > Display Options > Show Parentheses |
| swCommands_Dim_Snap_Horizontal | 787; valid for a selected vertical dimension; in the graphics area, vertical_dimension RMB menu > Set Horizontal |
| swCommands_Dim_Snap_To_Edge | 789; valid for a selected horizontal dimension; in the graphics area, horizontal_dimension RMB menu > Align to edge |
| swCommands_Dim_Snap_Vertical | 788; valid for a selected horizontal dimension; in the graphics area, horizontal_dimension RMB menu > Set Vertical |
| swCommands_Dim_Stop_Break | 2785; valid for a selected dimension; in the graphics area, dimension_with_break_lines RMB menu > Remove Dimension Breaks |
| swCommands_Dimension_Driven_Toggle | 3025; valid for an open sketch with an active sketch tool; Sketch toolbar > Sketch Dimension Driven |
| swCommands_DimensionAlignCollinear | 2974; valid for multi-selected dimensions; Align toolbar > Align Collinear |
| swCommands_DimensionPattern | 3101; valid for parts with a selected sketch; Features toolbar > Dimension Pattern |
| swCommands_DimensionRelations | 490; alternative to swCommands_Toolbar_Sketch_Rels; View menu > Toolbars > Dimensions/Relations |
| swCommands_DimensionSpaceEvenly | 2973; valid for multi-selected dimensions; Align toolbar > Dimension Space Evenly/Radial |
| swCommands_DimensionStagger | 2975; valid for multi-selected dimensions; Align toolbar > Align Stagger |
| swCommands_DimensionTextAlignBottom | 2978; valid for multi-selected dimensions; Align toolbar > Bottom Justify Dimension Text |
| swCommands_DimensionTextAlignLeft | 2979; valid for multi-selected dimensions; Align toolbar > Left Justify Dimension Text |
| swCommands_DimensionTextAlignRight | 2980; valid for multi-selected dimensions; Align toolbar > Right Justify Dimension Text |
| swCommands_DimensionTextAlignTop | 2977; valid for multi-selected dimensions; Align toolbar > Top Justify Dimension Text |
| swCommands_Dimetric | 468; View toolbar > View Orientation > Dimetric |
| swCommands_Disp_Dim_As_Diameter | 3486; Left or right click circular entity, display dimension context toolbar > diameter button |
| swCommands_Disp_Dim_As_Linear | 3487; Left or right click circular entity, display dimension context toolbar > linear diameter button |
| swCommands_Disp_Dim_As_Radius | 3485; Left or right click circular entity, display dimension context toolbar > radius button |
| swCommands_Display_States_Target | 3195; opens the Display State Target dialog; Render Tools toolbar > Display States Target |
| swCommands_DisplayControlPolygon | 572; valid for a selected sketch spline; Spline Tools toolbar > Display Control Polygon |
| swCommands_DisplayDeleteRelations | 60; valid for drawings; Layout toolbar > Display/Delete Relations |
| swCommands_Dissolve_Lib_Feature | 1576; valid for parts with a library feature; in the FeatureManager design tree, library_feature RMB menu > Dissolve Library Feature |
| swCommands_Dissolve_Sktext | 2470; valid for an open sketch with sketch text; in the graphics area, sketch_text RMB menu > Dissolve Sketch Text |
| swCommands_Dissolve_Subassembly | 1260; valid for assemblies with subassemblies; in the FeatureManager design tree, subassembly_name RMB menu > Dissolve Subassembly |
| swCommands_DissolveEntities | 3306; dissolves selected autoexplode lines so they can be edited as regular entities; Sketch toolbar > Dissolve Entities |
| swCommands_DocumentFont | 387; valid for annotations with text; Formatting toolbar > Document Font |
| swCommands_Dome | 137; valid for parts with a selected face; Features toolbar > Dome |
| swCommands_DowelPinSymbol | 369; valid for drawings with circular edges or arcs; Annotation toolbar > Dowel Pin Symbol |
| swCommands_DraftQualityHlrHlv | 298; View toolbar > Draft Quality HLR/HLV |
| swCommands_Draw_Bl_Isozag | 1582; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, break_line RMB menu > Small Zig Zag Cut |
| swCommands_Draw_Bl_Spline | 1522; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, break_line RMB menu > Curve Cut |
| swCommands_Draw_Bl_Straight | 1521; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, break_line RMB menu > Straight Cut |
| swCommands_Draw_Bl_Zigzag | 1523; valid for a drawing when the Broken View PropertyManager page is open; in the graphics area, break_line RMB menu > Zig Zag Cut |
| swCommands_Drawing_Feat_Edit | 2693; valid for drawing views; in the FeatureManager design tree, sheet > drawing_view RMB menu > Edit Feature |
| swCommands_Drawing_Feat_Edit_Def | 2497; in the FeatureManager design tree, macro_feature RMB menu > Edit Definition |
| swCommands_Drawing_Stats | 2172; valid for drawings; Tools menu > Evaluate > Performance Evaluation |
| swCommands_Drawings | 478; alternative to swCommands_Toolbar_Drawing; View menu > Toolbars > Drawing |
| swCommands_Driven_Dim | 1908; valid for a selected drawing dimension; in the graphics area, dim RMB menu > Driven |
| swCommands_DriveWorkXxpress | 2832; Tools toolbar > DriveWorksXpress Wizard |
| swCommands_Drview_Load_Model | 649; valid for detached drawings; drawing_view RMB menu > Load Model |
| swCommands_Drw_Rebuild_All | 1796; valid for drawings with a modified part when Automatic view update is not set in the FeatureManager design tree, top-level_drawing RMB menu > Update All Views |
| swCommands_Dt_Save_Table | 2508; valid for models with design tables; in the ConfigurationManager, Tables folder > Design Table RMB menu > Save Table |
| swCommands_Dv_Suppress | 1503; valid for a selected drawing view that is unsuppressed; in the graphics area, dr_view RMB menu > Hide |
| swCommands_Dv_Unsuppress | 1504; valid for a selected drawing view that is suppressed; in the graphics area, dr_view RMB menu > Show |
| swCommands_Dve_Blind | 1447; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Blind |
| swCommands_Dve_Mid_Plane | 1446; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Mid Plane |
| swCommands_Dve_Offsetfromsurface | 1450; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Offset From Surface |
| swCommands_Dve_Rmb_Back | 2164; valid for some open PropertyManager pages; in the graphics area, RMB menu > Back |
| swCommands_Dve_Rmb_Cancel | 1465; valid when a PropertyManager page is open; in the graphics area, RMB menu > Cancel |
| swCommands_Dve_Rmb_Close_Spline_Curve | 1653; valid when the Curve Through Reference Point PropertyManager page is open; in the graphics area, RMB menu > Closed Curve |
| swCommands_Dve_Rmb_Exit_Preview | 2439; valid when the Detailed Preview PropertyManager page is open; in the graphics area, RMB menu > Exit Preview |
| swCommands_Dve_Rmb_Lpat_Flip_Direction1 | 1657; valid when the LPattern1 PropertyManager page is open; in the graphics area, RMB menu > Reverse Direction 1 |
| swCommands_Dve_Rmb_Lpat_Flip_Direction2 | 1658; valid when the LPattern1 PropertyManager page is open; in the graphics area, RMB menu > Reverse Direction 2 |
| swCommands_Dve_Rmb_Lpat_Geometry_Pattern | 1656; valid when the LPattern1 PropertyManager page is open; in the graphics area, RMB menu > Geometry Pattern |
| swCommands_Dve_Rmb_Lpat_Varysketch | 1655; valid when the LPattern1 PropertyManager page is open for a model with a driving dimension selected for Pattern Direction 1; in the graphics area, RMB menu > Vary sketch |
| swCommands_Dve_Rmb_Mc_Select_Entities | 743; valid when the Move or Copy PropertyManager page is open; in the graphics area, RMB menu > Select Entities |
| swCommands_Dve_Rmb_Next | 2165; valid for some open PropertyManager pages; in the graphics area, RMB menu > Next |
| swCommands_Dve_Rmb_Ok | 1463; valid when a PropertyManager page is open; in the graphics area, RMB menu > OK |
| swCommands_Dve_Rmb_Pushpin | 740; valid when the Planar Surface PropertyManager page is open; in the graphics area, RMB menu > Pin Dialog |
| swCommands_Dve_Rmb_Redo | 1947; valid when a PropertyManager page is open, and Redo is enabled; in the graphics area, RMB menu > Redo |
| swCommands_Dve_Rmb_Select_Feature | 2459; valid when a PropertyManager page is open, and feature selection is enabled; in the graphics area, RMB menu > Select Feature |
| swCommands_Dve_Rmb_Undo | 1945; valid when a PropertyManager page is open, and Undo is enabled; in the graphics area, RMB menu > Undo |
| swCommands_Dve_Throughall | 1451; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Through All |
| swCommands_Dve_ThroughAll_Both | 3092; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Through All - Both Directions |
| swCommands_Dve_Throughnext | 1452; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Up To Next |
| swCommands_Dve_Uptobody | 2509; valid when the Surface-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Up To Body |
| swCommands_Dve_Uptosurface | 1449; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Up To Surface |
| swCommands_Dve_Uptovertex | 1448; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, RMB menu > Direction 1 > Up To Vertex |
| swCommands_Dymparam_Dlg_Cancel | 1037; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dymparam_Dlg_Designintent | 1041; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dymparam_Dlg_Increment | 1040; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dymparam_Dlg_Ok | 1036; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dymparam_Dlg_Regen | 1039; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dymparam_Dlg_Reverse | 1038; valid on a change parameter dialog pop-up toolbar |
| swCommands_Dynamic_Annotation_Views | 3145; View (Heads-Up) toolbar > Dynamic Annotation Views |
| swCommands_DynamicMirrorEntities | 529; valid for parts with an open sketch and selected sketch segment about which to mirror; Sketch toolbar > Dynamic Mirror Entities |
| swCommands_EdgeFlange | 359; valid for sheet metal parts; Sheet Metal toolbar > Edge Flange |
| swCommands_Edit_Ang_Ordinate | 3082; valid for drawings of circles or arcs with angular running dimensions; in the graphics area, angular_running_dimensi on RMB menu > Add to Running Dimension |
| swCommands_Edit_Annotation_View | 2234; in the FeatureManager design tree, Annotations folder > a nnotation_view RMB menu > Edit Annotation View |
| swCommands_Edit_Assembly | 967; valid for assemblies with subassemblies; in the FeatureManager design tree, subassembly_name RMB minibar > Edit Assembly or Assembly toolbar > Edit Component |
| swCommands_Edit_Broken_Out_Section | 1678; valid for a selected Broken-Out Section; in the FeatureManager design tree, broken_out_section RMB menu > Edit Definition |
| swCommands_Edit_Cavity_Part | 1741; valid for a selected body feature used in mold creation; sel_body RMB menu > Edit Cavity Part |
| swCommands_Edit_Comment | 2071; in the FeatureManager design tree, comment_name RMB menu > Edit Comment |
| swCommands_Edit_Csk_Pattern | 1392; valid for circular sketch patterns; in the graphics area, circular_sketch_entity RMB menu > Edit Circular Pattern |
| swCommands_Edit_Cut_List_Folder_Props | 2513; valid for weldments with a cut list folder; in the FeatureManager design tree, cut_list_item RMB menu > Properties |
| swCommands_Edit_Decal | 2207; Render Tools toolbar > Edit Decal |
| swCommands_Edit_Def_Assy | 655; valid for Smart Components open in edit mode; in the FeatureManager design tree, Smart Feature folder > RMB menu > Edit in Defining Assembly |
| swCommands_Edit_Delete_Replay | 1907; valid for a selected animation feature; RMB menu > Delete Replay |
| swCommands_Edit_Dissolve_Assembly | 1324; valid for a selected subassembly; Edit menu > Dissolve Assembly |
| swCommands_Edit_Dragitem | 831; valid for assemblies with MateReferences folders; in the FeatureManager design tree, MateReferences folder > mate_reference RMB menu > Edit Definition |
| swCommands_Edit_Drawview_Sketch | 1530; valid for drawing detail views or broken-out sections; FeatureManager design tree > detail_view folder > detail_circle RMB menu > Edit Sketch |
| swCommands_Edit_Equation | 1578; valid for a selected dimension with equations; sel_dim RMB menu > Edit Equation |
| swCommands_Edit_Exit_No_Save | 1787; Edit menu > Exit Sketch without Saving Changes |
| swCommands_Edit_Familytable | 866; valid for models with design tables; Edit menu > Design Table > Edit Table or in ConfigurationManager, Tables folder > Design Table RMB menu > Edit Table |
| swCommands_Edit_Familytable_Open | 867; valid for models with design tables; Edit menu > Design Table > Edit Table in New Window or in ConfigurationManager, Tables folder > Design Table RMB menu > Edit Table in New Window |
| swCommands_Edit_Findinfm | 1588; opens the Find In FeatureManager Design Tree dialog; in the FeatureManager design tree, fm_item RMB menu > Go To |
| swCommands_Edit_Flex_Tube_Rt | 2260; valid for the SOLIDWORKS Routing add-in and an open flexible tube routing assembly; Flexible Tubing toolbar > Edit Route |
| swCommands_Edit_Folder_Feat | 2390; valid for assemblies with a Mate group; Mates folder RMB menu > Edit Features |
| swCommands_Edit_Importfolder | 1583; valid for a selected import folder; sel_folder RMB menu > Edit import folder |
| swCommands_Edit_Incontext | 868; edits the selected model in the context of the assembly where it was created; in the FeatureManager design tree, model_name RMB menu > Edit in Context |
| swCommands_Edit_Layout | 2818; valid for assemblies; Layout Tools toolbar > Layout |
| swCommands_Edit_Lsk_Pattern | 1391; valid for open sketches with linear sketch patterns; in the graphics area, lin_sketch_pattern_entity RMB menu > Edit Linear Pattern |
| swCommands_Edit_Ordinate | 1507; valid for drawings with an ordinate dimension; in the graphics area, ordinate_dim RMB Menu > Add to Ordinate |
| swCommands_Edit_Paragraph | 2068; valid for selected text; Formatting toolbar > Paragraph Properties |
| swCommands_Edit_Part | 965; valid for assemblies; in the FeatureManager design tree, part_name RMB context toolbar > Edit Part ; alternative to Assembly toolbar > Edit Component |
| swCommands_Edit_Pipe_Rt | 2256; valid for the SOLIDWORKS Routing add-in and an open piping assembly; Piping toolbar > Edit Route |
| swCommands_Edit_Polygon | 1398; valid for an open sketch of a polygon; in the graphics area, polygon_entity RMB menu > Edit polygon |
| swCommands_Edit_Redolist | 1456; valid for models with an undo list; Standard toolbar > Redo |
| swCommands_Edit_Rollback | 815; valid for a model rebuilt with a feature; in the FeatureManager design tree, added_feature RMB context toolbar > Rollback or Edit menu > Rollback |
| swCommands_Edit_Rolltoend | 2503; valid for rolled back models; in the FeatureManager design tree, rolled_back_feat_name RMB menu > Roll to End or Edit menu > Roll to End |
| swCommands_Edit_Rolltoforward | 2506; valid for a selected rolled back feature; in the FeatureManager design tree, rolled_back_feat_name RMB menu > Roll Forward |
| swCommands_Edit_Rolltoprevious | 2502; valid for rolled back models; in the FeatureManager design tree, rolled_back_feat_name RMB menu > Roll to Previous or Edit menu > Roll to Previous |
| swCommands_Edit_Rtl_Mode | 2166; Text editor popup menu > Right to left reading order |
| swCommands_Edit_RV_Appearance | 2821; Render Tools or View toolbar > Edit Appearance |
| swCommands_Edit_Scene | 2967; Render Tools toolbar > Edit Scene |
| swCommands_Edit_Seed_Feature | 1242; valid for parts with a pattern feature; in the graphics area, pattern_entity RMB menu > Edit Seed Feature |
| swCommands_Edit_Select_All | 3027; Standard toolbar > Select All |
| swCommands_Edit_Sheet | 1502; finishes editing a drawing sheet in edit sheet format mode; in the FeatureManager design tree or the graphics area, sheet RMB menu > Edit Sheet |
| swCommands_Edit_Sk_Pattern | 1816; valid for a selected non-polygonal pattern relation; constraint RMB menu > Edit Pattern |
| swCommands_Edit_Sketch | 859; valid for sketches; Edit menu > Sketch or in the FeatureManager design tree, sketch_name RMB context toolbar > Edit Sketch |
| swCommands_Edit_Sketch_Belt | 2750; valid for sketch belts; in the FeatureManager design tree, belt_name RMB menu > Edit Belt |
| swCommands_Edit_Sketchplane | 863; valid for sketches; in the FeatureManager design tree or the graphics area, sketch RMB context toolbar > Edit Sketch Plane |
| swCommands_Edit_Smart_Comp_Inst | 2221; valid for assemblies with Smart Features; in the FeatureManager design tree, smart_feature RMB menu > Edit Feature |
| swCommands_Edit_Smart_Fastener | 2463; valid only for Toolbox add-ins and assemblies and existing Smart Fasteners; in the FeatureManager design tree, smart_fastener_feature RMB menu > Edit Smart Fastener |
| swCommands_Edit_Smart_Insert | 1856; valid for a selected Smart Insert feature; in the graphics area, feat RMB menu > Edit Smart Insert |
| swCommands_Edit_Suppress_All_Configs | 1417; valid for a selected feature that has multiple configurations; Edit menu > Suppress > All Configurations |
| swCommands_Edit_Suppress_Feature | 2498; valid for suppressible macro features; macro_feature RMB menu > Suppress |
| swCommands_Edit_Suppress_Select_Configs | 1419; valid for a selected feature that has multiple configurations; Edit menu > Suppress > Specified Configurations |
| swCommands_Edit_Swift_Schema | 2018; valid for a selected scheme in DimXpertManager, opens the Tolerance Scheme Properties PropertyManager page; in the DimXpertManager, sel_scheme RMB menu > Properties |
| swCommands_Edit_Template | 1501; valid for drawings; Sheet Format toolbar > Edit Sheet Format |
| swCommands_Edit_Text | 1811; valid for a selected note annotation; RMB menu > Edit Text |
| swCommands_Edit_Undolist | 813; Standard toolbar > Undo |
| swCommands_Edit_Unsuppress_All_Configs | 1421; valid for a suppressed selected feature that has multiple configurations; Edit menu > Unsuppress > All Configurations |
| swCommands_Edit_Unsuppress_Dependent_All_Configs | 1424; valid for a suppressed selected feature that has multiple configurations; Edit menu > Unsuppress with Dependents > All Configurations |
| swCommands_Edit_Unsuppress_Dependent_Select_Configs | 1425; valid for a suppressed selected feature that has multiple configurations; Edit menu > Unsuppress with Dependents > Specified Configurations |
| swCommands_Edit_Unsuppress_Feature | 2499; valid for suppressed macro features; macro_feature RMB menu > Unsuppress |
| swCommands_Edit_Unsuppress_Select_Configs | 1422; valid for a suppressed selected feature that has multiple configurations; Edit menu > Unsuppress > Specified Configurations |
| swCommands_Edit_Userdefined_Start_At_Point | 3167; valid for the SOLIDWORKS Routing add-in and an open routing assembly; User Defined Route toolbar > Edit Route |
| swCommands_Edit_Vsection | 1129; valid for a Section view; View menu > Modify > Section View |
| swCommands_Edit_Weldment_Props | 2360; valid for weldments; in the FeatureManager design tree, Weldment RMB menu > Properties |
| swCommands_EditBlock | 471; valid for models with blocks; Blocks toolbar > Edit Block |
| swCommands_EditColor | 170; valid for a selected curve or sketch; View toolbar > Edit Sketch or Curve Color |
| swCommands_EditComponent | 119; valid for a selected assembly component; Assembly toolbar > Edit Component |
| swCommands_EditFeature | 623; valid for parts with features, Edit Menu > Definition ; valid in many context toolbars, e.g., in the FeatureManager design tree, feat_name RMB context toolbar > Edit Feature ; valid for models with design tables; in the ConfigurationManager, Tables folder > Design Table RMB menu > Edit Feature |
| swCommands_EditFlexiblePartComp | 3421; valid for the selected flexible assembly component; RMB menu > Edit Flexible Part References |
| swCommands_EditMacro | 84; Macro toolbar > Edit Macro |
| swCommands_EditMaterial | 501; valid for a selected part in an assembly; Standard toolbar > Edit Material |
| swCommands_Edt_Elec_Route | 2251; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Electrical toolbar > Edit Route |
| swCommands_Elec_Rt_Properties | 2253; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Electrical toolbar > Route Properties |
| swCommands_Electrical_Autoroute | 2079; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Routing Tools toolbar > Auto Route |
| swCommands_Electrical_EditConnector | 3143; valid for the SOLIDWORKS Routing add-in and an open route; Electrical toolbar > Edit Connectors |
| swCommands_Electrical_Load_From_To_Data | 2078; valid for the SOLIDWORKS Routing add-in and an open route; Electrical toolbar > Edit Wires |
| swCommands_Electrical_Route | 2271; valid for the SOLIDWORKS Routing add-in; Routing toolbar > Electrical |
| swCommands_Ellipse | 87; valid in an open sketch; Sketch toolbar > Ellipse |
| swCommands_EmptyView | 351; valid for drawings; Drawing toolbar > Empty View |
| swCommands_Enable_Ann_View_Mode | 2443; valid for parts and assemblies; in the FeatureManager design tree, Annotations folder RMB menu > Enable Annotation View Visibility |
| swCommands_End_Contour_Single_Select | 661; valid for parts or assemblies in contour single select mode, ends contour single select mode |
| swCommands_End_Select_Contour | 2496; valid when a PropertyManager page is open, and RMB menu > Start Contour Selection was selected; in the graphics area, RMB menu > End Select Contours |
| swCommands_End_Smart_Selection | 2629; valid during Smart selection; RMB menu > End Smart Selection |
| swCommands_EndCap | 570; valid for weldments; Weldments toolbar > End Cap |
| swCommands_EndTreatment | 517; valid for drawings with a selected edge; Annotation toolbar > End Treatment |
| swCommands_EnterTheOffsetOfTheSupportArea | 6; alternative to swCommands_Toolbar_Table; View menu > Toolbars > Table |
| swCommands_Entity_Properties | 807; entity RMB menu > entity Properties |
| swCommands_Envelope_Publisher | 3416; Tools toolbar > Envelope Publisher |
| swCommands_Equations | 51; Tools toolbar > Equations |
| swCommands_Escape_Key_Down | 961; virtual key ESC |
| swCommands_ExcelBasedBillOfMaterials | 512; valid for a selected view in a drawing of an assembly; Table toolbar > Excel based Bill of Materials |
| swCommands_Exit_Measure | 2961; Measure dialog > Exit measure |
| swCommands_Exit_Sketch | 862; valid for an open sketch; RMB menu > Exit Sketch |
| swCommands_Exit_Structural_Member | 3404; valid when creating a structure system, exits from Advanced Structure System mode; Structure System toolbar > Exit Structure System |
| swCommands_Explode_Add_To_Group | 2544; valid when the Explode PropertyManager page is open, an explode step exists, and a component is selected; in the Explode PropertyManager page, Explode Steps > Explode Step > comp > RMB menu > Group |
| swCommands_Explode_Delete | 2540; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, Explode Steps > Chain > Group > comp > RMB menu > Delete |
| swCommands_Explode_Delete_Last_Step | 2545; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, RMB menu > Delete from last step |
| swCommands_Explode_Done_With_Step | 3385; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, RMB menu > Done with step |
| swCommands_Explode_Move_After_Group_T | 2550; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, Explode Steps > Chain > Group > comp > RMB menu > Ungroup and move down |
| swCommands_Explode_Move_Before_Group_T | 2546; valid when the Explode PropertyManager page is open, and a group of chained explode steps exists; in the Explode PropertyManager page, Explode Steps > Chain > Group > comp > RMB menu > Ungroup and move up |
| swCommands_Explode_Reuse_Sub | 2547; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the graphics area, RMB menu > Reuse subassembly explode |
| swCommands_Explode_Reuse_Tree_Sub | 2549; valid when the Explode PropertyManager page is open, and a subassembly is selected; in the Explode PropertyManager page, Explode Steps > subassembly RMB menu > Reuse subassembly explode |
| swCommands_Explode_Roll_Back | 3339; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Roll back |
| swCommands_Explode_Roll_Forward | 3340; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Roll forward |
| swCommands_Explode_Roll_To_End | 3342; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Roll to end |
| swCommands_Explode_Roll_To_Previous | 3341; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Roll to previous |
| swCommands_Explode_Suppress | 3348; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Suppress |
| swCommands_Explode_Tree_Edit | 2553; valid when the Explode PropertyManager page is open, and a drag manipulator is selected; in the graphics area, drag_manip RMB menu > Edit step |
| swCommands_Explode_Unsuppress | 3349; valid in an assembly's Exploded ViewN PropertyManager, Explode Steps > explode_stepN RMB menu > Unsuppress |
| swCommands_Explode_Update_Sub | 2548; valid when the Explode PropertyManager page is open, and a subassembly's explode has been reused ; in the Explode PropertyManager, Explode Steps > steps_of_subassembly RMB menu > Update subassembly's steps |
| swCommands_ExplodeBlock | 472; valid for blocks created in assembly layouts or drawings; Layout Tools toolbar > Explode Block |
| swCommands_ExplodedView | 135; valid for assemblies; Assembly toolbar > Exploded View |
| swCommands_ExplodeLineSketch | 395; valid for assemblies with exploded views; Assembly toolbar > Explode Line Sketch |
| swCommands_ExplodeSketch | 485; alternative to swCommands_Toolbar_Exploderoute; View menu > Toolbars > Explode Sketch |
| swCommands_ExtendEntities | 63; valid for open sketches; Sketch toolbar > Extend Entities |
| swCommands_ExtendSurface | 301; valid for selected edge or face of a surface sketch; Surfaces toolbar > Extend Surface |
| swCommands_Extrude | 392; valid only for parts; 2D to 3D toolbar > Convert to Extrusion |
| swCommands_ExtrudedBossBase | 8; valid for parts with a selected sketch; Features toolbar > Extruded Boss/Base |
| swCommands_ExtrudedCut | 10; valid for parts; Sheet Metal toolbar > Extruded Cut or Features toolbar > Extruded Cut |
| swCommands_ExtrudedSurface | 106; valid for a selected part sketch; Surfaces toolbar > Extruded Surface |
| swCommands_Face_Curvature | 1141; valid for parts or assemblies; alternative to swCommands_Curvature; View toolbar > Curvature |
| swCommands_FaceCurves | 321; valid for parts with a selected face; Sketch toolbar > Face Curves |
| swCommands_Far_Stack_Smart_Fastener | 2455; valid for a Smart Hole Fastener in an assembly; smart_hole_fastener_tree_item RMB > Bottom stack |
| swCommands_Feat_Edit | 865; valid for some selected surfaces and body features; in the graphics area, RMB menu > Edit |
| swCommands_Feature_Color | 651; in the FeatureManager design tree, sketch_name RMB menu > Sketch Color |
| swCommands_Feature_Pop_Make_Weld_Bead | 2391; valid for weldments with a selected feature; in the FeatureManager design tree, feature_name RMB menu > Make Weld Bead |
| swCommands_Feature_Pop_Remove_Weld_Bead | 2393; valid for weldments with a selected feature having weld beads; in the FeatureManager design tree, feature_name RMB menu > Make Non Weld Bead |
| swCommands_Feature_Pop_Suppress_Weld_Beads | 2392; valid for a selected weldment; in the FeatureManager design tree, Weldment RMB menu > Suppress Weld Beads |
| swCommands_Feature_Pop_Unsuppress_Weld_Beads | 2394; valid for a selected weldment; in the FeatureManager design tree, Weldment RMB menu > Unsuppress Weld Beads |
| swCommands_Feature_RV_Appearance | 2897; valid for parts or assemblies with a selected feature; in the FeatureManager design tree, feature_name RMB context toolbar > Appearances > feature_name |
| swCommands_Feature_Texture | 652; valid for a selected feature, opens the Texture PropertyManager page |
| swCommands_FeatureImportDiagnosis | 70; valid for imported geometry only; Tools toolbar > Import Diagnostics |
| swCommands_Features | 479; alternative to swCommands_Toolbar_Features; View menu > Toolbars > Features |
| swCommands_Featureworks | 438; SOLIDWORKS Add-ins toolbar > FeatureWorks |
| swCommands_File_Copy_Design | 2295; File menu > Pack and Go |
| swCommands_File_Derive_Comp | 992; valid for assemblies; File menu > Derive Component Part |
| swCommands_File_Find | 977; File menu > Find References |
| swCommands_File_Summaryinfo | 963; Standard toolbar > File Properties |
| swCommands_FileClose | 2789; File menu > Close or Standard toolbar > Close |
| swCommands_FileReload | 113; File menu > Reload or Standard toolbar > Reload |
| swCommands_Fillet | 9; valid for parts; Features toolbar > Fillet |
| swCommands_FilletBead | 505; valid for weldments with two preselected face sets and one preselected intersecting edge set; Weldment toolbar > Fillet Bead |
| swCommands_FillPattern | 558; valid for parts with a selected sketch; Features toolbar > Fill Pattern |
| swCommands_Filter_Toolbar | 1609; alternative to swCommands_Toolbar_Sel_Filter; View menu > Toolbars > Selection Filter |
| swCommands_FilterAxes | 279; Selection Filter toolbar > Filter Axes |
| swCommands_FilterBlocks | 361; Selection Filter toolbar > Filter Blocks |
| swCommands_FilterCenterlines | 441; Selection Filter toolbar > Filter Centerlines |
| swCommands_FilterCenterMarks | 284; Selection Filter toolbar > Filter Center Marks |
| swCommands_FilterConnectionPoints | 458; Selection Filter toolbar > Filter Connection Points |
| swCommands_FilterCosmeticThreads | 292; Selection Filter toolbar > Filter Cosmetic Threads |
| swCommands_FilterDatumFeatures | 289; Selection Filter toolbar > Filter Datum Features |
| swCommands_FilterDatumTargets | 291; Selection Filter toolbar > Filter Datum Targets |
| swCommands_FilterDimensionsHoleCallouts | 285; Selection Filter toolbar > Filter Dimensions/Hole Callouts |
| swCommands_FilterDowelPinSymbols | 382; Selection Filter toolbar > Filter Dowel Pin Symbols |
| swCommands_FilterEdges | 277; Selection Filter toolbar > Filter Edges |
| swCommands_FilterFaces | 278; Selection Filter toolbar > Filter Faces |
| swCommands_FilterGeometricTolerances | 287; Selection Filter toolbar > Filter Geometric Tolerances |
| swCommands_FilterMeshFacet | 3230; allows selection of mesh facets only; Selection Filter toolbar > Filter Mesh Facets |
| swCommands_FilterMeshFin | 3231; allows selection of mesh facet edges only; Selection Filter toolbar > Filter Mesh Facet Edges |
| swCommands_FilterMeshVertex | 3232; allows selection of mesh facet vertices only; Selection Filter toolbar > Filter Mesh Facet Vertices |
| swCommands_FilterMidpoints | 283; Selection Filter toolbar > Filter Midpoints |
| swCommands_FilterNotesBalloons | 288; Selection Filter toolbar > Filter Notes/Balloons |
| swCommands_FilterPlanes | 280; Selection Filter toolbar > Filter Planes |
| swCommands_FilterRoutingPoints | 459; Selection Filter toolbar > Filter Routing Points |
| swCommands_FilterSketches | 2857; Selection Filter toolbar > Filter Sketches |
| swCommands_FilterSketchPoints | 281; Selection Filter toolbar > Filter Sketch Points |
| swCommands_FilterSketchSegments | 282; Selection Filter toolbar > Filter Sketch Segments |
| swCommands_FilterSolidBodies | 419; Selection Filter toolbar > Filter Solid Bodies |
| swCommands_FilterSurfaceBodies | 303; Selection Filter toolbar > Filter Surface Bodies |
| swCommands_FilterSurfaceFinishSymbols | 286; Selection Filter toolbar > Filter Surface Finish Symbols |
| swCommands_FilterVertices | 276; Selection Filter toolbar > Filter Vertices |
| swCommands_FilterWeldBeads | 577; Selection Filter toolbar > Filter Weld Beads |
| swCommands_FilterWeldSymbols | 290; Selection Filter toolbar > Filter Weld Symbols |
| swCommands_Final_Render | 2969; Render Tools toolbar > Final Render |
| swCommands_Find_Next | 764; dialog resource Find Next |
| swCommands_Finish_Active_Contour | 665; valid for an active sketch in contour manipulation mode; in the graphics area, RMB menu > Finish Contour |
| swCommands_FitSpline | 426; valid for a sketch in edit mode; Spline Tools toolbar > Fit Spline |
| swCommands_FitText | 628; valid for selected text; Formatting toolbar > Fit Text |
| swCommands_Fix_Component | 957; valid for a selected floating component; in the FeatureManager design tree, comp RMB menu > Fix |
| swCommands_Fixed_Length_Covering | 3382; valid for SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; Routing Tools toolbar > Fixed Length Covering |
| swCommands_Fixed_Length_Route | 3149; valid for SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; Routing Tools toolbar > Fixed Length |
| swCommands_FlatPatternBendNotch | 3529; Insert > Sheet Metal > Bend Notch... |
| swCommands_Flatten | 138; valid for sheet metal parts; Sheet Metal toolbar > Flatten |
| swCommands_Flex | 409; valid for parts; Features toolbar > Flex |
| swCommands_Flex_Tube_Rt_Properties | 2261; valid for the SOLIDWORKS Routing add-in and an open flexible tubing assembly; Flexible Tubing toolbar > Route Properties |
| swCommands_Flexible_Part_Remove_Ref | 3430; valid for a selected reference entity in the Flexible References group box of the Activate Flexible Component PropertyManager; selected PM reference entity RMB menu > Delete |
| swCommands_Flexible_Tube_Route | 2272; valid for the SOLIDWORKS Routing add-in; Routing toolbar > Flexible Tube |
| swCommands_Flip_Direction | 2560; valid in sketch constraint list boxes; list_box RMB menu > Flip Relation |
| swCommands_Flip_Dowel_Sym | 1806; valid for a selected dowel symbol; dowel_sym RMB menu > Flip Symbol |
| swCommands_Flip_Endpoint_Tangency | 3535; Sketch toolbar > Flip Endpoint Tangent |
| swCommands_Flip_Ref_Dim | 1548; selected_reference_dimension RMB menu > Change Plane |
| swCommands_Flip_Smart_Fastener | 2453; valid only for Toolbox add-ins and assemblies and only when editing a Smart Fastener grouping; in the Smart Fasteners PropertyManager page, Results > Group1 > Series1 RMB menu > Flip |
| swCommands_FlowSimulation | 3504; SOLIDWORKS Flow Simulation |
| swCommands_FlowSimulation_ElCooling | 3506; SOLIDWORKS Flow Simulation + Electronics |
| swCommands_FlowSimulation_HVAC | 3505; SOLIDWORKS Flow Simulation + HVAC |
| swCommands_FlowSimulation_HVAC_ElCooling | 3507; SOLIDWORKS Flow Simulation + HVAC + Electronics |
| swCommands_Fmt_Painter | 2841; valid for a selected annotation or dimension from which to copy visual properties; Tools toolbar > Format Painter |
| swCommands_Fmt_Painter_Apply_All | 2856; valid after calling swCommands_Fmt_Painter (Format Painter) and selecting the annotation or dimension to copy from; in the graphics area, selected_anno_or_dim RMB menu > Apply to all |
| swCommands_Fold | 325; valid for sheet metal parts; Sheet Metal toolbar > Fold |
| swCommands_Font_Continue_Number | 2099; Text editor popup menu > Continue Numbering |
| swCommands_Font_Face | 1148; valid for selected text; Formatting toolbar > Document Font (dropdown) |
| swCommands_Font_Points | 1150; valid for selected text; Formatting toolbar > Font Points (dropdown) |
| swCommands_Font_Restart_Number | 2098; Text editor popup menu > Restart Numbering |
| swCommands_Font_Units | 1149; valid for selected text; Formatting toolbar > Font Units |
| swCommands_Fonts | 480; alternative to swCommands_Toolbar_Font; View menu > Toolbars > Formatting |
| swCommands_Force_Regen_Bucket | 3501; Regenerates drawing views; CTRL-Shift-Q |
| swCommands_ForceMateMisalignment | 3326; valid for a pre-selected concentric mate, forces misalignment; in the FeatureManager design tree, concentric mate RMB menu > Force misalignment |
| swCommands_Form_Newassembly | 1259; valid for assemblies with one or more selected components or feature foldesr; in the FeatureManager design tree, sel_comp RMB menu > Form New Subassembly |
| swCommands_FormingTool | 560; valid for sheet metal parts; Sheet Metal toolbar > Forming Tool |
| swCommands_Forward | 1615; palette toolbar > Forward |
| swCommands_FourView | 552; View toolbar > Four View |
| swCommands_Freeze_All | 3015; valid for a selected freeze bar in the FeatureManager design tree; freeze_bar RMB menu > Roll to End (Freeze All) |
| swCommands_Front | 161; View toolbar > View Orientation > Front |
| swCommands_FullScreenMode | 619; F11 or View menu > Full Screen or Standard toolbar > Full Screen View |
| swCommands_FullyDefineSketch | 600; valid for an open sketch; Dimensions/Relations toolbar > Fully Define Sketch |
| swCommands_Gantt_Zoomin | 2146; Motion Study Animator toolbar > Zoom In |
| swCommands_Gantt_Zoomout | 2147; Motion Study Animator toolbar > Zoom Out |
| swCommands_Gantt_Zoomtofit | 2916; Motion Study Animator toolbar > Zoom to Fit |
| swCommands_GeneralTable | 412; valid for drawings; Table toolbar > General Table |
| swCommands_GeneralToleranceTable | 3233; valid for drawings; Table toolbar > General Tolerance Table |
| swCommands_Generate_Region | 2510; valid during contour selection if region selection is enabled, RMB menu > Generate Regions |
| swCommands_Geometric_Callout | 1838; valid for a selected hole wizard callout dimension; RMB menu > Define by Geometry |
| swCommands_GeometricTolerance | 58; valid for drawings; Annotation toolbar > Geometric Tolerance |
| swCommands_GetSupport | 3446; Help > Get Support |
| swCommands_Glassbox_Done | 2196; valid after running swCommands_3DDrawingView for a selected drawing view; OK in popup toolbar dialog |
| swCommands_Glassbox_Exit | 2986; valid after running swCommands_3DDrawingView for a selected drawing view; Exit in popup toolbar dialog |
| swCommands_Glassbox_Pan | 2201; valid after running swCommands_3DDrawingView for a selected drawing view; Pan in popup toolbar dialog |
| swCommands_Glassbox_Rotate | 2200; valid after running swCommands_3DDrawingView for a selected drawing view; Rotate in popup toolbar dialog |
| swCommands_Glassbox_Save | 2987; valid after running swCommands_3DDrawingView for a selected drawing view; Save the view in popup toolbar dialog |
| swCommands_Glassbox_ViewOrient | 2988; valid after running swCommands_3DDrawingView for a selected drawing view; View Orientation in popup toolbar dialog |
| swCommands_Glassbox_Zoom | 2199; valid after running swCommands_3DDrawingView for a selected drawing view; Zoom in/out in popup toolbar dialog |
| swCommands_Glassbox_Zoomto | 2198; valid after running swCommands_3DDrawingView for a selected drawing view; Zoom to Area in popup toolbar dialog |
| swCommands_Glassbox_Zoomtofit | 2197; valid after running swCommands_3DDrawingView for a selected drawing view; Zoom to Fit in popup toolbar dialog |
| swCommands_Go_To_Mate_Component_1 | 2528; valid for assemblies with mate components; in the FeatureManager design tree, first_part_mate_relation RMB menu > second_part_mate > Go to |
| swCommands_Go_To_Mate_Component_2 | 2533; valid for assemblies with mate components; in the FeatureManager design tree, second _part_mate_relation RMB menu > first_part_mate > Go to |
| swCommands_Goto_Auxiliary_View | 1404; valid for drawings with an auxiliary view; in the drawing, selected_auxiliary_view_arrow RMB menu > Jump to Auxiliary View |
| swCommands_Goto_Component | 1587; valid for assembly views under special circumstances; in the graphics view, comp RMB menu > Go to Component (in Tree) |
| swCommands_Goto_Detail_View | 1402; valid for drawings with a detail view; in the drawing, detail_circle RMB menu > Jump to Detail View |
| swCommands_Goto_Feature | 1586; in the graphics area, selected_entity RMB menu > Go to Feature (in Tree) |
| swCommands_Goto_Parent_View | 1403; valid for drawings with a section or detail view; detail_view RMB menu > Jump to Parent View |
| swCommands_Goto_Projected_View | 1405; valid for drawings with a projected view; projected_view_arrow RMB menu > Jump to Projected View |
| swCommands_Goto_Section_View | 1401; valid for drawings with a section view; section _view_arrow RMB menu > Jump to Section View |
| swCommands_Gravity | 420; valid in the context of Basic Motion Studies; in the MotionManager toolbar, Gravity adds gravity to a motion study |
| swCommands_Grid_Align | 673; resource string or dialog resource Align Grid |
| swCommands_Grid_View | 2999; valid for a part or assembly with a GridSystem feature; in the FeatureManager design tree, grid_system RMB menu > View Grid Components |
| swCommands_GridFeature | 2982; valid for parts or assemblies; Features toolbar > Grid System or Insert > Reference Geometry > Grid System |
| swCommands_GridSnap | 41; valid for sketches; Quick Snaps toolbar > Grid Snap |
| swCommands_GrooveWeld | 3530; valid for parts, adds a groove weld bead feature between two selected disjoint bodies; Insert > Weldments > Groove Bead |
| swCommands_Ground_Plane | 3217; valid for assemblies only, opens the Ground Plane PropertyManage page; Insert menu > Reference Geometry > Ground Plane |
| swCommands_Group | 318; valid for multi-selected annotations or dimensions in a drawing; Align toolbar > Group |
| swCommands_Group_Remove_Item | 1455; valid for a drawing with a group of three or more annotations or dimensions; grouped_anno RMB menu > Group > Remove from Group |
| swCommands_Gusset | 453; valid for weldments with two selected adjoining faces; Weldments toolbar > Gusset |
| swCommands_HandSketch | 2850; valid only for a sketch opened in SOLIDWORKS running on supporting pen/stylus hardware; Sketch Ink toolbar > Insert HandSketch |
| swCommands_HandsketchColor | 3238; valid only on supporting pen/stylus hardware, sets pen stroke color; Sketch Ink toolbar > Color |
| swCommands_HandsketchConvertEntity | 3241; valid only on supporting pen/stylus hardware, automatically converts a pen stroke to sketch entities; Sketch Ink toolbar > Auto Convert to Entities |
| swCommands_HandsketchConvertShape | 3240; valid only on supporting pen/stylus hardware, automatically converts a pen stroke to recognized shapes; Sketch Ink toolbar > Auto Convert to Shape |
| swCommands_HandsketchDraw | 3455; valid only on supporting pen/stylus hardware, draws ink strokes; Sketch Ink toolbar > Pen |
| swCommands_HandsketchEditModify | 3413; valid only on supporting pen/stylus hardware, edit power modify sketch entities; Sketch Ink toolbar > Edit Power Modify |
| swCommands_HandsketchEraser | 3236; valid only on supporting pen/stylus hardware, erases pen strokes; Sketch Ink toolbar > Eraser |
| swCommands_HandsketchModify | 3409; valid only on supporting pen/stylus hardware, modifies the sketch; Sketch Ink toolbar > Power Modify |
| swCommands_HandsketchPen | 3235; valid only on supporting pen/stylus hardware, uses pen for sketch ink; Tools menu > Sketch Tools > Pen Tools > Pen |
| swCommands_HandsketchPenProps | 3295; valid only on supporting pen/stylus hardware, gets pen properties; Sketch Ink toolbar > Pen or Tools > Sketch Settings > Pen Settings > Pen Properties |
| swCommands_HandsketchProtractor | 3381; valid only on supporting pen/stylus hardware, toggles the pen sketch protractor; Sketch Ink toolbar > Protractor |
| swCommands_HandsketchReplaceChamfer | 3426; valid only on supporting pen/stylus hardware, converts power modify to sketch chamfer; Sketch Ink toolbar > Convert to Sketch Chamfer |
| swCommands_HandsketchReplaceComposite | 3345; valid only on supporting pen/stylus hardware, converts recognized shape with Composite; Sketch Ink toolbar > Convert to Composite |
| swCommands_HandsketchReplaceEllipse | 3347; valid only on supporting pen/stylus hardware, converts recognized shape with Ellipse; Sketch Ink toolbar > Convert to Ellipse |
| swCommands_HandsketchReplaceExtend | 3428; valid only on supporting pen/stylus hardware, converts power modify to sketch extend; Sketch Ink toolbar > Convert to Sketch Extend |
| swCommands_HandsketchReplaceFillet | 3427; valid only on supporting pen/stylus hardware, converts power modify to sketch fillet; Sketch Ink toolbar > Convert to Sketch Fillet |
| swCommands_HandsketchReplaceSlot | 3346; valid only on supporting pen/stylus hardware, converts recognized shape with Slot; Sketch Ink toolbar > Convert to Slot |
| swCommands_HandsketchReplaceSpline | 3344; valid only on supporting pen/stylus hardware, converts recognized shape with Spline; Sketch Ink toolbar > Convert to Spline |
| swCommands_HandsketchRuler | 3291; valid only on supporting pen/stylus hardware, toggles the pen sketch ruler; Sketch Ink toolbar > Ruler |
| swCommands_HandsketchSelect | 3237; valid only on supporting pen/stylus hardware, uses the pen to select; Sketch Ink toolbar > Select |
| swCommands_HandsketchSplineMode | 3387; valid only on supporting pen/stylus hardware, automatically converts complex stroke to spline; Sketch Ink toolbar > Auto Spline |
| swCommands_HandsketchTouch | 3290; valid only on supporting pen/stylus hardware, toggles Touch input to Pen Sketch; Sketch Ink toolbar > Touch |
| swCommands_HandsketchUpdateToEntity | 3241; valid only on supporting pen/stylus hardware, updates the selected pen stroke to sketch entities; Sketch Ink toolbar > Update to Entities |
| swCommands_HandsketchUpdateToShape | 3240; valid only on supporting pen/stylus hardware, updates the selected pen stroke to a recognized shape; Sketch Ink toolbar > Update to Shape |
| swCommands_Hatch_Properties | 674; valid for hatched section views in drawings or part sketches; selected_hatched_sketch RMB menu > Crosshatch Properties |
| swCommands_HealEdges | 518; valid for parts for selected faces; Features toolbar > Heal Edges |
| swCommands_Helix_Ccw | 2389; valid when the Helix/Spiral PropertyManager page is open, and the helix is going clockwise; in the graphics area, RMB menu > Counterclockwise |
| swCommands_Helix_Cw | 2387; valid when the Helix/Spiral PropertyManager page is open, and the helix is going counterclockwise; in the graphics area, RMB menu > Clockwise |
| swCommands_Helix_Taperhelix | 2388; valid when the Helix/Spiral PropertyManager page is open; in the graphics area, RMB menu > Taper Helix |
| swCommands_HelixAndSpiral | 94; valid for parts with a selected sketch of a single circle; Features toolbar > Curves > Helix and Spiral |
| swCommands_Helixdve_Revdir | 2386; valid when the Helix/Spiral PropertyManager page is open, and the helix is going counterclockwise; in the graphics area, RMB menu > Reverse Direction |
| swCommands_Help | 340; Standard toolbar > Help |
| swCommands_Help_Autocad_Users | 1882; Help menu > Moving from 2D to 3D |
| swCommands_Help_Onlinetutorial | 1423; Help menu > SOLIDWORKS Tutorials |
| swCommands_Hem | 363; valid for sheet metal parts; Sheet Metal toolbar > Hem |
| swCommands_HiddenLinesRemoved | 335; View toolbar > Display Style > Hidden Lines Removed |
| swCommands_HiddenLinesVisible | 336; View toolbar > Display Style > Hidden Lines Visible |
| swCommands_Hide_3d_Sketch_Triad | 3528; valid for an open 3D sketch displaying the sketcher triad; in the graphics area, RMB menu > Hide Sketcher Triad |
| swCommands_Hide_Bom | 1239; valid for a drawing view excel-based BOM; excel_based_bom RMB menu > Hide |
| swCommands_Hide_Components | 925; valid for selected components in assemblies; in the FeatureManager design tree, selected_comp RMB context toolbar > Hide Components |
| swCommands_Hide_Components_All_Configs | 1649; valid for a selected top-level assembly; Edit menu > Hide > All Display States |
| swCommands_Hide_Components_Select_Configs | 1650; valid for a selected top-level assembly, opens the Apply To Display States dialog; Edit menu > Hide > Specified Display States |
| swCommands_Hide_Cthread | 1528; valid for a model with a selected cosmetic thread; in the graphics area, cosmetic_thread RMB context toolbar > Hide Cosmetic Thread |
| swCommands_Hide_Dim | 1539; valid in drawings with annotations or dimension; in the graphics area, selected_anno RMB menu > Hide |
| swCommands_Hide_Dim_Leader | 2538; valid for a drawing with a dimension with a leader line; leader_line RMB menu > Hide Dimension Line |
| swCommands_Hide_Dim_Witness | 2526; valid for a drawing with a dimension with a witness line; witness_line RMB menu > Hide Extension Line |
| swCommands_Hide_Feature_Detail | 931; valid for a selected top-level assembly showing feature detail; in the graphics area, RMB menu > Show Hierarchy Only |
| swCommands_Hide_Incontext_Feature_Holders | 687; valid for a selected top-level assembly with visible update holders; selected_assembly RMB menu > Hide Update Holders |
| swCommands_Hide_Mate_Component_1 | 2529; valid for assemblies with visible mate components; in the FeatureManager design tree, first_part_mate_constraint RMB menu > second_part_mate > Hide component |
| swCommands_Hide_Mate_Component_2 | 2534; valid for assemblies with visible mate components; in the FeatureManager design tree, second_part_mate_constraint RMB menu > first_part_mate > Hide component |
| swCommands_Hide_Mesh_Feat | 3211; valid for a selected mesh feature that is visible; RMB menu > Hide |
| swCommands_Hide_Sketch_Dim_In_Drawing | 2478; valid for a selected visible dimension in a drawing sketch; RMB menu > Hide Dimensions |
| swCommands_Hide_Table | 2623; valid for models with tables; in the FeatureManager design tree, table_name RMB menu > Hide Table |
| swCommands_Hide_Zone | 1561; valid for assemblies with envelope components; in the FeatureManager design tree, envelope_feature RMB menu > Envelope > Select Using Envelope |
| swCommands_HideEdge | 353; valid for a selected edge in a drawing, hides the selected edge |
| swCommands_Hideshow_Brwser_Tree | 2556; F9 or View menu > User Interface > FeatureManager Tree Area |
| swCommands_HideShowAnnotations | 67; Annotation toolbar > Hide/Show Annotations |
| swCommands_HideShowComponents | 85; valid for selected components in an assembly; Assembly toolbar > Hide/Show Components |
| swCommands_HideShowEdges | 2938; valid for drawings; Line Format toolbar > Hide/Show Edges |
| swCommands_Hlink_History | 684; Web toolbar > web_history_dropdown |
| swCommands_Hole_Table_Expand_Same_Size | 2368; valid for drawings with hole tables where same-size holes are combined; in the FeatureManager design tree, hole_table RMB menu > Expand Same Sizes |
| swCommands_Hole_Table_Goto_Tag | 2364; valid for drawings with hole tables; in the drawing, hole_table_cell RMB menu > Jump to Tag |
| swCommands_Hole_Table_Hide_Centers | 2370; valid for drawings with hole tables whose hole centers are visible; in the drawing, hole_table RMB menu > Hide Hole Centers |
| swCommands_Hole_Table_Hide_Origin | 2362; valid for drawings with hole tables whose hole origins are visible; in the drawing, hole_table RMB menu > Hide Origin Indicator |
| swCommands_Hole_Table_Hide_Tags | 2438; valid for drawings with hole tables whose hole tags are visible; in the drawing, hole_table RMB menu > Hide Hole Tags |
| swCommands_Hole_Table_Show_Centers | 2369; valid for drawings with hole tables whose hole centers are hidden; in the drawing, hole_table RMB menu > Show Hole Centers |
| swCommands_Hole_Table_Show_Origin | 2363; valid for drawings with hole tables whose hole origins are hidden; in the drawing, hole_table RMB menu > Show Origin Indicator |
| swCommands_Hole_Table_Show_Tags | 2437; valid for drawings with hole tables whose hole tags are hidden; in the drawing, hole_table RMB menu > Show Hole Tags |
| swCommands_HoleAlignment | 2822 valid for assemblies; Assembly toolbar > Hole Alignment |
| swCommands_HoleCallout | 121; valid for drawings with holes or circular cut features; Annotation toolbar > Hole Callout |
| swCommands_HoleSeries | 556; valid for assemblies with multi-selected part locations for a series of holes; Features toolbar or Insert menu > Assembly Feature > Hole > Hole Series |
| swCommands_HoleTable | 446; valid for drawings; Table toolbar > Hole Table |
| swCommands_HoleWizard | 39; valid for parts with a selected sketch, opens the Hole Specification PropertyManager page; Features toolbar > Hole Wizard ; also valid for assemblies; Insert menu > Assembly Feature > Hole > Wizard |
| swCommands_Holewizard_Callout | 1839; valid for drawings with radial annotations; in the drawing, radial_dimension RMB menu > Display Options > Define by Hole Wizard |
| swCommands_Home | 1617; palette toolbar > Home |
| swCommands_HorizontalDimension | 66; valid for open sketches; Dimensions/Relations toolbar > Horizontal Dimension |
| swCommands_HorizontalOrdinateDimension | 347; valid for open sketches; Dimensions/Relations toolbar > Horizontal Ordinate Dimension |
| swCommands_HVPointSnap | 522; valid for sketches; Quick Snaps toolbar > H/V Point Snap |
| swCommands_HVSnap | 525; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > H/V Snap |
| swCommands_Ignore_Construction_Geom | 3332; valid when the Trim PropertyManager is active, graphics area RMB menu > Ignore trimming of construction geometry |
| swCommands_Import_To_Drawing | 1772; valid for a part with a location, basic location, or basic size dimension; location_dimension RMB menu > Mark for Drawing |
| swCommands_ImportedGeometry | 96; valid for parts; Features toolbar > Imported Geometry |
| swCommands_IncreaseIndent | 544; valid for selected text; Formatting toolbar > Increase indent |
| swCommands_Indent | 571; valid for multi-body parts with selected target and tool bodies; Features toolbar > Indent |
| swCommands_InkMarkupEraser | 3441; valid only in Markup Views, erases ink strokes; Markup toolbar > Erase |
| swCommands_InkMarkupMouse | 3440; valid only in Markup Views, draws with the mouse; Markup toolbar > Draw |
| swCommands_InkMarkupPen | 3439; valid only on supporting pen/stylus hardware and only in Markup Views, uses pen for Markup Ink input; Markup toolbar > Pen |
| swCommands_InkMarkupPenProps | 3438; valid only on supporting pen/stylus hardware and only in Markup Views, sets ink color and thickness; Markup toolbar > Color |
| swCommands_InkMarkupSelect | 3442; valid only on supporting pen/stylus hardware and only in Markup Views, selects ink strokes or notes; Markup toolbar > Select |
| swCommands_InkMarkupText | 3444; valid only on supporting pen/stylus hardware and only in Markup Views, adds a note to the current Markup View; Markup toolbar > Note |
| swCommands_InkMarkupView | 3398; inserts a Markup View; Markup toolbar > Markup View |
| swCommands_Insert_Baseline_Dimension | 3048; valid for a selected baseline dimension in a drawing; baseline_dim RMB menu > Add to BaseLine |
| swCommands_Insert_Bendtable_New | 1443; valid for a sheet metal part; Insert menu > Bend Table > New |
| swCommands_Insert_Bendtable_Open | 1442; valid for a sheet metal part; Insert menu > Bend Table > From File |
| swCommands_Insert_Camera | 2191; valid for parts; in DisplayManager, Scene, Lights, and Cameras > Camera RMB menu > Add Camera |
| swCommands_Insert_Chain_Dimension | 3405; starts the Chain Dimension tool; Tools menu > Dimensions > Chain |
| swCommands_Insert_Connection_Point | 1223; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Routing toolbar > Connection Point |
| swCommands_Insert_Connector | 2862; valid for the SOLIDWORKS Routing add-in and an open electrical routing assembly; Electrical toolbar > Insert Connectors |
| swCommands_Insert_Create_Assy_Feat | 1974; valid for parts with solid bodies; in the FeatureManager design tree, Cut list or Solid bodies folder RMB menu > Save Bodies; opens the Save Bodies PropertyManager |
| swCommands_Insert_Cthread_Callout | 845; valid for drawing views with a selected cosmetic thread that was created without a standard and with non-empty Thread Callout text; in the drawing, callout_thread RMB menu > Insert Callout |
| swCommands_Insert_Custom_Symbol_Save | 1208; custom_symbol RMB menu > Save to File |
| swCommands_Insert_Cut_Net | 2175; valid for parts with a selected sketch; Features toolbar > Boundary Cut |
| swCommands_Insert_Drw_Dxfdwg | 1849; Insert menu > DXF/DWG |
| swCommands_Insert_Feature_Lock | 29599; valid for models where feature freeze is enabled, and the feature to freeze is selected; in the FeatureManager design tree, feature RMB menu > Freeze |
| swCommands_Insert_Ff_View_3rd | 1244; valid when adding a 1st or 3rd angle view to a drawing; RMB menu > Insert From File |
| swCommands_Insert_Folder | 1829; valid for a selected item in the FeatureManager design tree; feature_name RMB menu > Add to New Folder |
| swCommands_Insert_Form_Assembly | 1325; valid for assemblies with selected components, opens Assembly Structure Editing dialog; Insert menu > Component > Assembly from [Selected] Components |
| swCommands_Insert_From_PartSupply | 3498; Opens 3DEXPERIENCE PartSupply in the SOLIDWORKS Task Pane. Browse PartSupply’s comprehensive and intelligent catalog of qualified sourceable 3D components to add to your assembly; only valid if 3DEXPERIENCE Marketplace Add-in is loaded and logged into; SOLIDWORKS menu > Insert > Component > Insert from PartSupply |
| swCommands_Insert_Geometry_Import | 1878; alternative to swCommands_ImportedGeometry; Features toolbar > Imported Geometry |
| swCommands_Insert_Light_Distantlight | 1295; in DisplayManager, Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Directional Light |
| swCommands_Insert_Light_Pointlight | 1293; in DisplayManager, Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Point Light |
| swCommands_Insert_Light_Spotlight | 1294; in DisplayManager, Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Spot Light |
| swCommands_Insert_Light_Sunlight | 3093; in DisplayManager, Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Add Sunlight |
| swCommands_Insert_Mirror_Subassembly | 1638; valid for assemblies; Assembly toolbar > Mirror Components |
| swCommands_Insert_Mirrored_Part | 988; valid for parts with a selected plane about which to mirror the part; Insert menu > Mirror Part |
| swCommands_Insert_Object | 818; opens an Insert Object dialog; Insert menu > Object |
| swCommands_Insert_Picture | 1131; valid for assemblies, opens an Open dialog with a Tiff Images (*.tif) selection filter; Insert > Picture |
| swCommands_Insert_Ref_Line | 1212; opens a Reference Line dialog |
| swCommands_Insert_Refdim | 909; valid for drawings, activates the dimensioning cursor; after calling this command, select one or two edges/vertices and then a location where to place the reference dimension text |
| swCommands_Insert_Route_Point | 1222; valid for the SOLIDWORKS Routing add-in, opens a Route Point PropertyManager page; Routing Tools toolbar > Route Point |
| swCommands_Insert_Schematic | 1632; valid for drawings, opens the Position Schematic PropertyManager page; Insert menu > Schematic |
| swCommands_Insert_Sculpt | 3051; valid for parts with two or more selected solid bodies; Features toolbar > Intersect |
| swCommands_Insert_Sectionline | 924; valid for a selected drawing sheet or view, opens a Make Section Line PropertyManager page; Insert menu > Make Section Line |
| swCommands_Insert_Sheet | 857; valid for drawings; Insert menu > Sheet |
| swCommands_Insert_Sketch_Dxfdwg | 1833; valid for parts with a selected plane where to insert the drawing, opens an Open dialog with a Dxf Files (*.dxf) filter; Insert menu > DXF/DWG |
| swCommands_Insert_Sketch_Import | 1408; valid for an open (minimized) drawing and an active window with an open sketch in a part; Insert menu > Sketch from Drawing (see the SOLIDWORKS Help) |
| swCommands_Insert_Smart_Features | 2220; valid for an assembly with a saved, selected Smart Component, opens the Smart Feature Insert PropertyManager page; Insert menu > Smart Features; in the FeatureManager design tree, Smart_Component RMB menu > Insert Smart Feature |
| swCommands_Insert_Smartfeature | 2235; valid for assemblies with saved Smart Components, opens the Smart Feature Insert PropertyManager page; in the FeatureManager design tree, History > Smart_Component_name > Smart Feature RMB menu > Insert |
| swCommands_Insert_Stock_Net | 2176; valid for parts with a selected sketch; Features toolbar > Boundary Boss/Base |
| swCommands_Insert_Target_Point | 1044; valid for a selected drawing view, activates the point cursor; after calling this command, select the location where to insert a datum target point |
| swCommands_Insert_Walkthrough | 2960; View toolbar > Add Walk-through or View menu > Lights and Cameras > Add Walk-through or Large Design Review tab > Add Walk-through |
| swCommands_Insert_Weld | 1024; valid for assemblies, opens the Weld Bead Type dialog |
| swCommands_Insert_Zone | 1139; valid for assemblies, opens an Open dialog with which to select the component to insert as an envelope feature |
| swCommands_InsertAbbrView | 3466; Opens the Model Break View PropertyManager; Insert > Model Break View... |
| swCommands_InsertAutoDim | 3244; valid for a selected sketch, applies the correct dimension based on selected entities; Dimension/Relations toolbar > Auto Insert Dimension |
| swCommands_InsertBelt | 616; valid for assemblies, opens the Belt/Chain PropertyManager page; Assembly or Blocks toolbar > Belt/Chain |
| swCommands_InsertBends | 118; valid for sheet metal parts; Sheet Metal toolbar > Insert Bends |
| swCommands_InsertBlock | 470; valid for a selected plane or planar face, opens the Insert Block PropertyManager page; Layout Tools or Blocks toolbar > Insert Block |
| swCommands_InsertBoundarySurface | 618; valid for parts, opens a Boundary-Surface PropertyManager page; Surfaces toolbar > Boundary Surface or Insert menu > Surface > Boundary Surface |
| swCommands_InsertCenterOfMass | 3057; valid for parts with a selected sketch; Features toolbar > Reference Geometry > Center of Mass or Reference Geometry toolbar > Center of Mass |
| swCommands_InsertCenterOfMassRefPoint | 3069; valid for parts with a Center of Mass; in the graphics area, c enter_of_mass context toolbar > Center of Mass Reference Point |
| swCommands_InsertComponents | 13; valid for assemblies, opens the Insert Component PropertyManager page; Assembly toolbar > Insert Component |
| swCommands_InsertCV | 3100; valid for open style splines; Spline Tools toolbar > Insert Control Vertex |
| swCommands_InsertDetailCenterLine | 425; valid for drawings, opens the Centerline PropertyManager page; Annotation toolbar > Centerline |
| swCommands_InsertDrawingviewSection | 34; valid for a selected drawing view; Drawing toolbar > SectionView |
| swCommands_InsertFaceDraft | 40; valid for parts with a selected sketch; Features toolbar > Draft |
| swCommands_InsertFamilyTable | 410; Insert menu > Tables > Family T able or Tables toolbar > Family Table |
| swCommands_InsertFamilyTable_Drw | 3537; Insert menu > Tables > Family T able or Tables toolbar > Family Table |
| swCommands_InsertFeatureBlend | 322; for assemblies with a mold base and design parts; Mold Tools toolbar > Filled Surface |
| swCommands_InsertFeatureMoveFace | 538; valid for parts, opens the Move Face ProeprtyManager page; Features toolbar > Move Face |
| swCommands_InsertFeatureNudge | 2928; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Move Face |
| swCommands_InsertHandSketch | 3243; valid for systems supporting stylus/pen hardware, inserts a pen sketch; Sketch toolbar > Pen Sketch |
| swCommands_InsertHyperlink | 134; opens an Insert Hyperlink dialog; Web toolbar > Insert Hyperlink |
| swCommands_InsertLiveSection | 2843; valid for parts and a selected face; Features toolbar > Live Section Plane |
| swCommands_InsertMoldFolders | 546; valid for parts; Mold Tools toolbar > Insert Mold Folders |
| swCommands_InsertNewFamilyMember | 3452; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Family Member PropertyManager to add a new part/assembly family member; ConfigurationManager > family_member RMB menu > New Family Member |
| swCommands_InsertNewPrivateFamilyMember | 3454; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Family Member PropertyManager to add a new private part/assembly family member that cannot be saved in the platform as a physical product; ConfigurationManager > family_member RMB menu > New Family Member |
| swCommands_InsertNewRepresentation | 3453; 3DEXPERIENCE SOLIDWORKS only, for a selected family member in ConfigurationManager, launches an Add Representation PropertyManager to add a new part/assembly representation of the configuration which is not managed on the platform as a physical product but has the same part number as the family member to which it is associated; ConfigurationManager > family_member RMB menu > New Family Member |
| swCommands_InsertOffsetRefSurface | 105; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Offset Surface |
| swCommands_InsertPart | 26; valid for parts, opens the Open dialog; Features toolbar > Insert Part |
| swCommands_InsertPartingLine | 111; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Split Line or Feature toolbar > Curves > Split Line |
| swCommands_InsertPartingPlane | 449; valid for parts; Mold Tools toolbar > Parting Surfaces |
| swCommands_InsertPlanarSurface | 168; valid for parts, opens the Planar Surface PropertyManager page; Surfaces or Mold Tools toolbar > Planar Surface |
| swCommands_InsertPlane | 23; valid for parts with a selected sketch; Features toolbar > Reference Geometry > Plane |
| swCommands_InsertRefpoint | 455; valid for parts with a selected sketch; Features toolbar > Reference Geometry > Point or Reference Geometry toolbar > Point |
| swCommands_InsertRefsurfaceRadiate | 155; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Radiate Surface |
| swCommands_InsertRefsurfaceSew | 156; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Knit Surface |
| swCommands_InsertRuledSurfaceFromEdge | 448; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Ruled Surface |
| swCommands_InsertScale | 350; valid for assemblies with a mold base and design parts; Mold Tools toolbar > Scale |
| swCommands_InsertSketchBelt | 611; valid for sketches with circles or arcs; Blocks toolbar > Belt/Chain |
| swCommands_InsertSketchEQCurve | 2881; valid for open sketches; Sketch toolbar > Equation Driven Curve |
| swCommands_InsertSplinePoint | 140; valid for an open sketch of a spline; Spline Tools toolbar > Insert Spline Point |
| swCommands_InsertSplitFeat | 397; valid for a selected solid body in a part; Features toolbar > Split |
| swCommands_InsertStructConnection | 3445; Structure System toolbar > Insert structural connection element |
| swCommands_InsertStudWiz | 3489; Insert menu > Features > Stud Wizard ...; Inserts a stud using a pre-defined cross-section |
| swCommands_InsertSubdExtrude | 3328; Insert menu > Freeshape > Extrude |
| swCommands_InsertSubdRevolve | 3329; Insert menu > Freeshape > Revolve |
| swCommands_InsertSubdSweep | 3330; Insert menu > Freeshape > Sweep |
| swCommands_InsertSymmDiaDim | 3490; Tools menu > Dimensions > Symmetric ; Creates a reference diameter dimension between selected entities |
| swCommands_InsertThreadWiz | 3181; valid for parts with a selected sketch; Features toolbar > Thread |
| swCommands_Int_Tree_Ignore | 2613; valid in an open Interference Detection DVE after calculation; Interference Detection PropertyManager page > Results > interference_tree RMB menu > Ignore |
| swCommands_Int_Tree_Open | 2614; valid in an open Interference Detection DVE after calculation; Interference Detection PropertyManager page > Results > interference_tree RMB menu > Open |
| swCommands_Int_Tree_Unignore | 2615; valid in an open Interference Detection DVE after calculation and only if Interference Detection > Options > Show ignored interferences is selected; Interference Detection PropertyManager page > Results > interference_tree RMB menu > Unignore |
| swCommands_Int_Tree_Zoom | 2616; valid in an open Interference Detection DVE after calculation; Interference Detection PropertyManager page > Results > interference_tree RMB menu > Zoom to selection |
| swCommands_InterferenceDetection | 344; valid for assemblies; Assembly toolbar > Interference Detection |
| swCommands_Internal_Dimension | 2594; valid for a selected dimension, toggles the Internal Dimension state and rebuilds the browser tree |
| swCommands_IntersectionCurve | 306; valid for sketches; Sketch toolbar > Intersection Curve |
| swCommands_IntersectionSnap | 524; valid for sketches; Quick Snaps toolbar > Intersection Snap |
| swCommands_InvertSelection | 564; Selection Filter toolbar > Invert Selection |
| swCommands_Iso_Draw_Electrical_Rt | 3353; Tools menu > Routing > Electrical > Create Drawing |
| swCommands_Iso_draw_pipe_rt | 2948; valid for the SOLIDWORKS Routing add-in and an open piping assembly; Piping toolbar > Pipe Drawing |
| swCommands_Isolate_Changed_Dims | 3023; valid for drawings saved in 2012 or later; Dimensions/Relations toolbar > Isolate Changed Dimensions |
| swCommands_Isometric | 167; View toolbar > View Orientation > Isometric |
| swCommands_Italic | 148; valid for selected text; Formatting toolbar > Italic |
| swCommands_Jog | 372; valid for sheet metal parts; Sheet Metal toolbar > Jog |
| swCommands_Jog_Ordinate | 1518; valid for a drawing of a circle or arc with a selected angular running dimension; in the graphics area, angular_running_dimensi on RMB menu > Display Options > Jog |
| swCommands_JogLine | 398; valid for a part with an open sketch and a selected segment; also valid for SOLIDWORKS Routing Add-in and an open route; Explode Sketch toolbar > Jog Line |
| swCommands_Join | 116; valid for an assembly to which a new join part is being added; Features toolbar > Join (see the SOLIDWORKS help) |
| swCommands_Join_Contours | 2516; valid for contour or loft DVEs; selection_list_box RMB menu > Join Contours |
| swCommands_Keep_Constraints | 2788; Move Confirm dialog resource Keep or Dangle |
| swCommands_Large_Icon | 1622; valid for content or palette list controls or component list views, RMB menu > Large Icons |
| swCommands_Large_List_Icon | 2065; valid for content or palette list controls or component list views, RMB menu > Large List Icons |
| swCommands_LargeAssemblyMode | 405; valid for assemblies; Assembly toolbar > Large Assembly Mode |
| swCommands_LaunchFilePrep_Asst | 3513; launches the File Preparation Assistant; Tools menu > File Preparation Assistant... |
| swCommands_Layer_Select | 1151; valid for drawings; Layer toolbar > drop-down menu |
| swCommands_Layer_Toolbar | 1955; alternative to swCommands_Toolbar_Layer; View menu > Toolbars > Layer |
| swCommands_LayerProperties | 296; valid for drawings; Line Format toolbar > Layer Properties |
| swCommands_Layout | 2817; alternative to swCommands_Toolbar_Layout; View menu > Toolbars > Layout Tools |
| swCommands_LayoutDefault | 2888; View menu > Workspace > Default |
| swCommands_LayoutDualMonitor | 2890; View menu > Workspace > Dual Monitor |
| swCommands_LayoutWidescreen | 2889; View menu > Workspace > Widescreen |
| swCommands_LDR_Update_Model_Graphics | 3090; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, top_level_assembly RMB menu > Update Model Graphics |
| swCommands_Leader_Add_Bent | 1780; valid for a drawing view with a selected leader; in the graphics area, leader RMB menu > Add Jog Point |
| swCommands_Leader_Add_Branch | 1778; valid for a drawing view with a selected leader; in the graphics area, leader RMB menu > Insert New Branch |
| swCommands_Leader_Delete_All | 1781; valid for a drawing with a selected multi-jog leader; in the graphics area, multi_jog_leader RMB menu > Delete Leader |
| swCommands_Leader_Delete_Bent | 1779; valid for a drawing view with a selected leader that has a jog; in the graphics area, leader RMB menu > Delete Jog Point |
| swCommands_Leader_Delete_Branch | 722; valid for a drawing view with a selected leader that has a branch; in the graphics area, leader RMB menu > Delete Branch |
| swCommands_Left | 164; View menu > View Orientation > Left |
| swCommands_LengthSnap | 540; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > Length Snap |
| swCommands_Light_Properties | 1296; valid for a selected SOLIDWORKS Light in the FeatureManager design tree if Scene, Lights, and Cameras > SOLIDWORKS Lights RMB menu > Show Lights is selected; in the graphics area, light RMB menu > Properties ; valid for a selected camera in DisplayManager; Camera > Camera1 RMB menu > Edit Camera |
| swCommands_Lightweight_All | 1235 valid for a selected assembly with resolved components; in the FeatureManager design tree, top_level_assy RMB menu > Set Resolved to Lightweight |
| swCommands_Line | 43; valid for an open sketch; Layout Tools or Sketch toolbar > Line |
| swCommands_Line_Center | 1312; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Center |
| swCommands_Line_Chain | 1311; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Chain |
| swCommands_Line_Dashed | 1309; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Dashed |
| swCommands_Line_Normal | 1317; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 0.25mm |
| swCommands_Line_Phantom | 1310; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Phantom |
| swCommands_Line_Solid | 1308; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Solid |
| swCommands_Line_Stitch | 1313; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Stitch |
| swCommands_Line_Stylebylayer | 1307; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Default |
| swCommands_Line_Thick | 1318; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 0.35mm |
| swCommands_Line_Thick2 | 1319; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 0.5mm |
| swCommands_Line_Thick3 | 1320; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 0.7mm |
| swCommands_Line_Thick4 | 1321; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 1mm |
| swCommands_Line_Thick5 | 1322; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 1.4mm |
| swCommands_Line_Thick6 | 1323; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 2mm |
| swCommands_Line_Thickthin | 1314; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Style > Thin/Thick Chain |
| swCommands_Line_Thin | 1316; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > 0.18mm |
| swCommands_Line_Weightbylayer | 1315; valid for drawings with a selected line; in the graphics area, selected_edge RMB context toolbar > Line Thickness > Default |
| swCommands_LinearMotor | 422; valid for MotionManager, opens the Motor PropertyManager page; MotionManager toolbar > Motor |
| swCommands_LinearPattern | 18; valid for parts with a selected sketch; Features toolbar > Linear Pattern |
| swCommands_LinearSketchPattern | 172; valid for an open sketch; Sketch toolbar > Linear Sketch Pattern |
| swCommands_LinearSpring | 444; valid for MotionManager, opens the Motor PropertyManager page; MotionManager toolbar > Spring |
| swCommands_LineColor | 141; valid for drawings and selected sketches; Line Format toolbar > Line Color |
| swCommands_LineFormats | 481; alternative to swCommands_Toolbar_Lineformat; View menu > Toolbars > Line Format |
| swCommands_LineStyle | 143; valid for drawings and selected sketches; Line Format toolbar > Line Style |
| swCommands_LineThickness | 142; valid for drawings and selected sketches; Line Format toolbar > Line Thickness |
| swCommands_Link_Dims | 1543; valid for sketches with dimensions, opens the Shared Values dialog; in the graphics area, dimension RMB menu > Link Values |
| swCommands_LinkViews | 553; valid for two or more viewport views; Standard Views toolbar > Link Views or Window menu > Viewport > Link Views |
| swCommands_List_Body_References | 2803; valid for a selected body in a part, opens the References for body dialog |
| swCommands_List_Comp_References | 2802; valid for a selected component in an assembly, opens the References for comp dialog |
| swCommands_List_Edge_References | 2806; valid for a selected edge in a part, opens the References for Edge dialog |
| swCommands_List_Exportents | 1080; valid for parts with named entities, opens the Named Entities dialog; in the FeatureManager design tree, top_level_part RMB menu > List Named Entities |
| swCommands_List_Extrefs | 1055; valid for parts and assemblies with external references, opens the External References For dialog; FeatureManager design tree > Assembly RMB menu > List External Refs |
| swCommands_List_Face_References | 2805; valid for a selected face in a part, opens the References for Face dialog |
| swCommands_List_Feat_References | 2804; valid for a selected feature in a part, opens the References for feat dialog |
| swCommands_List_Vert_References | 2807; valid for a selected vertex in a part, opens the References for Vertex dialog |
| swCommands_LiveSectionFitToPart | 2844; valid for models with a live section plane; in the graphics area, live_section_plane RMB menu > Fit To Part |
| swCommands_LiveSectionReset | 2845; valid for models with a live section plane; in the graphics area, live_section_plane RMB menu > Reset |
| swCommands_LiveSectionTriadHide | 2847; valid for models with a live section plane; in the graphics area, live_section_plane RMB context toolbar > Show Triad |
| swCommands_LiveSectionTriadShow | 2846; valid for models with a live section plane; in the graphics area, live_section_plane RMB context toolbar > Hide Triad |
| swCommands_Lock_Bom | 918; valid for a drawing view with an Excel-based Bill of Materials; in the graphics area, BOM_table RMB menu > Anchor > Lock to Anchor |
| swCommands_Lock_Configuration | 1847; valid in a PDM-enabled environment with an unlocked configuration; in ConfigurationManager, unlocked_config RMB menu > Lock Configuration |
| swCommands_Lock_Unlock_Focus | 2617; valid for drawings; in the graphics area or the FeatureManager design tree, drawing_view RMB menu > Lock View Focus or Unlock View Focus |
| swCommands_Lock_Unlock_Focus_Double_Click | 2618; valid for drawings; in the graphics area or the FeatureManager design tree, drawing_view RMB menu > double click |
| swCommands_LockViewPlane | 3436; valid for assemblies displaying a section view; graphics area RMB > Lock View |
| swCommands_LoftedBend | 406; valid for sheet metal parts; Sheet Metal toolbar > Lofted-Bend |
| swCommands_LoftedBossBase | 25; valid for parts with a selected sketch; Features toolbar > Lofted Boss/Base |
| swCommands_LoftedCut | 82; valid for parts with a selected sketch; Features toolbar > Lofted Cut |
| swCommands_LoftedSurface | 107; valid for parts; Surfaces toolbar > Lofted Surface |
| swCommands_LoopDve | 3098; valid for a selected plane, planar face, or edge on a part, opens the Path PropertyManager page |
| swCommands_Machined_Parts_Costing | 3028; SOLIDWORKS Costing task pane > Machining Costing |
| swCommands_Macros | 482; alternative to swCommands_Toolbar_Macro; View menu > Toolbars > Macro |
| swCommands_MagnetLine | 3007; valid for drawings with a selected start point for a magnetic line with which to align balloons; Annotation toolbar > Magnetic Line |
| swCommands_Make_Edit_Sketch | 3419; converts the selected reference sketch to an edit sketch; RMB menu > Make Edit Sketch |
| swCommands_Make_Lightweight | 1202; valid for assemblies with a resolved component; in the FeatureManager design tree, resolved_component RMB menu > Set to Lightweight |
| swCommands_Make_Reference_Sketch | 3420; converts the selected edit sketch to a reference sketch; RMB menu > Make Reference Sketch |
| swCommands_Make_Resolved | 1203; valid for assemblies with a lightweight component; in the FeatureManager design tree, lightweight_component RMB menu > Set to Resolved |
| swCommands_Make_Suppressed | 1204; valid for one or more selected components in an assembly |
| swCommands_Make_Trim_As_Construction | 3331; valid when the Trim PropertyManager is active, graphics area RMB menu > Keep trimmed entities as construction geometry |
| swCommands_MakeAssemblyFromPartAssembly | 462; opens the Begin Assembly PropertyManager page; Standard toolbar > Make Assembly From Part/Assembly |
| swCommands_MakeBlock | 469; Blocks toolbar > Make Block |
| swCommands_MakeDrawingFromPartAssembly | 461; opens the Sheet Format/Size dialog to create a drawing; Standard toolbar > Make Drawing from Part/Assembly |
| swCommands_MakeSmartComponent | 563; valid for assemblies, opens the Smart Component PropertyManager page; Assembly toolbar > Make Smart Component |
| swCommands_MakeVirtualCompIndependent | 3494; Makes the selected virtual assembly component independent; in the FeatureManager design tree, right-click a virtual assembly component and select Make Independent |
| swCommands_Manage_Equations | 3040; opens the Equations, Global Variables, and Dimensions dialog; in the FeatureManager design tree, Equations RMB menu > Manage Equations |
| swCommands_Manual_Viewlabel | 2073; valid for drawings with a selected view location label; in the graphics area, location_label RMB menu > Manual View Label Text |
| swCommands_Mark_LDR_Config | 3204; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark the configurations to display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark menu |
| swCommands_Mark_LDR_ConfigActive | 3206; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark the active configuration for display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark > Add Large Design Review Mark for This Configuration |
| swCommands_Mark_LDR_ConfigAll | 3207; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark all of the configurations for display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark > Add Large Design Review Mark for All Configurations |
| swCommands_Mark_LDR_ConfigOff | 3205; valid for an assembly opened in Resolved or Lightweight mode, allows the user to unmark a configuration to prevent its display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark > Remove Large Design Review Mark |
| swCommands_Mark_LDR_ConfigSpecific | 3208; valid for an assembly opened in Resolved or Lightweight mode, allows the user to mark a specific configuration to display when the assembly is opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark > Add Large Design Review Mark for Specified Configurations |
| swCommands_Mark_Smart_Fastener_Uptodate | 2464; valid only for Toolbox add-ins and an assembly with a selected Smart Fastener; in FeatureManager design tree, smart_fastener_feature RMB menu > Mark up to date |
| swCommands_Mark_Smart_Insert_Uptodate | 1857; valid only for Toolbox add-ins and an assembly with a Smart Insert that needs to be updated; in the graphics area, RMB menu > Update Smart Insert |
| swCommands_MassProperties | 343; Tools toolbar > Mass Properties |
| swCommands_Mate | 90; valid for assemblies with two or more selected components to mate; Assembly toolbar > Mate |
| swCommands_Mate_Cancel | 698; Add Mate dialog resource Undo |
| swCommands_Mate_Delete | 2517; valid in the assembly Mate PropertyManager page for a selected mate; Mates tab > Mate Selections > mate RMB menu > Delete |
| swCommands_Mate_Preview | 702; Add Mate dialog resource Preview |
| swCommands_MateReference | 160; valid for parts with a selected sketch; Features toolbar > Reference Geometry > Mate Reference or Reference Geometry toolbar > Mate Reference |
| swCommands_Mating_Component | 3305; applies dimensions and tolerances on target based on source component; DimXpert toolbar > Auto Pair Tolerance |
| swCommands_MBD | 3140; View menu > Toolbars > SOLIDWORKS MBD |
| swCommands_MBD_Load_Unload | 3185; SOLIDWORKS Add-ins toolbar > SOLIDWORKS MBD SNL |
| swCommands_MBD_Template_Editor | 3142; SOLIDWORKS MBD toolbar > 3D PDF Template Editor |
| swCommands_Measure | 92; opens the Measure dialog; Tools toolbar > Measure |
| swCommands_Measure_Csys | 2104; Measure dialog > XYZ Relative To |
| swCommands_Measure_History | 3066; Measure dialog > Measurement History |
| swCommands_Measure_Minmax | 2101; valid for the Measure dialog if Point-to-Point is not selected; Measure dialog > Arc/Circle Measurements |
| swCommands_Measure_Proj | 2100; Measure dialog > Projected On |
| swCommands_Measure_Proj_None | 2108; valid for the Measure dialog; Projected On > None |
| swCommands_Measure_Proj_Plane | 2110; valid for the Measure dialog; Projected On > Select Face/Plane |
| swCommands_Measure_Proj_Recent | 2111; valid for the Measure dialog; Projected On > no selection |
| swCommands_Measure_Proj_Screen | 2109; valid for the Measure dialog; Projected On > Screen |
| swCommands_Measure_PtoP | 3065; Measure dialog > Point-to-Point |
| swCommands_Measure_Showcallouts | 2398; valid if Measure dialog > Show XYZ Measurements is selected and an entity is selected; in the graphics area, measurement callout RMB menu > Show XYZ dimensions and associated geometry |
| swCommands_Measure_Units | 2102; opens the Measure Units/Precision dialog; Measure dialog > Units/Precision |
| swCommands_Measure_Xyz | 2103; Measure dialog > Show XYZ Measurements |
| swCommands_Midpointline | 3118; Sketch toolbar > Midpoint Line |
| swCommands_MidpointSnap | 523; valid for sketches; Quick Snaps toolbar > Midpoint Snap |
| swCommands_MidSurface | 117; valid for parts with offset face pairs, opens the MidSurface1 PropertyManager page; Surfaces toolbar > Mid-Surface |
| swCommands_Mirrcmd_Browse | 1687; valid if the Mirror Components PropertyManager page is open, opens the Choose File dialog; Mirror Components > Step 3: Opposite Hand > Opposite Hand Versions > Create new files > browse_button |
| swCommands_Mirrcmd_Copy_All_Instances | 1686; valid for a selected subassembly and an open Mirror Components PropertyManager page; Mirror Components > Step 2: Set Orientation > Orient Components > top_level_comp RMB menu > Copy All Instances |
| swCommands_Mirrcmd_Mirror_All_Children | 1683; valid for a selected subassembly and an open Mirror Components PropertyManager page; Mirror Components > Step 2: Set Orientation > Orient Components > top_level_comp RMB menu > Mirror All Children |
| swCommands_Mirrcmd_Mirror_All_Instances | 1684; valid for a selected subassembly and an open Mirror Components PropertyManager page; Mirror Components > Step 2: Set Orientation > Orient Components > top_level_comp RMB menu > Mirror All Instances |
| swCommands_Mirror | 83; valid for parts with a selected sketch; Features toolbar > Mirror or for assemblies with a selected assembly feature, opens the Mirror PropertyManager page ; Insert > Assembly Feature > Mirror |
| swCommands_MirrorEntities | 61; valid for an open sketch, opens the Mirror PropertyManager page; Sketch or Layout Tools toolbar > Mirror Entities |
| swCommands_MiterFlange | 324; valid for sheet metal parts; Sheet Metal toolbar > Miter Flange |
| swCommands_MixModel_LightWeight | 3322; Assembly toolbar > Set Component to Lightweight |
| swCommands_MixModel_Resolve | 3321; Assembly toolbar > Set Component to Resolved |
| swCommands_ModelItems | 513; valid for drawings; Annotation toolbar > Model Items |
| swCommands_ModelView | 77; valid for drawings, opens the Model View PropertyManager page; Drawing toolbar > Model View |
| swCommands_Modify_Curv_Scale | 646; valid for a selected curve with curvature combs, opens the Curvature Scale PropertyManager page; in the graphics area, curve RMB menu > Modify Curvature Scale |
| swCommands_ModifySketch | 100; valid for selected sketches, opens the Modify Sketch dialog; Sketch toolbar > Modify Sketch |
| swCommands_MoldflowxpressAnalysisWizard | 414; runs the MoldflowXpress Analysis Wizard, if the product is available |
| swCommands_Molds | 483; alternative to swCommands_Toolbar_Mold; View menu > Toolbars > Mold Tools |
| swCommands_MostRecentlyUsed_File1 | 3365; opens file 1 in File > Open Recent |
| swCommands_MostRecentlyUsed_File10 | 3374; opens file 10 in File > Open Recent |
| swCommands_MostRecentlyUsed_File11 | 3375; opens file 11 in File > Open Recent |
| swCommands_MostRecentlyUsed_File12 | 3376; opens file 12 in File > Open Recent |
| swCommands_MostRecentlyUsed_File13 | 3377; opens file 13 in File > Open Recent |
| swCommands_MostRecentlyUsed_File14 | 3378; opens file 14 in File > Open Recent |
| swCommands_MostRecentlyUsed_File15 | 3379; opens file 15 in File > Open Recent |
| swCommands_MostRecentlyUsed_File16 | 3380; opens file 16 in File > Open Recent |
| swCommands_MostRecentlyUsed_File2 | 3366; opens file 2 in File > Open Recent |
| swCommands_MostRecentlyUsed_File3 | 3367; opens file 3 in File > Open Recent |
| swCommands_MostRecentlyUsed_File4 | 3368; opens file 4 in File > Open Recent |
| swCommands_MostRecentlyUsed_File5 | 3369; opens file 5 in File > Open Recent |
| swCommands_MostRecentlyUsed_File6 | 3370; opens file 6 in File > Open Recent |
| swCommands_MostRecentlyUsed_File7 | 3371; opens file 7 in File > Open Recent |
| swCommands_MostRecentlyUsed_File8 | 3372; opens file 8 in File > Open Recent |
| swCommands_MostRecentlyUsed_File9 | 3373; opens file 9 in File > Open Recent |
| swCommands_Move_Down_Using_Arrow_Key | 2001; VK_DOWN; shift-control-down arrow key |
| swCommands_Move_Dve_Resume_Drag | 1464; valid for collision detection and dynamic clearance list boxes in the Move Component PropertyManager page; RMB menu > Resume Drag |
| swCommands_Move_Left_Using_Arrow_Key | 2002; VK_LEFT; shift-control-left arrow key |
| swCommands_Move_Right_Using_Arrow_Key | 2003; VK_RIGHT; shift-control-left arrow key |
| swCommands_Move_Show_Delta_Xyz | 1135; valid after component RMB menu > Move with Triad command in an assembly; in the graphics area, triad_center_ball RMB menu > Show Translate Delta XYZ Box |
| swCommands_Move_Show_Xyz | 1142; valid after component RMB menu > Move with Triad command in an assembly; in the graphics area, triad_center_ball RMB menu > Show Translate XYZ Box |
| swCommands_Move_Up_Using_Arrow_Key | 2000; VK_UP; shift-control-up arrow key |
| swCommands_MoveComponent | 20; valid for assemblies, opens the Move Component PropertyManager page; in the graphics area, RMB menu > Move Component |
| swCommands_MoveCopyBodies | 408; valid for multibody parts; Features toolbar > Move/Copy Bodies |
| swCommands_MoveEntities | 502; valid for an open sketch, opens the Move PropertyManager page; Sketch toolbar > Move Entities |
| swCommands_MoveSizeFeatures | 386; valid for parts; Features toolbar > Instant3D |
| swCommands_MultiJogLeader | 367; valid for drawings; Annotation toolbar > Multi-jog Leader |
| swCommands_Near_Stack_Smart_Fastener | 2454; valid for a Smart Hole Fastener in an assembly; smart_hole_fastener_tree_item RMB > Top stack |
| swCommands_NearestSnap | 520; valid for sketches; Quick Snaps toolbar > Nearest Snap |
| swCommands_New | 1; File menu > New ; Standard toolbar > New |
| swCommands_New_Display_State | 2129; Visual Overlay dialog toolbar > New Display State |
| swCommands_New_Subassembly | 1258; valid for assemblies; in the FeatureManager design tree, top_level_assembly RMB menu > Insert New Subassembly |
| swCommands_New_Toolbar_Sel_Filter | 1177; alternative to swCommands_SelectionFilters; View menu > Toolbars > Selection Filter |
| swCommands_New_View | 1231; opens a Named View dialog; View toolbar > View Orientation > New View |
| swCommands_NewAssembly | 295; valid for assemblies; Assembly toolbar > New Assembly |
| swCommands_NewMacro | 573; opens the Save As dialog; Macro toolbar > New Macro |
| swCommands_NewMacroButton | 272; creates custom macros, swCommands_UserMacro01 - swCommands_UserMacro98; Macro toolbar > New Macro Button |
| swCommands_NewPart | 91; valid for assemblies with a selected face or plane; Assembly toolbar > New Part |
| swCommands_NewWindow | 580; Window menu > New Window ; Standard toolbar > New Window |
| swCommands_NextCmdMgrTab | 3046; navigates to the next CommandManager tab |
| swCommands_NoBends | 139; valid for sheet metal parts; Sheet Metal toolbar > No Bends |
| swCommands_NoCommand | -3; no command is running |
| swCommands_NoExternalReferences | 578; valid for assemblies; Assembly toolbar > No External References |
| swCommands_NormalTo | 169; View toolbar > View Orientation > Normal To |
| swCommands_NoSolveMove | 171; valid for parts; Sketch toolbar > No Solve Move |
| swCommands_Note | 36; opens the Note PropertyManager page; Annotation toolbar > Note |
| swCommands_NoteCPat | 2994; opens the Circular Note Pattern PropertyManager page; Annotation toolbar > Circular Note Pattern |
| swCommands_NoteLPat | 2993; opens the LinearNote Pattern PropertyManager page; Annotation toolbar > Linear Note Pattern |
| swCommands_Number | 539; valid for selected text; Formatting toolbar > Number |
| swCommands_Numeric_Input_Toggle | 3029; Sketch toolbar > Sketch Numeric Input |
| swCommands_Nx_Rmb_Auto_Ok | 2744; valid if SelectionManager is open; in the graphics area, RMB menu > Auto-OK Selections |
| swCommands_Nx_Rmb_Cancel | 2736; valid if SelectionManager is open; in the graphics area, RMB menu > Cancel |
| swCommands_Nx_Rmb_Clear_All | 2737; valid if SelectionManager is open with multiple selections; in the graphics area, RMB menu > Clear All |
| swCommands_Nx_Rmb_Ok | 2735; valid if SelectionManager is open and with multiple selections; in the graphics area, RMB menu > OK |
| swCommands_Nx_Rmb_Push_Pin | 2743; valid if SelectionManager is open; in the graphics area, RMB menu > Pin Dialog |
| swCommands_Nx_Rmb_Sel_Closed_Loop | 2741; valid if SelectionManager is open; in the graphics area, RMB menu > Select Closed Loop |
| swCommands_Nx_Rmb_Sel_Group | 2739; valid if SelectionManager is open; in the graphics area, RMB menu > Select Group |
| swCommands_Nx_Rmb_Sel_Open_Loop | 2740; valid if SelectionManager is open; in the graphics area, RMB menu > Select Open Loop |
| swCommands_Nx_Rmb_Sel_Region | 2742; valid if SelectionManager is open; in the graphics area, RMB menu > Select Region |
| swCommands_Nx_Rmb_Sel_Regular | 2738; valid if SelectionManager is open; in the graphics area, RMB menu > Select |
| swCommands_Nx_Sel_Clear_All | 2722; SelectionManager dialog > Clear |
| swCommands_Nx_Sel_Group | 2721; SelectionManager dialog > Select Group |
| swCommands_Nx_Sel_Loop | 2720; SelectionManager dialog > Select Closed Loop |
| swCommands_Nx_Sel_Open_Loop | 2723; SelectionManager dialog > Select Open Loop |
| swCommands_Nx_Sel_Region | 2724; SelectionManager dialog > Select Region |
| swCommands_Nx_Sel_Regular | 2725; SelectionManager dialog > Standard Selection |
| swCommands_Nx_Select_Manager | 2718; opens the SelectionManager dialog which is valid only during creation of loft, sweep, and boundary surface features and path mates; in the graphics area, RMB menu > SelectionManager |
| swCommands_Nx_Select_Manager_End | 2719; valid if SelectionManager is open during creation of loft, sweep, and boundary surface features and path mates; in the active PropertyManager page list box, RMB menu > End SelectionManager |
| swCommands_Object_Displayasicon | 799; valid for an embedded OLE object; Edit menu > Object > Display as Icon |
| swCommands_Object_Displaycontent | 798; valid for an embedded OLE object; Edit menu > Object > Display Content |
| swCommands_Object_Popup_Menu | 672; embedded OLE object popup menu |
| swCommands_Object_Resetsize | 800; valid for an embedded OLE object; Edit menu > Object > Reset Size |
| swCommands_OfficeAddin3dExperienceMarketPlace | 3328; loads or unloads the 3DEXPERIENCE Marketplace add-in; Standard toolbar > 3DEXPERIENCE Marketplace |
| swCommands_OfficeButtonFlowSimulation | 3146; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Flow Simulation |
| swCommands_OfficeButtonInspection | 3148; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Inspection |
| swCommands_OfficeButtonPlastics | 3147; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Plastics |
| swCommands_OfficeButtonTolAnalyst | 2894; SOLIDWORKS Add-ins toolbar > TolAnalyst |
| swCommands_Offset_Dim_Text | 1607; valid for drawings with a selected dimension text; in the graphics area, dimension_text RMB menu > Display Options > Offset Text |
| swCommands_OffsetEntities | 76; valid for a selected face, edge, curve, or sketch entity in a part or assembly; Layout Tools or Sketch toolbar > Offset Entities |
| swCommands_OffsetOnSurface | 3190; opens the Offset On Surface PropertyManager page; Sketch toolbar > Offset On Surface |
| swCommands_Ok | 766; OK in dialogs |
| swCommands_Ok_Command | 3042; Standard toolbar > OK |
| swCommands_Ole_Edit | 1675; valid for a selected embedded OLE object; RMB menu > Edit with tool_name |
| swCommands_Ole_Property_Sheet | 1500; valid for a selected embedded OLE object, opens the OLE Object Property dialog; RMB menu > Properties |
| swCommands_On_Demand_Maufacturing | 3499; Opens 3DEXPERIENCE Make in the SOLIDWORKS Task Pane. Make provides instant quotes for your parts and connects you with manufacturing service providers; only valid if 3DEXPERIENCE Marketplace Add-in is loaded and logged into; Tools toolbar > On Demand Manufacturing |
| swCommands_On_Hide_Cosmetic_Welds | 2998; valid for a weldment part with a visible weld bead feature and a selected Weld Folder; in the FeatureManager design tree, Weld Folder RMB menu > Hide Cosmetic Welds |
| swCommands_On_Hold_Cosmetic_Welds_Rebuild | 3127; valid for a weldment part with a weld bead feature and a selected Weld Folder; in the FeatureManager design tree, Weld Folder RMB menu > Suspend Automatic Rebuild |
| swCommands_On_Rebuild_Cosmetic_Welds | 3128; valid for a weldment part with a weld bead feature and a selected Weld Folder; in the FeatureManager design tree, Weld Folder RMB menu > Rebuild Welds |
| swCommands_On_Screen_Dim_Dialog | 3488; For a selected drawing dimension, opens an on-screen dimension dialog that mirrors the Dimension Text section of the Dimension PropertyManager |
| swCommands_On_Show_Cosmetic_Welds | 2997; valid for a weldment part with a hidden weld bead feature and a selected Weld Folder; in the FeatureManager design tree, Weld Folder RMB menu > Show Cosmetic Welds |
| swCommands_Online_Familytable_Closed | 3417 |
| swCommands_OnViewCenterOfMassSymbol | 3059; View toolbar > Hide/Show Items > View Center of Mass |
| swCommands_Open | 0; File menu > Open; Standard toolbar > Open |
| swCommands_Open_Assembly | 3009; valid for a drawing view with a selected assembly; in the FeatureManager design tree, drw_view_assem RMB menu > Open Assembly |
| swCommands_Open_Associated_Drw | 2458; valid for a selected model, opens the Open dialog; in the FeatureManager design tree, model RMB context toolbar > Open Drawing |
| swCommands_Open_Bookmark_Editor | 3515; valid only in SOLDWORKS Connected, accesses the Bookmark Editor; Lifecycle and Collaboration toolbar > Add to Bookmark > Open Bookmark Editor |
| swCommands_Open_Comp_Assem_File | 1377; valid for a selected component in a drawing, opens the component file |
| swCommands_Open_Comp_File | 970; valid for a selected component in an assembly; in the FeatureManager design tree, selected_comp RMB context toolbar > Open Part |
| swCommands_Open_Detailing_Drw | 3497; opens drawing in detailing mode; Standard toolbar > Open Drawing in Detailing Mode |
| swCommands_Open_LightWeight | 3039; valid for assemblies opened in Large Design Review mode; Assembly toolbar > Open in Lightweight |
| swCommands_Open_Part | 3008; valid for a drawing view with a selected component; in the FeatureManager design tree, drw_view_comp RMB toolbar > Open Part |
| swCommands_Open_Partdrawg_For_Drawing | 3503; Opens the drawing for the selected part or assembly in the drawing; In a drawing view, RMB on a part or assembly > Open Drawing |
| swCommands_Open_Sub_Assembly | 3011; valid for a drawing of an assembly with subassemblies; in the graphics area, face_or_edge RMB context toolbar > Open Subassembly |
| swCommands_OpenCollaborativeTask | 3534; valid only in SOLIDWORKS Connected, opens the Collaborative Tasks app in the SOIDWORKS Task Pane; Lifecycle and Collaboration toolbar > Open Collaborative Task |
| swCommands_OpenFromPC | 3495; Opens a dialog to select a document on this PC to open in SOLIDWORKS Power-By; File > Open from This PC... |
| swCommands_OpenInternetAddress | 130; opens the Open Internet Address dialog; Web toolbar > Open Internet Address |
| swCommands_Option_Relations_Snaps | 2169; opens the Relations/Snaps page of the System Options dialog for a selected sheet or drawing view in a drawing; in the FeatureManager design tree, sheet RMB menu > Relations/Snaps Options |
| swCommands_Options | 342; opens the System Options dialog; Standard toolbar > Options |
| swCommands_OrdinateDimension | 346; valid for an open sketch; Dimensions/Relations toolbar > Ordinate Dimension |
| swCommands_Orient_Annotation_By_Selection | 2216; valid for a selected linear radial dimension; in the graphics area, lin_radial_dim RMB menu > Display Options > Orientation > By Selection |
| swCommands_Orient_Annotation_View | 2442; valid for parts and assemblies with a selected active annotation view; in the FeatureManager design tree, active_anno_view RMB menu > Orient |
| swCommands_Page_Setup | 975; File menu > Page Setup |
| swCommands_Pan | 330; View toolbar > Pan |
| swCommands_Parabola | 151; Sketch toolbar > Parabola |
| swCommands_Parallelogram | 294; opens the Rectangle PropertyManager page; Sketch tools > Parallelogram |
| swCommands_ParallelSnap | 526; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > Parallel Snap |
| swCommands_Parent_Child_Rel | 806; valid for a selected item in the FeatureManager design tree, opens the Parent/Child Relationships dialog; in the FeatureManager design tree, tree_item RMB menu > Parent/Child |
| swCommands_PartialEllipse | 86; valid for a selected plane, planar face, or edge on which to create a partial elliptical sketch: Sketch toolbar > Partial Ellipse |
| swCommands_PartingLines | 445; valid for parts; Mold Tools toolbar > Parting Lines |
| swCommands_PartReviewer | 3058; valid for parts; Tools toolbar > Part Reviewer |
| swCommands_Paste | 585; valid for a non-empty clipboard; Standard toolbar > Paste |
| swCommands_Paste_Appearance | 3054; valid for a selection after an appearance has been copied; Render Tools or View toolbar > Paste Appearance |
| swCommands_PathLengthDimension | 3096; valid for an open sketch with selected entities that are end-to-end coincident and form a single chain, opens the Path Length PropertyManager page; Dimensions/Relations toolbar > Path Length Dimension |
| swCommands_PatternStructConnection | 3509; Opens the Pattern Connection Element to Corners PropertyManager; SOLIDWORKS Menu > Insert > Structure System > Pattern Connection Element to Corner |
| swCommands_Pe_Newsgroup | 1948; valid on the SOLIDWORKS Personal Edition Help menu |
| swCommands_PerimeterCircle | 545; valid for a selected plane, planar face, or edge, opens the Circle PropertyManager page; Sketch or Layout Tools toolbar > Perimeter Circle |
| swCommands_PerpendicularSnap | 527; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > Perpendicular Snap |
| swCommands_Perspective | 349; valid for parts and assemblies; View toolbar > View Settings > Perspective |
| swCommands_Pick_Identicalcomponents | 3186; valid for assemblies with a selected component; Tools menu > Component Selection > Select Identical Components |
| swCommands_PickMode | 345; places the model in pick mode; Sketch or Standard toolbar > Select |
| swCommands_Pin_Orientation_Dialog | 2838; valid after View toolbar > View Orientation > More Options > Orientation dialog; Pin/Unpin the dialog |
| swCommands_Pipe_Route | 2270; valid for the SOLIDWORKS Routing add-in, displays the Piping toolbar; Routing Tools toolbar > Piping |
| swCommands_Pipe_Rt_Properties | 2257; valid for the SOLIDWORKS Routing add-in and an open piping assembly; Piping toolbar > Route Properties |
| swCommands_Piping_Custom_Pipe_Config | 1353; valid for a selected reducer route component in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, reducer_route_comp RMB menu > Create Custom Pipe Configuration |
| swCommands_Piping_Make_Flange_Driven | 1356; valid for a selected fitting in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, comp RMB menu > Constrain Fitting to Sketch |
| swCommands_Piping_Make_Flange_Driving | 1355; valid for a selected fitting in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, comp RMB menu > Constrain Sketch to Fitting |
| swCommands_Piping_Standard_Pipe_Config | 1354; valid for a selected reducer route component in a custom pipe configuration in a piping drawing or the Input folder of a piping assembly; in the FeatureManager design tree, reducer_route_comp RMB menu > Use Standard Pipe\Tube Configuration |
| swCommands_Plane | 554; valid for a selected reference in a part, opens the Sketch Plane PropertyManager page; Sketch toolbar > Plane |
| swCommands_PlasticsPremium | 3493; SOLIDWORKS Plastics Premium |
| swCommands_PlasticsPro | 3492; SOLIDWORKS Plastics Professional |
| swCommands_PlasticsStd | 3491; SOLIDWORKS Plastics Standard |
| swCommands_PLM_Gen_Derived_Output_Number | 3483; SOLIDWORKS Connected only; Allows you to generate derived output for a selected object; MySession widget > Action Bar > Tools > Generate Derived Output or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Generate Derived Output |
| swCommands_PLM_Maturity | 3476; for SOLIDWORKS Connected only, changes the maturity state of a selected object; MySession widget > Action Bar > Lifecycle > Maturity or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Maturity |
| swCommands_PLM_Move_to | 3478; SOLIDWORKS Connected only; Allows you to move a selected object to another collaborative space and/or organization and change its owner; MySession widget > Action Bar > Lifecycle > Move To or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Move To |
| swCommands_PLM_New_Revision | 3477; SOLIDWORKS Connected only; Allows you to create a new revision of a selected object and refresh local information to reflect the new revision; MySession widget > Action Bar > Lifecycle > New Revision or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > New Revision |
| swCommands_PLM_Properties | 3479; SOLIDWORKS Connected only; Displays the 3DEXPERIENCE properties of the selected object; MySession widget > Action Bar > View > Properties or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > PLM Properties |
| swCommands_PLM_Relations | 3480; SOLIDWORKS Connected only; Displays the ecosystem of the related objects by navigating on relationships and paths; MySession widget > Action Bar > Tools > Relations or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Relations |
| swCommands_PLM_Reload_fromServer | 3474; SOLIDWORKS Connected only; Updates the selected revision in a session with the latest version that exists in 3DEXPERIENCE; MySession widget > Action Bar > Lifecycle > Reload from Server or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Reload from Server |
| swCommands_PLM_Replace_By_Revision | 3475; SOLIDWORKS Connected only; Opens the Replace by Revision dialog box to replace the revision that is open in the session; MySession widget > Action Bar > Lifecycle > Replace by Revision or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Replace by Revision |
| swCommands_PLM_Replace_Content | 3481; SOLIDWORKS Connected only; Opens the File Selection Box in which you can select an object to replace a pre-selected object; MySession widget > Action Bar > Tools > Replace Content or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Replace Content |
| swCommands_PLM_Reserve | 3472; SOLIDWORKS Connected only; Reserves the selected object; MySession widget > Action Bar > Lifecycle > Reserve or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Reserve |
| swCommands_PLM_Set_Ent_Item_Number | 3482; SOLIDWORKS Connected only; Opens the Set Enterprise Item Number dialog box where you can enter the enterprise item number for parts and assemblies; MySession widget > Action Bar > Tools > Set Enterprise Item Number or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Set Enterprise Item Number |
| swCommands_PLM_Unreserve | 3473; SOLIDWORKS Connected only; Removes the reservation of the selected object; MySession widget > Action Bar > Lifecycle > Unreserve or SOLIDWORKS menu bar > Tools > Lifecycle and Collaboration > Unreserve |
| swCommands_PmCancel | -1; valid on PropertyManager pages; Cancel |
| swCommands_PmOK | -2; valid on PropertyManager pages; OK |
| swCommands_Point | 72; valid for a selected plane, planar face, or edge; Sketch toolbar > Point |
| swCommands_PointSnap | 521; valid for sketches; Quick Snaps toolbar > Point Snap |
| swCommands_Polygon | 305; valid for a selected plane, planar face, or edge, opens the Polygon PropertyManager page; Sketch tools > Polygon |
| swCommands_Popup_Hide_Component | 812; valid for a selected, visible component; RMB menu > Hide Component |
| swCommands_Popup_Hide_Hidden | 810; valid for a selected feature with visible edges; RMB menu > Hide Hidden Edges |
| swCommands_Popup_Show_Component | 811; valid for a selected, hidden component; RMB menu > Show Component |
| swCommands_Popup_Show_Hidden | 808; valid for a selected feature with hidden edges; RMB menu > Show Hidden Edges |
| swCommands_Predefined_Add_Model | 2507; valid for a predefined drawing view; predefined_drawing_view RMB menu > Insert Model |
| swCommands_PredefinedView | 428; valid for drawings; Drawing toolbar > Predefined View |
| swCommands_PrevCmdMgrTab | 3047; VK_PRIOR; navigates to the previous CommandManager tab; resource string "Previous CommandManager Tab" |
| swCommands_Preview_Sketch_Dimension_Toggle | 3518; Toggles preview of selected sketch dimension; Sketch toolbar > Preview Sketch Dimension |
| swCommands_PreviousVersionCheck | 3523; launches previous release check dialog to check the model for incompatible features; Tools > Evaluate > Previous Release Check |
| swCommands_PreviousView | 159; valid for models with changed views; View toolbar or View Orientation dialog > Previous View |
| swCommands_PrimaryAdvStructMember | 3336; creates a primary structural member feature by sweeping pre-defined profiles along user-defined paths; Structures toolbar > Primary Structural Member... |
| swCommands_Print | 589; valid for an open document, opens the Print dialog; Standard toolbar > Print |
| swCommands_PrintPreview | 590; Standard toolbar > Print Preview |
| swCommands_ProfileProperties | 3386; creates a predefined pierce point in the weldment profile; Insert > Structure System > Profile Properties |
| swCommands_ProjectCurve | 74; valid for parts with a selected sketch; Features toolbar > Curves > Project Curve |
| swCommands_ProjectedView | 28; valid for a selected drawing view; Drawing toolbar > Projected View |
| swCommands_Propagate_Slots | 3517; Opens Slot Propagation PropertyManager; Propagates slots to a selected instance or all instances of an assembly component containing a tab feature; RMB menu for selected component with tab feature > Propagate Slots... |
| swCommands_Properties | 75; opens a Properties dialog for the current selection; Standard toolbar > Properties |
| swCommands_Properties_Smart_Fastener | 2456; valid for a selected Smart Fastener; smart_fastener RMB menu > Properties |
| swCommands_Publish_3DSwym_3D | 3503; valid only for 3DEXPERIENCE platform/SOLIDWORKS Connected; Tools menu > Lifecycle and Collaboration > Publish to 3DSwym > Share as 3D ; exports the current model as a 3DXML file and publishes it in a 3DSwym community or conversation |
| swCommands_Publish_3DSwym_Picture | 3502; valid only for 3DEXPERIENCE platform/SOLIDWORKS Connected; Tools menu > Lifecycle and Collaboration > Publish to 3DSwym > Share as Picture ; publishes a picture of the current model in a 3DSwym community or conversation |
| swCommands_Publish_Dl_Content | 2758; valid for the Motion Study gantt chart and a selected, suppressed simulation element row; in the MotionManager design tree, rotary_motor_bar RMB menu > Add to Library |
| swCommands_Publish_HomeByMe | 3496; publishes the current document to HomebyMe; Tools toolbar > Publish to HomeByMe... |
| swCommands_Publish_To_Edrawing | 2931; Standard toolbar > Publish eDrawings File |
| swCommands_Publish3DPDF | 3451; SOLIDWORKS MBD toolbar > Publish to 3D PDF |
| swCommands_PublishSTEP242File | 3198; SOLIDWORKS MBD toolbar > Publish STEP 242 File |
| swCommands_PunchTable | 3036; valid for drawings, opens the Punch Table PropertyManager page; Table toolbar > Punch Table |
| swCommands_PushPull | 609; valid for parts, opens the Freeform PropertyManager page; Features toolbar > Freeform |
| swCommands_QuadrantSnap | 537; valid for sketches; Quick Snaps toolbar > Quadrant Snap |
| swCommands_Query_Advanced | 1140; valid for assemblies, opens the Advanced Component Selection dialog; Tools menu > Component Selection > Advanced Select |
| swCommands_Quick_Create_Plane | 1736; valid for a part, opens the Plane PropertyManager page |
| swCommands_Rad_Dim_Diametric | 1570; valid for a part with a selected radial dimension; rad _dim RMB menu > Display Options > Display as Diameter |
| swCommands_Rad_Dim_Lindiamtric | 1571; valid for a part with a selected diameter dimension; diam_dim RMB menu > Display Options > Display as Linear |
| swCommands_Rad_Dim_Radial | 1568; valid for a part with a selected diameter dimension; diam_dim RMB menu > Display Options > Display as Radius |
| swCommands_RapidPrototype | 624; valid for Windows 8.1 or later, opens the Print3D PropertyManager page; Standard toolbar > Print3D |
| swCommands_RapidSketch | 2835; Sketch toolbar > Rapid Sketch |
| swCommands_Re_Jog | 3083; valid for a drawing of a circle or arc with a selected angular running dimension; in the graphics area, angular_running_dimensi on RMB menu > Display Options > Re-Jog Running Dimension |
| swCommands_Read_Only_Pref | 1905; valid in an open file dialog with preview, RMB menu > Open as Read-only |
| swCommands_RealviewGraphics | 499; valid for parts and assemblies; View toolbar > View Settings > RealView Graphics |
| swCommands_RealViewPlusGraphics | 500; valid if enabled in the registry (graphics, RealViewPlus_Enable = 1); View menu > Display > RealView Plus Graphics |
| swCommands_Reattach_Dim | 3521; Re-attaches the selected dangling dimension; RMB click a dimension > Reattach |
| swCommands_Reattach_to_CMarkSet | 3137; valid for a selected dangling center mark in a drawing; in the graphics area, dangling_center_mark RMB menu > Reattach |
| swCommands_Rebuild | 17; Standard toolbar > Rebuild |
| swCommands_RebuildAll | 3200; Standard toolbar > Rebuild All configuration |
| swCommands_RebuildAndSaveConfig | 3060; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, configuration RMB menu > Add Rebuild/Save Mark |
| swCommands_RebuildAndSaveConfigActive | 3; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, top_assembly RMB menu > Rebuild/Save Mark > Add Mark for This Configuration |
| swCommands_RebuildAndSaveConfigAll | 3063; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, top_assembly RMB menu > Rebuild/Save Mark > Add Mark for All Configurations |
| swCommands_RebuildAndSaveConfigOff | 3061; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, configuration RMB menu > Remove Rebuild/Save Mark |
| swCommands_RebuildAndSaveConfigSpecific | 3064; valid for parts and assemblies with multiple configurations, opens the Rebuild and Save Settings dialog; in the ConfigurationManager, top_assembly RMB menu > Rebuild/Save Mark > Add Mark for Specified Configurations |
| swCommands_Recall_Last_Render | 2971; opens the Use perspective Views in Renderings dialog; Render Tools toolbar > Recall Last Render |
| swCommands_RecordPauseMacro | 29; Macro toolbar > Record\Pause Macro |
| swCommands_Rectangle | 79; valid for a part with a selected plane, planar face, or edge, opens the Rectangle PropertyManager page; Sketch or Layout Tools toolbar > Corner Rectangle |
| swCommands_RectangleAtAngle | 2793; valid for a part with a selected plane, planar face, or edge, opens the Rectangle PropertyManager page; Sketch or Layout Tools toolbar > 3 Ponit Corner Rectangle |
| swCommands_Redo | 587; valid for a model for which an Undo action occurred; Standard toolbar > Redo |
| swCommands_Redraw | 355; View toolbar > Redraw |
| swCommands_Ref_Help | 771; Edit Referenced File Locations dialog > Help |
| swCommands_Reference_arrow | 3138; valid for a selected component in an assembly; comp RMB menu context toolbar > Dynamic Reference Visualization (Parent) |
| swCommands_ReferenceGeometry | 484; alternative to swCommands_Toolbar_Refgeom; View menu > Toolbars > Reference Geometry |
| swCommands_RefPlane_Flip_Normal | 3113; valid for a selected reference plane in a part; in the graphics area, ref_plane RMB context toolbar > Flip Normal |
| swCommands_Reimport_From_To_Lst | 2861; valid for a SOLIDWORKS Routing add-in and an assembly to which from-to list was imported; Electrical toolbar > Re-Import From/To |
| swCommands_RelativeView | 27; valid for a drawing with a selected planar face, opens the Relative View PropertyManager page; Drawing toolbar > Relative View |
| swCommands_Reload | 1618; P alette toolbar > Reload |
| swCommands_Remove_Body_Appearance | 2935; valid in a body appearance callout; body_appearance_callout RMB menu context toolbar > This instance |
| swCommands_Remove_Component_Appearance | 2936; valid in a component appearance callout; comp_appearance_callout RMB menu context toolbar > This instance |
| swCommands_Remove_Feature_Appearance | 2934; valid in a feature appearance callout; feature_appearance_callout RMB menu context toolbar > This instance |
| swCommands_Remove_Feature_Dims | 1553; valid for a selected, dimensioned feature; in the FeatureManager design tree, feature RMB menu > HideAll Dimensions |
| swCommands_Remove_From_ChainDim | 3412; valid for a selected dimension in a chain dimension set, makes the selected dimension independent from the chain dimension set; RMB menu > Convert To Chain |
| swCommands_Remove_From_Library | 1525; valid for a selected library feature; in the FeatureManager design tree, lib_feat RMB menu > Remove From Library |
| swCommands_Remove_Mark_LDR_AndPurgeDataForAllConfig | 3209; valid for an assembly opened in Resolved or Lightweight mode, allows the user to unmark the configurations to display for the assembly opened in Large Design Review mode; in the ConfigurationManager, top_level_assembly RMB menu > Large Design Review Mark > Remove Mark and Purge Data for All Configurations |
| swCommands_Remove_Part_Appearance | 2937; valid in a part appearance callout; part_appearance_callout RMB menu context toolbar > This instance |
| swCommands_Remove_Smc_Reference | 2677; valid in Missing Reference list boxes of PropertyManager pages; list_box_item RMB menu > Delete |
| swCommands_Remove_Snap | 1554; valid for a drawing with a selected dimension extension line endpoint configured with a snap option; dim_ext_line_endpt_with_snap RMB menu > Display Options > Default Extension Snap |
| swCommands_RemoveAllDisplayStates | 3037; valid for a part that is not in edit mode; in the ConfigurationManager, white_space RMB menu > Remove all display states |
| swCommands_RemovedSection | 3352; adds a removed section view; Drawing toolbar > Removed Section |
| swCommands_RemoveMarkAndPurgeDataForAllConfig | 3091; valid for parts and assemblies with multiple configurations; in the ConfigurationManager, top_assem bly RMB menu > Rebuild/Save Mark > Remove Mark and Purge Data for All Configurations |
| swCommands_RemoveMateMisalignment | 3327; valid for pre-selected concentric misaligned mate, removes its mate misalignment property; in the FeatureManager design tree, concentric mate RMB menu > Remove misalignment |
| swCommands_Rename_Annotation_View | 3136; valid for a selected annotation view in the Select Annotation View dialog; anno_view RMB menu > Rename |
| swCommands_Render_Options | 2968; Render Tools toolbar > Options |
| swCommands_Render_Region | 3115; Render Tools toolbar > Render Region |
| swCommands_RenderToolbar | 2962; alternative to swCommands_Toolbar_Render; View menu > Toolbars > Render Tools |
| swCommands_Renumber_Hole_Table | 2964; valid for drawings with hole tables; in the FeatureManager design tree, hole_table RMB menu > Renumber all Tags |
| swCommands_Renumber_Series_Table | 2965; valid for a selected row in the TAG column of a drawing hole table; in the graphics area, hole_table_row_tag_column RMB menu > Renumber Series |
| swCommands_Repair_Route | 2289; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Routing Tools toolbar > Repair Route |
| swCommands_RepairSketch | 380; valid only for sketches in edit mode; Sketch toolbar > Repair Sketch |
| swCommands_Repeat_Command | 2114; Edit menu > Repeat Last Command |
| swCommands_Repeat_Mate | 2819; valid for selected components in an assembly, opens the Copy with Mates PropertyManager page; Assembly toolbar > Copy with Mates |
| swCommands_ReplaceComponents | 575; valid for assemblies, opens the Replace PropertyManager page; Assembly toolbar > Replace Components |
| swCommands_ReplaceEntity | 3104; valid for a selected sketch entity in an open sketch, opens the Replace Entity PropertyManager page; Sketch toolbar > Replace Entity |
| swCommands_ReplaceFace | 371; valid for a solid or surface body, opens the Replace Face1 PropertyManager page; Surface toolbar > Replace Face |
| swCommands_ReplaceFormTool | 3024; valid for parts with a Forming Tool, opens the Open dialog; in the FeatureManager design tree, forming_tool RMB menu > Replace Form Tool |
| swCommands_ReplaceMateEntities | 574; valid for a selected Mate Group entity in assemblies; in the FeatureManager design tree, Assembly toolbar > Replace Mate Entities |
| swCommands_Reset | 635; dialog > Reset |
| swCommands_Reset_Dim_Extension_Centerline | 3107; valid for a drawing with a centered dimension extension line; in the graphics area, dim_ext_line RMB menu > Reset Extension Line Style |
| swCommands_Reset_Line_Font | 1575; valid for a selected drawing edge whose line format was changed from the default; in the graphics area, sel_edge RMB menu > Reset line font |
| swCommands_Reset_Std_View | 700; valid after View toolbar > View Orientation > More Options is selected; Orientation dialog > Reset Standard Views |
| swCommands_Resolve_All | 1234; valid for selected assembly with lightweight components; in the FeatureManager design tree, top_level_assy RMB menu > Set Lightweight to Resolved |
| swCommands_Resolve_Conflict | 2192; valid for an open, over-defined sketch, opens the SketchXpert PropertyManager page; Tools menu > Sketch Tools > SketchXPert |
| swCommands_Resolve_Drawing | 3447; valid only for drawings in Detailing mode; FeatureManager design tree root node RMB menu > Resolve drawing or first button in every CommandManager toolbar |
| swCommands_Resolve_Mate_Component_1 | 2532; valid for an assembly with two lightweight mate components, one of which is suppressed; in the FeatureManager design tree, unsuppressed_lightweight_mate_component > Mates in assy_name > constraint_of_suppressed_lightweight_mate_component_1 RMB menu > supp_ltwt_mate_comp_1 > Resolve component |
| swCommands_Resolve_Mate_Component_2 | 2537; valid for an assembly with a mate containing three lightweight mate components, two of which are suppressed; in the FeatureManager design tree, unsuppressed_lightweight_mate_component > Mates in assy_name > constraint_of_suppressed_lightweight_mate_component_2 RMB menu > supp_ltwt_mate_comp_2 > Resolve component |
| swCommands_Resolve_Out_Of_Date_Lwcomps | 1407; valid for a selected assembly with out-of-date lightweight components; top_assy RMB menu > Set out-of-date Lightweight to Resolved |
| swCommands_Resolve_Top | 3034; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, top_assy RMB menu > Set All to Resolved |
| swCommands_Resolve_Top_LightWeight | 3035; valid for a selected assembly opened in Large Design Review mode; in the FeatureManager design tree, top_assy RMB menu > Set All to Lightweight |
| swCommands_Restore_Align | 1513; valid only for a selected drawing view that has been aligned; in the FeatureManager design tree, sel_align_view RMB menu > Alignment > Default Alignment |
| swCommands_Restore_Rotation | 637; valid for a selected drawing view that has been rotated; in the FeatureManager design tree, sel_rot_view RMB menu > Alignment > Default Rotation |
| swCommands_Restore_Settings | 3114; Tools menu > Save/Restore Settings |
| swCommands_Resume_Stacking_Balloons | 676; valid for a selected balloon in a drawing view, opens the Stacked Balloon PropertyManager page; sel_balloon RMB menu > Add to Stack |
| swCommands_Reverse_Endpoint_Tangency | 3304; Sketch toolbar > Reverse Endpoint Tangent |
| swCommands_Review_Pending_Updates | 2989; valid for a selected frozen feature that has updates pending due to the lock, opens a What's Wrong dialog with the pending updates; in the FeatureManager design tree, frozen_feature RMB menu > Review Pending Updates ; resource string "Show all pending updates due to Freeze. Review Pending Updates" |
| swCommands_RevisionCloud | 3052; valid for drawings, opens the Revision Cloud PropertyManager page; Annotation toolbar > Revision Cloud |
| swCommands_RevisionSymbol | 457; valid for a drawing with a revision table with one or more revision rows; Annotation toolbar > Revision Symbol |
| swCommands_RevisionTable | 456; valid for drawings, opens the Revision Table PropertyManager page; Table toolbar > Revision Table |
| swCommands_RevolvedBossBase | 24; valid for parts with a selected sketch; Features toolbar > Revolved Boss/Base |
| swCommands_RevolvedCut | 48; valid for parts with a selected sketch; Features toolbar > Revolved Cut |
| swCommands_RevolvedSurface | 104; valid for a selected profile and the centerline about which to revolve the surface, opens the Surface-Revolve PropertyManager page; Surfaces toolbar > Revolve Surface |
| swCommands_Rib | 125; valid for parts with a selected sketch, opens the Rib1 PropertyManager page; Features toolbar > Rib |
| swCommands_Right | 165; View toolbar > View Orientation > Right |
| swCommands_Rip | 297; valid for sheet metal parts; Sheet Metal toolbar > Rip |
| swCommands_Rip_Both_Directions | 1707; valid when inserting a sheet metal rip; in the graphics area, rip_manipulator RMB menu > Both Directions |
| swCommands_Rip_Single_Direction | 1708; valid when inserting a sheet metal rip; in the graphics area, rip_manipulator RMB menu > Single Direction |
| swCommands_Rmb_Ann_Use_Jog_Leader | 1808; valid for a new drawing annotation; in the graphics area, new_anno RMB menu > Use Multi-jog Leader |
| swCommands_Rmb_Appear_Callout_Delete_Body_Color | 2696; valid for a selected body row in an appearance callout; RMB menu > Remove Color |
| swCommands_Rmb_Appear_Callout_Delete_Body_Texture | 2697; valid for a selected body row in an appearance callout; RMB menu > Remove Texture |
| swCommands_Rmb_Appear_Callout_Delete_Comp_Color | 2698; valid for a selected component row in an appearance callout; RMB menu > Remove Color |
| swCommands_Rmb_Appear_Callout_Delete_Comp_Texture | 2699; valid for a selected component row in an appearance callout; RMB menu > Remove Texture |
| swCommands_Rmb_Appear_Callout_Delete_Face_Color | 2685; valid for a selected face row in an appearance callout; RMB menu > Remove Color |
| swCommands_Rmb_Appear_Callout_Delete_Face_Texture | 2686; valid for a selected face row in an appearance callout; RMB menu > Remove Texture |
| swCommands_Rmb_Appear_Callout_Delete_Feat_Color | 2694; valid for a selected feature row in an appearance callout; RMB menu > Remove Color |
| swCommands_Rmb_Appear_Callout_Delete_Feat_Texture | 2695; valid for a selected feature row in an appearance callout; RMB menu > Remove Texture |
| swCommands_Rmb_Appear_Callout_Delete_Part_Color | 2700; valid for a selected part row in an appearance callout; RMB menu > Remove Color |
| swCommands_Rmb_Appear_Callout_Delete_Part_Texture | 2701; valid for a selected part row in an appearance callout; RMB menu > Remove Texture |
| swCommands_Rmb_Appear_Callout_Edit_Body_Color | 2688; valid for a selected body row in an appearance callout; RMB menu > Edit Color |
| swCommands_Rmb_Appear_Callout_Edit_Body_Texture | 2691; valid for a selected body row in an appearance callout; RMB menu > Edit Texture |
| swCommands_Rmb_Appear_Callout_Edit_Color | 2649; valid for a selected face row in an appearance callout; RMB menu > Edit Color |
| swCommands_Rmb_Appear_Callout_Edit_Comp_Color | 2702; valid for a selected component row in an appearance callout; RMB menu > Edit Color |
| swCommands_Rmb_Appear_Callout_Edit_Comp_Texture | 2703; valid for a selected component row in an appearance callout; RMB menu > Edit Texture |
| swCommands_Rmb_Appear_Callout_Edit_Feat_Color | 2687; valid for a selected feature row in an appearance callout; RMB menu > Edit Color |
| swCommands_Rmb_Appear_Callout_Edit_Feat_Texture | 2690; valid for a selected feature row in an appearance callout; RMB menu > Edit Texture |
| swCommands_Rmb_Appear_Callout_Edit_Part_Color | 2689; valid for a selected part row in an appearance callout; RMB menu > Edit Color |
| swCommands_Rmb_Appear_Callout_Edit_Part_Texture | 2692; valid for a selected part row in an appearance callout; RMB menu > Edit Texture |
| swCommands_Rmb_Appear_Callout_Edit_Texture | 2650; valid for a selected face row in an appearance callout; RMB menu > Edit Texture |
| swCommands_Rmb_Appearance_Co | 2646; valid for a selected face, displays an appearance callout in the graphics area |
| swCommands_Rmb_BiDir | 3383; valid when the Projected Curve PropertyManager is active, graphics area RMB menu > Bi-Directional Projection |
| swCommands_RMB_Blind_Direction_2 | 3072; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, revolve_sketch RMB menu > Direction 2 > Blind |
| swCommands_Rmb_Bodyappearance_Co | 2679; valid for a selected solid body, displays an appearance callout in the graphics area |
| swCommands_Rmb_Collect_All_Bends | 730; valid for sheet metal parts when the Fold PropertyManager page is open; in the graphics area, RMB menu > Collect All Bends |
| swCommands_Rmb_Compappearance_Co | 2680; valid for a selected component, displays an appearance callout in the graphics area |
| swCommands_Rmb_Cpat_Equal_Space | 1660; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, RMB menu > Equal Spacing ; valid only if swCommands_Rmb_Cpat_Symmetric is called |
| swCommands_Rmb_Cpat_Equal_Spacing1 | 3213; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, RMB menu > Equal Spacing Direction 1 ; not valid if swCommands_Rmb_Cpat_Symmetric is called; see swCommands_Rmb_Cpat_Equal_Space |
| swCommands_Rmb_Cpat_Equal_Spacing2 | 3214; valid when a Circular Pattern PropertyManager page is open for a non-dimension circular pattern; in the graphics area, RMB menu > Equal Spacing Direction 2 ; not valid if swCommands_Rmb_Cpat_Symmetric is called; see swCommands_Rmb_Cpat_Equal_Space |
| swCommands_Rmb_Cpat_Flip_Direction | 1667; valid when a Circular Pattern PropertyManager page is open; in the graphics area, RMB menu > Reverse Direction |
| swCommands_Rmb_Cpat_Geometry_Pattern | 1661; valid when a Circular Pattern PropertyManager page is open for a non-dimension, non-body circular pattern in an assembly that is not in edit mode; in the graphics area, RMB menu > Geometry Pattern |
| swCommands_Rmb_Cpat_Symmetric | 3192; valid when a Circular Pattern PropertyManager page is open; in the graphics area, RMB menu > Symmetric |
| swCommands_Rmb_Create_Hole_Series | 2660; valid for a selected assembly Wizard Hole; in the FeatureManager design tree, wizard_hole_feature RMB menu > Create Hole Series |
| swCommands_Rmb_Delete_Manipulator | 2500; valid for a selected manipulator for some dialogs (mold shut-off surface and fillet); RMB menu > Delete |
| swCommands_RMB_Direction_2_OnOff | 3079; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, revolve_sketch RMB menu > Direction 2 > Direction 2 Off |
| swCommands_Rmb_Display_Camera_FOV_Box | 2840; valid for a model with a selected camera in DisplayManager; in the display area, RMB menu > Display Field of View Box |
| swCommands_Rmb_Edit_Camera | 1059; valid for a model with a selected camera in DisplayManager; Camera > Camera1 RMB menu > Edit Camera |
| swCommands_Rmb_Edit_Section | 753; valid for a section view; in the graphics area of a section view, RMB menu > Section View Properties |
| swCommands_Rmb_Edit_SimResults | 3202; opens the View Simulation Results PropertyManager page; valid only if the SOLIDWORKS Simulation add-in is loaded, Simulation study results are available for the current model, View toolbar > View Simulation Results was previously clicked, and the View Simulation Results PropertyManager page was configured to display simulation results with the model; in the graphics area, RMB menu > Simulation Results Properties |
| swCommands_Rmb_Enable_Appear_Callouts | 2704; Appearance Callout dialog > Enable Appearance Callouts |
| swCommands_Rmb_Extend_Distance | 1664; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, surface_extend_sketch RMB menu > Distance |
| swCommands_Rmb_Extend_Upto_Point | 1665; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, surface_extend_sketch RMB menu > Up to Point |
| swCommands_Rmb_Extend_Upto_Surface | 1666; valid when the Surface-Extend1 PropertyManager page is open; in the graphics area, surface_extend_sketch RMB menu > Up to Surface |
| swCommands_Rmb_Face_Zebra_Stripes | 1807; valid for a selected face, opens the Zebra Stripes PropertyManager page; sel_face RMB menu > Zebra Stripes |
| swCommands_Rmb_Featappearance_Co | 2678; valid for a selected feature, displays an appearance callout in the graphics area |
| swCommands_Rmb_Find_Intersection | 3110; use to define virtual sharps; valid for an open sketch while in the dimension tool; in the graphics area, sketch_entity RMB menu > Find Intersection |
| swCommands_Rmb_Iso_Ad_Mesh | 731; valid when the Face Curves PropertyManager page is open, and Position is selected; in the graphics area, RMB menu > Mesh |
| swCommands_Rmb_Iso_Constrain_Model | 733; valid when the Face Curves PropertyManager page is open; in the graphics area, RMB menu > Constrain to Model |
| swCommands_Rmb_Iso_Ignore_Holes | 734; valid when the Face Curves PropertyManager page is open; in the graphics area, RMB menu > Ignore Holes |
| swCommands_Rmb_Iso_Position | 732; valid when the Face Curves PropertyManager page is open, and Mesh is selected; in the graphics area, RMB menu > Position |
| swCommands_Rmb_Leader_Done | 2475; valid for drawings while adding an annotation leader; anno_leader RMB menu > End Leader (double click) |
| swCommands_Rmb_Lock_Camera | 1062; valid when a model is in Camera View mode; in the graphics area, RMB menu > Lock Camera |
| swCommands_Rmb_Loft_Close | 726; valid when the Surface-Loft PropertyManager page is open; in the graphics area, loft_sketch RMB menu > Close Loft |
| swCommands_Rmb_Loft_Mesh_Allfaces1 | 2630; valid when the Boundary-Surface PropertyManager page is open, and two directions are selected; in the graphics area, RMB menu > Mesh Preview > Mesh All Faces |
| swCommands_Rmb_Loft_Mesh_Clear_Allfaces1 | 2632; valid when the Boundary-Surface PropertyManager page is open, two directions are selected, and all faces are meshed; in the graphics area, RMB menu > Mesh Preview > Clear All Meshed Faces |
| swCommands_Rmb_Loft_Mesh_Clear_Oneface1 | 2633; valid when the Boundary-Surface PropertyManager page is open, and a face is meshed; in the graphics area, RMB menu > Mesh Preview > Clear Meshed Faces |
| swCommands_Rmb_Loft_Mesh_Oneface1 | 2631; valid when the Boundary-Surface PropertyManager page is open; in the graphics area, RMB menu > Mesh Preview > Mesh Face |
| swCommands_Rmb_Loft_Show_All | 2525; valid when the Loft PropertyManager page is open, and connectors have been hidden; in the graphics area, RMB menu > Show All Connectors |
| swCommands_Rmb_Loft_Synch_Hide | 2522; valid when the Loft PropertyManager page is open, and a connector is selected; in the graphics area, connector RMB menu > Hide Connector |
| swCommands_Rmb_Loft_Synch_Hide_All | 2524; valid when the Loft PropertyManager page is open; in the graphics area, RMB menu > Hide All Connectors |
| swCommands_Rmb_Loft_Synch_Undo | 2523; valid when the Surface-Loft PropertyManager page is open; in the graphics area, RMB menu > Reset Connectors |
| swCommands_Rmb_Loft_Synch_Undo_Last_Oper | 2611; valid when the Loft PropertyManager page is open, and a connector has been deleted; in the graphics area, RMB menu > Undo connector edit |
| swCommands_Rmb_Loft_Tangency | 724; valid when the Surface-Loft PropertyManager page is open; in the graphics area, loft_sketch RMB menu > Merge tangent faces |
| swCommands_Rmb_Mvsrf_Copy | 746; valid when the Move Face PropertyManager page is open; in the graphics area, RMB menu > Copy |
| swCommands_RMB_OffsetFromSurface_Direction_2 | 3075; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, revolve_sketch RMB menu > Direction 2 > Offset From Surface |
| swCommands_Rmb_Onto_Face | 2473; valid when the Projected Curve PropertyManager page is open, and Projection type is Sketch on sketch; in the graphics area, RMB menu > Sketch onto Face(s) |
| swCommands_Rmb_Onto_Sketch | 2472; valid when the Projected Curve PropertyManager page is open, and Projection type is Sketch on faces; in the graphics area, RMB menu > Sketch onto Sketch |
| swCommands_Rmb_Reverse | 2474; valid when the Projected Curve PropertyManager page is open; in the graphics area, RMB menu > Reverse Projection |
| swCommands_RMB_Reverse_Direction | 3080; valid when the Surface-Revolve PropertyManager page is open; in the graphics area, revolve_sketch RMB menu > Direction 1 > Reverse Direction |
| swCommands_Rmb_Rib_Both_Sides | 1791; valid when the Rib1 PropertyManager page is open; in the graphics area, RMB menu > Both Sides |
| swCommands_Rmb_Rib_First_Side | 1789; valid when the Rib1 PropertyManager page is open; in the graphics area, RMB menu > First Side |
| swCommands_Rmb_Rib_Normal_To_Sketch | 1792; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Parallel to Sketch; in the graphics area, RMB menu > Normal to Sketch |
| swCommands_Rmb_Rib_Parallel_To_Sketch | 1793; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Normal to Sketch; in the graphics area, RMB menu > Parallel to Sketch |
| swCommands_Rmb_Rib_Second_Side | 1790; valid when the Rib1 PropertyManager page is open, and Extrusion direction is Parallel to Sketch; in the graphics area, RMB menu > Second Side |
| swCommands_Rmb_Skcham_Angle | 736; valid when the Sketch Chamfer PropertyManager page is open, and Distance-distance is selected; in the graphics area, RMB menu > Angle-Distance |
| swCommands_Rmb_Skcham_Dist | 735; valid when the Sketch Chamfer PropertyManager page is open, and Angle-distance is selected; in the graphics area, RMB menu > Distance-Distance |
| swCommands_Rmb_Skcham_Equal | 737; valid when the Sketch Chamfer PropertyManager page is open, and Distance-distance is selected; in the graphics area, RMB menu > Equal Distance |
| swCommands_Rmb_Sm_Bend_Revdir | 739; valid when the Sketched Bend PropertyManager page is open; in the graphics area, RMB menu > Reverse Direction |
| swCommands_Rmb_Sm_Reverse_Dir | 738; valid when the Revolve PropertyManager page is open, and Thin Feature is selected; in the graphics area, RMB menu > Reverse Direction (second version) |
| swCommands_Rmb_Spat_Centroid | 1662; valid when a Sketch Driven Pattern PropertyManager page is open, and Reference point is Selected point; in the graphics area, RMB menu > Bounding box center |
| swCommands_Rmb_Spat_Geometry_Pattern | 1663; valid when a Sketch Driven Pattern PropertyManager page is open; in the graphics area, RMB menu > Geometry Pattern |
| swCommands_Rmb_Spat_Selpoint | 1773; valid when a Sketch Driven Pattern PropertyManager page is open, and Reference point is Centroid; in the graphics area, RMB menu > Selected point |
| swCommands_Rmb_Sweep_Align | 729; valid when the Cut-Sweep PropertyManager page is open; in the graphics area, RMB menu > Align with end faces |
| swCommands_Rmb_Sweep_Tangency | 727; valid when the Surface-Sweep PropertyManager page is open; in the graphics area, sweep_sketch RMB menu > Merge tangent faces |
| swCommands_RMB_Throughall_Direction_2 | 3076; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 2 > Through All |
| swCommands_RMB_ThroughNext_Direction_2 | 3077; valid when the Cut-Extrude PropertyManager page is open; in the graphics area, RMB menu > Direction 2 > Up To Next |
| swCommands_RMB_UptoBody_Direction_2 | 3078; valid when the Surface-Extrude PropertyManager page is open; in the graphics area, extrude_sketch RMB menu > Direction 2 > Up To Body |
| swCommands_RMB_UptoSurface_Direction_2 | 3074; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, revolve_sketch RMB menu > Direction 2 > Up To Surface |
| swCommands_RMB_UptoVertex_Direction_2 | 3073; valid when the Surface-Revolve PropertyManager page is open, and Direction 1 is not set to Mid Plane; in the graphics area, revolve_sketch RMB menu > Direction 2 > Up To Vertex |
| swCommands_Rmb_Zebra_Properties | 1761; valid for a model with zebra stripes, opens the Zebra Stripes PropertyManager page; in the graphics area, RMB menu > Zebra Stripe Properties |
| swCommands_RMBFreeshapeCancel | 3320; cancels FreeShape; FreeShape RMB menu > Cancel |
| swCommands_RMBFreeshapeOK | 3319; FreeShape RMB menu > OK |
| swCommands_Roll | 605; View toolbar > Roll |
| swCommands_RotaryMotor | 423; MotionManager toolbar > Motor |
| swCommands_Rotate_180_Degrees | 2278; valid when the move triad is visible; in the graphics area, triad_ring RMB menu > rotate 180⁰ |
| swCommands_Rotate_45_Degrees | 2880; valid for a selected ZX triad ring of a live section plane; in the graphics area, ZX_triad_ring RMB menu > rotate 45⁰ |
| swCommands_Rotate_90_Degrees | 2277; valid when the move triad is visible; in the graphics area, triad_ring RMB menu > rotate 90⁰ |
| swCommands_Rotate_Routing_Clip | 1637; valid for the SOLIDWORKS Routing add-in with a selected routing clip in an open routing assembly; Routing Tools toolbar > Rotate Clip |
| swCommands_Rotate_Show_Delta_Xyz | 1136; valid after component RMB menu > Move with Triad command in an assembly; in the graphics area, triad_center_ball RMB menu > Show Rotate Delta XYZ Box |
| swCommands_Rotate_Xaxis_By90 | 3132; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, RMB menu > Rotate X 90 Deg |
| swCommands_Rotate_Yaxis_By90 | 3133; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, RMB menu > Rotate Y 90 Deg |
| swCommands_Rotate_Zaxis_By90 | 3134; valid when the Insert Component PropertyManager page is open, and a part or assembly to insert is selected; in the graphics area, RMB menu > Rotate Z 90 Deg |
| swCommands_RotateComponent | 21; valid for assemblies; Tools menu > Component > Rotate or Assembly toolbar > Rotate Component |
| swCommands_RotateEntities | 503; valid for a sketch with a selected entity or annotation; Sketch toolbar > Rotate Entities |
| swCommands_RotateView | 329; View toolbar > Rotate View |
| swCommands_Route_Add_To_Fab | 1328; valid for the SOLIDWORKS Routing add-in, an open routing assembly, and a selected connection point or component; in the graphics area, cpoint_or_comp RMB menu > Add to Route |
| swCommands_Route_Get_Property | 721; valid for the SOLIDWORKS Routing add-in with a selected routing segment in an open routing assembly; in the graphics area, route_segment RMB menu > Route Segment Properties |
| swCommands_Route_Io_Output | 2397; valid for the SOLIDWORKS Routing add-in and an open pipe or tube routing assembly; in the graphics area, route_pipe_or_tube RMB menu > Export Pipe/Tube Data |
| swCommands_Route_Properties | 693; valid for the SOLIDWORKS Routing add-in and an open piping route, opens the Route Properties PropertyManager page; Piping toolbar > Route Properties |
| swCommands_Route_Realign_Fitting | 1326; valid for the SOLIDWORKS Routing add-in with an open routing assembly and a selected piping fitting; in the graphics area, sel_piping_fitting RMB menu > Change Fitting Alignment |
| swCommands_Route_Remove_Pipe | 723; valid for the SOLIDWORKS Routing add-in with an open routing assembly and a selected pipe; in the graphics area, sel_pipe RMB menu > Remove Pipe |
| swCommands_Route_Rotate_Clip | 2266; valid for SOLIDWORKS Routing add-in and an open routing assembly; Routing Tools toolbar > Rotate Clip |
| swCommands_Route_Start_Con_Point | 1238; valid for the SOLIDWORKS Routing add-in with a selected component in a route that is not in edit mode; in the graphics area, comp RMB menu > Start Route |
| swCommands_Route_Through | 2267; valid for the SOLIDWORKS Routing add-in and an open route; Routing Tools toolbar > Route Through Clip |
| swCommands_Route_Unhook_From | 2268; valid for SOLIDWORKS Routing add-in and an open route; Routing Tools toolbar > Unhook from Clip |
| swCommands_RouteLine | 396; valid for the SOLDWORKS Routing add-in and an open route; Explode Sketch toolbar > Route Line |
| swCommands_Router_Change_Mode | 2558; valid for the SOIDWORKS Routing add-in, when the Auto Route PropertyManager page is open, and Auto Route Orthogonal route is selected; in the graphics area, RMB menu > Edit Mode |
| swCommands_Routing_Reuse_Route | 3190; valid for the SOLIDWORKS Routing add-in and an open electrical routing assembly; Electrical toolbar > Reuse Route |
| swCommands_Routing_Tools | 2448; valid for the SOLIDWORKS Routing add-in; Route toolbar > Routing Tools |
| swCommands_RunMacro | 30; Macro toolbar > Run Macro |
| swCommands_SageExpress | 2952; valid for parts, opens the Enable SustainabilityXpress dialog; Tools toolbar > SustainabilityXpress |
| swCommands_Save | 2; for modified parts, opens the Save Modified Documents dialog; Standard toolbar > Save or Older version file |
| swCommands_Save_Comp | 2118; valid for shared assemblies in a multi-user environment (select Tools > Options > System Options > Collaboration > Add shortcut menu items for multi-user environment ; in the FeatureManager design tree, comp RMB menu > Save |
| swCommands_Save_Config_Preview | 1853; valid for a document that is already saved, saves a configuration preview |
| swCommands_Save_Journal_As_Word | 2060; valid for a selected journal, saves it in Word format |
| swCommands_Save_Template | 921; valid for drawings, opens the Save Sheet Format dialog; File menu > Save Sheet Format |
| swCommands_Save_To_Webfolder | 1680; saves an assembly to a web folder |
| swCommands_Save_Virtual_Comp | 3464; performs an external save of a virtual component in an assembly; in the FeatureManager design tree, right click a virtual component and select RMB menu > Save Part(In External file) |
| swCommands_SaveAll | 19; Standard toolbar > Save All |
| swCommands_SaveAs | 620; Standard toolbar > Save As |
| swCommands_SaveBlock | 473; valid for blocks created in assembly layouts; Blocks toolbar > Save Sketch as Block |
| swCommands_SaveLocally | 3457; 3DEXPERIENCE SOLIDWORKS only, saves the active document to your cache; File menu > Save Locally |
| swCommands_Savenotification | 2357; valid during autosave, sends the current window the save notification specifics |
| swCommands_Saveto_Separate_File | 2375; valid for weldment cut-list items, opens the Insert Into New Part PropertyManager page; in the FeatureManager design tree, Cut list folder > item RMB menu > Insert into New Part |
| swCommands_SaveWithOptions | 3456; 3DEXPERIENCE SOLIDWORKS only, opens a dialog of options with which to save the active document; File menu > Save with Options... |
| swCommands_ScaleEntities | 504; valid for an open sketch, opens the Scale PropertyManager page; Sketch toolbar > Scale Entities |
| swCommands_ScanEqual | 78; valid for drawings; Dimensions/Relations toolbar > Scan Equal |
| swCommands_ScanTo3D | 622; SOLIDWORKS Add-ins toolbar > ScanTo3D |
| swCommands_Scene | 2799; View toolbar > Apply Scene |
| swCommands_Schedule_Render | 2970; opens the Schedule Render dialog; Render Tools toolbar > Schedule Render |
| swCommands_ScreenCapture | 604; Screen Capture toolbar > Image Capture |
| swCommands_ScreenCaptureAvi_Begin | 2814; opens the Record Screen Capture to File dialog; Screen Capture toolbar > Record Video |
| swCommands_ScreenCaptureAvi_End | 2815; valid if a screen is being videoed; Screen Capture toolbar > Stop Video Record |
| swCommands_ScreenCaptureToolbar | 2813; alternative to swCommands_Toolbar_ScreenCapture; View menu > Toolbars > Screen Capture |
| swCommands_Search_Detail_Items | 1998; accelerator F key to Find/Replace text in detail items |
| swCommands_SearchCommands | 3019; Help menu > Search > Commands |
| swCommands_SearchFilesAndModels | 3020; Help menu > Search > Files and Models |
| swCommands_SearchHelp | 3016; Help menu > Search > SOLIDWORKS Help |
| swCommands_SearchManufacturers | 3180; Help menu > Search > Manufacturers |
| swCommands_SearchMySolidworks | 3174; Help menu > Search > MySolidWorks |
| swCommands_SecondaryAdvStructMember | 3337; creates a secondary structural member feature by sweeping pre-defined profiles along user-defined planes; Structures toolbar > Secondary Structural Member... |
| swCommands_SectionProperties | 383; opens the Section Properties dialog; Tools toolbar > Section Properties |
| swCommands_SectionView | 124; opens the Section View PropertyManager page; View toolbar > Section View |
| swCommands_Segment | 3129; valid for an open sketch, opens the Segment PropertyManager page; Sketch toolbar > Segment |
| swCommands_SegmentImportedMeshBody | 3357; segments imported solid and surface mesh bodies; Features toolbar > Segment Imported Mesh Body |
| swCommands_Select_All | 634; dialog resource Select All |
| swCommands_Select_Annotation_View | 3135; valid for 3D annotations; opens the Select annotation view dialog; in the graphics area, dim RMB menu > Select Annotation View |
| swCommands_Select_Chain | 2471; valid for an open sketch, in the graphics area, selected_line RMB menu > Select Chain |
| swCommands_Select_Display_State | 2808; Display States toolbar > dropdown |
| swCommands_Select_Loop | 1420; in the graphics area, selected_edge RMB menu > Select Loop |
| swCommands_Select_Midpoint | 802; valid for specific dialogs, such as the Deform PropertyManager page; in the graphics area, RMB menu > Select Midpoint ; also valid for selected_edge RMB menu > Select Midpoint |
| swCommands_Select_Open_Edge_Loop | 1697; valid when the Untrim Surface PropertyManager page is open, and a surface edge is selected; in the graphics area, surface_edge RMB menu > Select Open Loop |
| swCommands_Select_Open_Half_Loop | 2435; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, surface_edge RMB menu > Select Partial Loop |
| swCommands_Select_Seed_Feature | 1802; valid for a selected pattern feature; in the graphics area, sel_pattern RMB menu > Select Seed of Pattern |
| swCommands_Select_Snapshot | 3031; valid for assemblies, opens the Name Snapshot dialog; View toolbar > Take Snapshot |
| swCommands_Select_SubAssembly_In_GraphicsView | 2824; valid for a selected component of a subassembly; in the graphics area, subasm_comp RMB menu > Select Subassembly |
| swCommands_Select_Tangency | 1428; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, surface_edge RMB menu > Select Tangency |
| swCommands_Select_Tangency_Laminar | 1696; valid when the Surface-Untrim1 PropertyManager page is open, and a surface edge is selected; in the graphics area, surface_edge RMB menu > Select Open Tangency |
| swCommands_SelectAllFilters | 275; Selection Filter toolbar > Select All Filters |
| swCommands_SelectConfigurations | 3116; Configurations toolbar > dropdown |
| swCommands_SelectionFilters | 486; alternative to swCommands_New_Toolbar_Sel_Filter; View menu > Toolbars > Selection Filter |
| swCommands_Selective_Open | 3033; valid for a selected assembly opened in Large Design Review mode, opens the Selective Open dialog; in the FeatureManager design tree, top_assy RMB menu > Selective Open |
| swCommands_Selective_Open_LightWeight | 3038; valid for a selected assembly opened in Large Design Review mode, opens the Selective Open in Lightweight dialog; in the FeatureManager design tree, top_assy RMB menu > Selective Open in Lightweight |
| swCommands_SelectOverGeometry | 3310; VIRTKEY "T"; enables/disables box and lasso selection to start on faces; Standard toolbar > Select over Geometry |
| swCommands_SendTo | 3045; File menu > Send To |
| swCommands_Set_As_Anchor | 1624; valid for a selected point in a drawing sheet whose format is in edit mode; sketch_pt RMB menu > Set as Anchor > table_type |
| swCommands_Set_Current_View_As_Back | 3085; valid for assemblies and parts; View menu > Modify > Set Current View As > Back |
| swCommands_Set_Current_View_As_Bottom | 3087; valid for assemblies and parts; View menu > Modify > Set Current View As > Bottom |
| swCommands_Set_Current_View_As_Front | 3084; valid for assemblies and parts; View menu > Modify > Set Current View As > Front |
| swCommands_Set_Current_View_As_Left | 3089; valid for assemblies and parts; View menu > Modify > Set Current View As > Left |
| swCommands_Set_Current_View_As_Right | 3088; valid for assemblies and parts; View menu > Modify > Set Current View As > Right |
| swCommands_Set_Current_View_As_Top | 3086; valid for assemblies and parts; View menu > Modify > Set Current View As > Top |
| swCommands_Set_Dim_Extension_Centerline | 3106; valid for a drawing with a dimension extension line; in the graphics area, dim_ext_line RMB menu > Set Extension Line as Centerline |
| swCommands_Set_QuickView_Transparency | 3032; valid for assemblies opened in Large Design Review mode with one or more modified components; View toolbar > Filter Modified Components |
| swCommands_Shaded | 337; View toolbar > Display Style > Shaded |
| swCommands_ShadedSketchContours | 3189; Sketch toolbar > Shaded Sketch Contours |
| swCommands_ShadedWithEdges | 506; View toolbar > Display Style > Shaded With Edges |
| swCommands_ShadowsInShadedMode | 399; valid for parts and assemblies; View toolbar > View Settings > Shadows in Shaded Mode |
| swCommands_Share | 3524; opens a Share dialog to share a copy of the current model with members outside or inside your organization; File > Share |
| swCommands_Share_A_File | 3516; opens Share file_name_with_extension dialog; Tools > Lifecycle and Collaboration > Share a file |
| swCommands_Sheet_Tab_Popup_Activate | 950; valid for drawings with a selected sheet tab; sheet_tab RMB menu > Activate |
| swCommands_Sheet_Tab_Popup_Add | 948; valid for drawings with a selected sheet tab; sheet_tab RMB menu > Add Sheet |
| swCommands_Sheet_Tab_Popup_Delete | 949; valid for drawings with a selected sheet tab; sheet_tab RMB menu > Delete |
| swCommands_Sheet_Tab_Popup_Properties | 947; valid for drawings with a selected sheet tab; sheet_tab RMB menu > Properties |
| swCommands_Sheet_Tab_Popup_Rename | 2717; valid for drawings with a selected sheet tab; sheet_tab RMB menu > Rename |
| swCommands_SheetMetal | 487; alternative to swCommands_Toolbar_Sht_Mtl; View menu > Toolbars > Sheet Metal |
| swCommands_SheetmetalCosting | 3006; Tools toolbar > Costing |
| swCommands_Shell | 32; valid for parts with a selected sketch; Features toolbar > Shell |
| swCommands_Show_3d_Sketch_Triad | 2440; valid for an open 3D sketch; in the graphics area, RMB menu > Show Sketcher Triad |
| swCommands_Show_Ann_Based_Swift_Tree | 2086; valid for a selected scheme in DimXpertManager; in the DimXpertManager, sel_scheme RMB menu > Tree Display > Show annotation based tree |
| swCommands_Show_Bom | 1240; valid for a drawing view with an Excel-based BOM; excel_based_bom RMB menu > Show |
| swCommands_Show_CADFamily_Name | 3461; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the CAD family in which the part reference belongs in the FeatureManager design tree; FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show CAD Family Name |
| swCommands_Show_Comp_Des | 2490; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Component Descriptions |
| swCommands_Show_Comp_Filename | 2489; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Component Names |
| swCommands_Show_ComponentInstance_Name | 3458; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the full name derived from the component's properties in the FeatureManager design tree; FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component Instance Name |
| swCommands_Show_ComponentReference_Name | 3459; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the Family Name (physical product) of the part being referenced in the FeatureManager design tree; FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component ReferenceName |
| swCommands_Show_Components | 926; valid for selected components in assemblies; in the FeatureManager design tree, selected_comp RMB context toolbar > Show Components |
| swCommands_Show_Components_All_Configs | 1651; valid for a selected top-level assembly; Edit menu > Show > All Display States |
| swCommands_Show_Components_Select_Configs | 1652; valid for a selected top-level assembly, opens the Apply To Display States dialog; Edit menu > Show > Specified Display States |
| swCommands_Show_Config_Description | 2511; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Component Configuration Descriptions |
| swCommands_Show_Config_Name | 2491; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Component Configuration Names |
| swCommands_Show_Config_Or_DisplayState_Name | 3199; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Configuration/Display State Names if at least one exists |
| swCommands_Show_Config_Previews | 2494; valid for a selected configuration; in the ConfigurationManager, config RMB menu > Show Preview |
| swCommands_Show_Configdes_In_Configtree | 2493; valid for assemblies; in ConfigurationManager, top_level_config RMB menu > Tree Display > Show Configuration Descriptions |
| swCommands_Show_Configname_In_Configtree | 2492; valid for assemblies; in ConfigurationManager, top_level_config RMB menu > Tree Display > Show Configuration Names |
| swCommands_Show_Configuration | 1535; valid for a selected inactive configuration, in ConfigurationManager, inactive_config RMB menu > Show Configuration |
| swCommands_Show_Configuration_Adv | 1558; valid for assemblies, opens the Advanced Show/Hide Components dialog |
| swCommands_Show_Cthread | 1529; valid for a model with a hidden, selected cosmetic thread; in the FeatureManager design tree, cosmetic_thread RMB context toolbar > Show Cosmetic Thread |
| swCommands_Show_Dependents | 1046; valid for a selected top-level assembly; Edit Menu > Show with Dependents > Current Display State |
| swCommands_Show_Dependents_All_Configs | 1647; valid for a selected top-level assembly; Edit Menu > Show with Dependents > All Display States |
| swCommands_Show_Dependents_Select_Configs | 1648; valid for a selected top-level assembly; Edit Menu > Show with Dependents > Specified Display States |
| swCommands_Show_Dim | 1540; use swCommands_HideShowAnnotations to display hidden annotations |
| swCommands_Show_Dim_Align | 1564; valid for a selected drawing dimension to which Align Collinear/Radial has been applied; in the graphics area, aligned_dim RMB menu > Show Alignment |
| swCommands_Show_Dim_Leader | 2539; valid for a drawing with a selected dimension with a hidden leader line; leader_line RMB menu > Show Dimension Lines |
| swCommands_Show_Dim_Witness | 2527; valid for a drawing with a selected dimension with a hidden witness line; witness_line RMB menu > Show Extension Lines |
| swCommands_Show_Explode_Steps | 1556; valid for a selected component in an assembly with an Exploded View; in the FeatureManager design tree, component RMB menu > Show Explode Steps |
| swCommands_Show_Feat_Based_Swift_Tree | 2085; valid for a selected scheme in DimXpertManager; in the DimXpertManager, sel_scheme RMB menu > Tree Display > Show feat based tree |
| swCommands_Show_Feature_Des | 2488; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Feature Descriptions |
| swCommands_Show_Feature_Detail | 927; valid for a selected top-level assembly showing hierarchy only; in the graphics area, RMB menu > Show Feature Detail |
| swCommands_Show_Feature_History | 2599; valid for a part with a selected solid or surface body folder; sel_folder RMB menu > Show Feature History |
| swCommands_Show_Feature_Name | 2487; valid for a selected top-level assembly; in the FeatureManager design tree, top_asm RMB menu > Tree Display > Show Feature Names |
| swCommands_Show_Flat_Swift_Tree | 2087; valid for a selected scheme in DimXpertManager; in the DimXpertManager, sel_scheme RMB menu > Tree Display > Show flat tree |
| swCommands_Show_Hidden_comps | 2810; valid for assemblies, opens the Show Hidden dialog; Assembly toolbar > Show Hidden Components |
| swCommands_Show_Hidden_comps_Exit | 3022; dialog resource Cancel |
| swCommands_Show_Hidden_comps_Undo | 3021; dialog resource Undo |
| swCommands_Show_Hide_Fixed_Length_Route_Manipulators | 3150; valid for the SOLIDWORKS Routing add-in and an open assembly with a route and selected route segments; Routing Tools toolbar > Show Fixed Length Dimensions |
| swCommands_Show_Incontext_Feature_Holders | 686; valid for a selected top-level assembly with hidden update holders; selected_assembly RMB menu > Show Update Holders |
| swCommands_Show_LDR_Configuration | 3203; valid for assemblies opened in Large Design Review mode for a selected configuration in ConfigurationManager; in the ConfigurationManager, hidden_config RMB menu > Show Configuration |
| swCommands_Show_Mate_Component_1 | 2530; valid for assemblies with hidden mate components; in the FeatureManager design tree, first_part_mate_constraint RMB menu > second_part_mate > Show component |
| swCommands_Show_Mate_Component_2 | 2535; valid for assemblies with hidden mate components; in the FeatureManager design tree, second _part_mate_constraint RMB menu > first_part_mate > Show component |
| swCommands_Show_Mesh_Feat | 3210; valid for a selected mesh feature that is hidden; RMB menu > Show |
| swCommands_Show_Representation_Name | 3460; 3DEXPERIENCE SOLIDWORKS assemblies only, displays the representation name of the part in the FeatureManager design tree; FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Component Reference Representation Name |
| swCommands_Show_Revision_And_Maturity | 3462; 3DEXPERIENCE SOLIDWORKS assemblies only, displays a component's revisions and maturity in the FeatureManager design tree; FeatureManager design tree > Top Assembly RMB menu > Tree Display > Show Revision and Maturity |
| swCommands_Show_Sketch_Dim_In_Drawing | 2479; valid for a selected hidden dimension in a drawing sketch; RMB menu > Show Dimensions |
| swCommands_Show_Table | 2622; valid for models with hidden tables; in the FeatureManager design tree, table_name RMB menu > Show Table |
| swCommands_Show_Triad_Manipulator | 769; valid for a selected component in an assembly, displays the triad manipulator |
| swCommands_Show_View_Palette | 2243; valid for drawings; accelerator key P to display view palette |
| swCommands_Show_Zone | 1560; valid for assemblies with envelope components; in the FeatureManager design tree, envelope_feature RMB menu > Envelope > Show/Hide Using Envelope |
| swCommands_ShowCurvatureCombs | 4; valid for a selected spline, opens the Curvature Scale PropertyManager page; Spline Tools toolbar > Show Curvature Combs |
| swCommands_ShowEdge | 352; valid for drawings, opens the Show Edge PropertyManager page |
| swCommands_ShowGuidelines | 2983; valid for the SOLIDWORKS Routing add-in for an open assembly route; Routing Tools toolbar > Show Guidelines |
| swCommands_ShowInflectionPoints | 417; valid for an open sketch of a selected spline, opens the Spline PropertyManager page; Spline Tools toolbar > Show Inflection Points |
| swCommands_ShowMinimumRadius | 418; valid for an open sketch of a selected spline, opens the Spline PropertyManager page; Spline Tools toolbar > Show Minimum Radius |
| swCommands_ShowSplineHandles | 443; valid for an open sketch of a selected spline; Spline Tools toolbar > Show Spline Handles |
| swCommands_ShutOffSurfaces | 452; valid for parts; Mold Tools toolbar > Shut-off Surfaces |
| swCommands_SimElementOff | 2829; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the gantt chart, rotary_motor_bar RMB menu > Off |
| swCommands_SimElementOn | 2828; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the gantt chart, rotary_motor_bar RMB menu > On |
| swCommands_SimElementSuppress | 2830; valid only in the context of a Motion Study gantt chart for a selected simulation element row; in the MotionManager design tree, rotary_motor_bar RMB menu > Suppress |
| swCommands_SimElementUnsuppress | 2831; valid only in the context of a Motion Study gantt chart for a selected, suppressed simulation element row; in the MotionManager design tree, rotary_motor_bar RMB menu > Unsuppress |
| swCommands_SimpleHole | 12; valid for sheet metal parts; Sheet Metal toolbar > Simple Hole |
| swCommands_SimplifySpline | 144; valid for a selected spline in an open sketch; Spline Tools toolbar > Simplify Spline |
| swCommands_SimulationDesigner | 3527; SOLIDWORKS Connected only; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Designer |
| swCommands_SimulationPremium | 3435; valid only if entitled; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Premium |
| swCommands_SimulationPro | 3434; valid only if entitled; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Professional |
| swCommands_SimulationStd | 3433; valid only if entitled; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Simulation Standard |
| swCommands_SingleView | 549; View toolbar > View Orientation > Single View |
| swCommands_Sk_Close_Contour | 1048; valid for a selected open profile in an open sketch; Tools menu > Sketch Tools > Close Sketch to Model |
| swCommands_Sk_Endchain | 1674; valid during insertion of an arc or line in an open sketch; in the graphics area, sketch_line RMB menu > End chain (double-click) |
| swCommands_Sk_Endcos | 2126; valid for an open sketch duirng spline on surface creation, stops the drawing of the spline and opens the Spline PropertyManager page |
| swCommands_Sk_Endspline | 1804; valid for an open sketch duirng spline creation, stops the drawing of the spline and opens the Spline PropertyManager page |
| swCommands_Sketch | 45; valid for a selected plane or sketch; Sketch toolbar > Sketch |
| swCommands_Sketch_Align_Grid_Origin | 2727; valid for an open sketch, opens the Align Grid/Origin PropertyManager page; Tools > Sketch Tools > Align > Align Grid/Origin |
| swCommands_Sketch_Detach | 1547; valid for an open sketch; Sketch toolbar > Detach Segment On Drag |
| swCommands_Sketch_Jog_Flip | 1817; valid for a sketch jog line in an assembly view; RMB menu > Flip Direction |
| swCommands_Sketch_Suppress_Constraints | 1936; valid for a selected sketch relations manipulator; in the graphics area, manip RMB menu > Toggle Suppression |
| swCommands_SketchChamfer | 358; valid for an open sketch, opens the Sketch Chamfer PropertyManager page; Sketch toolbar > Sketch Chamfer |
| swCommands_SketchCreateChain | 617; valid when inserting a Grid System, opens the Path PropertyManager page; in the graphics area, RMB menu > Make Path |
| swCommands_SketchDrivenPattern | 304; valid for parts with a selected sketch; Features toolbar > Sketch Driven Pattern |
| swCommands_SketchedBend | 323; valid for sheet metal parts; Sheet Metal toolbar > Sketched Bend |
| swCommands_SketchFillet | 62; valid for an open sketch, opens the Sketch Fillet PropertyManager page; Sketch toolbar > Sketch Fillet |
| swCommands_SketchGroupRebuild | 555; valid for an open sketch block; Blocks toolbar > Rebuild |
| swCommands_SketchPicture | 368; opens the Open dialog; Sketch toolbar > Sketch Picture |
| swCommands_Sketchplane_Delete | 2681; valid for a selected sketch plane in the 3D sketch environment; RMB menu > Delete |
| swCommands_Sketchplane_Deleteall | 2682; valid for a selected sketch plane in the 3D sketch environment; RMB menu > Delete all |
| swCommands_Sketchplane_Rename | 2683; valid for a selected sketch plane in the 3D sketch environment; RMB menu > Rename |
| swCommands_SketchSlicing | 3399; opens the Slicing PropertyManager; Insert menu > Slicing or Sketch toolbar > Slicing |
| swCommands_SketchSlot_Arc_Center | 2867; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; Sketch toolbar > Centerpoint Arc Slot |
| swCommands_SketchSlot_Arc3P | 2866; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; Sketch toolbar > 3 Point Arc Slot |
| swCommands_SketchSlot_Line | 2864; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; Sketch toolbar > Straight Slot |
| swCommands_SketchSlot_Line_Center | 2865; valid for a selected plane, planar face, or edge, opens the Slot PropertyManager page; Sketch toolbar > Centerpoint Straight Slot |
| swCommands_SketchToolbar | 489; alternative to swCommands_Toolbar_Sketch; View menu > Toolbars > Sketch |
| swCommands_Skey_SearchBox | 3471; Opens a command search box; in the graphics area, click "s" or select Help menu > Search > Commands |
| swCommands_Skg_Cancel | 2027; valid during block creation, cancels |
| swCommands_Skg_Ok | 2026; valid during a block edit; RMB menu > Exit Block Edit |
| swCommands_Skg_Remove | 2023; removes a selected sketch block |
| swCommands_SkSilhouetteEnts | 3414; converts silhouette outlines of bodies and components into sketch segments; Sketch toolbar > Silhouette Entities |
| swCommands_Sktools_Autoconstr | 987; valid for an open, unconstrained sketch; Tools menu > Relations> Constrain All Relations |
| swCommands_Sm_Clear_Problem_Areas | 2945; valid for a sheet metal flat pattern feature with problem areas; in the graphics area, RMB menu > Clear problem areas |
| swCommands_Sm_Convert_To_Sheetmetal | 2245; converts a part to a sheet metal part |
| swCommands_Sm_Measure_Bend_Deviation | 1830; valid for a selected sheet metal bend feature; in the FeatureManager design tree, bend RMB menu > Bend Deviation |
| swCommands_Sm_Reorder_Bends | 1096; valid for a selected sheet metal bend feature; in the FeatureManager design tree, bend RMB menu > Reorder Bends |
| swCommands_Sm_Show_Problem_Areas | 2944; valid for a selected sheet metal flat pattern feature with cleared problem areas; in the graphics area, RMB menu > Show problem areas |
| swCommands_Sm_Toggle_Flat_Display | 2924; valid for a selected flat pattern feature of a sheet metal part; in the graphics area, RMB menu > Toggle flat display |
| swCommands_Small_Icon | 1621; valid in the Appearances, Scenes, and Decals task pane palette; palette RMB menu > Small Icons |
| swCommands_Small_List_Icon | 2064; valid in content list popups; RMB menu > List, Small Icons |
| swCommands_Smart_Feature_Preview | 2218; valid for assemblies with a selected smart feature component; in the FeatureManager design tree, History folder > smart_component > Smart Feature folder > Components > comp RMB menu > Preview |
| swCommands_Smart_Mate | 1343; valid for assemblies, opens the SmartMates PropertyManager page; Assembly toolbar > SmartMates |
| swCommands_SmartDimension | 38; opens the Dimension PropertyManager page; Layout Tools or Dimensions/Relations toolbar > Smart Dimension |
| swCommands_SmartFasteners | 7; valid for assemblies, opens the Smart Fasteners PropertyManager page; Assembly toolbar > Smart Fasteners |
| swCommands_Smc_Help | 2219; valid for a Smart Component as it is being edited in its defining assembly, opens the Editing Definition of a Smart Component topic in the SOLIDWORKS help; SMC popup toolbar > Help |
| swCommands_SMGusset | 3111; valid for sheet metal parts, opens the Sheet Metal Gusset PropertyManager page; Sheet Metal toolbar > Sheet Metal Gusset |
| swCommands_SMNormalCut | 3196; opens the Normal Cut PropertyManager page; Sheet Metal toolbar > Normal Cut |
| swCommands_SmoothMesh | 3469; Opens the Smooth Graphics Mesh PropertyManager for a selected graphics body or facet group; Insert menu > Mesh > Mesh Smoothing |
| swCommands_SMStamp | 3518; Inserts a sheet metal stamp; Insert menu > Sheet Metal > Stamp |
| swCommands_Snap_To_Selection | 2275; valid after component RMB menu > Move with Triad command in assembly; in the graphics area, triad_center_ball RMB menu > Move to selection |
| swCommands_Snap_While_Dragging | 2276; valid for a selected Move with Triad ring in an assembly; triad_ring RMB menu > Snap while dragging |
| swCommands_Solid_Data_Manager | 1393; valid if SOLIDWORKS Explorer is installed; Tools menu > SOLIDWORKS Applications > SOLIDWORKS Explorer |
| swCommands_SolidToSheetMetal | 2882; valid for sheet metal parts; Sheet Metal toolbar > Convert to Sheet Metal |
| swCommands_SolidWorks_backoffice | 3356; Tools menu > SOLIDWORKS Applications > SOLIDWORKS Task Scheduler... |
| swCommands_SolidworksAnimator | 433; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Animator |
| swCommands_SolidworksOffice | 491; alternative to swCommands_Toolbar_Office; View menu > Toolbars > SOLIDWORKS Add-ins |
| swCommands_SolidworksRouting | 566; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Routing |
| swCommands_SolidworksToolbox | 437; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Toolbox |
| swCommands_SolidworksUtilities | 436; SOLIDWORKS Add-ins toolbar > SOLIDWORKS Utilities |
| swCommands_SolveAsFlexibleOrRigid | 3095; valid for a selected subassembly; Assembly toolbar > Make Subassembly Flexible |
| swCommands_Sort_Stacked_Balloons | 3161; valid for a selected annotation with stacked balloons; in the graphics area, stacked_balloon_anno RMB menu > Sort Stacked Balloons |
| swCommands_SpaceEvenlyAcross | 312; valid for multi-selected annotations or dimensions; Align toolbar > Space Evenly Across |
| swCommands_SpaceEvenlyDown | 313; valid for multi-selected annotations or dimensions; Align toolbar > Space Evenly Down |
| swCommands_SpaceTightlyAcross | 316; valid for multi-selected annotations or dimensions; Align toolbar > Space Tightly Across |
| swCommands_SpaceTightlyDown | 317; valid for multi-selected annotations or dimensions; Align toolbar > Space Tightly Down |
| swCommands_SpellChecker | 535; opens the Spelling Check PropertyManager page; Tools toolbar > Spell Checker |
| swCommands_Spline | 47; valid for a selected plane or planar face; Sketch toolbar > Spline |
| swCommands_SplineOnSurface | 542; valid for a selected face or surface; Sketch toolbar > Spline on Surface |
| swCommands_Splines | 492; alternative to swCommands_Toolbar_Spline_Tools; View menu > Toolbars > Spline Tools |
| swCommands_Split_Open_Route | 2342; valid for the SOLIDWORKS Routing add-in; splits an open route for selected splittable segments |
| swCommands_Split_Open_Segm_Ar | 1858; valid for the SOLIDWORKS Routing Add-in and when the Auto Route PropertyManager page is open; in the graphics area, RMB menu > Split Entity |
| swCommands_Split_Route | 2269; valid for the SOLIDWORKS Routing add-in and an open routing assembly; Routing Tools toolbar > Split Route |
| swCommands_SplitEntities | 293; valid for an open sketch and a selected sketch entity; Sketch toolbar > Split Entities |
| swCommands_Spool_Command | 3013; valid for the SOLIDWORKS Routing add-in and an open piping route, opens the Spools PropertyManager page; Piping toolbar > Define Spools |
| swCommands_Spool_Tube_Command | 3044; valid for SOLIDWORKS Routing add-in and an open flexible tube assembly; in the graphics area, sel_route_or_tube_comp RMB menu > Define Spools |
| swCommands_Stack | 534; valid for selected text; Formatting toolbar > Stack |
| swCommands_Stack_Dir_Down | 678; valid for a selected stacked balloon stacked left, right, or up; in the graphics area, stacked_balloon RMB menu > Down |
| swCommands_Stack_Dir_Left | 680; valid for a selected stacked balloon stacked down, right, or up; in the graphics area, stacked_balloon RMB menu > Left |
| swCommands_Stack_Dir_Right | 681; valid for a selected stacked balloon stacked left, down, or up; in the graphics area, stacked_balloon RMB menu > Right |
| swCommands_Stack_Dir_Up | 677; valid for a selected stacked balloon stacked left, right, or down; in the graphics area, stacked_balloon RMB menu > Up |
| swCommands_StackedBalloons | 319; opens the Stacked Balloon PropertyManager page; Annotation toolbar > Stacked Balloons |
| swCommands_StackFasteners | 3410; valid for assemblies, adds a fastener stack to the asembly using the SOLIDWORKS Toolbox library of standard hardware; Assembly toolbar > Fastener Stack |
| swCommands_Standard | 493; alternative to swCommands_Toolbar_Standard; View menu > Toolbars > Standard |
| swCommands_Standard3View | 42; Drawing toolbar > Standard 3 View |
| swCommands_StandardViews | 494; alternative to swCommands_Toolbar_Stdview; View menu > Toolbars > Standard Views |
| swCommands_Start_Contour_Single_Select | 660; valid for parts or assemblies, starts contour single select mode |
| swCommands_Start_Screen | 3229; opens the Welcome dialog; CTRL-F2; Standard toolbar > Welcome to SOLIDWORKS |
| swCommands_Start_Select_Contour | 2495; valid for a selected sketch contour; sketch_contour RMB menu > Contour Select Tool |
| swCommands_Start_Select_Contour_2 | 2514; valid when the Planar Surface PropertyManager page is open, and the planar surface sketch is selected; in the graphics area, planar_surface_sketch RMB menu > Start Contour Selection |
| swCommands_Start_Smart_Selection | 2628; valid when a PropertyManager page supporting multi-edge selection is open; in the graphics area, sel_edge RMB menu > Start/Edit Smart Selection |
| swCommands_Statistics | 427; valid for parts and drawings; Tools toolbar > Performance Evaluation |
| swCommands_StopCurrentJump | 129; Web toolbar > Stop Current Jump |
| swCommands_StopMacro | 31; valid for a running macro, opens the Save As dialog; Macro toolbar > Stop Macro |
| swCommands_StretchEntities | 2851; valid for an open sketch, opens the Stretch PropertyManager page; Sketch toolbar > Stretch Entities |
| swCommands_Strikeout | 532; valid for selected text; Formatting toolbar > StrikeOut |
| swCommands_StructuralMember | 465; valid for weldments, opens the Structural Member PropertyManager page; Weldments toolbar > Structural Member |
| swCommands_Submit | 794; dialog resource Submit |
| swCommands_Suppress | 14; valid for one or more selected features; Edit menu > Suppress > This Configuration |
| swCommands_Suppress_Mate_Component_1 | 2531; valid for assemblies with visible, resolved mate components; in the FeatureManager design tree, first_part_mate_constraint RMB menu > second_part_mate > Suppress component |
| swCommands_Suppress_Mate_Component_2 | 2536; valid for assemblies with visible, resolved mate components; in the FeatureManager design tree, second_part_mate_constraint RMB menu > first_part_mate > Suppress Component |
| swCommands_Surface_Flatten | 3139; opens the Flatten PropertyManager page; Surfaces toolbar > Surface Flatten |
| swCommands_SurfaceFinish | 112; opens the Surface Finish PropertyManager page; Annotation toolbar > Surface Finish |
| swCommands_Surfaces | 495; alternative to swCommands_Toolbar_Surface; View menu > Toolbars > Surfaces |
| swCommands_SurfFromMesh | 3218; creates surfaces from mesh; Mold or Surface toolbar > Surface From Mesh |
| swCommands_Sw_Animatorpane | 2811; valid for assemblies; View menu > Toolbars > MotionManager |
| swCommands_Sw_Beta_Report | 1412; opens the SOLIDWORKS Beta problem report from www.solidworks.com , if available |
| swCommands_Sw_Educator_Resources | 3465; Opens www.solidworks.com/eduwhatsnew |
| swCommands_Sw_Release_Notes | 1411; opens the Administration Guides from www.solidworks.com ; Help menu > Release Notes |
| swCommands_Sw_Taskpane | 2127; View menu > User Interface > Task Pane |
| swCommands_SwConnected_Release_Notes | 3500; displays the release notes for the installed version of SOLIDWORKS Connected; SOLIDWORKS menu > Help > Release Notes > SOLIDWORKS Connected yyyy x |
| swCommands_SweptBossBase | 64; valid for parts with a selected sketch; Features toolbar > Swept Boss/Base |
| swCommands_SweptCut | 65; valid for parts with a selected sketch; Features toolbar > Swept Cut |
| swCommands_SweptFlange | 3041; valid for sheet metal parts, opens the Swept Flange PropertyManager page; Sheet Metal toolbar > Swept Flange |
| swCommands_SweptSurface | 103; opens the Surface-Sweep PropertyManager page; Surfaces toolbar > Swept Surface |
| swCommands_Swift_Create_Basic_Dim | 2780; valid for DimXpertManager and a selected Position tolerance; in the DimXpertManager, position_tol RMB menu > Recreate basic dim |
| swCommands_Swift_Fpo_Boss | 2755; DimXpert feature selector > Boss |
| swCommands_Swift_Fpo_Chamfer | 2754; DimXpert feature selector > Chamfer |
| swCommands_Swift_Fpo_Compound | 2665; DimXpert feature selector > Compound Hole |
| swCommands_Swift_Fpo_Cone | 2669; DimXpert feature selector > Cone |
| swCommands_Swift_Fpo_Constr_Circle | 2283; DimXpert feature selector > Intersect Circle |
| swCommands_Swift_Fpo_Constr_Line | 2282; DimXpert feature selector > Intersect Line |
| swCommands_Swift_Fpo_Constr_Plane | 2284; DimXpert feature selector > Intersect Plane |
| swCommands_Swift_Fpo_Constr_Point | 2281; DimXpert feature selector > Intersect Point |
| swCommands_Swift_Fpo_Contersink | 2667; DimXpert feature selector > Countersink |
| swCommands_Swift_Fpo_Counterbore | 2666; DimXpert feature selector > Counterbore |
| swCommands_Swift_Fpo_Cylinder | 2670; DimXpert feature selector > Cylinder |
| swCommands_Swift_Fpo_DimType_Angular | 2940; DimXpert feature selector > Angular Dimension |
| swCommands_Swift_Fpo_DimType_Linear | 2939; DimXpert feature selector > Linear Dimension |
| swCommands_Swift_Fpo_Fillet | 2753; DimXpert feature selector > Fillet |
| swCommands_Swift_Fpo_Hole | 2664; DimXpert feature selector > Hole |
| swCommands_Swift_Fpo_Notch | 2752; DimXpert feature selector > Notch |
| swCommands_Swift_Fpo_Ok | 2676; DimXpert feature selector > OK |
| swCommands_Swift_Fpo_Pattern | 2675; DimXpert feature selector > Pattern |
| swCommands_Swift_Fpo_Plane | 2663; DimXpert feature selector > Plane |
| swCommands_Swift_Fpo_Pocket | 2674; DimXpert feature selector > Pocket |
| swCommands_Swift_Fpo_Slot | 2672; DimXpert feature selector > Slot |
| swCommands_Swift_Fpo_Sphere | 2671; DimXpert feature selector > Sphere |
| swCommands_Swift_Fpo_Surf | 2662; DimXpert feature selector > Surface |
| swCommands_Swift_Fpo_Width | 2673; DimXpert feature selector > Width |
| swCommands_SwiftAddTaStudy | 2801; valid for SOLIDWORKS Premium assemblies whose parts have been assigned dimensions and tolerances; DimXpert toolbar > TolAnalystStudy |
| swCommands_SwiftDeleteAll | 596; valid for parts with assigned tolerances; DimXpert toolbar > Delete All Tolerances |
| swCommands_SwiftInsertAngleDimension | 3467; Adds a DimXpert angle dimension from the DimXPertManager tab; Tools menu > MBD Dimension > Angle Dimension... |
| swCommands_SwiftInsertBasicDimension | 3182; valid for parts; DimXpert toolbar > Basic Dimension |
| swCommands_SwiftInsertBasicSizeDimension | 3197; valid for parts; DimXpert toolbar > Basic Size Dimension |
| swCommands_SwiftInsertDatum | 593; valid for parts; DimXpert toolbar > Datum |
| swCommands_SwiftInsertDatumTarget | 3450; Inserts a DimXpert datum target; Tools menu > MBD Dimension > Datum Target |
| swCommands_SwiftInsertDimension | 592; valid for parts; DimXpert toolbar > Location Dimension |
| swCommands_SwiftInsertGeneralProfileTolerance | 3325; adds a Profile of Surface geometric tolerance to an open part; DimXpert toolbar > General Profile Tolerance |
| swCommands_SwiftInsertGtol | 594; valid for parts, opens the GeometricTolerance Properties dialog; DimXpert toolbar > Geometric Tolerance |
| swCommands_SwiftInsertPatternFeature | 627; valid for parts, opens the DimXpert Pattern/Collection PropertyManager page; DimXpert toolbar > Pattern Feature |
| swCommands_SwiftInsertSizeDimension | 625; valid for parts; DimXpert toolbar > Size Dimension |
| swCommands_SwiftRecognizeFeatures | 591; valid for parts; DimXpert toolbar > Auto Dimension Scheme |
| swCommands_SwiftShowConstraintStatus | 595; valid for parts; DimXpert toolbar > Show Tolerance Status |
| swCommands_SWPremium | 3432; SOLIDWORKS Premium |
| swCommands_SWUltimate | 3532; SOLIDWORKS Ultimate |
| swCommands_TabAndSlot | 3234; adds a tab and slot feature; Sheet Metal toolbar > Tab and Slot |
| swCommands_Table_Cell_Sub_Total | 1975; inserts "Sub-total" into a selected table cell |
| swCommands_Table_Cell_Total | 1976; inserts "Total" into a selected table cell |
| swCommands_TableDrivenPattern | 300; valid for parts with a selected sketch; Features toolbar > Table Driven Pattern |
| swCommands_TangentArc | 69; Layout Tools or Sketch toolbar > Tangent Arc |
| swCommands_TangentSnap | 528; valid during sketch creation only with parts that contain curves such as circles, arcs, fillets, parabolas, ellipses, partial ellipses, or splines; Quick Snaps toolbar > Tangent Snap |
| swCommands_Text | 109; Sketch toolbar > Text |
| swCommands_Thicken | 97; valid for a part with two or more knit surfaces, opens the Thicken PropertyManager page; Features toolbar > Thicken |
| swCommands_ThickenedCut | 98; valid for a part with two or more knit surfaces, opens the Cut-Thicken PropertyManager page; Features toolbar > Thickened Cut |
| swCommands_TileHorizontally | 581; Standard toolbar > Tile Horizontally |
| swCommands_TileVertically | 582; Standard toolbar > Tile Vertically |
| swCommands_TitleBlockDefine | 2852; valid for a drawing with its sheet format open, opens the Title Block Table PropertyManager page; Sheet Format toolbar > Title Block Fields |
| swCommands_TitleBlockEdit | 2853; valid for a drawing sheet format with a title block defined, opens the Title Block Table; in the FeatureManager design tree, sheet_folder > sheet_format_folder > title_block_table RMB menu > Title Block Fields |
| swCommands_TitleBlockEnterData | 2854; valid for a drawing sheet format with a title block defined, opens the Title Block Data PropertyManager page; in the FeatureManager design tree, sheet_folder > sheet_format_folder > title_block_table RMB menu > Enter Title Block Data |
| swCommands_TitleBlockTable | 2949; valid for parts and assemblies, opens the Title Block Table PropertyManager page; Table toolbar > Title Block Table |
| swCommands_Toggle_Context_Switch | 1990; CommandManager RMB menu > Use Large Buttons With Text |
| swCommands_Toggle_Grid | 1509; valid when inserting a Grid System; in the graphics area, RMB menu > Display Grid |
| swCommands_Toggle_MagMate | 3216; valid for assemblies only, toggles magnetic mates; alt-M or Tools menu or toolbar > Magnetic Mate ON/OFF |
| swCommands_Toggle_Magnified_Selection | 3135; Standard toolbar > Magnified Selection |
| swCommands_Toggle_Notes_UpperCase | 3105; toggles Note case to upper case; press F3 |
| swCommands_Toggle_Ole_Owner | 1555; valid for a drawing with a selected object; in the graphics area, ole_object RMB menu > Show on this sheet only |
| swCommands_Toggle_Pic_Texture | 1900; valid for a selected picture with a texture; in the graphics area, pic_with_texture RMB menu > Hide/Show Texture |
| swCommands_Toggle_Power_Dim_Mode | 2445; valid when Power Assist PropertyManager page is open; in the graphics area, RMB menu > DimXpert dimension toggle |
| swCommands_Toggle_Smart_Dim_Mode | 2444; valid when Power Assist PropertyManager page is open; in the graphics area, RMB menu > Smart dimension toggle |
| swCommands_Toggle_Viewing_Dir | 1593; valid for a selected drawing view arrow; in the graphics area, sel_view_arrow RMB menu > Toggle View Direction |
| swCommands_ToggleGraphicsDisplay | 3246; Tools toolbar > Display Graphics Components |
| swCommands_ToggleInstant2D | 3188; Sketch toolbar > Instant2D |
| swCommands_ToggleSelectionFilters | 273; Selection Filters toolbar > Toggle Selection Filters |
| swCommands_ToggleSelectionFilterToolbar | 356; Standard toolbar > Toggle Selection Filter Toolbar |
| swCommands_TolXpert | 612; alternative to swCommands_Toolbar_DimXpert; View menu > Toolbars > DimXpert |
| swCommands_Toogle_Bwrtree | 2446; valid in Full Screen mode; Full Screen toolbar > Hide/Show FeatureManager |
| swCommands_Toolbar_2dto3d | 1182; alternative to swCommands_2dto3d_Toolbar; View menu > Toolbars > 2D to 3D |
| swCommands_Toolbar_Adv_Struct_System | 3334; View menu > Toolbars > Structure System |
| swCommands_Toolbar_Align | 1180; alternative to swCommands_Align; View menu > Toolbars > Align |
| swCommands_Toolbar_Annotation | 1167; alternative to swCommands_Annotations; View menu > Toolbars > Annotation |
| swCommands_Toolbar_Assembly | 1155; alternative to swCommands_Assemblies; View menu > Toolbars > Assembly |
| swCommands_Toolbar_Context | 1205; View menu > Toolbars > CommandManager |
| swCommands_Toolbar_Curve | 1175; alternative to swCommands_Curves; View menu > Toolbars > Curves |
| swCommands_Toolbar_DimXpert | 1192; alternative to swCommands_TolXpert; View menu > Toolbars > DimXpert |
| swCommands_Toolbar_Display_States | 2809; View menu > Toolbars > Display States |
| swCommands_Toolbar_Drawing | 1156; alternative to swCommands_Drawings; View menu > Toolbars > Drawing |
| swCommands_Toolbar_Exploderoute | 1183; alternative to swCommands_ExplodeSketch; View menu > Toolbars > Explode Sketch |
| swCommands_Toolbar_Features | 1157; alternative to swCommands_Features; View menu > Toolbars > Features |
| swCommands_Toolbar_Font | 1166; alternative to swCommands_Fonts; View menu > Toolbars > Formatting |
| swCommands_Toolbar_Handsketch | 3242; valid only for a sketch opened in SOLIDWORKS running on supporting pen/stylus hardware; alternative to swCommands_Handsketch_Toolbar |
| swCommands_Toolbar_Inference | 1190; alternative to swCommands_ClickHereToSeeThePreview; View menu > Toolbars > Quick Snaps |
| swCommands_Toolbar_Inkmarkup | 3437; View menu > Toolbars > Markup |
| swCommands_Toolbar_Layer | 1180; alternative to swCommands_Layer_Toolbar; View menu > Toolbars > Layer |
| swCommands_Toolbar_Layout_Tools | 2816; alternative to swCommands_Layout; View menu > Toolbars > Layout Tools |
| swCommands_Toolbar_Lifecycle_And_Collaboration | 3484; For SOLIDWORKS Connected only; Activates the Lifecycle and Collaboration toolbar; View menu > Toolbars > Lifecycle and Collaboration |
| swCommands_Toolbar_Lineformat | 1165; alternative to swCommands_LineFormats; View menu > Toolbars > Line Format |
| swCommands_Toolbar_Macro | 1159; alternative to swCommands_Macros; View menu > Toolbars > Macro |
| swCommands_Toolbar_Mold | 1172; alternative to swComnmands_Molds; View menu > Toolbars > Mold Tools |
| swCommands_Toolbar_Office | 1187; alternative to swCommands_SolidworksOffice; View menu > Toolbars > SOLIDWORKS Add-ins |
| swCommands_Toolbar_OneClick | 3289; Tools menu > 3DEXPERIENCE Simulation Connector |
| swCommands_Toolbar_Refgeom | 1178; alternative to swCommands_ReferenceGeometry; View menu > Toolbars > Reference Geometry |
| swCommands_Toolbar_Render | 2963; alternative to swCommands_RenderToolbar; View menu > Toolbars > Render Tools |
| swCommands_Toolbar_ScreenCapture | 2812; alternative to swCommands_ScreenCaptureToolbar; View menu > Toolbars > Screen Capture |
| swCommands_Toolbar_Sel_Filter | 1160; alternative to swCommands_Filter_Toolbar; View menu > Toolbars > Selection Filter |
| swCommands_Toolbar_Sht_Mtl | 1173; alternative to swCommands_SheetMetal; View menu > Toolbars > Sheet Metal |
| swCommands_Toolbar_Sketch | 1161; alternative to swCommands_SketchToolbar; View menu > Toolbars > Sketch |
| swCommands_Toolbar_Sketch_Group | 2028; alternative to swCommands_Blocks; View menu > Toolbars > Blocks |
| swCommands_Toolbar_Sketch_Rels | 1162; alternative to swCommands_DimensionRelations; View menu > Toolbars > Dimensions/Relations |
| swCommands_Toolbar_Spline_Tools | 1185; alternative to swCommands_Splines; View menu > Toolbars > Spline Tools |
| swCommands_Toolbar_Standard | 1153; alternative to swCommands_Standard; View menu > Toolbars > Standard |
| swCommands_Toolbar_Stdview | 1169; alternative to swCommands_StandardViews; View menu > Toolbars > Standard Views |
| swCommands_Toolbar_Surface | 1174; alternative to swCommands_Surfaces; View menu > Toolbars > Surfaces |
| swCommands_Toolbar_Table | 1191; alternative to swCommands_EnterTheOffsetOfTheSupportArea; View menu > Toolbars > Table |
| swCommands_Toolbar_Tools | 1179; alternative to swCommands_Tools; View menu > Toolbars > Tools |
| swCommands_Toolbar_View | 1154; alternative to swCommands_View; View menu > Toolbars > View |
| swCommands_Toolbar_Web | 1164; alternative to swCommands_Web; View menu > Toolbars > Web |
| swCommands_Toolbar_Weldment | 1189; alternative to swCommands_Weldments; View menu > Toolbars > Weldments |
| swCommands_ToolingSplit | 464; valid for parts containing 3 surface bodies (core, cavity, and parting) and a selected face or plane perpendicular to the direction of pull; Mold Tools toolbar > Tooling Split |
| swCommands_Tools | 496 alternative to swCommands_Toolbar_Tools; View menu > Toolbars > Tools |
| swCommands_Tools_Addins | 1073; opens the Add-Ins dialog; Tools menu > Add-Ins |
| swCommands_Tools_Addview_Ff | 1245; valid for drawings with the Relative View PropertyManager page open, opens the Open dialog; in the graphics area, RMB menu > Insert From File |
| swCommands_Tools_Align_Horz | 889; valid for a selected drawing view; Tools > Align Drawing View > Horizontal Edge |
| swCommands_Tools_Align_Vert | 890; valid for a selected drawing view; Tools > Align Drawing View > Vertical Edge |
| swCommands_Tools_Arrange_Components | 1254; valid for assemblies, opens the Assembly Structure Editing dialog; Tools menu > Reorganize Components |
| swCommands_Tools_Configuration | 973; valid for parts and assemblies, opens the SOLIDWORKS ConfigurationManager dialog |
| swCommands_Tools_Crop_Delete | 1389; valid for a selected Crop View in a drawing; crop_view RMB menu > Crop View > Remove Crop |
| swCommands_Tools_Crop_Edit | 1388; valid for a selected Crop View in a drawing; crop_view RMB menu > Crop View > Edit Crop |
| swCommands_Tools_Customize | 1137; opens the Customize dialog; Tools menu > Customize |
| swCommands_Tools_Dim_Pref | 945; valid for an open model, opens the Document Properties dialog; in the FeatureManager design tree, top_level_document RMB menu > Document Properties |
| swCommands_Tools_Drw_Autoregen | 1573; valid for a selected drawing; in the FeatureManager design tree, drawing RMB menu > Automatic view update |
| swCommands_Tools_Drw_Dimtext_Link | 636; valid for a selected drawing; in the FeatureManager design tree, drawing RMB menu > Link external dim text |
| swCommands_Tools_Font_Tan | 1078; valid for parts; View menu > Display > Tangent Edges as Phantom |
| swCommands_Tools_Font_Tangent_Edges | 1546; valid for drawings for a selected view; View menu > Display > Tangent Edges With Font |
| swCommands_Tools_Hide_Dv | 979; valid for drawings; View menu > Hide / Show > Hidden Views |
| swCommands_Tools_Macro_Mru_1 | 2376; opens the first macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > first_macro |
| swCommands_Tools_Macro_Mru_2 | 2377; opens the second macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > second_macro |
| swCommands_Tools_Macro_Mru_3 | 2378; opens the third macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > third_macro |
| swCommands_Tools_Macro_Mru_4 | 2379; opens the fourth macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > fourth_macro |
| swCommands_Tools_Macro_Mru_5 | 2380; opens the fifth macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > fifth_macro |
| swCommands_Tools_Macro_Mru_6 | 2381; opens the sixth macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > sixth_macro |
| swCommands_Tools_Macro_Mru_7 | 2382; opens the seventh macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > seventh_macro |
| swCommands_Tools_Macro_Mru_8 | 2383; opens the eighth macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > eighth_macro |
| swCommands_Tools_Macro_Mru_9 | 2384; opens the ninth macro in the recent macros list in Microsoft Visual Basic for Applications; Tools menu > Macro > ninth_macro |
| swCommands_Tools_Remove_Tan | 1079; valid for parts; View menu > Display > Tangent Edges Removed |
| swCommands_Tools_Remove_Tangent_Edges | 1515; valid for drawings for a selected view; View menu > Display > Tangent Edges Removed |
| swCommands_Tools_Show_Tan | 1077; valid for parts; View menu > Display > Tangent Edges Visible |
| swCommands_Tools_Show_Tangent_Edges | 1545; valid for drawings for a selected view; View menu > Display > Tangent Edges Visible |
| swCommands_ToolsGrid | 2791; opens the Document Properties - Grid/Snap dialog; Sketch toolbar > Grid/Snap |
| swCommands_ToolsSensor | 2892; opens the Sensor PropertyManager page; Tools toolbar > Sensor |
| swCommands_Top | 163; View toolbar > View Orientation > Top |
| swCommands_Top_Left | 923; valid for a selected Excel-based BOM in a drawing view; Excel_BOM RMB menu > Anchor > Top Left |
| swCommands_Top_Right | 920; valid for a selected Excel-based BOM in a drawing view; Excel_BOM RMB menu > Anchor > Top Right |
| swCommands_Translate_Drawing | 638; valid for a drawing, opens the Move Drawing dialog; in the FeatureManager design tree, drawing RMB menu > Move |
| swCommands_Triad_Blob_Align_To | 2449; valid after component RMB menu > Move with Triad command in assembly; in the graphics area, triad_center_ball RMB menu > Align to |
| swCommands_TrimAsGroupWithPreAdvStructMember | 3362; trims with previous advanced structure member |
| swCommands_TrimAsIndAdvStructMember | 3363; trims as an individual advanced structural member |
| swCommands_TrimCornerCorner | 2792; valid for a flattened sheet metal part with a selected corner, opens the Corner-Trim PropertyManager page; Sheel Metal toolbar > Corner-Trim |
| swCommands_TrimEntities | 59; valid for an open sketch, opens the Trim PropertyManager page; Sketch or Layout Tools toolbar > Trim Entities |
| swCommands_Trimetric | 467; Standard Views toolbar > Trimetric |
| swCommands_TrimExtend | 466; valid for weldments, opens the Trim/Extend PropertyManager page; Weldment toolbar > Trim/Extend |
| swCommands_TrimSurface | 302; valid for a part with one or more selected surfaces, opens the Trim Surface PropertyManager page; Surfaces toolbar > Trim Surface |
| swCommands_Tube_Properties | 3012; valid for the SOLIDWORKS Routing add-in and a selected tube in an open flexible tube route; flex_tube RMB menu > Tube Properties |
| swCommands_Turn | 606; valid for a model with a camera; View menu > Modify > Turn Camera |
| swCommands_TwoViewHorizontal | 550; View toolbar > View Orientation > Two View - Horizontal |
| swCommands_TwoViewVertical | 551; View toolbar > View Orientation > Two View - Vertical |
| swCommands_Unblank_Atom_Body | 1028; in the FeatureManager design tree, click body_folder RMB context toolbar > Show |
| swCommands_Unblank_Atom_Body2 | 2731; valid for a part with a solid or surface body; in the FeatureManager design tree, body_folder > body RMB context toolbar > Show |
| swCommands_Unblank_Grid_Comp | 3001; valid for a part or assembly with the GridSystem PropertyManager page open and the grid feature component hidden; in the graphics area, RMB menu > Show |
| swCommands_Unblank_Origin_Sketch | 2469; valid for a hidden profile sketch; in the graphics area, prof_sketch RMB menu > Show |
| swCommands_Unblank_Part_Body | 1413; valid for a selected face of an atom feature in an assembly; in the graphics area, sel_face RMB menu > Show Solid Body |
| swCommands_Unblank_Pic_Feat | 2486; valid for a selected hidden picture feature object; in the graphics area, pic_feat RMB menu > Show |
| swCommands_Unblank_Refgeom | 896; valid for a selected reference geometry; in the FeatureManager design tree, ref_geom RMB menu > Show |
| swCommands_Unblank_Sketch | 955; valid for a selected drawing sketch; in the graphics area, sketch RMB menu > Show |
| swCommands_Unbreak_View | 1520; valid for a drawing break view; in the FeatureManager design tree, break_view RMB menu > Un-Break View |
| swCommands_Underive_Sketch | 1010; valid for a selected derived sketch; in the FeatureManager design tree, sketch_derived RMB menu > Underive |
| swCommands_Underline | 149; valid for selected text; Formatting toolbar > Underline |
| swCommands_Undo | 586; Standard toolbar > Undo |
| swCommands_Undo_Eq | 633; dialog resource Undo |
| swCommands_Unfix_Component | 959; valid for a selected fixed assembly component; in the FeatureManager design tree, comp RMB menu > Float |
| swCommands_Unfold | 326; valid for sheet metal parts; Sheet Metal toolbar > Unfold |
| swCommands_Unfreeze_All | 3014; valid for models where feature freeze is enabled, and the selected feature is frozen; in the FeatureManager design tree, feature RMB menu > Unfreeze All Features |
| swCommands_Ungroup | 327; valid for multi-selected annotations or dimensions; Align toolbar > Ungroup |
| swCommands_Unlink_Dim | 1544; valid for sketches with dimensions with shared parameters, opens the Shared Values dialog; in the graphics area, shared_dimension RMB menu > Unlink Value |
| swCommands_Unload_Hidden_Comps | 2868; valid for a selected assembly; in the FeatureManager design tree, top_level_assy RMB menu > Unload Hidden Components |
| swCommands_Unlock_Bom | 914; valid for a drawing view with an Excel-based Bill of Materials; in the graphics area, BOM_table RMB menu > Anchor > Unlock from Anchor |
| swCommands_Unlock_Configuration | 1846; valid in a PDM-enabled environment with a locked configuration; in ConfigurationManager, locked_config RMB menu > Unlock Configuration |
| swCommands_Unslant_Dim | 1533; valid for a selected dimension with a witness line that is slanted; in the graphics area, dim_with_slanted_witness RMB menu > Display Options > Remove Slant |
| swCommands_Unsuppress | 15; valid for one or more selected suppressed features; Edit menu > Unsuppress > This Configuration |
| swCommands_UnsuppressWithDependents | 50; valid for one or more selected suppressed features; Edit menu > Unsuppress with Dependents > This Configuration |
| swCommands_UntrimSurface | 400; valid for a part with a selected face or edge to patch, opens the Untrim Surface PropertyManager page; Surfaces toolbar > Untrim Surface |
| swCommands_Update_Cutlist | 2602; valid for a part with a selected Cut list folder; in the FeatureManager design tree, cut_list_folder RMB menu > Update |
| swCommands_Update_Msg | 2786; dialog resource Update |
| swCommands_Update_Std_View | 885; View toolbar > View Orientation > More options > Orientation dialog > Update Standard Views |
| swCommands_UpdateAllSpeedpakConfig | 3070; valid for assemblies; Assembly toolbar > Update Speedpak |
| swCommands_UpdateImportedModel | 3343; updates an imported model |
| swCommands_UpdateView | 385; valid for drawings with a selected view; Drawing toolbar > Update View |
| swCommands_User_Communities | 3463; Help menu > User Communities |
| swCommands_User_Defined_Route | 3189; valid for the SOLIDWORKS Routing or the SOLDWORKS Electrical add-in, opens the Projects Manager dialog; Routing or SOLIDWORKS Electrical: Application toolbar > User Defined Route |
| swCommands_User_Job_Cancel | 699; dialog resource Cancel |
| swCommands_User_Toolbar_Max | 1628; maximum allowed number of toolbar commands |
| swCommands_User_Toolbar_Min | 1627; minimum allowed number of toolbar commands |
| swCommands_Userdefined_Add_Fitting | 3165; valid for SOLIDWORKS Routing add-in with an open route; User Defined toolbar > Add Fitting |
| swCommands_Userdefined_Rt_On_Fly | 3166; valid for SOLIDWORKS Routing add-in with an open route; User Defined toolbar > Start at Point |
| swCommands_Userdefined_Rt_Properties | 3168; valid for SOLIDWORKS Routing add-in with an open route; User Defined toolbar > Route Properties |
| swCommands_UserMacro01 | 174; runs the first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro02 | 175; runs the second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro03 | 176; runs the third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro04 | 177; runs the fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro05 | 178; runs the fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro06 | 179; runs the sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro07 | 180; runs the seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro08 | 181; runs the eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro09 | 182; runs the ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro10 | 183; runs the tenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro11 | 184; runs the eleventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro12 | 185; runs the twelfth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro13 | 186; runs the thirteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro14 | 187; runs the fourteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro15 | 188; runs the fifteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro16 | 189; runs the sixteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro17 | 190; runs the seventeenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro18 | 191; runs the eighteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro19 | 192; runs the nineteenth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro20 | 193; runs the twentieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro21 | 194; runs the twenty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro22 | 195; runs the twenty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro23 | 196; runs the twenty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro24 | 197; runs the twenty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro25 | 198; runs the twenty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro26 | 199; runs the twenty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro27 | 200; runs the twenty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro28 | 201; runs the twenty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro29 | 202; runs the twenty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro30 | 203; runs the thirtieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro31 | 204; runs the thirty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro32 | 205; runs the thirty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro33 | 206; runs the thirty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro34 | 207; runs the thirty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro35 | 208; runs the thirty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro36 | 209; runs the thirty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro37 | 210; runs the thirty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro38 | 211; runs the thirty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro39 | 212; runs the thirty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro40 | 213; runs the fortieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro41 | 214; runs the forty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro42 | 215; runs the forty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro43 | 216; runs the forty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro44 | 217; runs the forty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro45 | 218; runs the forty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro46 | 219; runs the forty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro47 | 220; runs the forty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro48 | 221; runs the forty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro49 | 222; runs the forty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro50 | 223; runs the fiftieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro51 | 224; runs the fifty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro52 | 225; runs the fifty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro53 | 226; runs the fifty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro54 | 227; runs the fifty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro55 | 228; runs the fifty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro56 | 229; runs the fifty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro57 | 230; runs the fifty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro58 | 231; runs the fifty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro59 | 232; runs the fifty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro60 | 233; runs the sixtieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro61 | 234; runs the sixty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro62 | 235; runs the sixty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro63 | 236; runs the sixty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro64 | 237; runs the sixty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro65 | 238; runs the sixty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro66 | 239; runs the sixty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro67 | 240; runs the sixty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro68 | 241; runs the sixty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro69 | 242; runs the sixty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro70 | 243; runs the seventieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro71 | 244; runs the seventy-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro72 | 245; runs the seventy-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro73 | 246; runs the seventy-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro74 | 247; runs the seventy-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro75 | 248; runs the seventy-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro76 | 249; runs the seventy-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro77 | 250; runs the seventy-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro78 | 251; runs the seventy-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro79 | 252; runs the seventy-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro80 | 253; runs the eightieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro81 | 254; runs the eighty-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro82 | 255; runs the eighty-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro83 | 256; runs the eighty-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro84 | 257; runs the eighty-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro85 | 258; runs the eighty-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro86 | 259; runs the eighty-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro87 | 260; runs the eighty-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro88 | 261; runs the eighty-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro89 | 262; runs the eighty-ninth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro90 | 263; runs the nintieth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro91 | 264; runs the ninety-first macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro92 | 265; runs the ninety-second macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro93 | 266; runs the ninety-third macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro94 | 267; runs the ninety-fourth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro95 | 268; runs the ninety-fifth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro96 | 269; runs the ninety-sixth macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro97 | 270; runs the ninety-seventh macro defined by Macro toolbar > New Macro Button |
| swCommands_UserMacro98 | 271; runs the ninety-eighth macro defined by Macro toolbar > New Macro Button |
| swCommands_VerticalBreak | 110; valid for a drawing and a selected view; Drawing toolbar > Break |
| swCommands_VerticalDimension | 68; Dimensions/Relations toolbar > Vertical Dimension |
| swCommands_VerticalOrdinateDimension | 348; Dimensions/Relations toolbar > Vertical Ordinate Dimension |
| swCommands_View | 498; alternative to swCommands_Toolbar_View; View menu > Toolbars > View |
| swCommands_View_Animate_Collapse_Assembly | 1983; valid for an assembly with a selected exploded view, opens the Animation Controller dialog; in the ConfigurationManager, ExplView RMB menu > Animate collapse |
| swCommands_View_Animate_Explode_Assembly | 1982; valid for an assembly with a selected exploded view that was collapsed, opens the Animation Controller dialog; in the ConfigurationManager, ExplView RMB menu > Animate explode |
| swCommands_View_Assy_Full | 748; valid for an assembly with a component being edited in context; in the graphics area, RMB menu > Assembly Transparency > Force Transparency |
| swCommands_View_Assy_Maintain | 749; valid for an assembly with a component being edited in context; in the graphics area, RMB menu > Assembly Transparency > Maintain Transparency |
| swCommands_View_Assy_Opaque | 747; valid for an assembly with a component being edited in context; in the graphics area, RMB menu > Assembly Transparency > Opaque |
| swCommands_View_Clear_Select | 1541; valid in many contexts; pop-up menu item "Clear Selections" |
| swCommands_View_Collapse_Assembly | 995; valid for an assembly with a selected explode view; in the ConfigurationManager, exploded_view RMB menu > Collapse |
| swCommands_View_Disp_Hideall | 1810; View menu > Hide / Show > Hide All Types |
| swCommands_View_Edit_Perspective | 1043; valid for a perspective view, opens the Perspective View PropertyManager page; View menu > Modify > Perspective |
| swCommands_View_Explode_Assembly | 993; valid for an assembly with a selected explode view that is collapsed; in the ConfigurationManager, exploded_view RMB menu > Explode |
| swCommands_View_Fm_By_Dep | 1031; View menu > User Interface > FeatureManager Tree > By Dependencies |
| swCommands_View_Fm_By_Feat | 1030; View menu > User Interface > FeatureManager Tree > By Features |
| swCommands_View_Hide_Behind_Plane | 875; valid for a drawing document, opens the Hide Behind Plane dialog; in the FeatureManager design tree, ref_plane RMB menu > Hide Behind Plane |
| swCommands_View_Hideshow | 1390; valid for part or assembly with bodies, opens the Hide / Show Bodies PropertyManager page; View menu > Hide / Show > Bodies |
| swCommands_View_Lock_Camera | 1061; valid for a model with a selected camera in DisplayManager; in DisplayManager, Camera > Camera1 > RMB menu > Lock Camera |
| swCommands_View_Move_Manipulator | 1993; valid for assemblies; in the graphics area, comp RMB menu > Move with Triad |
| swCommands_View_Normal_To | 1640; valid for annotation, BOM, and title block tables; in the graphics area, table RMB menu > Normal To |
| swCommands_View_Orientation_Rmb | 916; valid in many contexts; in the graphics area, RMB menu > View Orientation |
| swCommands_View_Orientation_ViewBox | 3081; View toolbar > View Orientation > View Selector |
| swCommands_View_Query_Select | 891; valid in many contexts; in the graphics area, RMB menu > Select Other |
| swCommands_View_Rotate_About_Vertical | 3071; View menu > Modify > Rotate About Scene Floor |
| swCommands_View_Rotateminusx | 1472; Press DOWN ARROW |
| swCommands_View_Rotateminusy | 1469; Press LEFT ARROW |
| swCommands_View_Rotateminusz | 1471; Press Alt-LEFT ARROW |
| swCommands_View_Rotateplusx | 1473; Press UP ARROW |
| swCommands_View_Rotateplusy | 1468; Press RIGHT ARROW |
| swCommands_View_Rotateplusz | 1470; Press Alt-RIGHT ARROW |
| swCommands_View_Rotx_Minusninety | 1474; Press Shift-DOWN ARROW |
| swCommands_View_Rotx_Plusninety | 1475; Press Shift-UP ARROW |
| swCommands_View_Roty_Minusninety | 1476; Press Shift-LEFT ARROW |
| swCommands_View_Roty_Plusninety | 1477; Press Shift-RIGHT ARROW |
| swCommands_View_Ruler | 1303; valid for drawings; View menu > User Interface > Rulers |
| swCommands_View_Sheet_Next | 898; valid for drawings; View menu > Next Sheet |
| swCommands_View_Sheet_Previous | 897; valid for drawings; View menu > Previous Sheet |
| swCommands_View_ShowAnnotationTextExpression | 3538; View menu > Hide / Show > Annotation Text Expression |
| swCommands_View_Showantn_Linkerrors | 1895; View menu > Hide / Show > Annotation Link Errors |
| swCommands_View_Showantn_Linkvar | 2145; View menu > Hide / Show > Annotation Link Variables |
| swCommands_View_Showhide_Tb | 2756; View menu > User Interface > Toolbars |
| swCommands_View_This_Camera | 1060; valid for a selected camera; in the DisplayManager, camera RMB menu > Camera View |
| swCommands_View_Transminusx | 1479; Press Ctrl-LEFT ARROW |
| swCommands_View_Transminusy | 1481; Press Ctrl-UP ARROW |
| swCommands_View_Transplusx | 1478; Press Ctrl-RIGHT ARROW |
| swCommands_View_Transplusy | 1480; Press Ctrl-DOWN ARROW |
| swCommands_View_Undo_Last | 1584; valid for parts; View menu > Modify > Previous View |
| swCommands_View_Zoom_About_Center | 1803; View menu > Modify > Zoom About Screen Center |
| swCommands_View_Zoomin | 1482; Press Shift-Z |
| swCommands_View_Zoomout | 1483; Press Z |
| swCommands_View3DSketchDimensions | 562; View toolbar > View Sketch Dimensions |
| swCommands_View3DSketchPlane | 561; View toolbar > View 3D Sketch Plane |
| swCommands_ViewAllAnnotations | 404; View toolbar > View All Annotations |
| swCommands_ViewAssemAnnotations | 3120; View toolbar > View Top Level Annotations |
| swCommands_ViewAssemEnvelopes | 3423; View toolbar > View Top Level Envelopes |
| swCommands_ViewAxes | 339; View toolbar > View Axes |
| swCommands_ViewBendLines | 3468; Controls the visibility of bend lines; View menu > Hide / Show > Bend Lines or View toolbar > View Bend Lines |
| swCommands_ViewCameras | 608; View toolbar > View Cameras |
| swCommands_ViewCompAnnotations | 3119; View toolbar > View Component Annotations |
| swCommands_ViewCompEnvelopes | 3422; View toolbar > View Component Envelopes |
| swCommands_ViewCoordinateSystems | 153; View toolbar > View Coordinate Systems |
| swCommands_ViewCosmeticWeldSymbol | 3004; View toolbar > View Weld Beads |
| swCommands_ViewCurves | 402; View toolbar > View Curves |
| swCommands_ViewDatumReferenceFrame | 3184; View toolbar > View Datum Reference Frame |
| swCommands_ViewDecals | 2925; View toolbar > View Decals |
| swCommands_ViewDimNames | 2954; View toolbar > View Dimension Names |
| swCommands_ViewGlobalBBox | 3323; controls the visibility of the bounding box; View menu > View Bounding Box |
| swCommands_ViewLights | 607; View toolbar > View Lights |
| swCommands_ViewLiveSections | 2875; View toolbar > View Live Section Planes |
| swCommands_ViewOrientation | 341; Press SPACEBAR |
| swCommands_ViewOrigins | 126; View toolbar > View Origins |
| swCommands_ViewPartingLines | 547; View toolbar > View Parting Lines |
| swCommands_ViewPlanes | 338; View toolbar > View Planes |
| swCommands_ViewPoints | 511; View toolbar > View Points |
| swCommands_Viewport_Unsplit_Camera | 2185; valid when the Camera1 PropertyManager page is open; in the Camera1 PropertyManager page, click X . |
| swCommands_ViewRoutingPoints | 510; View toolbar > View Routing Points |
| swCommands_ViewSimResults | 3201; opens the View Simulation Results PropertyManager page; valid only if the SOLIDWORKS Simulation add-in is loaded, and Simulation study results are available for the current model; View toolbar > View Simulation Results |
| swCommands_ViewSimulationSymbol | 2992; View toolbar > View Simulation Symbols |
| swCommands_ViewSketches | 403; View toolbar > View Sketches |
| swCommands_ViewSketchRelations | 440; View toolbar > View Sketch Relations |
| swCommands_ViewTemporaryAxes | 99; View toolbar > View Temporary Axes |
| swCommands_Visual_State_Clear_Override | 785; valid for assemblies with display settings; in the Display Pane, RMB menu > Clear Override |
| swCommands_Visual_State_Clear_Override_All | 786; valid for assemblies with display settings; in the Display Pane, RMB menu > Clear All Top Level Overrides |
| swCommands_VisualizationTool | 2883; valid for assemblies; Assembly toolbar > Assembly Visualization |
| swCommands_Watch_Exit | 715; dialog resource Exit |
| swCommands_Watch_Start | 713; dialog resource Start |
| swCommands_Watch_Stop | 714; dialog resource Stop |
| swCommands_Web | 497; alternative to swCommands_Toolbar_Web; View menu > Toolbars > Web |
| swCommands_WebToolbar | 136; Standard toolbar > Web Toolbar |
| swCommands_Weld_Gap | 2981; valid for SOLIDWORKS Routing add-in with an open piping route; Piping toolbar > Weld Gap |
| swCommands_WeldBead | 2796; valid for sheet metal parts; Sheet Metal toolbar > Corners > Welded Corner |
| swCommands_Weldment | 450; valid for parts; Weldments toolbar > Weldment |
| swCommands_WeldmentCutList | 463; Table toolbar > Weldment Cut List |
| swCommands_Weldments | 508; alternative to swCommands_Toolbar_Weldment; View menu > Toolbars > Weldments |
| swCommands_WeldSymbol | 131; opens the Weld Symbol PropertyManager page and the ISO Weld Symbol Properties dialog; Annotation toolbar > Weld Symbol |
| swCommands_WeldTable | 3002; Table toolbar > Weld Table |
| swCommands_Whats_New_Html | 2951; opens the What's New in SOLIDWORKS year HTML page; Help menu > What's New > HTML |
| swCommands_Whats_New_Interactive | 1987; Help menu > What's New > Interactive |
| swCommands_Whats_New_Pdf | 2950; Help menu > What's New > PDF |
| swCommands_Whats_Wrong | 809; valid in many contexts; RMB menu > What's Wrong? |
| swCommands_Window_Closeall | 1033; Window menu > Close All |
| swCommands_Window_Redraw | 1494; View menu > Redraw |
| swCommands_Wireframe | 334; View toolbar > Wireframe |
| swCommands_Work_Offline | 3508; Standard toolbar > Work Offline ; Work for a limited time while disconnected from the 3DEXPERIENCE platform |
| swCommands_XRayToggleAssem | 3317; toggles transparency of the top-level assembly; Assembly toolbar > Top Level Transparency |
| swCommands_XRayTogglePart | 3318; toggles transparency of the part; Assembly toolbar > Top Level Transparency |
| swCommands_YUpViewOrientation | 3448 |
| swCommands_Zebra_Properties | 1805; valid for assemblies with Zebra Stripes, opens the Zebra Stripes PropertyManager page; View menu > Modify > Zebra Stripe Properties |
| swCommands_Zebra_Stripe_Preview | 2356; valid in several contexts, including when the Surface-Sweep PropertyManager page is open; in the graphics area, sweep_sketch RMB menu > Zebra Stripes Preview |
| swCommands_ZebraStripes | 365; valid for assemblies with Zebra Stripes; View menu > Display > Zebra Stripes |
| swCommands_Zone_Editor | 3144; valid for drawings open in a SOLIDWORKS debug build, and the ENABLE_ZONE_TAG_EDITOR debug variable is set, opens the Zone Tag Editor PropertyManager page; in the FeatureManager design tree, sheet > Sheet Format1 RMB menu > Zone Tag Editor |
| swCommands_ZoomInOut | 331; View toolbar > Zoom In/Out |
| swCommands_ZoomToArea | 333; View toolbar > Zoom to Area |
| swCommands_ZoomToFit | 332; View toolbar > Zoom to Fit |
| swCommands_ZoomToFitKey | 601; Press F |
| swCommands_ZoomToSelection | 354; View toolbar > Zoom to Selection |
| swCommands_ZoomtoSheet | 3121; valid for drawings; View toolbar > Zoom to Sheet |
| swCommands_ZUpViewOrientation | 3449 |

## See Also

[SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.html)
