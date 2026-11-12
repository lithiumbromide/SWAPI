---
title: "HasMaterialPropertyValues Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "HasMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.html"
---

# HasMaterialPropertyValues Method (IComponent2)

Gets whether this component has an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasMaterialPropertyValues() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.HasMaterialPropertyValues()
```

### C#

```csharp
System.bool HasMaterialPropertyValues()
```

### C++/CLI

```cpp
System.bool HasMaterialPropertyValues();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component has an appearance, false if not

## VBA Syntax

See [Component2::HasMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Component2~HasMaterialPropertyValues.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::MaterialPropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IComponent2::GetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::RemoveMaterialProperty2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::GetModelMaterialPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues.html)
[IComponent2::SetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
