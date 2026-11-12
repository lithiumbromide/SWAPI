---
title: "ReferencePoint Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "ReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.html"
---

# ReferencePoint Property (ITablePatternFeatureData)

Gets or sets the reference point for pattern instances of this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Object

instance.ReferencePoint = value

value = instance.ReferencePoint
```

### C#

```csharp
System.object ReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference point of this table-driven pattern feature

## VBA Syntax

See [TablePatternFeatureData::ReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~ReferencePoint.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::GetReferencePointType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetReferencePointType.html)
[ITablePatternFeatureData::UseCentroid Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~UseCentroid.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
