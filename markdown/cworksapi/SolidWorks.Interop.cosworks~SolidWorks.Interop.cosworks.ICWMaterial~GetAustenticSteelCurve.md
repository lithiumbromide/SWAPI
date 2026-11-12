---
title: "GetAustenticSteelCurve Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetAustenticSteelCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetAustenticSteelCurve.html"
---

# GetAustenticSteelCurve Method (ICWMaterial)

Gets the austentic steel curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAustenticSteelCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Object

value = instance.GetAustenticSteelCurve()
```

### C#

```csharp
System.object GetAustenticSteelCurve()
```

### C++/CLI

```cpp
System.Object^ GetAustenticSteelCurve();
```

### Return Value

Array of austentic steel curve data (see **Remarks**)

## VBA Syntax

See [CWMaterial::GetAustenticSteelCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetAustenticSteelCurve.html).

## Remarks

Austentic steel curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- x1 = number of cycles for point 1
- y1 = alternating stress for point 1
- ...
- xn = number of cycles for point n
- yn = alternating stress for point n

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
