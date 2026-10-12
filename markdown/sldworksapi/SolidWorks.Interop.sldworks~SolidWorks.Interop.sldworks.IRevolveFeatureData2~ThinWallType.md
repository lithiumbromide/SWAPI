---
title: "ThinWallType Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "ThinWallType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.html"
---

# ThinWallType Property (IRevolveFeatureData2)

Gets and sets the thin wall type for a thin revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinWallType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Integer

instance.ThinWallType = value

value = instance.ThinWallType
```

### C#

```csharp
System.int ThinWallType {get; set;}
```

### C++/CLI

```cpp
property System.int ThinWallType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type and direction as defined in [swThinWallType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

## VBA Syntax

See [RevolveFeatureData2::ThinWallType](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~ThinWallType.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
