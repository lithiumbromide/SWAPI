---
title: "UseReliefRatio Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "UseReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html"
---

# UseReliefRatio Property (IOneBendFeatureData)

Gets or sets whether to use the relief ratio for this bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseReliefRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Boolean

instance.UseReliefRatio = value

value = instance.UseReliefRatio
```

### C#

```csharp
System.bool UseReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool UseReliefRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the relief ratio, false to not

## VBA Syntax

See [OneBendFeatureData::UseReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~UseReliefRatio.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefDepth.html)
[IOneBendFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html)
[IOneBendFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html)
[IOneBendFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html)
[IOneBendFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AutoReliefType.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
