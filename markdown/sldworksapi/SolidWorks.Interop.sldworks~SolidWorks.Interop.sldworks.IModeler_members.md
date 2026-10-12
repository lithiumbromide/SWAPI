---
title: "IModeler Interface Members"
project: "SOLIDWORKS API Help"
interface: "IModeler_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html"
---

# IModeler Interface Members

The following tables list the members exposed by [IModeler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | GeneralTopology | Gets or sets the Parasolid option to create general (non-manifold) bodies. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CheckInterference | Obsolete. Superseded by IModeler::CheckInterference3 . |
| Method | CheckInterference3 | Checks for interferences among the specified bodies in a part. |
| Method | CheckInterferenceBetweenTwoBodies | Checks for interference between the specified bodies in an assembly. |
| Method | CopyWizardHole | Copies hole data from the source hole to the destination hole. |
| Method | CreateArc | Creates an arc. |
| Method | CreateBodiesFromSheets | Obsolete. Superseded by IModeler::CreateBodiesFromSheets2 . |
| Method | CreateBodiesFromSheets2 | Sews sheets to make sheet (surface) or solid bodies. |
| Method | CreateBodyFromBox | Obsolete. Superseded by IModeler::CreateBodyFromBox3 . |
| Method | CreateBodyFromBox3 | Creates a temporary body from the specified box dimensions. |
| Method | CreateBodyFromCone | Creates a temporary body from cone dimensions. |
| Method | CreateBodyFromCyl | Creates a temporary body from cylinder dimensions. |
| Method | CreateBodyFromFaces2 | Creates a temporary body from a list of faces. |
| Method | CreateBrepBody | Obsolete. Superseded by IModeler::CreateBrepBody3 . |
| Method | CreateBrepBody3 | Creates a temporary body from BREP (boundary representation) data. |
| Method | CreateBsplineCurve | Creates a b-spline curve. |
| Method | CreateBsplineSurface | Creates a b-spline surface. |
| Method | CreateConicalSurface | Obsolete. Superseded by IModeler::CreateConicalSurface2 . |
| Method | CreateConicalSurface2 | Creates an untrimmed conical surface. |
| Method | CreateCoonsBSurface | Creates a coons b-surface using the four specified boundary curves. |
| Method | CreateCylindricalSurface | Obsolete. Superseded by IModeler::CreateCylindricalSurface2 . |
| Method | CreateCylindricalSurface2 | Creates an untrimmed cylindrical surface. |
| Method | CreateEllipse | Creates a temporary elliptical curve. |
| Method | CreateExtrudedBody | Creates a temporary extruded body. |
| Method | CreateExtrusionSurface | Creates an extruded surface. |
| Method | CreateLine | Creates a line. |
| Method | CreateLoftBody | Obsolete. Superseded by IModeler::CreateLoftBody2 . |
| Method | CreateLoftBody2 | Creates a loft body using the specified profiles, guide curves, and centerline. |
| Method | CreateLoftSurface | Creates a loft surface. |
| Method | CreateOffsetSurface | Creates a surface that is offset from an existing surface. |
| Method | CreatePCurve | Creates a pcurve. |
| Method | CreatePlanarSurface | Obsolete. Superseded by IModeler::CreatePlanarSurface2 . |
| Method | CreatePlanarSurface2 | Creates a new infinite planar surface. |
| Method | CreateRuledSurface | Creates a ruled surface from the curves. |
| Method | CreateRuledSurfaceFromEdge | Creates a ruled surface using the specified edges and returns a surface body. |
| Method | CreateSheetFromFaces | Creates a sheet (surface) body from connected faces. |
| Method | CreateSheetFromSurface | Creates a sheet (surface) body from a surface. |
| Method | CreateSphericalSurface | Obsolete. Superseded by IModeler::CreateSphericalSurface2 . |
| Method | CreateSphericalSurface2 | Creates an untrimmed spherical surface. |
| Method | CreateSpring | Creates the geometry for a spring. |
| Method | CreateSweptBody | Creates a swept body. |
| Method | CreateSweptSurface | Creates a swept surface from a curve. |
| Method | CreateToroidalSurface | Creates an untrimmed toroidal surface from the specified arguments. |
| Method | CreateWireBody | Creates a wire body from the input entities, which can be edges or curves. |
| Method | DeleteFacesFromSheetBody | Deletes the unused faces of the sheet body. |
| Method | FindTwoEdgeMaxDeviation | Finds the maximum distance between two edges. |
| Method | GetBodyOutline | Obsolete. Superseded by IModeler::GetBodyOutline2 . |
| Method | GetBodyOutline2 | Gets the curves that form the outline of a body. |
| Method | GetInitKnitGapWidth | Gets the initial gap bound width for knitting a body. |
| Method | GetManifoldBodiesCount | Gets the number of manifold bodies created from the specified non-manifold body. |
| Method | GetToleranceValue | Gets the current tolerance value of the given tolerance ID. |
| Method | ICheckInterference | Obsolete. Superseded by IModeler::ICheckInterference2 . |
| Method | ICheckInterference2 | Obsolete. Superseded by IModeler::ICheckInterference3 . |
| Method | ICheckInterference3 | Checks the interference among the specified bodies. |
| Method | ICheckInterferenceCount | Obsolete. Superseded by IModeler::ICheckInterferenceCount2 . |
| Method | ICheckInterferenceCount2 | Obsolete. Superseded by IModeler::ICheckInterferenceCount3 . |
| Method | ICheckInterferenceCount3 | Checks interference among the specified bodies and returns the number of interferences. |
| Method | ICopyWizardHole | Copies hole data from the source hole to the destination hole. |
| Method | ICreateArc | Creates an arc. |
| Method | ICreateBodiesFromSheets | Obsolete. Superseded by IModeler::ICreateBodiesFromSheets2 . |
| Method | ICreateBodiesFromSheets2 | Sews sheets to make a sheet (surface) or solid bodies. |
| Method | ICreateBodyFromBox | Obsolete. Superseded by IModeler::ICreateBodyFromBox2 . |
| Method | ICreateBodyFromBox2 | Obsolete. Superseded by IModeler::CreateBodyFromBox3 . |
| Method | ICreateBodyFromCone | Obsolete. Superseded by IModeler::ICreateBodyFromCone2 . |
| Method | ICreateBodyFromCone2 | Creates a temporary body from cone dimensions. |
| Method | ICreateBodyFromCyl | Obsolete. Superseded by IModeler::ICreateBodyFromCyl2 . |
| Method | ICreateBodyFromCyl2 | Creates a temporary body from cylinder dimensions. |
| Method | ICreateBodyFromFaces | Obsolete. Superseded by IModeler::ICreateBodyFromFace3 . |
| Method | ICreateBodyFromFaces2 | Obsolete. Superseded by IModeler::ICreateBodyFromFace3 . |
| Method | ICreateBodyFromFaces3 | Creates a temporary body from a list of faces. |
| Method | ICreateBrepBody | Obsolete. Superseded by IModeler::ICreateBrepBody3 . |
| Method | ICreateBrepBody2 | Obsolete. Superseded by IModeler::ICreateBrepBody3 . |
| Method | ICreateBrepBody3 | Creates a temporary body from BREP (boundary representation) data. |
| Method | ICreateBsplineCurve | Creates a b-spline curve. |
| Method | ICreateBsplineSurface | Creates a b-spline surface. |
| Method | ICreateConicalSurface | Obsolete. Superseded by IModeler::ICreateConicalSurface2 . |
| Method | ICreateConicalSurface2 | Creates an untrimmed conical surface. |
| Method | ICreateCylindricalSurface | Obsolete. Superseded by IModeler::ICreateCylindricalSurface2 . |
| Method | ICreateCylindricalSurface2 | Creates an untrimmed cylindrical surface. |
| Method | ICreateEllipse | Creates a temporary elliptical curve. |
| Method | ICreateExtrusionSurface | Creates an extruded surface. |
| Method | ICreateLine | Creates a line. |
| Method | ICreateLoftSurface | Creates a loft surface. |
| Method | ICreateOffsetSurface | Creates a surface that is offset from an existing surface. |
| Method | ICreatePCurve | Creates a pcurve. |
| Method | ICreatePlanarSurface | Obsolete. Superseded by IModeler::ICreatePlanarSurface2 . |
| Method | ICreatePlanarSurface2 | Creates a new infinite planar surface. |
| Method | ICreateRuledSurface | Creates a ruled surface from the curves. |
| Method | ICreateRuledSurfaceFromEdge | Creates a ruled surface using the specified edges and returns a surface body. |
| Method | ICreateSheetFromFaces | Creates a sheet (surface) body from connected faces. |
| Method | ICreateSheetFromSurface | Obsolete. Superseded by IModeler::ICreateSheetFromSurface2 . |
| Method | ICreateSheetFromSurface2 | Creates a sheet (surface) body from a surface. |
| Method | ICreateSphericalSurface | Obsolete. Superseded by IModeler::ICreateSphericalSurface2 . |
| Method | ICreateSphericalSurface2 | Creates an untrimmed spherical surface. |
| Method | ICreateSweptSurface | Creates a swept surface from a curve. |
| Method | ICreateToroidalSurface | Creates an untrimmed toroidal surface from the specified arguments. |
| Method | ICreateWireBody | Creates a wire body from the input entities, which can be edges or curves. |
| Method | IDeleteFacesFromSheetBody | Deletes the unused faces of the sheet body. |
| Method | IFindTwoEdgeMaxDeviation | Finds the maximum distance between two edges. |
| Method | IImprintingFaces | Imprints the specified tool faces onto the specified target faces. |
| Method | IImprintingFacesCount | Obsolete. Superseded by IModeler::IImprintingFacesCount2 . |
| Method | IImprintingFacesCount2 | Gets the number of imprinted edges and vertices in the model. |
| Method | IMakeManifoldBodies | Creates manifold bodies from the specified non-manifold body. |
| Method | IMergeCurves | Merges multiple curves into one curve. |
| Method | ImprintingFaces | Imprints the specified tool faces onto the specified target faces. |
| Method | IReplaceSurfaces | Obsolete. Superseded by IModeler::IReplaceSurfaces2 . |
| Method | IReplaceSurfaces2 | Replaces the surfaces of the given faces. |
| Method | IRestore | Obsolete. Superseded by IModeler::IRestore2 . |
| Method | IRestore2 | Restores a temporary body object from the specified stream. |
| Method | ISplitFaceOnParam | Obsolete. Superseded by IModeler::ISplitFaceOnParam2 . |
| Method | ISplitFaceOnParam2 | Splits and retrieves the faces on the U or V parameter. |
| Method | ISplitFaceOnParamCount | Obsolete. Superseded by IModeler::ISplitFaceOnParamCount2 . |
| Method | ISplitFaceOnParamCount2 | Sets up and counts the number of new faces split on the U or V parameter. |
| Method | MakeManifoldBodies | Creates manifold bodies from the specified non-manifold body. |
| Method | MergeCurves | Merges multiple curves into one curve. |
| Method | ProjectCurveOnSurface | Projects a curve on a surface. |
| Method | ReplaceSurfaces | Replaces the surfaces of the given faces. |
| Method | Restore | Restores a temporary body object from the specified stream. |
| Method | SetInitKnitGapWidth | Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, IBody2::CreateBodyFromSurfaces . |
| Method | SetTolerances | Obsolete. Superseded by IModeler::GetToleranceValue and IModeler::SetToleranceValue . |
| Method | SetToleranceValue | Sets tolerances governing geometry output. |
| Method | SplitFaceOnParam | Splits and retrieves the faces on the U or V parameter |
| Method | ThickenSheet | Thickens a sheet body. |
| Method | UnsetTolerances | Sets the tolerances back to system settings. |

[Top](#topBookmark)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
