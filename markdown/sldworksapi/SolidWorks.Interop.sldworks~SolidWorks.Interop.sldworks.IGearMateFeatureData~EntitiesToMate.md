---
title: "EntitiesToMate Property (IGearMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGearMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IGearMateFeatureData)

Gets or sets the entities to mate in this gear mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGearMateFeatureData
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

Array of two entities to mate (cylindrical or conical [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [axes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or linear [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html))

## VBA Syntax

See [GearMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~GearMateFeatureData~EntitiesToMate.html).

## Examples

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html) example.

## Remarks

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html)
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
