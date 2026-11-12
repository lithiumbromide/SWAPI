---
title: "PickPoints Property (IConcentricMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConcentricMateFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~PickPoints.html"
---

# PickPoints Property (IConcentricMateFeatureData)

Gets or sets the pick points for the entities to mate in this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConcentricMateFeatureData
Dim value As System.Object

instance.PickPoints = value

value = instance.PickPoints
```

### C#

```csharp
System.object PickPoints {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PickPoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of x, y, z-coordinates, one set for each mate entity

## VBA Syntax

See [ConcentricMateFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~ConcentricMateFeatureData~PickPoints.html).

## Remarks

After you set the pick points for a given selection of [IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html), you cannot modify the pick points. If you want to use new pick points, then you must create an entirely new concentric mate.

## See Also

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html)
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
