---
title: "EntitiesToMate Property (IHingeMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHingeMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IHingeMateFeatureData)

Gets or sets the entities to mate in this hinge mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate( _
   ByVal EntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHingeMateFeatureData
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

- `EntityType`: Type of entity as defined in [swHingeMateEntityType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHingeMateEntityType_e.html)

### Property Value

Array of mate entities (see **Remarks**)

## VBA Syntax

See [HingeMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~HingeMateFeatureData~EntitiesToMate.html).

## Examples

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html) example.

## Remarks

If EntityType is set to swHingeMateEntityType_e.:

- swHingeMateEntityType_Concentric, then select two mate entities as specified in the Remarks of [IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html).
- swHingeMateEntityType_Coincident, then select two mate entities:

  1. [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html) or planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
  2. another plane or planar face, [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html), [reference point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
- swHingeMateEntityType_Angle, then select two faces. This type is valid only if [IHingeMateFeatureData::AngleSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.html) is set to true.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1 for concentric entities, Mark = 32768 for coincident entities, and Mark = 65536 for angle faces. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html)
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
