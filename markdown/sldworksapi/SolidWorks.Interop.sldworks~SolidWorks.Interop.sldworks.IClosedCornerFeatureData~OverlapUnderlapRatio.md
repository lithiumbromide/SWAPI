---
title: "OverlapUnderlapRatio Property (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "OverlapUnderlapRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~OverlapUnderlapRatio.html"
---

# OverlapUnderlapRatio Property (IClosedCornerFeatureData)

Gets or sets the overlap/underlap ratio for this closed corner.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverlapUnderlapRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim value As System.Double

instance.OverlapUnderlapRatio = value

value = instance.OverlapUnderlapRatio
```

### C#

```csharp
System.double OverlapUnderlapRatio {get; set;}
```

### C++/CLI

```cpp
property System.double OverlapUnderlapRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ratio

## VBA Syntax

See [ClosedCornerFeatureData::OverlapUnderlapRatio](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~OverlapUnderlapRatio.html).

## Examples

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
