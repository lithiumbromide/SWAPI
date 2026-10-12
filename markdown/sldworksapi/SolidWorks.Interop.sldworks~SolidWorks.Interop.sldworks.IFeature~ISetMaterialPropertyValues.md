---
title: "ISetMaterialPropertyValues Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ISetMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues.html"
---

# ISetMaterialPropertyValues Method (IFeature)

Obsolete. Superseded by [IFeature::ISetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetMaterialPropertyValues( _
   ByRef MaterialPropertyValues As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim MaterialPropertyValues As System.Double
Dim value As System.Boolean

value = instance.ISetMaterialPropertyValues(MaterialPropertyValues)
```

### C#

```csharp
System.bool ISetMaterialPropertyValues(
   ref System.double MaterialPropertyValues
)
```

### C++/CLI

```cpp
System.bool ISetMaterialPropertyValues(
   System.double% MaterialPropertyValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MaterialPropertyValues`:

## VBA Syntax

See [Feature::ISetMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Feature~ISetMaterialPropertyValues.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
