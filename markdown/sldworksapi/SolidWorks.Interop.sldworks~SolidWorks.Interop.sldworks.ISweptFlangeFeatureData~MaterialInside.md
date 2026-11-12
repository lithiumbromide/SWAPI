---
title: "MaterialInside Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "MaterialInside"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~MaterialInside.html"
---

# MaterialInside Property (ISweptFlangeFeatureData)

Gets or sets whether to flatten the flange profile with material inside of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialInside As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.MaterialInside = value

value = instance.MaterialInside
```

### C#

```csharp
System.bool MaterialInside {get; set;}
```

### C++/CLI

```cpp
property System.bool MaterialInside {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flatten the flange profile with material inside, false to not

## VBA Syntax

See [SweptFlangeFeatureData::MaterialInside](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~MaterialInside.html).

## Remarks

This property is valid only:

- if [ISweptFlangeFeatureData::FlattenAlongPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.html) is true,

- and -

- when not creating the swept flange on an existing sheet metal feature.

The flat pattern of the model may fail for either setting of this property, depending on whether self-intersecting geometry occurs with material inside or outside. You should test your model to determine which setting of this property successfully flattens the flange [profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.html).

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
