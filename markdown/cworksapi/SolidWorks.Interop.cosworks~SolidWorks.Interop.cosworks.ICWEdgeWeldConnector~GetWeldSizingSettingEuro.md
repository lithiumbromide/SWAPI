---
title: "GetWeldSizingSettingEuro Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "GetWeldSizingSettingEuro"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingEuro.html"
---

# GetWeldSizingSettingEuro Method (ICWEdgeWeldConnector)

Gets the European Standard settings for weld sizing calculations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldSizingSettingEuro( _
   ByRef NWeakMaterial As System.Integer, _
   ByRef DUltimateTensileStrength As System.Double, _
   ByRef NTensileStrengthUnit As System.Integer, _
   ByRef DCorrelationFactor As System.Double, _
   ByRef DPartialSafetyFactor As System.Double, _
   ByRef BIsEstimatedWeldSize As System.Boolean, _
   ByRef DEstimatedWeldSize As System.Double, _
   ByRef NEstimatedWeldSizeUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NWeakMaterial As System.Integer
Dim DUltimateTensileStrength As System.Double
Dim NTensileStrengthUnit As System.Integer
Dim DCorrelationFactor As System.Double
Dim DPartialSafetyFactor As System.Double
Dim BIsEstimatedWeldSize As System.Boolean
Dim DEstimatedWeldSize As System.Double
Dim NEstimatedWeldSizeUnit As System.Integer
Dim value As System.Integer

value = instance.GetWeldSizingSettingEuro(NWeakMaterial, DUltimateTensileStrength, NTensileStrengthUnit, DCorrelationFactor, DPartialSafetyFactor, BIsEstimatedWeldSize, DEstimatedWeldSize, NEstimatedWeldSizeUnit)
```

### C#

```csharp
System.int GetWeldSizingSettingEuro(
   out System.int NWeakMaterial,
   out System.double DUltimateTensileStrength,
   out System.int NTensileStrengthUnit,
   out System.double DCorrelationFactor,
   out System.double DPartialSafetyFactor,
   out System.bool BIsEstimatedWeldSize,
   out System.double DEstimatedWeldSize,
   out System.int NEstimatedWeldSizeUnit
)
```

### C++/CLI

```cpp
System.int GetWeldSizingSettingEuro(
   [Out] System.int NWeakMaterial,
   [Out] System.double DUltimateTensileStrength,
   [Out] System.int NTensileStrengthUnit,
   [Out] System.double DCorrelationFactor,
   [Out] System.double DPartialSafetyFactor,
   [Out] System.bool BIsEstimatedWeldSize,
   [Out] System.double DEstimatedWeldSize,
   [Out] System.int NEstimatedWeldSizeUnit
)
```

### Parameters

- `NWeakMaterial`: Material of weaker joined part as defined in [swsWeakMaterial_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeakMaterial_e.html)
- `DUltimateTensileStrength`: Ultimate tensile strength of NWeakMaterial
- `NTensileStrengthUnit`: DUltimateTensileStrength units as defined in [swsWeldStrengthUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeldStrengthUnits_e.html)
- `DCorrelationFactor`: 0.8 <= correlation factor for weld calculations <= 1.0
- `DPartialSafetyFactor`: 1.0 <= partial safety factor for joints <= 1.25
- `BIsEstimatedWeldSize`: True to calculate the appropriate size for the weld connector and compare it to DEstimatedWeldSize in the Weld Check Plot; false to just use DEstimatedWeldSize
- `DEstimatedWeldSize`: Estimated weld size
- `NEstimatedWeldSizeUnit`: DEstimatedWeldSize units as defined in [swsEstimatedWeldSizeUnits_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEstimatedWeldSizeUnits_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::GetWeldSizingSettingEuro](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~GetWeldSizingSettingEuro.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only if [ICWEdgeWeldConnector::GetCodeType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetCodeType.html) returns [swsEdgeWeldSolverCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldSolverCode_e.html).swsEdgeWeldSolverCodeEURO.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingEuro.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingUS.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
