---
title: "MaterialUnits Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "MaterialUnits"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html"
---

# MaterialUnits Property (ICWMaterial)

Gets or sets the units for the material.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.MaterialUnits = value

value = instance.MaterialUnits
```

### C#

```csharp
System.int MaterialUnits {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialUnits {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWMaterial::MaterialUnits](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~MaterialUnits.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
