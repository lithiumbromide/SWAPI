---
title: "ReliefTearType Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReliefTearType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefTearType.html"
---

# ReliefTearType Property (IEdgeFlangeFeatureData)

Gets or sets the type of relief tear for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefTearType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer

instance.ReliefTearType = value

value = instance.ReliefTearType
```

### C#

```csharp
System.int ReliefTearType {get; set;}
```

### C++/CLI

```cpp
property System.int ReliefTearType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief tear type as defined in [swReliefTearType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReliefTearTypes_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::ReliefTearType](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReliefTearType.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendRelief.html) is set to false,

- and -

- [IEdgeFlangeFeatureData::AutoReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AutoReliefType.html) is set to swSheetMetalReliefTypes_e.swSheetMetalReliefTear.

The default value of this property is swReliefTearType_e.swReliefTearTypeRip.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefDepth.html)
[IEdgeFlangeFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefRatio.html)
[IEdgeFlangeFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefWidth.html)
[IEdgeFlangeFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseReliefRatio.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
