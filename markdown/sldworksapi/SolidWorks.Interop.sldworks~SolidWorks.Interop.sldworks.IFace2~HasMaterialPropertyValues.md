---
title: "HasMaterialPropertyValues Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "HasMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasMaterialPropertyValues.html"
---

# HasMaterialPropertyValues Method (IFace2)

Gets whether this face has an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasMaterialPropertyValues() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

True if this face has an appearance, false if not

## VBA Syntax

See [Face2::HasMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Face2~HasMaterialPropertyValues.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::MaterialPropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.html)
[IFace2::GetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetMaterialPropertyValues2.html)
[IFace2::RemoveMaterialProperty2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty2.html)
[IFace2::SetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetMaterialPropertyValues2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
