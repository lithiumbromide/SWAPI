---
title: "GetMaterialDataCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetMaterialDataCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetMaterialDataCurve.html"
---

# GetMaterialDataCurve Method (ICWMaterial)

Obsolete. Superseded by [ICWMaterial::GetMaterialDataCurve3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetMaterialDataCurve3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialDataCurve( _
   ByVal NIndex As System.Integer, _
   ByRef BUseCurve As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NIndex As System.Integer
Dim BUseCurve As System.Integer
Dim value As System.Object

value = instance.GetMaterialDataCurve(NIndex, BUseCurve)
```

### C#

```csharp
System.object GetMaterialDataCurve(
   System.int NIndex,
   out System.int BUseCurve
)
```

### C++/CLI

```cpp
System.Object^ GetMaterialDataCurve(
   System.int NIndex,
   [Out] System.int BUseCurve
)
```

### Parameters

- `NIndex`: 0-based index of material data curve
- `BUseCurve`: - 1 = Use material data curve
  - 0 = Do not use material data curve

### Return Value

Array of material curve data (see **Remarks**)

## VBA Syntax

See [CWMaterial::GetMaterialDataCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetMaterialDataCurve.html).

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
[ICWMaterial::SetMaterialDataCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetMaterialDataCurve.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
