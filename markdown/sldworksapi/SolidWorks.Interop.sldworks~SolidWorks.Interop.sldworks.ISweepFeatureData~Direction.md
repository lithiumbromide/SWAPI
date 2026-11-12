---
title: "Direction Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html"
---

# Direction Property (ISweepFeatureData)

Gets or sets the direction type of this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.int Direction {get; set;}
```

### C++/CLI

```cpp
property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sweep path direction type as defined in [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html); -1 if not valid

## VBA Syntax

See [SweepFeatureData::Direction](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~Direction.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is valid only if the profile is a [sketch profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html), and the [sweep path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html) extends through both sides of the sketch profile.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
