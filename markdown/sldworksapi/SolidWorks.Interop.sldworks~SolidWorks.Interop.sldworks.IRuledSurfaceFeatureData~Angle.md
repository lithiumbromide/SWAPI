---
title: "Angle Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Angle.html"
---

# Angle Property (IRuledSurfaceFeatureData)

Gets or sets the taper angle of this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [RuledSurfaceFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~Angle.html).

## Remarks

This property is only available when [IRuledSurfaceFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~Type.html) is set to [swRuledSurfaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRuledSurfaceType_e.html).swRuledSurfaceType_TaperedToVector.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
