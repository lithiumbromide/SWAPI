---
title: "SetTimeCurve Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetTimeCurve.html"
---

# SetTimeCurve Method (ICWForce)

Obsolete. Superseded by [ICWForce::SetTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeCurve( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.SetTimeCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
System.int SetTimeCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetTimeCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

1 if the time curve data is set, 0 if not

## VBA Syntax

See [CWForce::SetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetTimeCurve.html).

## Remarks

Time curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn,` `yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

Time curves are used to specify feature variation with respect to time in linear and nonlinear dynamic studies.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
