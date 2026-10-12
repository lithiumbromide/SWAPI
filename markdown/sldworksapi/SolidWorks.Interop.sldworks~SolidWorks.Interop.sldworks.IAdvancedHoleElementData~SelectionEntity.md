---
title: "SelectionEntity Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "SelectionEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~SelectionEntity.html"
---

# SelectionEntity Property (IAdvancedHoleElementData)

Gets or sets the entity used to specify the Up to Selection or Offset from Surface end condition for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Object

instance.SelectionEntity = value

value = instance.SelectionEntity
```

### C#

```csharp
System.object SelectionEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition entity

## VBA Syntax

See [AdvancedHoleElementData::SelectionEntity](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~SelectionEntity.html).

## Remarks

This property is valid only when [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html):

- swEndCondOffsetFromSurface (end condition entity is a [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html))

- or -

- swEndCondUpToSelection (end condition entity is a face, surface, or plane)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
