---
title: "AddDefaultFatigueStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultFatigueStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultFatigueStudyPlot.html"
---

# AddDefaultFatigueStudyPlot Method (ICWModelDoc)

Specifies a default fatigue study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultFatigueStudyPlot( _
   ByVal NResultType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NResultType As System.Integer
Dim value As System.Integer

value = instance.AddDefaultFatigueStudyPlot(NResultType)
```

### C#

```csharp
System.int AddDefaultFatigueStudyPlot(
   System.int NResultType
)
```

### C++/CLI

```cpp
System.int AddDefaultFatigueStudyPlot(
   System.int NResultType
)
```

### Parameters

- `NResultType`: Type of fatigue study result to plot as defined by [swsFatigueStudyResultType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueStudyResultType_e.html)

### Return Value

Error code as defined by [swsAddDefaultFatigueStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultFatigueStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultFatigueStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultFatigueStudyPlot.html).

## Examples

[Create Fatigue Study (VBA)](Create_Fatigue_Study_Example_VB.htm)
[Create Fatigue Study (VB.NET)](Create_Fatigue_Study_Example_VBNET.htm)
[Create Fatigue Study (C#)](Create_Fatigue_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::DeleteAllDefaultFatigueStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultFatigueStudyPlots.html)
[ICWModelDoc::DeleteDefaultFatigueStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultFatigueStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
