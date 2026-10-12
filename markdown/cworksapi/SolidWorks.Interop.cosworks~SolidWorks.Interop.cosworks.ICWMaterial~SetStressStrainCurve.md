---
title: "SetStressStrainCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetStressStrainCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetStressStrainCurve.html"
---

# SetStressStrainCurve Method (ICWMaterial)

Sets the stress-strain curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetStressStrainCurve( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer

instance.SetStressStrainCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
void SetStressStrainCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void SetStressStrainCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of stress-strain curve data
- `ErrorCode`: Error as defined in [swsMaterialStressStrainCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialStressStrainCurveError_e.html)

## VBA Syntax

See [CWMaterial::SetStressStrainCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetStressStrainCurve.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetStressStrainCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetStressStrainCurve.html)
