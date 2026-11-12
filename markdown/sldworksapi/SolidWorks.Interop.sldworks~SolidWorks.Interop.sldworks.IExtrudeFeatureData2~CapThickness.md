---
title: "CapThickness Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "CapThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.html"
---

# CapThickness Property (IExtrudeFeatureData2)

Gets or sets the end cap thickness for a thin base extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CapThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Double

instance.CapThickness = value

value = instance.CapThickness
```

### C#

```csharp
System.double CapThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CapThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thickness of the end cap

## VBA Syntax

See [ExtrudeFeatureData2::CapThickness](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~CapThickness.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)
[IExtrudeFeatureData2::CapEnds Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
