---
title: "EntitiesToMate Property (ICamFollowerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICamFollowerMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ICamFollowerMateFeatureData)

Gets or sets the entities to mate in this cam-follower mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate( _
   ByVal EntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICamFollowerMateFeatureData
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

- `EntityType`: Type of cam entity to mate as defined in [swCamMateEntityType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCamMateEntityType_e.html) (see **Remarks**)

### Property Value

Array of entities to mate (see **Remarks**)

## VBA Syntax

See [CamFollowerMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~CamFollowerMateFeatureData~EntitiesToMate.html).

## Examples

See the [ICamFollowerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.html) example.

## Remarks

Use this property with EntityType set to swCamMateEntityType_e.:

- CamPath, to get or set the cam [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) to mate.
- CamFollower, to get or set the cam-follower face or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) to mate.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1 for the cam face and Mark = 8 for the cam follower face or vertex. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[ICamFollowerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.html)
[ICamFollowerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
