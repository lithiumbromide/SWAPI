---
title: "UseAutoRelief Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "UseAutoRelief"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseAutoRelief.html"
---

# UseAutoRelief Property (IOneBendFeatureData)

Gets or sets whether to use auto relief for this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAutoRelief As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Boolean

instance.UseAutoRelief = value

value = instance.UseAutoRelief
```

### C#

```csharp
System.bool UseAutoRelief {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAutoRelief {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use auto relief, false to not

## VBA Syntax

See [OneBendFeatureData::UseAutoRelief](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~UseAutoRelief.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html)
[IOneBendFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html)
[IOneBendFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html)
[IOneBendFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html)
[IOneBendFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AutoReliefType.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
