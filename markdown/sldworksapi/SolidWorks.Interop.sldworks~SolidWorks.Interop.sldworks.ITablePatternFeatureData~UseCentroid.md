---
title: "UseCentroid Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "UseCentroid"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~UseCentroid.html"
---

# UseCentroid Property (ITablePatternFeatureData)

Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCentroid As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Boolean

instance.UseCentroid = value

value = instance.UseCentroid
```

### C#

```csharp
System.bool UseCentroid {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCentroid {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the seed feature's centroid as the reference point, false to not

## VBA Syntax

See [TablePatternFeatureData::UseCentroid](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~UseCentroid.html).

## Examples

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html) example.

## Remarks

If this property is set to false, then you must specify [ITablePatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.html).

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
