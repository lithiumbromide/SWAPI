---
title: "UseDefaultBendRelief Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "UseDefaultBendRelief"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendRelief.html"
---

# UseDefaultBendRelief Property (ISweptFlangeFeatureData)

Gets or sets whether to use the bend relief from the original sheet metal feature in this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRelief As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRelief = value

value = instance.UseDefaultBendRelief
```

### C#

```csharp
System.bool UseDefaultBendRelief {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRelief {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend relief, false to specify custom bend relief values (see **Remarks**)

## VBA Syntax

See [SweptFlangeFeatureData::UseDefaultBendRelief](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~UseDefaultBendRelief.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

For cylindrical/conical swept flanges, this property is valid only during creation.

If this property is false, then you can set:

- [ISweptFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.html)
- [ISweptFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseReliefRatio.html)

If ISweptFlangeFeatureData::UseReliefRatio is:

- True, then you can set [ISweptFlangeFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefRatio.html).
- False, then you can set [ISweptFlangeFeatureData::ReliefDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefDepth.html) and [ISweptFlangeFeatureData::ReliefWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefWidth.html).

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
