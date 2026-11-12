---
title: "IVariableFilletFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html"
---

# IVariableFilletFeatureData2 Interface Members

The following tables list the members exposed by [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AsymmetricFillet | Gets or sets whether this variable radius fillet is asymmetric. |
| Property | ConicTypeForCrossSectionProfile | Gets or sets the type of profile for this fillet. |
| Property | CurvatureContinuous | Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature. |
| Property | DefaultConicRhoOrRadius | Gets or sets the default conic rho or conic radius of this fillet. |
| Property | DefaultDistance | Gets or sets the default Distance 2 radius of this asymmetric fillet. |
| Property | DefaultRadius | Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet. |
| Property | FilletEdgeCount | Gets the number of edges to fillet. |
| Property | OverflowType | Gets or sets the overflow type for this variable fillet feature. |
| Property | PropagateFeatureToParts | Gets or sets whether to extend the fillet feature to all affected parts in the assembly. |
| Property | PropagateToTangentFaces | Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge. |
| Property | TransitionType | Gets or sets the type of transition between this variable fillet and an adjacent fillet. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections used to define the variable fillet feature. |
| Method | GetConicRhoOrRadius | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | GetConicRhoOrRadius2 | Gets the conic rho or radius at the specified vertex. |
| Method | GetControlPointConicRhoOrRadiusAtIndex | Gets the conic rho or radius at the specified control point. |
| Method | GetControlPointDistanceAtIndex | Gets the Distance 2 radius at the specified control point for the asymmetric fillet. |
| Method | GetControlPointRadiusAtIndex | Gets the radius at the specified control point. |
| Method | GetControlPointsCount | Gets the number of intermediate control points on this variable fillet feature. |
| Method | GetDistance | Gets the Distance 2 radius for this asymmetric fillet. |
| Method | GetFilletEdgeAtIndex | Gets the fillet edge at the specified index. |
| Method | GetRadius | Obsolete. Superseded by IVariableFilletFeatureData2::GetRadius2 . |
| Method | GetRadius2 | Gets the value of the Distance 1 radius at the specified vertex. |
| Method | GetSetbackDistanceCount | Gets the number of setback distances for the specified vertex on this variable fillet feature. |
| Method | GetSetbackVertexDistance | Gets the setback distance for the specified vertex on this variable fillet feature. |
| Method | GetSetbackVertices | Gets the setback vertices for this variable fillet feature. |
| Method | GetSetbackVerticesCount | Gets the number of setback vertices for this variable fillet feature. |
| Method | IAccessSelections | Gains access to the selections used to define the variable fillet feature. |
| Method | IGetConicRhoOrRadius | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | IGetFilletEdgeAtIndex | Gets the fillet edge at the specified index. |
| Method | IGetRadius | Obsolete. Superseded by IVariableFilletFeatureData2::Radius2 . |
| Method | IGetSetbackVertexDistance | Gets the setback distance for the specified vertex on this variable fillet feature. |
| Method | IGetSetbackVertices | Gets the setback vertices for this variable fillet feature. |
| Method | ISetConicRhoOrRadius | Sets the conic rho, conic radius, or circular radius of this fillet. |
| Method | ISetRadius | Sets the radius value for specified fillet item. |
| Method | ISetSetbackVertexDistance | Sets the setback distance for the specified vertex and its edges on this variable fillet feature. |
| Method | ISetSetbackVertices | Sets the setback vertices for this variable fillet feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the variable fillet feature. |
| Method | SetConicRhoOrRadius | Sets the conic rho or radius for the specified fillet item. |
| Method | SetControlPointConicRhoOrRadiusAtIndex | Sets the conic rho or radius at the specified control point. |
| Method | SetControlPointDistanceAtIndex | Sets the Distance 2 radius at the specified control point for the asymmetric fillet. |
| Method | SetControlPointRadiusAtIndex | Sets the radius at the specified control point. |
| Method | SetDistance | Sets the Distance 2 radius for this asymmetric fillet. |
| Method | SetRadius | Sets the value of the Distance 1 radius at the specified vertex. |
| Method | SetSetbackVertexDistance | Sets the setback distances on fillet edges from the specified fillet corner vertex on this variable fillet feature. |
| Method | SetSetbackVertices | Sets the setback vertices for this variable fillet feature. |

[Top](#topBookmark)

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
