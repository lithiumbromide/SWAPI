---
title: "ISetPropertiesForComponent Method (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "ISetPropertiesForComponent"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~ISetPropertiesForComponent.html"
---

# ISetPropertiesForComponent Method (ISustainabilityMaterial)

Applies material to the specified components.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPropertiesForComponent( _
   ByRef ComponentsNames As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim ComponentsNames As System.String

instance.ISetPropertiesForComponent(ComponentsNames)
```

### C#

```csharp
void ISetPropertiesForComponent(
   ref System.string ComponentsNames
)
```

### C++/CLI

```cpp
void ISetPropertiesForComponent(
   System.String^% ComponentsNames
)
```

### Parameters

- `ComponentsNames`: - in-process, unmanaged C++: Pointer to an array of the names of the components to which to apply material properties
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISustainabilityMaterial::IGetMissingMaterialComponentList](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~IGetMissingMaterialComponentList.html) to populate ComponentsNames with the list of all of the components that are missing material.

This method applies the following material properties to the components specified in ComponentsNames:

- [ISustainabilityMaterial::MaterialClass](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialClass.html)
- [ISustainabilityMaterial::MaterialName](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialName.html)
- [ISustainabilityMaterial::RecycledContent](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~RecycledContent.html)

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)
[ISustainabilityMaterial::SetPropertiesForComponent Method](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~SetPropertiesForComponent.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
