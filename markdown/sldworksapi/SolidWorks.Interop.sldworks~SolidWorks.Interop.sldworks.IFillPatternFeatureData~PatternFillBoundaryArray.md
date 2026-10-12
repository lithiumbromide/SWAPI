---
title: "PatternFillBoundaryArray Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternFillBoundaryArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternFillBoundaryArray.html"
---

# PatternFillBoundaryArray Property (IFillPatternFeatureData)

Gets or sets the array of objects representing the boundary of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFillBoundaryArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Object

instance.PatternFillBoundaryArray = value

value = instance.PatternFillBoundaryArray
```

### C#

```csharp
System.object PatternFillBoundaryArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFillBoundaryArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of objects representing the fill boundary

## VBA Syntax

See [FillPatternFeatureData::PatternFillBoundaryArray](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternFillBoundaryArray.html).

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
