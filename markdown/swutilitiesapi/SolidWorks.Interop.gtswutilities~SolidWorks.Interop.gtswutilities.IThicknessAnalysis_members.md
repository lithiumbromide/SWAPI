---
title: "IThicknessAnalysis Interface Members"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis_members"
member: ""
kind: "members"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html"
---

# IThicknessAnalysis Interface Members

The following tables list the members exposed by [IThicknessAnalysis](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Close | Ends the current session of a thickness analysis. |
| Method | GetAnalysisDetails | Gets the percentage of area and number of faces in each thickness range. |
| Method | GetAvgWeightedTckOnAnalArea | Gets the average weighted thickness on the analyzed area. |
| Method | GetAvgWeightedTckOnCritArea | Gets the average weighted thickness on the critical area. |
| Method | GetCriticalFeatureNames | Gets the names of the features that violate the target thickness. |
| Method | GetCriticalSurfaceArea | Gets the critical surface area. |
| Method | GetIntervalCount | Gets the number of intervals in the thickness color scale. |
| Method | GetMaxDeviationfromTargetThickness | Gets the maximum deviation from the target thickness. |
| Method | GetMaxTckOnAnalArea | Gets the maximum thickness of the analyzed area. |
| Method | GetMinTckOnAnalArea | Gets the minimum thickness of the analyzed area. |
| Method | GetNumCriticalFaces | Gets the number of critical faces in the analyzed area. |
| Method | GetNumCriticalFeatures | Gets the number of critical features in the analyzed area. |
| Method | GetThicknessAnalysisBody | Gets the SOLIDWORKS body in a multibody part selected for the thickness analysis. |
| Method | GetTotalSurfaceAreaAnalyzed | Gets the total surface area analyzed. |
| Method | Init | Initializes the Thickness Analysis utility with the active SOLIDWORKS document. |
| Method | RunThickAnalysis | Obsolete. Superseded by IThicknessAnalysis::RunThickAnalysis2 . |
| Method | RunThickAnalysis2 | Runs a thickness analysis, shows the thick regions, and generates a report. |
| Method | RunThinAnalysis | Obsolete. Superseded by IThicknessAnalysis::RunThinAnalysis2 . |
| Method | RunThinAnalysis2 | Runs a thickness analysis, shows the thin regions, and generates a report. |
| Method | SetThicknessAnalysisBody | Sets the SOLIDWORKS body in a multibody part to use in the thickness analysis. |

[Top](#topBookmark)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
