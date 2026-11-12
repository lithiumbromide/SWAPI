---
title: "ImportDiagnosis Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ImportDiagnosis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosis.html"
---

# ImportDiagnosis Method (IPartDoc)

Diagnoses and repairs any gaps or bad faces on imported features.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportDiagnosis( _
   ByVal CloseAllGaps As System.Boolean, _
   ByVal RemoveFaces As System.Boolean, _
   ByVal FixFaces As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim CloseAllGaps As System.Boolean
Dim RemoveFaces As System.Boolean
Dim FixFaces As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer

value = instance.ImportDiagnosis(CloseAllGaps, RemoveFaces, FixFaces, Options)
```

### C#

```csharp
System.int ImportDiagnosis(
   System.bool CloseAllGaps,
   System.bool RemoveFaces,
   System.bool FixFaces,
   System.int Options
)
```

### C++/CLI

```cpp
System.int ImportDiagnosis(
   System.bool CloseAllGaps,
   System.bool RemoveFaces,
   System.bool FixFaces,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CloseAllGaps`: True to repair any gaps, false to not
- `RemoveFaces`: True to remove any bad faces and create gaps in the feature, false to not
- `FixFaces`: True to fix the bad faces, false to not
- `Options`: Not used

### Return Value

>= 0 if import diagnosis is successful, -1 if an error occurred

## VBA Syntax

See [PartDoc::ImportDiagnosis](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ImportDiagnosis.html).

## Examples

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

## Remarks

Use this method for an imported solid body that has rebuild errors or for an imported surface that did not knit into a solid body.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ImportDiagnosisGapCloser Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosisGapCloser.html)
[IBody2::Diagnose Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.html)
[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html)

## Availability

SOLIDWORKS 99, datecode 1999207
