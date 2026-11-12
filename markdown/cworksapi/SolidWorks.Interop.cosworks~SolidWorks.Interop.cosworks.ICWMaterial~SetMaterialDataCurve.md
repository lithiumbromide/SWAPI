---
title: "SetMaterialDataCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetMaterialDataCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetMaterialDataCurve.html"
---

# SetMaterialDataCurve Method (ICWMaterial)

Obsolete. Superseded by [ICWMaterial::SetMaterialDataCurve3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetMaterialDataCurve3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialDataCurve( _
   ByVal NIndex As System.Integer, _
   ByVal BUseCurve As System.Integer, _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NIndex As System.Integer
Dim BUseCurve As System.Integer
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer

instance.SetMaterialDataCurve(NIndex, BUseCurve, VarCurveData, ErrorCode)
```

### C#

```csharp
void SetMaterialDataCurve(
   System.int NIndex,
   System.int BUseCurve,
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void SetMaterialDataCurve(
   System.int NIndex,
   System.int BUseCurve,
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of material data curve
- `BUseCurve`: - 1 = Use material data curve
  - 0 = Do not use material data curve
- `VarCurveData`: Array of material curve data (see Remarks)
- `ErrorCode`: Error as defined in [swsMaterialDataCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialDataCurveError_e.html)

## VBA Syntax

See [CWMaterial::SetMaterialDataCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetMaterialDataCurve.html).

## Remarks

Array of material curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- x1 = X property value for point 1
- y1 = Y property value for point 1
- ...
- xn = X property value for point n
- yn = Y property value for point n

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetMaterialDataCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetMaterialDataCurve.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
