---
title: "SkippedItemArray Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (IFillPatternFeatureData)

Gets or sets the pattern instances to skip in this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Object

instance.SkippedItemArray = value

value = instance.SkippedItemArray
```

### C#

```csharp
System.object SkippedItemArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SkippedItemArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of pattern instances to skip (see **Remarks**)

## VBA Syntax

See [FillPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~SkippedItemArray.html).

## Remarks

The array is linear and zero-based and contains the (row_id, column_id) of each pattern instance to skip.

For example,

[row_id_instance1, column_id_instance1, row_id_instance2, column_id_instance2, ...]

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
