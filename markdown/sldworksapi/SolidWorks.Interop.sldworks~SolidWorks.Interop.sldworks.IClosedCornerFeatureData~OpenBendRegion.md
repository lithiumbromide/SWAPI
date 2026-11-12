---
title: "OpenBendRegion Property (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "OpenBendRegion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~OpenBendRegion.html"
---

# OpenBendRegion Property (IClosedCornerFeatureData)

Gets or sets whether this closed corner has an open bend region.

## Syntax

### Visual Basic (Declaration)

```vb
Property OpenBendRegion As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim value As System.Boolean

instance.OpenBendRegion = value

value = instance.OpenBendRegion
```

### C#

```csharp
System.bool OpenBendRegion {get; set;}
```

### C++/CLI

```cpp
property System.bool OpenBendRegion {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if an open bend region, false if not

## VBA Syntax

See [ClosedCornerFeatureData::OpenBendRegion](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~OpenBendRegion.html).

## Examples

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
