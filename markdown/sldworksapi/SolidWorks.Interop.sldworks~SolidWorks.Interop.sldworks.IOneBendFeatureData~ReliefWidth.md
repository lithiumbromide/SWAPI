---
title: "ReliefWidth Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "ReliefWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html"
---

# ReliefWidth Property (IOneBendFeatureData)

Gets or sets the relief width of this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Double

instance.ReliefWidth = value

value = instance.ReliefWidth
```

### C#

```csharp
System.double ReliefWidth {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OneBendFeatureData::ReliefWidth](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~ReliefWidth.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefDepth.html)
[IOneBendFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html)
[IOneBendFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html)
[IOneBendFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html)
[IOneBendFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AutoReliefType.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
