---
title: "GetPropertyExtension Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IFeature)

Gets the property extension on this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim ID As System.Integer
Dim value As System.Object

value = instance.GetPropertyExtension(ID)
```

### C#

```csharp
System.object GetPropertyExtension(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ GetPropertyExtension(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: 0

### Return Value

Value of the property extension on this feature

## VBA Syntax

See [Feature::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetPropertyExtension.html).

## Remarks

SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), or [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::AddPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddPropertyExtension.html)
[IFeature::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ResetPropertyExtension.html)
