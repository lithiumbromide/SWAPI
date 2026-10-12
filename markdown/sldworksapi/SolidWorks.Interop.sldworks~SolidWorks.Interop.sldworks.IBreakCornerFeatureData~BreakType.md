---
title: "BreakType Property (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "BreakType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~BreakType.html"
---

# BreakType Property (IBreakCornerFeatureData)

Gets or sets the break corner type.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim value As System.Integer

instance.BreakType = value

value = instance.BreakType
```

### C#

```csharp
System.int BreakType {get; set;}
```

### C++/CLI

```cpp
property System.int BreakType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Break corner type as defined in [swBreakCornerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

## VBA Syntax

See [BreakCornerFeatureData::BreakType](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~BreakType.html).

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
