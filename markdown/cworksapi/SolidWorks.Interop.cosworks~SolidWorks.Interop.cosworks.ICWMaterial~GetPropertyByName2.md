---
title: "GetPropertyByName2 Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "GetPropertyByName2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetPropertyByName2.html"
---

# GetPropertyByName2 Method (ICWMaterial)

Gets the value of the material property by the property name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyByName2( _
   ByVal NUnit As System.Integer, _
   ByVal SName As System.String, _
   ByRef BTempDependent As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim NUnit As System.Integer
Dim SName As System.String
Dim BTempDependent As System.Boolean
Dim value As System.Double

value = instance.GetPropertyByName2(NUnit, SName, BTempDependent)
```

### C#

```csharp
System.double GetPropertyByName2(
   System.int NUnit,
   System.string SName,
   out System.bool BTempDependent
)
```

### C++/CLI

```cpp
System.double GetPropertyByName2(
   System.int NUnit,
   System.String^ SName,
   [Out] System.bool BTempDependent
)
```

### Parameters

- `NUnit`: Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)
- `SName`: Property name; for example, 'EX' for Elastic modulus, 'NUXY' for Poisson's ratio, etc.
- `BTempDependent`: -1 or true if temperature dependent, 0 or false if not (see **Remarks**)

### Return Value

Value of material property

## VBA Syntax

See [CWMaterial::GetPropertyByName2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~GetPropertyByName2.html).

## Remarks

This method returns a boolean or integer in out parameter BTempDependent, depending on its prior declaration.

If out parameter BTempDependent is cast as a:

- Boolean, true or false is returned.
- Long or integer, -1 (=true) or 0 (=false) is returned.

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
