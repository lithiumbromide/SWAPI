---
title: "MaterialClass Property (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "MaterialClass"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~MaterialClass.html"
---

# MaterialClass Property (ISustainabilityMaterial)

Gets or sets the class of material applied to the current part or the specified assembly components.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim value As System.String

instance.MaterialClass = value

value = instance.MaterialClass
```

### C#

```csharp
System.string MaterialClass {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialClass {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the class of material (see **Remarks**)

## VBA Syntax

See [SustainabilityMaterial::MaterialClass](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~MaterialClass.html).

## Examples

See the examples in [ISustainabilityMaterial](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial.html).

## Remarks

The material class specified by this property constrains the material names that can be specified by [ISustainabilityMaterial::MaterialName](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialName.html). This property is valid only if ISustainabilityMaterial::MaterialName is set. The available material classes are stored in the SOLIDWORKS Materials database. See SOLIDWORKS Help for more information.

This property applies only to the assembly components specified by [ISustainabilityMaterial::SetPropertiesForComponent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~SetPropertiesForComponent.html) and [ISustainabilityMaterial::ISetPropertiesForComponent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~ISetPropertiesForComponent.html).

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
