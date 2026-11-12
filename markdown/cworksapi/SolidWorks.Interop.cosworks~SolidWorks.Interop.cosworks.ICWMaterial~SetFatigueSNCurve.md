---
title: "SetFatigueSNCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetFatigueSNCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetFatigueSNCurve.html"
---

# SetFatigueSNCurve Method (ICWMaterial)

Sets the fatigue S-N curve data for user-defined curve sources.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFatigueSNCurve( _
   ByVal NIndex As System.Integer, _
   ByVal DStressRatio As System.Double, _
   ByVal VarFatigueSNCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NIndex As System.Integer
Dim DStressRatio As System.Double
Dim VarFatigueSNCurveData As System.Object
Dim ErrorCode As System.Integer

instance.SetFatigueSNCurve(NIndex, DStressRatio, VarFatigueSNCurveData, ErrorCode)
```

### C#

```csharp
void SetFatigueSNCurve(
   System.int NIndex,
   System.double DStressRatio,
   System.object VarFatigueSNCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void SetFatigueSNCurve(
   System.int NIndex,
   System.double DStressRatio,
   System.Object^ VarFatigueSNCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based S-N curve data index
- `DStressRatio`: Stress ratio
- `VarFatigueSNCurveData`: Array of S-N curve data (see Remarks)
- `ErrorCode`: Error as defined in [swsMaterialFatigueSNCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialSNCurveSource_e.html)

## VBA Syntax

See [CWMaterial::SetFatigueSNCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetFatigueSNCurve.html).

## Remarks

This method is valid only if [ICWMaterial::SNCurveSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SNCurveSource.html) is set to [swsMaterialSNCurveSource_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSNCurveSource_e.html).swsMaterialSNCurveSourceUserDefined.

VarFatigueSNCurveData:

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
[ICWMaterial::GetFatigueSNCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetFatigueSNCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
