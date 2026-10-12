---
title: "PickPoints Property (IParallelMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IParallelMateFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData~PickPoints.html"
---

# PickPoints Property (IParallelMateFeatureData)

Gets or sets the pick points for the entities to mate in this parallel mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IParallelMateFeatureData
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

See [ParallelMateFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~ParallelMateFeatureData~PickPoints.html).

## Remarks

After you set the pick points for a given selection of [IParallelMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData~EntitiesToMate.html), you cannot modify the pick points. If you want to use new pick points, then you must create an entirely new parallel mate.

## See Also

[IParallelMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.html)
[IParallelMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
