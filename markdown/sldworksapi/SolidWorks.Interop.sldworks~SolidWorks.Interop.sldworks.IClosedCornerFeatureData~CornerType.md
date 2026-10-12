---
title: "CornerType Property (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "CornerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~CornerType.html"
---

# CornerType Property (IClosedCornerFeatureData)

Gets or sets the closed corner type.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim value As System.Integer

instance.CornerType = value

value = instance.CornerType
```

### C#

```csharp
System.int CornerType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner type as defined in [swClosedCornerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swClosedCornerTypes_e.html)

## VBA Syntax

See [ClosedCornerFeatureData::CornerType](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~CornerType.html).

## Examples

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
