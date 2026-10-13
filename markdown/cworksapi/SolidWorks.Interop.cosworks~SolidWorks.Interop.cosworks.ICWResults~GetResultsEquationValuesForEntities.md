---
title: "GetResultsEquationValuesForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetResultsEquationValuesForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetResultsEquationValuesForEntities.html"
---

# GetResultsEquationValuesForEntities Method (ICWResults)

Gets the result values for the specified equation and selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResultsEquationValuesForEntities( _
   ByVal SResultsEquation As System.String, _
   ByVal BValueByElem As System.Boolean, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal NShellOptions As System.Integer, _
   ByVal ArraySelectedEntities As System.Object, _
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
Dim ArraySelectedEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetResultsEquationValuesForEntities(SResultsEquation, BValueByElem, NUnits, NStepNumber, NShellOptions, ArraySelectedEntities, ErrorCode)
```

### C#

```csharp
System.object GetResultsEquationValuesForEntities(
   System.string SResultsEquation,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   System.object ArraySelectedEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetResultsEquationValuesForEntities(
   System.String^ SResultsEquation,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   System.Object^ ArraySelectedEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SResultsEquation`: Results equation
- `BValueByElem`: True to plot element values, false to plot node values
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Number of solution step to plot
- `NShellOptions`: Shell face as defined in [swsShellFace_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFace_e.html); valid only for shell and mixed mesh models
- `ArraySelectedEntities`: Array of selected entities; Nothing or null to return values for the entire model
- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetResultsEquationValuesForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetResultsEquationValuesForEntities.html).

## Examples

[Create Results Equation Plot (VBA)](Create_Results_Equation_Plot_Example_VB.htm)
[Create Results Equation Plot (VB.NET)](Create_Results_Equation_Plot_Example_VBNET.htm)
[Create Results Equation Plot (C#)](Create_Results_Equation_Plot_Example_CSharp.htm)

## Remarks

This method returns the following array:

{

`node_or_element_1`,

`value_1,`

`...`

`node_or_element_n,`

`value_n`

},

where the nodes/elements are integer indexes, and the values are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetMinMaxResultsEquationValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxResultsEquationValues.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
