---
title: "SetPropertyByName Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetPropertyByName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName.html"
---

# SetPropertyByName Method (ICWMaterial)

Obsolete. Superseded by [ICWMaterial::SetPropertyByName2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPropertyByName( _
   ByVal SName As System.String, _
   ByVal DValue As System.Double, _
   ByVal BValue As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim SName As System.String
Dim DValue As System.Double
Dim BValue As System.Integer

instance.SetPropertyByName(SName, DValue, BValue)
```

### C#

```csharp
void SetPropertyByName(
   System.string SName,
   System.double DValue,
   System.int BValue
)
```

### C++/CLI

```cpp
void SetPropertyByName(
   System.String^ SName,
   System.double DValue,
   System.int BValue
)
```

### Parameters

- `SName`: Property name; for example, 'EX' for Elastic modulus, 'NUXY' for Poisson's ratio, etc.
- `DValue`: Value of material property
- `BValue`: True if temperature dependent, false if not

## VBA Syntax

See [CWMaterial::SetPropertyByName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetPropertyByName.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName.html)
[ICWMaterial::Count Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Count.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
