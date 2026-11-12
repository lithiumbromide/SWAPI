---
title: "GenerateReport Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "GenerateReport"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GenerateReport.html"
---

# GenerateReport Method (ICWStudy)

Creates a report about all aspects of this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GenerateReport( _
   ByVal SReportPath As System.String, _
   ByVal SDocName As System.String, _
   ByVal BShowOnPublish As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SReportPath As System.String
Dim SDocName As System.String
Dim BShowOnPublish As System.Boolean
Dim value As System.Integer

value = instance.GenerateReport(SReportPath, SDocName, BShowOnPublish)
```

### C#

```csharp
System.int GenerateReport(
   System.string SReportPath,
   System.string SDocName,
   System.bool BShowOnPublish
)
```

### C++/CLI

```cpp
System.int GenerateReport(
   System.String^ SReportPath,
   System.String^ SDocName,
   System.bool BShowOnPublish
)
```

### Parameters

- `SReportPath`: Path in which to create this report
- `SDocName`: File name of the report
- `BShowOnPublish`: True to display the report after creation, false to not

### Return Value

Error code as defined in [swsGenerateReportError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsGenerateReportError_e.html)

## VBA Syntax

See [CWStudy::GenerateReport](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~GenerateReport.html).

## Examples

[Copy Mesh and Generate Report (VBA)](Copy_Mesh_and_Gen_Report_Example_VB.htm)
[Copy Mesh and Generate Report (VB.NET)](Copy_Mesh_and_Gen_Report_Example_VBNET.htm)
[Copy Mesh and Generate Report (C#)](Copy_Mesh_and_Gen_Report_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ExportSimulationStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ExportSimulationStudy.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
