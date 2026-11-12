---
title: "EntitiesToMate Property (IRackPinionMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRackPinionMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IRackPinionMateFeatureData)

Gets or sets the entities to mate in this rack and pinion mate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate( _
   ByVal EntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRackPinionMateFeatureData
Dim EntityType As System.Integer
Dim value As System.Object

instance.EntitiesToMate(EntityType) = value

value = instance.EntitiesToMate(EntityType)
```

### C#

```csharp
System.object EntitiesToMate(
   System.int EntityType
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get(System.int EntityType);
   void set (System.int EntityType, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Entity type to mate as defined in [swRackPinionMateEntityType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateEntityType_e.html)

### Property Value

Array of entities to mate (see **Remarks**)

## VBA Syntax

See [RackPinionMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~RackPinionMateFeatureData~EntitiesToMate.html).

## Remarks

If EntityType is set to swRackPinionMateEntityType_e.:

- swRackPinionMateEntityType_Pinion, then set the array with a a cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) or [arc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html), sketch circle, [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), or revolved [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html).
- swRackPinionMateEntityType_Rack, then set the array with a linear edge, [sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [centerline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.html), axis, or cylindrical face.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 64 for the rack and Mark = 128 for the pinion. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html)
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
