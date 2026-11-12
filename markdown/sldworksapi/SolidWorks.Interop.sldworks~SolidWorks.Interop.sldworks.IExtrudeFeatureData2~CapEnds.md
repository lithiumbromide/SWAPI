---
title: "CapEnds Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "CapEnds"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.html"
---

# CapEnds Property (IExtrudeFeatureData2)

Caps the ends for a thin base extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CapEnds As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.CapEnds = value

value = instance.CapEnds
```

### C#

```csharp
System.bool CapEnds {get; set;}
```

### C++/CLI

```cpp
property System.bool CapEnds {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True caps the ends, false does not

## VBA Syntax

See [ExtrudeFeatureData2::CapEnds](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~CapEnds.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)
[IExtrudeFeatureData2::CapThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
