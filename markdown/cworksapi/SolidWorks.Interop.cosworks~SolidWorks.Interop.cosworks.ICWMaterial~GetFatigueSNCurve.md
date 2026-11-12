---
title: "GetFatigueSNCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetFatigueSNCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetFatigueSNCurve.html"
---

# GetFatigueSNCurve Method (ICWMaterial)

Gets the fatigue S-N curve data for user-defined curve sources.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFatigueSNCurve( _
   ByVal NIndex As System.Integer, _
   ByRef DStressRatio As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NIndex As System.Integer
Dim DStressRatio As System.Double
Dim value As System.Object

value = instance.GetFatigueSNCurve(NIndex, DStressRatio)
```

### C#

```csharp
System.object GetFatigueSNCurve(
   System.int NIndex,
   out System.double DStressRatio
)
```

### C++/CLI

```cpp
System.Object^ GetFatigueSNCurve(
   System.int NIndex,
   [Out] System.double DStressRatio
)
```

### Parameters

- `NIndex`: 0-based S-N curve data index
- `DStressRatio`: Stress ratio

### Return Value

Array of S-N curve data (see **Remarks**)

## VBA Syntax

See [CWMaterial::GetFatigueSNCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetFatigueSNCurve.html).

## Remarks

This method is valid only if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceUserDefined.

Array of S-N curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- x1 = number of cycles for point 1
- y1 = alternating stress for point 1
- ...
- xn = number of cycles for point n
- yn = alternating stress for point n

See the SOLIDWORKS Help topic, **Material Dialog Box - Fatigue SN Curves Tab**, for more information about S-N curve equations.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::SetFatigueSNCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetFatigueSNCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
