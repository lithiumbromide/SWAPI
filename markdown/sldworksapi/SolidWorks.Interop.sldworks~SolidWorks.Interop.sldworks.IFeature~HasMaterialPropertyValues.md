---
title: "HasMaterialPropertyValues Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "HasMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.html"
---

# HasMaterialPropertyValues Method (IFeature)

Gets whether this feature has an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasMaterialPropertyValues() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
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

True if this feature has an appearance, false if not

## VBA Syntax

See [Feature::HasMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Feature~HasMaterialPropertyValues.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.html)
[IFeature::SetMaterialPropertyValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.html)
[IFeature::RemoveMaterialProperty2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
