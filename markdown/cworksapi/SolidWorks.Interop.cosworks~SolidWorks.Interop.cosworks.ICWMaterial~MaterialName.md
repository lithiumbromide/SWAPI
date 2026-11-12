---
title: "MaterialName Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "MaterialName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html"
---

# MaterialName Property (ICWMaterial)

Gets or sets the name of the material name.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.String

instance.MaterialName = value

value = instance.MaterialName
```

### C#

```csharp
System.string MaterialName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Material name

## VBA Syntax

See [CWMaterial::MaterialName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~MaterialName.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Matierals (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
