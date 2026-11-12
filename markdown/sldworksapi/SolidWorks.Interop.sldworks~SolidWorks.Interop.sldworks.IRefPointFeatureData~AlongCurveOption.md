---
title: "AlongCurveOption Property (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "AlongCurveOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~AlongCurveOption.html"
---

# AlongCurveOption Property (IRefPointFeatureData)

Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlongCurveOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
Dim value As System.Integer

instance.AlongCurveOption = value

value = instance.AlongCurveOption
```

### C#

```csharp
System.int AlongCurveOption {get; set;}
```

### C++/CLI

```cpp
property System.int AlongCurveOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables this option, false does not

## VBA Syntax

See [RefPointFeatureData::AlongCurveOption](ms-its:sldworksapivb6.chm::/sldworks~RefPointFeatureData~AlongCurveOption.html).

## Examples

See [IRefPointFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPointFeatureData.html) examples.

## Examples

[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
