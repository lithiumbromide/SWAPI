---
title: "TotalInstances Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "TotalInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances.html"
---

# TotalInstances Property (ICircularPatternFeatureData)

Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Integer

instance.TotalInstances = value

value = instance.TotalInstances
```

### C#

```csharp
System.int TotalInstances {get; set;}
```

### C++/CLI

```cpp
property System.int TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total number of pattern instances in Direction 1

## VBA Syntax

See [CircularPatternFeatureData::TotalInstances](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~TotalInstances.html).

## Examples

[Get Transform for Each Circular Pattern Instance (C#)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm)
[Get Transform for Each Circular Pattern Instance (VB.NET)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm)
[Get Transform for Each Circular Pattern Instance (VBA)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.html)
[ICircularPatternFeatureData::Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.html)
[ICircularPatternFeatureData::TotalInstances2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
