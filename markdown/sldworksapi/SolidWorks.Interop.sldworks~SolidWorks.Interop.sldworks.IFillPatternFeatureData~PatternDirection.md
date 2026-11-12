---
title: "PatternDirection Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternDirection.html"
---

# PatternDirection Property (IFillPatternFeatureData)

Gets or sets the direction reference for the layout of this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternDirection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Object

instance.PatternDirection = value

value = instance.PatternDirection
```

### C#

```csharp
System.object PatternDirection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction reference for the pattern layout

## VBA Syntax

See [FillPatternFeatureData::PatternDirection](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternDirection.html).

## Remarks

Before calling this property, call [IFillPatternFeatureData::PatternDirectionType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternDirectionType.html) to get the type of pattern direction reference returned by this property. If this property is not specified, SOLIDWORKS chooses an appropriate reference for the specified [IFillPatternFeatureData::PatternLayoutType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternLayoutType.html).

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
