---
title: "Filter Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "Filter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~Filter.html"
---

# Filter Property (IStraightElementData)

Gets or sets the filter for this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Filter As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
Dim value As System.Integer

instance.Filter = value

value = instance.Filter
```

### C#

```csharp
System.int Filter {get; set;}
```

### C++/CLI

```cpp
property System.int Filter {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Filter as defined in [swStraightHoleFilter_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightHoleFilter_e.html)

## VBA Syntax

See [StraightElementData::Filter](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~Filter.html).

## Remarks

This property is valid only if [IAdvancedHoleElementData::Standard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Standard.html) is set to [swWzdHoleStandards_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandards_e.html):

- swStandardPEMInch

- or -

- swStandardPEMMetric

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
