---
title: "HasMaterialPropertyValues Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "HasMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.html"
---

# HasMaterialPropertyValues Method (IBody2)

Gets whether this body has an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasMaterialPropertyValues() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
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

True if this body has an appearance, false if not

## VBA Syntax

See [Body2::HasMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Body2~HasMaterialPropertyValues.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::MaterialPropertyValues2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IBody2::RemoveMaterialProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::GetMaterialPropertyName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
