---
title: "Category Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "Category"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Category.html"
---

# Category Property (ICWMaterial)

Gets or sets the category of the material.

## Syntax

### Visual Basic (Declaration)

```vb
Property Category As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.String

instance.Category = value

value = instance.Category
```

### C#

```csharp
System.string Category {get; set;}
```

### C++/CLI

```cpp
property System.String^ Category {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Category

## VBA Syntax

See [CWMaterial::Category](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~Category.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::Description Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Description.html)
[ICWMaterial::MaterialName Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialName.html)
[ICWMaterial::MaterialUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~MaterialUnits.html)
[ICWMaterial::Source Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~Source.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
