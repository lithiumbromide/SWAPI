---
title: "GetMaterialDataCurve3 Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetMaterialDataCurve3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetMaterialDataCurve3.html"
---

# GetMaterialDataCurve3 Method (ICWMaterial)

Gets the material data curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialDataCurve3( _
   ByVal NIndex As System.Integer, _
   ByRef BUseCurve As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NIndex As System.Integer
Dim BUseCurve As System.Boolean
Dim value As System.Object

value = instance.GetMaterialDataCurve3(NIndex, BUseCurve)
```

### C#

```csharp
System.object GetMaterialDataCurve3(
   System.int NIndex,
   out System.bool BUseCurve
)
```

### C++/CLI

```cpp
System.Object^ GetMaterialDataCurve3(
   System.int NIndex,
   [Out] System.bool BUseCurve
)
```

### Parameters

- `NIndex`: 0-based index of material data curve
- `BUseCurve`: - -1 or true = Uses material data curve
  - 0 or false = Does not use material data curve

  (see **Remarks**)

### Return Value

Array of material curve data (see **Remarks**)

## VBA Syntax

See [CWMaterial::GetMaterialDataCurve3](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetMaterialDataCurve3.html).

## Remarks

This method returns a boolean or integer in out parameter BUseCurve, depending on its prior declaration.

If out parameter BUseCurve is cast as a:

- Boolean, true or false is returned.
- Long or integer, -1 (=true) or 0 (=false) is returned.

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

## Availability

SOLIDWORKS Simulation API 2021 SP04
