---
title: "ExtrusionDirection Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "ExtrusionDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ExtrusionDirection.html"
---

# ExtrusionDirection Property (IRibFeatureData2)

Gets or sets the direction in which to extrude the rib.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtrusionDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Integer

instance.ExtrusionDirection = value

value = instance.ExtrusionDirection
```

### C#

```csharp
System.int ExtrusionDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ExtrusionDirection {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction as defined in [swRibExtrusionDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRibExtrusionDirection_e.html)

## VBA Syntax

See [RibFeatureData2::ExtrusionDirection](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~ExtrusionDirection.html).

## Examples

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html) examples.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
