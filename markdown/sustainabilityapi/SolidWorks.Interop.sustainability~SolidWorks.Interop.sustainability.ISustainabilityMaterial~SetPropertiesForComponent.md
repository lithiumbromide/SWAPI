---
title: "SetPropertiesForComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "SetPropertiesForComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~SetPropertiesForComponent.html"
---

# SetPropertiesForComponent Method (ISustainabilityMaterial)

Applies material to the specified components.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPropertiesForComponent( _
   ByRef ComponentsNames As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim ComponentsNames As System.Object

instance.SetPropertiesForComponent(ComponentsNames)
```

### C#

```csharp
void SetPropertiesForComponent(
   ref System.object ComponentsNames
)
```

### C++/CLI

```cpp
void SetPropertiesForComponent(
   System.Object^% ComponentsNames
)
```

### Parameters

- `ComponentsNames`: Array of the names of the components to which to apply material properties

## VBA Syntax

See [SustainabilityMaterial::SetPropertiesForComponent](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~SetPropertiesForComponent.html).

## Examples

[Calculate Environmental Impact of Assembly (VBA)](Calculate_Environmental_Impact_of_Assembly_Example_VB.htm)

## Remarks

Before calling this method, call [ISustainabilityMaterial::GetMissingMaterialComponentList](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~GetMissingMaterialComponentList.html) to populate ComponentsNames with the list of all of the components that are missing material.

This method applies the following material properties to the components specified in ComponentsNames:

- [ISustainabilityMaterial::MaterialClass](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialClass.html)
- [ISustainabilityMaterial::MaterialName](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialName.html)
- [ISustainabilityMaterial::RecycledContent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~RecycledContent.html)

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::ISetPropertiesForComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ISetPropertiesForComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
