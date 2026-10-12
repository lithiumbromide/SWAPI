---
title: "AddDefaultFrequencyOrBucklingStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultFrequencyOrBucklingStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultFrequencyOrBucklingStudyPlot.html"
---

# AddDefaultFrequencyOrBucklingStudyPlot Method (ICWModelDoc)

Specifies a default frequency or buckling study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultFrequencyOrBucklingStudyPlot( _
   ByVal BAllModeShapes As System.Boolean, _
   ByVal NDefMaxModeShapeValue As System.Integer, _
   ByVal BDisplacement As System.Boolean, _
   ByVal NDisplacementValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim BAllModeShapes As System.Boolean
Dim NDefMaxModeShapeValue As System.Integer
Dim BDisplacement As System.Boolean
Dim NDisplacementValue As System.Integer
Dim value As System.Integer

value = instance.AddDefaultFrequencyOrBucklingStudyPlot(BAllModeShapes, NDefMaxModeShapeValue, BDisplacement, NDisplacementValue)
```

### C#

```csharp
System.int AddDefaultFrequencyOrBucklingStudyPlot(
   System.bool BAllModeShapes,
   System.int NDefMaxModeShapeValue,
   System.bool BDisplacement,
   System.int NDisplacementValue
)
```

### C++/CLI

```cpp
System.int AddDefaultFrequencyOrBucklingStudyPlot(
   System.bool BAllModeShapes,
   System.int NDefMaxModeShapeValue,
   System.bool BDisplacement,
   System.int NDisplacementValue
)
```

### Parameters

- `BAllModeShapes`: True to create plots for all mode shapes, false to create plots for the first NDefMaxModeShapeValue mode shapes
- `NDefMaxModeShapeValue`: Maximum number of mode shapes to plot; valid only if BAllModeShapes is false
- `BDisplacement`: True to plot displacement, false to not
- `NDisplacementValue`: Type of displacement result to plot as defined by [swsFrequencyBucklingResultDisplacementComponentTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFrequencyBucklingResultDisplacementComponentTypes_e.html)

### Return Value

Error code as defined by [swsAddDefaultFrequencyOrBucklingStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultFrequencyOrBucklingStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultFrequencyOrBucklingStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultFrequencyOrBucklingStudyPlot.html).

## Examples

[Create Frequency Study with Solid Mesh (VBA)](Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm)
[Create Frequency Study with Solid Mesh (VB.NET)](Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm)
[Create Frequency Study with Solid Mesh (C#)](Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
