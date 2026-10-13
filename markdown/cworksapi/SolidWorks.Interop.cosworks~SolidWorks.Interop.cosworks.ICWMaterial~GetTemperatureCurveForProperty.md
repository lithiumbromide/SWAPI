---
title: "GetTemperatureCurveForProperty Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetTemperatureCurveForProperty"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetTemperatureCurveForProperty.html"
---

# GetTemperatureCurveForProperty Method (ICWMaterial)

Gets the temperature curve data for the material property.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemperatureCurveForProperty( _
   ByVal SPropName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim SPropName As System.String
Dim value As System.Object

value = instance.GetTemperatureCurveForProperty(SPropName)
```

### C#

```csharp
System.object GetTemperatureCurveForProperty(
   System.string SPropName
)
```

### C++/CLI

```cpp
System.Object^ GetTemperatureCurveForProperty(
   System.String^ SPropName
)
```

### Parameters

- `SPropName`: Property name

### Return Value

Array of temperature data (see Remarks)

## VBA Syntax

See [CWMaterial::GetTemperatureCurveForProperty](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetTemperatureCurveForProperty.html).

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
[ICWMaterial::SetTemperatureCurveForProperty Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetTemperatureCurveForProperty.html)
[ICWMaterial::GetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName.html)
[ICWMaterial::SetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
