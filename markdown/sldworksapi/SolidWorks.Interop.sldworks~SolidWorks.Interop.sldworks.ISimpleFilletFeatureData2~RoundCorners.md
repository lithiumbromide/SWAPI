---
title: "RoundCorners Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "RoundCorners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners.html"
---

# RoundCorners Property (ISimpleFilletFeatureData2)

Gets or sets whether to round the corners of this simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoundCorners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.RoundCorners = value

value = instance.RoundCorners
```

### C#

```csharp
System.bool RoundCorners {get; set;}
```

### C++/CLI

```cpp
property System.bool RoundCorners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if simple fillet feature has round corners, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::RoundCorners](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~RoundCorners.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

This property is valid only if [ISimpleFilletFeatureData2::CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html) is false, and at least two adjacent edges to fillet are selected.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
