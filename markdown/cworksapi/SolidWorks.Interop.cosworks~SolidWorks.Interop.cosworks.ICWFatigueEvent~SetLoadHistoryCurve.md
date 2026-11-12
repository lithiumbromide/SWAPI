---
title: "SetLoadHistoryCurve Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "SetLoadHistoryCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~SetLoadHistoryCurve.html"
---

# SetLoadHistoryCurve Method (ICWFatigueEvent)

Sets the load history curve data for this variable amplitude fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLoadHistoryCurve( _
   ByVal VarLHCurveXData As System.Object, _
   ByVal VarLHCurveYData As System.Object, _
   ByVal NType As System.Integer, _
   ByVal DSamplingRate As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim VarLHCurveXData As System.Object
Dim VarLHCurveYData As System.Object
Dim NType As System.Integer
Dim DSamplingRate As System.Double
Dim value As System.Integer

value = instance.SetLoadHistoryCurve(VarLHCurveXData, VarLHCurveYData, NType, DSamplingRate)
```

### C#

```csharp
System.int SetLoadHistoryCurve(
   System.object VarLHCurveXData,
   System.object VarLHCurveYData,
   System.int NType,
   System.double DSamplingRate
)
```

### C++/CLI

```cpp
System.int SetLoadHistoryCurve(
   System.Object^ VarLHCurveXData,
   System.Object^ VarLHCurveYData,
   System.int NType,
   System.double DSamplingRate
)
```

### Parameters

- `VarLHCurveXData`: Array of times; valid only if NType = [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html).swsFatigueLoadHistoryCurveType_TimeAndAmplitude
- `VarLHCurveYData`: Array of amplitudes
- `NType`: Type of curve as defined in [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html)
- `DSamplingRate`: Sampling rate in seconds; valid only if NType = [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html).swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude

### Return Value

Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

## VBA Syntax

See [CWFatigueEvent::SetLoadHistoryCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~SetLoadHistoryCurve.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::GetLoadHistoryCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~GetLoadHistoryCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
