---
title: "EntitiesToMate Property (ISlotMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ISlotMateFeatureData)

Gets or sets the entities to mate in this slot mate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of two entities to mate (see **Remarks**)

## VBA Syntax

See [SlotMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData~EntitiesToMate.html).

## Examples

See the [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html) example.

## Remarks

Select the [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) of a straight or arced slot and another entity:

- Face of another straight or arced slot
- [Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
- Cylindrical face

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
