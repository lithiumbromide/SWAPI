---
title: "GetEntityState Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetEntityState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.html"
---

# GetEntityState Method (IAttribute)

Returns the state of the associated entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityState( _
   ByVal WhichState As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim WhichState As System.Integer
Dim value As System.Boolean

value = instance.GetEntityState(WhichState)
```

### C#

```csharp
System.bool GetEntityState(
   System.int WhichState
)
```

### C++/CLI

```cpp
System.bool GetEntityState(
   System.int WhichState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichState`: Entity state are defined in [swAssociatedEntityStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssociatedEntityStates_e.html)

### Return Value

True if the query state matches WhichState, false if not

## VBA Syntax

See [Attribute::GetEntityState](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetEntityState.html).

## Examples

[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

## Remarks

If the attribute is not associated to any entity (that is, it is associated to the document), all queries return false.

The WhichState argument can take any of the values in the swAssociatedEntityStates_e, where:

- swIsEntityInvalid is a general query. It returns true when the associated entity is not valid due to a suppression or modeling operation.
- swIsEntitySuppressed is a more specific query. It returns true only if the associated entity is not valid due to a suppression.

[IAttribute::GetEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetEntity.html) and [IAttribute::IGetEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~IGetEntity2.html) return Nothing or null when the attribute is associated with:

- document
- invalid entity
- suppressed entity

For example, if an attribute is applied to a face on a boss feature and then that boss feature is suppressed, your application might make the following calls:

- IAttribute::GetEntity - Returns Nothing or null
- IAttribute::GetEntityState(`swIsEntityInvalid`) - Returns true to indicate possibly a suppressed or deleted entity
- IAttribute::GetEntityState(`swIsEntitySuppressed`) - Returns true to indicate that the entity is currently suppressed

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.html)
[IAnnotation::IGetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntities.html)
[IAttribute::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition.html)
[IAttribute::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.html)
[IAttribute::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetName.html)
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.html)
[IAttribute::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.html)
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.html)
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.html)
[IComponent2::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute.html)
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.html)
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.html)
[IEntity::GetSafeEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.html)
[IEntity::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetType.html)
[IFaultEntity::Entity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity.html)
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.html)
