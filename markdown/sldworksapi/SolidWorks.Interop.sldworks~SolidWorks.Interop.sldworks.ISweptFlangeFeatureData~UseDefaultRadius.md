---
title: "UseDefaultRadius Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "UseDefaultRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultRadius.html"
---

# UseDefaultRadius Property (ISweptFlangeFeatureData)

Gets or sets whether to use the bend radius from the original sheet metal feature in this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean

instance.UseDefaultRadius = value

value = instance.UseDefaultRadius
```

### C#

```csharp
System.bool UseDefaultRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the original sheet metal bend radius, false to use a custom bend radius (see **Remarks**)

## VBA Syntax

See [SweptFlangeFeatureData::UseDefaultRadius](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~UseDefaultRadius.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

If this property is false, then use [ISweptFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~BendRadius.html) to get or set a custom bend radius.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
