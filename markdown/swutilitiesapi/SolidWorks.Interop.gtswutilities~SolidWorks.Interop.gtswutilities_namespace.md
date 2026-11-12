---
title: "SolidWorks.Interop.gtswutilities Namespace"
project: "SOLIDWORKS Utilities API Help"
interface: "SolidWorks.Interop.gtswutilities"
member: ""
kind: "namespace"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html"
---

# SolidWorks.Interop.gtswutilities Namespace

SOLIDWORKS Utilities API

## Interfaces

| Interface | Description |
| --- | --- |
| gtcocswCompareDocument | Compares the properties of two SOLIDWORKS documents. See ICompareDocument . |
| gtcocswCompareFeature | Identifies the differences in solid features between two versions of the same part. See ICompareFeature . |
| gtcocswCompareGeometry | Identifies the differences in geometry in both solid features and surface models between two versions of the same part. See ICompareGeometry . |
| gtcocswFeaturePaint | Allows you to copy the feature parameters from one feature in a SOLIDWORKS part to a feature in a different SOLIDWORKS part. See IFeaturePaint . |
| gtcocswFindReplaceAnnotations | Finds and replaces text for the annotations in the currently open part, assembly, or drawing document. See IFindReplaceAnnotations . |
| gtcocswGeometryAnalysis | Identifies geometric entities in a part that could cause a problem in other applications. See IGeometryAnalysis . |
| gtcocswPowerSelect | Allows selection of entities (edges, loops, faces, or features) in a part that meet the specified criteria. See IPowerSelect . |
| gtcocswThicknessAnalysis | Allows you to determine and analyze the thickness of a part. See IThicknessAnalysis . |
| gtcocswUtilities | Gets the SOLIDWORKS Utilities tool interface and options. See IUtilities . |
| gtcocswUtilOptions | Gets or sets the angular and position tolerance options when comparing faces. See IUtilOptions . |
| ICompareDocument | Compares the properties of two SOLIDWORKS documents. |
| ICompareFeature | Identifies the differences in solid features between two versions of the same part. |
| ICompareGeometry | Identifies the differences in geometry in both solid features and surface models between two versions of the same part. |
| IFeaturePaint | Allows you to copy the feature parameters from one feature in a SOLIDWORKS part to a feature in a different SOLIDWORKS part. |
| IFindReplaceAnnotations | Finds and replaces text for the annotations in the currently open part, assembly, or drawing document. |
| IGeometryAnalysis | Identifies geometric entities in a part that could cause a problem in other applications. |
| IPowerSelect | Allows selection of entities (edges, loops, faces, or features) in a part that meet the specified criteria. |
| IThicknessAnalysis | Allows you to determine and analyze the thickness of a part. |
| IUtilities | Gets the SOLIDWORKS Utilities tool interface and options. |
| IUtilOptions | Gets or sets the angular and position tolerance options when comparing faces. |

## Enumerations

| Enumeration | Description |
| --- | --- |
| gtCodOperationOption_e | Options for comparing documents. Bitmask . |
| gtError_e | Error codes returned by SOLIDWORKS Utilities APIs. |
| gtFraFilterType_e | Types of annotations. Bitmask . |
| gtFraOptionType_e | Options to use to filter a search for a find and replace annotation operation. Bitmask . |
| gtGdfOperationOption_e | Comparison options. |
| gtpslEdgeAngleOperator_e | Edge-angle operator types for IPowerSelect . |
| gtpslFeatureType_e | Feature type IDs for IPowerSelect . |
| gtpslFilterType_e | Filter types for IPowerSelect . Bitmask . |
| gtPslSelectionType_e | Select types for IPowerSelect . Bitmask . |
| gtResultOptions_e | Options for results reporting. |
| gtSwTools_e | Tool IDs for IUtilities::GetToolInterface . |
| gttckResolutionOptions_e | Resolution options for IThicknessAnalysis . |
| gtVolDiffStatusOptionType_e | Error types returned by ICompareGeometry::CompareGeometry3 . |

## See Also

[SolidWorks.Interop.gtswutilities Assembly](SolidWorks.Interop.gtswutilities.html)
