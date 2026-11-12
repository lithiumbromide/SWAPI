---
title: "ReliefRatio Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (IOneBendFeatureData)

Gets and sets the relief ratio for the one bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Double

instance.ReliefRatio = value

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief ratio

## VBA Syntax

See [OneBendFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~ReliefRatio.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefDepth.html)
[IOneBendFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html)
[IOneBendFeatureData::UseAutoRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseAutoRelief.html)
[IOneBendFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html)
[IOneBendFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
