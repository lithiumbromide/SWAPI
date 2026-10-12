---
title: "Getting Started"
project: "SOLIDWORKS Utilities API Help"
interface: ""
member: ""
kind: "topic"
source: "swutilitiesapi/GettingStarted-swutilitiesapi.html"
---

# Getting Started

Writing a SOLIDWORKS Utilities application typically involves:

1. Opening the SOLIDWORKS Design document or documents, either interactively or programmatically.
2. Getting a pointer to the SOLIDWORKS Utilities interface.
3. If comparing faces on the SOLIDWORKS Design parts, [getting and setting the angular or position tolerances.](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IUtilOptions.html)
4. Any of these actions:

- [Analyzing the geometry of a part](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IGeometryAnalysis.html)
- [Comparing features of the documents](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareFeature.html)
- [Comparing geometry of the documents](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareGeometry.html)
- [Comparing properties of the documents](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareDocument.html)
- [Painting faces on the target part the same color as the source part](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFeaturePaint.html)
- [Running a PowerSelect session](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect.html)
- [Running a thickness analysis](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis.html)

1. Displaying or saving the results to a file.
2. Performing any necessary cleanup.
