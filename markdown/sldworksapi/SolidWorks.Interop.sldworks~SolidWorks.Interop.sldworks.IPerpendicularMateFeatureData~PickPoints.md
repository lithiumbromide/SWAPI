---
title: "PickPoints Property (IPerpendicularMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPerpendicularMateFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData~PickPoints.html"
---

# PickPoints Property (IPerpendicularMateFeatureData)

Gets or sets the pick points for the entities to mate in this perpendicular mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPerpendicularMateFeatureData
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

See [PerpendicularMateFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~PerpendicularMateFeatureData~PickPoints.html).

## Remarks

After you set the pick points for a given selection of [IPerpendicularMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData~EntitiesToMate.html), you cannot modify the pick points. If you want to use new pick points, then you must create an entirely new perpendicular mate.

## See Also

[IPerpendicularMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData.html)
[IPerpendicularMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
