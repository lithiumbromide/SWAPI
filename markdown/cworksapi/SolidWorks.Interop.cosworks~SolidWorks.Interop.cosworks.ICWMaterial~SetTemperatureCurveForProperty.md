---
title: "SetTemperatureCurveForProperty Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetTemperatureCurveForProperty"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetTemperatureCurveForProperty.html"
---

# SetTemperatureCurveForProperty Method (ICWMaterial)

Sets the temperature curve data for the material property.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTemperatureCurveForProperty( _
   ByVal SPropName As System.String, _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim SPropName As System.String
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer

instance.SetTemperatureCurveForProperty(SPropName, VarCurveData, ErrorCode)
```

### C#

```csharp
void SetTemperatureCurveForProperty(
   System.string SPropName,
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void SetTemperatureCurveForProperty(
   System.String^ SPropName,
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPropName`: Property name
- `VarCurveData`: Array of temperature data (see Remarks)
- `ErrorCode`: Error as defined in [swsMaterialTemperatureCurveForPropertyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialTemperatureCurveForPropertyError_e.html)

## VBA Syntax

See [CWMaterial::SetTemperatureCurveForProperty](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetTemperatureCurveForProperty.html).

## Remarks

Array of temperature data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- x1 = temperature value for point 1
- y1 = property value for point 1
- ...
- xn = temperature value for point n
- yn = property value for point n

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetTemperatureCurveForProperty Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetTemperatureCurveForProperty.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
