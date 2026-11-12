---
title: "SetMaterialPropertyValues Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues.html"
---

# SetMaterialPropertyValues Method (IFeature)

Obsolete. Superseded by [IFeature::SetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~SetMaterialPropertyValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialPropertyValues( _
   ByVal MaterialPropertyValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim MaterialPropertyValues As System.Object
Dim value As System.Boolean

value = instance.SetMaterialPropertyValues(MaterialPropertyValues)
```

### C#

```csharp
System.bool SetMaterialPropertyValues(
   System.object MaterialPropertyValues
)
```

### C++/CLI

```cpp
System.bool SetMaterialPropertyValues(
   System.Object^ MaterialPropertyValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MaterialPropertyValues`:

## VBA Syntax

See [Feature::SetMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetMaterialPropertyValues.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
