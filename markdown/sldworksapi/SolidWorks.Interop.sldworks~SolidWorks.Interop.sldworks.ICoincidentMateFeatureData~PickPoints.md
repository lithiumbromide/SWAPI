---
title: "PickPoints Property (ICoincidentMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoincidentMateFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~PickPoints.html"
---

# PickPoints Property (ICoincidentMateFeatureData)

Gets or sets the pick points for the entities to mate in this coincident mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoincidentMateFeatureData
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

Array of x, y, z-coordinates, one set for each mate entity in [ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

## VBA Syntax

See [CoincidentMateFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~CoincidentMateFeatureData~PickPoints.html).

## Remarks

Pick points define the position of the entities to mate. If no pick points are specified, then entities are mated using default pick points.

After you create this mate using the pick points for a given selection of ICoincidentMateFeatureData::EntitiesToMate, you cannot edit the pick points. If you want to use new pick points, then you must create an entirely new coincident mate with mate entities and pick points.

If you pre-select the mate entities by coordinates (e.g., [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)), then you do not need to specify pick points.

## See Also

[ICoincidentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.html)
[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
