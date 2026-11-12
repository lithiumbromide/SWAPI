---
title: "GetLoadHistoryCurve Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "GetLoadHistoryCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~GetLoadHistoryCurve.html"
---

# GetLoadHistoryCurve Method (ICWFatigueEvent)

Gets the load history curve data for this variable amplitude fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoadHistoryCurve( _
   ByRef NType As System.Integer, _
   ByRef DSamplingRate As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim NType As System.Integer
Dim DSamplingRate As System.Double
Dim value As System.Object

value = instance.GetLoadHistoryCurve(NType, DSamplingRate)
```

### C#

```csharp
System.object GetLoadHistoryCurve(
   out System.int NType,
   out System.double DSamplingRate
)
```

### C++/CLI

```cpp
System.Object^ GetLoadHistoryCurve(
   [Out] System.int NType,
   [Out] System.double DSamplingRate
)
```

### Parameters

- `NType`: Type of curve as defined in [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html)
- `DSamplingRate`: Sampling rate in seconds; valid only if NType = [swsFatigueLoadHistoryCurveType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html).swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWFatigueEvent::GetLoadHistoryCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~GetLoadHistoryCurve.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## Remarks

This method is valid only if this is a variable amplitude fatigue event.

This method returns the following array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = amplitude associated with time xi

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::SetLoadHistoryCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~SetLoadHistoryCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
