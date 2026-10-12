---
title: "Description Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "Description"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html"
---

# Description Property (ICWMaterial)

Gets or sets the description for the material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.String

instance.Description = value

value = instance.Description
```

### C#

```csharp
System.string Description {get; set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Description

## VBA Syntax

See [CWMaterial::Description](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~Description.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::Category Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
