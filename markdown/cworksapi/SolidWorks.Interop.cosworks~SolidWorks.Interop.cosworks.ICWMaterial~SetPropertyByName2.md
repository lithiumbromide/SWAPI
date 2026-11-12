---
title: "SetPropertyByName2 Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetPropertyByName2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName2.html"
---

# SetPropertyByName2 Method (ICWMaterial)

Sets the value of the specified material property.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPropertyByName2( _
   ByVal SName As System.String, _
   ByVal DValue As System.Double, _
   ByVal BValue As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim SName As System.String
Dim DValue As System.Double
Dim BValue As System.Boolean

instance.SetPropertyByName2(SName, DValue, BValue)
```

### C#

```csharp
void SetPropertyByName2(
   System.string SName,
   System.double DValue,
   System.bool BValue
)
```

### C++/CLI

```cpp
void SetPropertyByName2(
   System.String^ SName,
   System.double DValue,
   System.bool BValue
)
```

### Parameters

- `SName`: Property name; for example, 'EX' for Elastic modulus, 'NUXY' for Poisson's ratio, etc.
- `DValue`: Value of material property
- `BValue`: -1 or true if temperature dependent, 0 or false if not (see **Remarks**)

## VBA Syntax

See [CWMaterial::SetPropertyByName2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetPropertyByName2.html).

## Remarks

Specify BValue as a boolean or integer: true = -1, false = 0.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
