---
title: "ModelType Property (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "ModelType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~ModelType.html"
---

# ModelType Property (ICWMaterial)

Gets or sets the material model.

## Syntax

### Visual Basic (Declaration)

```vb
Property ModelType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim value As System.Integer

instance.ModelType = value

value = instance.ModelType
```

### C#

```csharp
System.int ModelType {get; set;}
```

### C++/CLI

```cpp
property System.int ModelType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of material model as defined in [swsMaterialModelType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialModelType_e.html)

## VBA Syntax

See [CWMaterial::ModelType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~ModelType.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
