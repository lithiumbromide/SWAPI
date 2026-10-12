---
title: "ReverseThicknessDir Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "ReverseThicknessDir"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir.html"
---

# ReverseThicknessDir Property (IRibFeatureData2)

Gets or sets whether the extrusion is on the reverse side of this single-sided rib.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseThicknessDir As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Boolean

instance.ReverseThicknessDir = value

value = instance.ReverseThicknessDir
```

### C#

```csharp
System.bool ReverseThicknessDir {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseThicknessDir {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this single-sided rib is extruded on the reverse side, false if not

## VBA Syntax

See [RibFeatureData2::ReverseThicknessDir](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~ReverseThicknessDir.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## Remarks

This property is valid only when [IRibFeatureData2::IsTwoSided](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IsTwoSided.html) is set to false.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
