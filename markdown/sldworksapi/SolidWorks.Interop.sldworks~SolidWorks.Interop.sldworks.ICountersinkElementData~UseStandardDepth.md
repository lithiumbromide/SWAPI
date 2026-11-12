---
title: "UseStandardDepth Property (ICountersinkElementData)"
project: "SOLIDWORKS API Help"
interface: "ICountersinkElementData"
member: "UseStandardDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~UseStandardDepth.html"
---

# UseStandardDepth Property (ICountersinkElementData)

Gets or sets whether to use the standard offset distance for the end condition of this countersink hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseStandardDepth As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICountersinkElementData
Dim value As System.Boolean

instance.UseStandardDepth = value

value = instance.UseStandardDepth
```

### C#

```csharp
System.bool UseStandardDepth {get; set;}
```

### C++/CLI

```cpp
property System.bool UseStandardDepth {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the standard offset distance, false to not (see **Remarks**)

## VBA Syntax

See [CountersinkElementData::UseStandardDepth](ms-its:sldworksapivb6.chm::/sldworks~CountersinkElementData~UseStandardDepth.html).

## Remarks

This property is valid only if [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html) is set to true.

If this property is set to false, then use [IAdvancedHoleElementData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.html) to set the custom offset distance.

## See Also

[ICountersinkElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
[ICountersinkElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.html)
[IAdvancedHoleElementData::OffsetReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
