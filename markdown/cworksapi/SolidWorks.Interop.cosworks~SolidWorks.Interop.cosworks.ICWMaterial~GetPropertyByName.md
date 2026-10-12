---
title: "GetPropertyByName Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetPropertyByName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName.html"
---

# GetPropertyByName Method (ICWMaterial)

Obsolete. Superseded by er[ICWMaterial::GetPropertyByName2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyByName( _
   ByVal NUnit As System.Integer, _
   ByVal SName As System.String, _
   ByRef BTempDependent As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NUnit As System.Integer
Dim SName As System.String
Dim BTempDependent As System.Integer
Dim value As System.Double

value = instance.GetPropertyByName(NUnit, SName, BTempDependent)
```

### C#

```csharp
System.double GetPropertyByName(
   System.int NUnit,
   System.string SName,
   out System.int BTempDependent
)
```

### C++/CLI

```cpp
System.double GetPropertyByName(
   System.int NUnit,
   System.String^ SName,
   [Out] System.int BTempDependent
)
```

### Parameters

- `NUnit`: Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)
- `SName`: Property name; for example, 'EX' for Elastic modulus, 'NUXY' for Poisson's ratio, etc.
- `BTempDependent`: True if temperature dependent, false if not

### Return Value

Value of material property

## VBA Syntax

See [CWMaterial::GetPropertyByName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetPropertyByName.html).

## Examples

[Apply Material to Bodies (C#)](Apply_Material_to_Bodies_Example_CSharp.htm)
[Apply Material to Bodies (VB.NET)](Apply_Material_to_Bodies_Example_VBNET.htm)
[Apply Material to Bodies (VBA)](Apply_Material_to_Bodies_Example_VB.htm)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::SetPropertyByName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetPropertyByName.html)
[ICWMaterial::Count Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Count.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
