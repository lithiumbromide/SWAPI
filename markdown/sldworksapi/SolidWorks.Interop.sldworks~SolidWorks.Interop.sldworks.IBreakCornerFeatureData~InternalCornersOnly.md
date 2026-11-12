---
title: "InternalCornersOnly Property (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "InternalCornersOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~InternalCornersOnly.html"
---

# InternalCornersOnly Property (IBreakCornerFeatureData)

Gets or sets whether to add or subtract material from break corner/corner trim features.

## Syntax

### Visual Basic (Declaration)

```vb
Property InternalCornersOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim value As System.Boolean

instance.InternalCornersOnly = value

value = instance.InternalCornersOnly
```

### C#

```csharp
System.bool InternalCornersOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool InternalCornersOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add or subtract material from break corner/corner trim features, false to not

## VBA Syntax

See [BreakCornerFeatureData::InternalCornersOnly](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~InternalCornersOnly.html).

## Examples

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)
