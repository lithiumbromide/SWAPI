---
title: "FindAttribute Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "FindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.html"
---

# FindAttribute Method (IEntity)

Finds an attribute on an entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindAttribute( _
   ByVal AttributeDef As System.Object, _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim AttributeDef As System.Object
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.FindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
System.object FindAttribute(
   System.object AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ FindAttribute(
   System.Object^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`: Attribute definition you want to find
- `WhichOne`: Instance of this type on this entity (0,1,2,3, and so on)

### Return Value

[Attribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) instance

## VBA Syntax

See [Entity::FindAttribute](ms-its:sldworksapivb6.chm::/sldworks~Entity~FindAttribute.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)
[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)
[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

## Remarks

After you add an attribute instance to a face, edge, vertex, loop, feature, or document, you can retrieve the attribute for query or modification in several ways:

- Because an attribute instance is a feature:

  - You can use any of the standard feature traversal functions ([IPartDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FeatureByName.html), [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html), and [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html)) to get the feature representation of the attribute. You can then use the Feature object that represents the attribute instance with [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get the underlying Attribute object.
  - It can be suppressed. Check its state by using [IAttribute::GetEntityState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetEntityState.html) (swIsEntitySuppressed).
- If the user selected the attribute in the FeatureManager design tree, you can use standard selection control to get the Feature object for the attribute instance ([ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)) and call Feature::GetSpecificFeature2 to get the underlying attribute object.
- If you traverse body topology, you can locate any Attribute object with a call to Entity::FindAttribute from the Entity object (for example, the face or edge). If the attribute instance was placed on the document, then you must use Feature::GetSpecificFeature2 to get back to it.
- Always call [IAttribute::GetEntityState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetEntityState.html) to check if the attribute instance is valid and unambiguous.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.html)
[IAttribute::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition.html)
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.html)
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.html)
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.html)
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.html)
