---
title: "UseDefaultBendRelief Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "UseDefaultBendRelief"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRelief.html"
---

# UseDefaultBendRelief Property (IOneBendFeatureData)

Gets or sets whether to use the default bend relief of this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRelief As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRelief = value

value = instance.UseDefaultBendRelief
```

### C#

```csharp
System.bool UseDefaultBendRelief {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRelief {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend relief, false to not

## VBA Syntax

See [OneBendFeatureData::UseDefaultBendRelief](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~UseDefaultBendRelief.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefDepth.html)
[IOneBendFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefRatio.html)
[IOneBendFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~ReliefWidth.html)
[IOneBendFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseReliefRatio.html)
[IOneBendFeatureData:AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~AutoReliefType.html)

## Availability

SOLIDWORKS 2001 SP!, Revision Number 9.1
