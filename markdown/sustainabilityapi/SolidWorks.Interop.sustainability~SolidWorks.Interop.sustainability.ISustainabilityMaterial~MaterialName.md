---
title: "MaterialName Property (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "MaterialName"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~MaterialName.html"
---

# MaterialName Property (ISustainabilityMaterial)

Gets or sets the material name for the current material class.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
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

Name of the material (see **Remarks**)

## VBA Syntax

See [SustainabilityMaterial::MaterialName](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~MaterialName.html).

## Examples

See the examples in [ISustainabilityMaterial](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial.html).

## Remarks

The material class specified by [ISustainabilityMaterial::MaterialClass](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialClass.html) constrains the material names that can be specified by this property. This property is valid only if ISustainabilityMaterial::MaterialClass is set. The available material classes are stored in the SOLIDWORKS Materials database. See SOLIDWORKS Help for more information.

This property applies only to the assembly components specified by [ISustainabilityMaterial::SetPropertiesForComponent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~SetPropertiesForComponent.html) and [ISustainabilityMaterial::ISetPropertiesForComponent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~ISetPropertiesForComponent.html).

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
