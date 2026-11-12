---
title: "GetMinMaxResultsEquationValues Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxResultsEquationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxResultsEquationValues.html"
---

# GetMinMaxResultsEquationValues Method (ICWResults)

Gets the algebraic minimum and maximum from the plot of the specified results equation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxResultsEquationValues( _
   ByVal SResultsEquation As System.String, _
   ByVal BValueByElem As System.Boolean, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal NShellOptions As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SResultsEquation As System.String
Dim BValueByElem As System.Boolean
Dim NUnits As System.Integer
Dim NStepNumber As System.Integer
Dim NShellOptions As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxResultsEquationValues(SResultsEquation, BValueByElem, NUnits, NStepNumber, NShellOptions, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxResultsEquationValues(
   System.string SResultsEquation,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxResultsEquationValues(
   System.String^ SResultsEquation,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SResultsEquation`: Results equation
- `BValueByElem`: True to plot element values, false to plot node values
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Number of solution step to plot
- `NShellOptions`: Shell face as defined in [swsShellFace_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFace_e.html); valid only for shell and mixed mesh models
- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxResultsEquationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxResultsEquationValues.html).

## Examples

[Create Results Equation Plot (VBA)](Create_Results_Equation_Plot_Example_VB.htm)
[Create Results Equation Plot (VB.NET)](Create_Results_Equation_Plot_Example_VBNET.htm)
[Create Results Equation Plot (C#)](Create_Results_Equation_Plot_Example_CSharp.htm)

## Remarks

This method returns the following array:

{

`node_or_element_with_minimum_value`,

`minimum_value`,

`node_or_element_with_maximum_value`,

`maximum_value`

},

where the nodes/elements are integer indexes, and the values are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetResultsEquationValuesForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetResultsEquationValuesForEntities.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
