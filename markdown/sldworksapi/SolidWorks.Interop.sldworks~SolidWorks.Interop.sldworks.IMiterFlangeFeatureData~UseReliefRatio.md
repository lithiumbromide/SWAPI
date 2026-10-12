---
title: "UseReliefRatio Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "UseReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.html"
---

# UseReliefRatio Property (IMiterFlangeFeatureData)

Gets or sets whether to use the specified relief ratio for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseReliefRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

True to use the specified relief ratio, false to not

## VBA Syntax

See [MiterFlangeFeatureData::UseReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~UseReliefRatio.html).

## Remarks

If this property is True, SOLIDWORKS uses [IMiterMiterFlangeFeatureData::ReliefRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefRatio.html). If it is false, SOLIDWORKS uses [IMiterFlangeFeatureData::ReliefDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefDepth.html) and [IMiterFlangeFeatureData::ReliefWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefWidth.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRelief.html)
[IMiterFlangeFeatureData::ReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefType.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
