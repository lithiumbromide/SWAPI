---
title: "FlipDirection Property (ISlotMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: "FlipDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection.html"
---

# FlipDirection Property (ISlotMateFeatureData)

Gets or sets whether to change the endpoint from where to measure distance.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
Dim value As System.Boolean

instance.FlipDirection = value

value = instance.FlipDirection
```

### C#

```csharp
System.bool FlipDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to change the endpoint, false to not

## VBA Syntax

See [SlotMateFeatureData::FlipDirection](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData~FlipDirection.html).

## See Also

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)
[ISlotMateFeatureData::Distance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Distance.html)
[ISlotMateFeatureData::Percent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Percent.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
