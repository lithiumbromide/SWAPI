---
title: "PickPoints Property (ITangentMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITangentMateFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData~PickPoints.html"
---

# PickPoints Property (ITangentMateFeatureData)

Gets or sets the pick points for the entities to mate in this tangent mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITangentMateFeatureData
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

See [TangentMateFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~TangentMateFeatureData~PickPoints.html).

## Remarks

After you set the pick points for a given selection of [ITangentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData~EntitiesToMate.html), you cannot modify the pick points. If you want to use new pick points, then you must create an entirely new tangent mate.

## See Also

[ITangentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html)
[ITangentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
