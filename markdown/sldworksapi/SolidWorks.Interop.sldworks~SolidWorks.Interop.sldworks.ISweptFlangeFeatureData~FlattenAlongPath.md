---
title: "FlattenAlongPath Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "FlattenAlongPath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.html"
---

# FlattenAlongPath Property (ISweptFlangeFeatureData)

Gets or sets whether to flatten the flange profile along the sweep path of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlattenAlongPath As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.FlattenAlongPath = value

value = instance.FlattenAlongPath
```

### C#

```csharp
System.bool FlattenAlongPath {get; set;}
```

### C++/CLI

```cpp
property System.bool FlattenAlongPath {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flatten the profile along the sweep path, false to not

## VBA Syntax

See [SweptFlangeFeatureData::FlattenAlongPath](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~FlattenAlongPath.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

This property is valid only when not creating the swept flange on an existing sheet metal feature.

If this property is true, then you can also specify [ISweptFlangeFeatureData::MaterialInside](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~MaterialInside.html).

If this property is:

- True, then when the model is flattened the [profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.html) flattens and is rotated parallel to the plane of the path. The [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html) is not flattened, and the result is a the shape of the path.
- False, then when the model is flattened the profile flattens and is rotated perpendicular to the plane of the path. The path is flattened, and the result is a rectangular shape.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
