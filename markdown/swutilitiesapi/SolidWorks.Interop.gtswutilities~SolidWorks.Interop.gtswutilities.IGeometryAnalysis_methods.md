---
title: "IGeometryAnalysis Interface Methods"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis_methods"
member: ""
kind: "methods"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_methods.html"
---

# IGeometryAnalysis Interface Methods

For a list of all members of this type, see [IGeometryAnalysis members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Close | Performs any necessary cleanup after the geometry analysis finishes. |
| Method | GetDiscontinuousEdgesCount | Gets the number of discontinuous edges in the part. |
| Method | GetDiscontinuousFacesCount | Gets the number of discontinuous faces in the part. |
| Method | GetKnifeEdgesCount | Gets the number of knife edges in the part. |
| Method | GetKnifeVerticesCount | Gets the number of knife vertices in the part. |
| Method | GetShortEdgesCount | Gets the number of edges shorter than the specified length on the part. |
| Method | GetSliverFacesCount | Gets the number of sliver faces in the part. |
| Method | GetSmallFacesCount | Gets the number of small faces on the part. |
| Method | Init | Initiates geometry analysis for the model document. |
| Method | SaveReport | Obsolete. Superseded by IGeometryAnalysis::SaveReport2 . |
| Method | SaveReport2 | Generates a report containing the results of the geometry analysis. |
| Method | ShowResultsDialog | Displays the results of the geometry analysis in the Results dialog box. |

[Top](#topBookmark)

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
