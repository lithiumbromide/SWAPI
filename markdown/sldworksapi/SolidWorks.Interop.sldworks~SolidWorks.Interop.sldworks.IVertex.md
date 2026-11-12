---
title: "IVertex Interface"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html"
---

# IVertex Interface

Represents the start or end of an [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IVertex
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
```

### C#

```csharp
public interface IVertex
```

### C++/CLI

```cpp
public interface class IVertex
```

## VBA Syntax

See [Vertex](ms-its:sldworksapivb6.chm::/sldworks~Vertex.html).

## Examples

[Display Vertices (VBA)](Display_Vertices_Example_VB.htm)
[Get Maximum Edge and Vertex Gaps (VBA)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VB.htm)
[Get Maximum Edge and Vertex Gaps (VB.NET)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VBNET.htm)
[Get Maximum Edge and Vertex Gaps (C#)](Get_Maximum_Edge_and_Vertex_Gaps_Example_CSharp.htm)

## Remarks

This interface allows you to get the associated edges in an enumerated list or the coordinates of the vertex.

## Accessors

[IAdvancedHoleElementData::SelectionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~SelectionEntity.html)

[IBeltChainFeatureData::BeltLocationPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLocationPlane.html)

[IBody2::AddVertexPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~AddVertexPoint.html) and [IBody2::IAddVertexPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddVertexPoint.html)

[IBody2::GetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetVertices.html) and [IBody2::IGetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetVertices.html)

[ICamFollowerMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData~EntitiesToMate.html)

[IChainPatternFeatureData::Group1PathLink1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.html)

[IChainPatternFeatureData::Group1PathLink2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.html)

[IChainPatternFeatureData::Group2PathLink1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)

[IChainPatternFeatureData::Group2PathLink2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html)

[IChamferFeatureData2::Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~Vertex.html) and [IChamferFeatureData2::IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~IVertex.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html)

[IEdge::GetEndVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetEndVertex.html) and [IEdge::IGetEndVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetEndVertex.html)

[IEdge::GetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetStartVertex.html) and [IEdge::IGetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetStartVertex.html)

[IFacet::GetFacetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet~GetFacetVertices.html)

[FillPatternFeatureData::SeedFeatureCenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SeedFeatureCenter.html)

[IHingeMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate.html)

[IIndentFeatureData::ToolBodyRegion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.html)

[ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html)

[ILinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndSeedReference.html)

[ILinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndReference.html)

[ILinearPatternFeatureData::D2EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndSeedReference.html)

[ILocalCurvePatternFeatureData::SelectedPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~SelectedPoint.html)

[ILocalLinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference.html)

[ILocalLinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndSeedReference.html)

[ILocalLinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndReference.html)

[ILocalLinearPatternFeatureData::D2EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndSeedReference.html)

[ILoop2::GetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetVertices.html) and [ILoop2::IGetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetVertices.html)

[IModeler::ImprintingFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ImprintingFaces.html) and [IModeler::IImprintingFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IImprintingFaces.html)

[IMoveCopyBodyFeatureData::TransofrmReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html)

[IMoveCopyBodyFeatureData::TranslateToVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TranslateToVertex.html)

[IMoveFaceFeatureData::GetEndConditionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)

[IPrimaryMemberPointLengthFeatureData::GetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~GetPoints.html)

[ISecondaryMemberUpToMembersFeatureData::GetFromPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPoint.html)

[ISecondaryMemberUpToMembersFeatureData::GetPointMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetPointMemberPairs.html)

[ISimpleFilletFeatureData2::GetSetbackVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.html) and [ISimpleFilletFeatureData2::IGetSetbackVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.html)

[ISimpleFilletFeatureData2::HelpPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html)

[ISimpleHoleFeatureData2::Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~Vertex.html) and [ISimpleHoleFeatureData2::IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IVertex.html)

[ISketchPatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.html)

[ISMGussetFeatureData::ReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html)

[ISurfaceExtendFeatureData::Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceExtendFeatureData~Vertex.html)

[ISurfaceFlattenFeatureData::FixPointVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~FixPointVertex.html)

[ISurfExtrudeFeatureData::GetVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.html) and [ISurfExtrudeFeatureData::IGetVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.html)

[ISweepFeatureData::EndDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndDirectionVector.html)

[ISweepFeatureData::StartDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartDirectionVector.html)

[ISymmetricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.html)

[ITabAndSlotGroupData::SelectionEndReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint.html)

[ITabAndSlotGroupData::SelectionStartReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint.html)

[ITablePatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.html)

[IThreadFeatureData::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.html)

[IThreadFeatureData::ProfileLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ProfileLocation.html)

[IThreadFeatureData::StartEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~StartEntity.html)

[IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.html)

[IVariableFilletFeatureData2::GetSetbackVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.html) and [IVariableFilletFeatureData2::IGetSetbackVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.html)

[IWizardHoleFeatureData2::Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~Vertex.html) and [IWizardHoleFeatureData2::IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html)

## Access Diagram

[Vertex](SWObjectModel.pdf#Vertex)

## See Also

[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
