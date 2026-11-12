---
title: "AutoReliefType Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "AutoReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AutoReliefType.html"
---

# AutoReliefType Property (IOneBendFeatureData)

Gets or sets the auto-relief type from this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

instance.AutoReliefType = value

value = instance.AutoReliefType
```

### C#

```csharp
System.int AutoReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int AutoReliefType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Auto-relief type as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

## VBA Syntax

See [OneBendFeatureData::AutoReliefType](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~AutoReliefType.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefDepth.html)
[IOneBendFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html)
[IOneBendFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html)
[IOneBendFeatureData::UseAutoRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseAutoRelief.html)
[IOneBendFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html)
[IOneBendFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
