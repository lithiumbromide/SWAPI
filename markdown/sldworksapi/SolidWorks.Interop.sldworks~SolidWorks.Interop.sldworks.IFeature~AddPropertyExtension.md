---
title: "AddPropertyExtension Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IFeature)

Adds a property extension to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`: Value of the property extension to add to this feature

### Return Value

1 if the property extension is added to the feature, -1 if not

## VBA Syntax

See [Feature::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Feature~AddPropertyExtension.html).

## Remarks

This method does not support adding multiple property extensions to the same feature.

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the feature.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), or [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetPropertyExtension.html)
[IFeature::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ResetPropertyExtension.html)
