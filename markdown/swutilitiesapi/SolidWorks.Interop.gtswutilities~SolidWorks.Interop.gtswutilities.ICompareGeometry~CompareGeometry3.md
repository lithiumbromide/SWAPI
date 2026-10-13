---
title: "CompareGeometry3 Method (ICompareGeometry)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareGeometry"
member: "CompareGeometry3"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry~CompareGeometry3.html"
---

# CompareGeometry3 Method (ICompareGeometry)

Identifies the differences in geometry in the solid features and surface models between two versions of the same part and generates a report.

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareGeometry3( _
   ByVal reffile As System.String, _
   ByVal refconfig As System.String, _
   ByVal modfile As System.String, _
   ByVal modconfig As System.String, _
   ByVal lOperationOptions As System.Integer, _
   ByVal lResultOptions As System.Integer, _
   ByVal reportname As System.String, _
   ByVal vtAddToBinderOption As System.Boolean, _
   ByVal vtOverwrite As System.Boolean, _
   ByRef volDiffStatus As System.Integer, _
   ByRef faceDiffStatus As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareGeometry
Dim reffile As System.String
Dim refconfig As System.String
Dim modfile As System.String
Dim modconfig As System.String
Dim lOperationOptions As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim volDiffStatus As System.Integer
Dim faceDiffStatus As System.Integer
Dim value As System.Integer

value = instance.CompareGeometry3(reffile, refconfig, modfile, modconfig, lOperationOptions, lResultOptions, reportname, vtAddToBinderOption, vtOverwrite, volDiffStatus, faceDiffStatus)
```

### C#

```csharp
System.int CompareGeometry3(
   System.string reffile,
   System.string refconfig,
   System.string modfile,
   System.string modconfig,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite,
   out System.int volDiffStatus,
   out System.int faceDiffStatus
)
```

### C++/CLI

```cpp
System.int CompareGeometry3(
   System.String^ reffile,
   System.String^ refconfig,
   System.String^ modfile,
   System.String^ modconfig,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite,
   [Out] System.int volDiffStatus,
   [Out] System.int faceDiffStatus
)
```

### Parameters

- `reffile`: Path and filename of the SOLIDWORKS document containing the referenced part
- `refconfig`: Name of reference part's configuration; if blank, then the active configuration is used
- `modfile`: Path and filename of the SOLIDWORKS document containing the modified part
- `modconfig`: Name of modified part's configuration
- `lOperationOptions`: Compare face, volume, or face and volume options as defined by [gtGdfOperationOption_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtGdfOperationOption_e.html)
- `lResultOptions`: Display the results or save the results to a report as defined by [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html)
- `reportname`: Path where to save the results report
- `vtAddToBinderOption`: True to add the results report to the Design Binder, false to not
- `vtOverwrite`: True to overwrite an existing results report of the same name, false to not
- `volDiffStatus`: Error types for volume differences as defined in [gtVolDiffStatusOptionType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtVolDiffStatusOptionType_e.html)
- `faceDiffStatus`: Error types for face differences as defined in [gtVolDiffStatusOptionType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtVolDiffStatusOptionType_e.html)

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareGeometry::CompareGeometry3](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareGeometry~CompareGeometry3.html).

## Examples

[Compare Geometry (VBA)](Compare_Geometry_VB6.htm)
[Compare Geometry (VB.NET)](Compare_Geometry_VBNET.htm)
[Compare Geometry (C#)](Compare_Geometry_CSharp.htm)
[Set Tolerances and Compare Geometry (VBA)](Set_Tolerances_and_Compare_Geometry_VB6.htm)
[Set Tolerances and Compare Geometry (VB.NET)](Set_Tolerances_and_Compare_Geometry_VBNET.htm)
[Set Tolerances and Compare Geometry (C#)](Set_Tolerances_and_Compare_Geometry_CSharp.htm)

## Remarks

The vtAddToBinderOption argument is disabled when comparing:

- Two documents with the same name, but located in different folders, or
- Two configurations of the same part, or
- Documents selected from the PDM vault

because the documents are saved as temporary files during the comparison.

This method returns a value that reflects the status of the last command executed (face comparison, volume comparison, or report generation).

Before face and volume comparisons are made, certain checks occur to ascertain the sanity of the proposed comparison.

If validation:

- fails, then the out parameters, volDiffStatus/faceDiffStatus, contain gtVolDiffStatusOptionType_e.gtNotPerformed and this method may return one of the following gt_error:

  - gtErrUtilityAlreadyRunning
  - gtErrCompGeomInvalidRefFile
  - gtErrCompGeomInvalidModFile
  - gtErrDocsAreSame
  - gtErrDocsConfigsAreSame
  - gtErrCompGeomOperationOptions
  - gtErrCompGeomResultOption
  - gtErrCompGeomInvalidRefFil
  - gtErrCompGeomInvalidRefConfi
  - gtErrCompGeomInvalidModFil
  - gtErrCompGeomInvalidModConfi
  - gtErrCompGeomSameRefModFilesConfig
  - gtErrFaceComparisonNotPossibleInAssemblies
  - gtErrAssemblyInEditPartMod

- is successful:

  - Geometries can be checked for each document. In the report, this is representated as "Model Check". This option is set through the Compare tab in the SOLIDWORKS task pane by selecting "Check documents before Compare Geometry" on the **Tools > Compare >** **Options > Geometry** tab. If the geometries check is not successful, then this method returns gt_errors.gtUnknownErr.

If the geometries check is successful:

- Face comparison begins. If faceDiffStatus contains gtSuccess, gtIdenticalParts, gtDifferentParts, or gtCanceled, then this method returns gt_error.gtNOErr. If faceDiffStatus contains gtNoSolidBody or gtFailed, then this method returns gt_error.gtUnknownErr.
- Volume comparison begins. If volDiffStatus contains gtSuccess, gtIdenticalParts, gtDifferentParts, or gtCanceled, then this method returns gt_error.gtNOErr. If volDiffStatus contains gtNoSolidBody or gtFailed, then this method returns gt_error.gtUnknownErr.
- If lResultOptions is set to gtResultOptions_e.gtResultSaveReport, a report is generated. This method may return gt_error.gtNOErr, gtErrIncorrectReportPath, or gtErrReportAlreadyExists.

For more information about the SOLIDWORKS Compare Utility, see the SOLIDWORKS Utilities topics in the SOLIDWORKS user-interface help.

## See Also

[ICompareGeometry Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry.html)
[ICompareGeometry Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
