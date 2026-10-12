---
title: "GapDistance Property (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "GapDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~GapDistance.html"
---

# GapDistance Property (IClosedCornerFeatureData)

Gets or sets the distance for the gap in a closed corner in a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim value As System.Double

instance.GapDistance = value

value = instance.GapDistance
```

### C#

```csharp
System.double GapDistance {get; set;}
```

### C++/CLI

```cpp
property System.double GapDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap distance

## VBA Syntax

See [ClosedCornerFeatureData::GapDistance](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~GapDistance.html).

## Examples

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
