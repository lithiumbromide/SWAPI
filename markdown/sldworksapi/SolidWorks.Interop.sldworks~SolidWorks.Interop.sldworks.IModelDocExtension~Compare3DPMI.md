---
title: "Compare3DPMI Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Compare3DPMI"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Compare3DPMI.html"
---

# Compare3DPMI Method (IModelDocExtension)

Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Compare3DPMI( _
   ByVal ReferenceDocument As System.String, _
   ByVal ModifiedDocument As System.String, _
   ByVal ReportName As System.String, _
   ByVal ReportFolderPath As System.String, _
   ByVal ReportSaveOptions As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ReferenceDocument As System.String
Dim ModifiedDocument As System.String
Dim ReportName As System.String
Dim ReportFolderPath As System.String
Dim ReportSaveOptions As System.Integer
Dim value As System.Boolean

value = instance.Compare3DPMI(ReferenceDocument, ModifiedDocument, ReportName, ReportFolderPath, ReportSaveOptions)
```

### C#

```csharp
System.bool Compare3DPMI(
   System.string ReferenceDocument,
   System.string ModifiedDocument,
   System.string ReportName,
   System.string ReportFolderPath,
   System.int ReportSaveOptions
)
```

### C++/CLI

```cpp
System.bool Compare3DPMI(
   System.String^ ReferenceDocument,
   System.String^ ModifiedDocument,
   System.String^ ReportName,
   System.String^ ReportFolderPath,
   System.int ReportSaveOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceDocument`: Path and file name of the open part document
- `ModifiedDocument`: Path and file name of a different and open version of ReferenceDocument
- `ReportName`: Name for the report and name of the folder to which to save the report and bitmap image files
- `ReportFolderPath`: Path to the folder specified in ReportName in which to save the report and bitmap image files
- `ReportSaveOptions`: Save options for the report as defined in [sw3DPMISaveOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DPMISaveOptions_e.html)

### Return Value

True if the method executed, false if not

## VBA Syntax

See [ModelDocExtension::Compare3DPMI](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Compare3DPMI.html).

## Examples

[Compare DimXpert Annotations in Different Versions of Same Part (C#)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_CSharp.htm)
[Compare DimXpert Annotations in Different Versions of Same Part (VB.NET)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_VBNET.htm)
[Compare DimXpert Annotations in Different Versions of Same Part (VBA)](Compare_DimXpert_Annotations_in_Different_Versions_of_Same_Part_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
