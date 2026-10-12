---
title: "GeometryPattern Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GeometryPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GeometryPattern.html"
---

# GeometryPattern Property (ITablePatternFeatureData)

Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometryPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Boolean

instance.GeometryPattern = value

value = instance.GeometryPattern
```

### C#

```csharp
System.bool GeometryPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to pattern using only geometry of the features; false to pattern and solve entire features

## VBA Syntax

See [TablePatternFeatureData::GeometryPattern](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GeometryPattern.html).

## Examples

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html) example.

## Remarks

This property is valid with [ITablePatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray.html) or [ITablePatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.html) and is invalid with [ITablePatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.html).

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
