---
title: "SetTimeCurve Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "SetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTimeCurve.html"
---

# SetTimeCurve Method (ICWRadiation)

Obsolete. Superseded by [ICWRadiation::SetTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTimeCurve2.html).

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
Dim instance As ICWRadiation
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

## VBA Syntax

See [CWRadiation::SetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~SetTimeCurve.html).

## Remarks

Array of time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::GetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~GetTimeCurve.html)
[ICWRadiation::UseTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
