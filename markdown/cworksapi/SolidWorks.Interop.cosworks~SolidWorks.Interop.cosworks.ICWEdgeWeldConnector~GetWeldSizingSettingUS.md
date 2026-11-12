---
title: "GetWeldSizingSettingUS Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "GetWeldSizingSettingUS"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingUS.html"
---

# GetWeldSizingSettingUS Method (ICWEdgeWeldConnector)

Gets the American Standard settings for weld sizing calculations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldSizingSettingUS( _
   ByRef NElectrodeMaterial As System.Integer, _
   ByRef DWeldStrength As System.Double, _
   ByRef NWeldStrengthUnit As System.Integer, _
   ByRef NSafetyFactorLiftOption As System.Integer, _
   ByRef DSafetyFactor As System.Double, _
   ByRef BIsEstimatedWeldSize As System.Boolean, _
   ByRef DEstimatedWeldSize As System.Double, _
   ByRef NEstimatedWeldSizeUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NElectrodeMaterial As System.Integer
Dim DWeldStrength As System.Double
Dim NWeldStrengthUnit As System.Integer
Dim NSafetyFactorLiftOption As System.Integer
Dim DSafetyFactor As System.Double
Dim BIsEstimatedWeldSize As System.Boolean
Dim DEstimatedWeldSize As System.Double
Dim NEstimatedWeldSizeUnit As System.Integer
Dim value As System.Integer

value = instance.GetWeldSizingSettingUS(NElectrodeMaterial, DWeldStrength, NWeldStrengthUnit, NSafetyFactorLiftOption, DSafetyFactor, BIsEstimatedWeldSize, DEstimatedWeldSize, NEstimatedWeldSizeUnit)
```

### C#

```csharp
System.int GetWeldSizingSettingUS(
   out System.int NElectrodeMaterial,
   out System.double DWeldStrength,
   out System.int NWeldStrengthUnit,
   out System.int NSafetyFactorLiftOption,
   out System.double DSafetyFactor,
   out System.bool BIsEstimatedWeldSize,
   out System.double DEstimatedWeldSize,
   out System.int NEstimatedWeldSizeUnit
)
```

### C++/CLI

```cpp
System.int GetWeldSizingSettingUS(
   [Out] System.int NElectrodeMaterial,
   [Out] System.double DWeldStrength,
   [Out] System.int NWeldStrengthUnit,
   [Out] System.int NSafetyFactorLiftOption,
   [Out] System.double DSafetyFactor,
   [Out] System.bool BIsEstimatedWeldSize,
   [Out] System.double DEstimatedWeldSize,
   [Out] System.int NEstimatedWeldSizeUnit
)
```

### Parameters

- `NElectrodeMaterial`: Electrode material as defined in [swsElectrodeMaterialTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsElectrodeMaterialTypes_e.html)
- `DWeldStrength`: Ultimate shear strength of NElectrodeMaterial; if NElectrodeMaterial is swsElectrodeMaterialTypes_e.swsElectrodeMaterialCustomAl or swsElectrodeMaterialTypes_e.swsElectrodeMaterialCustomSteel, ultimate shear strength for the weld throat
- `NWeldStrengthUnit`: DWeldStrength units as defined in [swsWeldStrengthUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeldStrengthUnits_e.html)
- `NSafetyFactorLiftOption`: Lift safety factor by which to reduce DWeldStrength as defined in [swsEdgeWeldConnectorSafetyFactorLiftOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorSafetyFactorLiftOption_e.html)
- `DSafetyFactor`: Custom safety factor by which to reduce DWeldStrength; overrides the lift safety factor specified in NSafetyFactorLiftOption
- `BIsEstimatedWeldSize`: True to calculate the appropriate size for the weld connector and compare it to DEstimatedWeldSize in the Weld Check Plot; false to just use DEstimatedWeldSize
- `DEstimatedWeldSize`: Estimated weld size
- `NEstimatedWeldSizeUnit`: DEstimatedWeldSize units as defined in [swsEstimatedWeldSizeUnits_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEstimatedWeldSizeUnits_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::GetWeldSizingSettingUS](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~GetWeldSizingSettingUS.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only if [ICWEdgeWeldConnector::GetCodeType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetCodeType.html) returns [swsEdgeWeldSolverCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldSolverCode_e.html).swsEdgeWeldSolverCodeAWS.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingUS.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingEuro.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
