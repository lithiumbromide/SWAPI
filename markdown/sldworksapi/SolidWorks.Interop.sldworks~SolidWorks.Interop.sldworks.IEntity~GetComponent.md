---
title: "GetComponent Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "GetComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetComponent.html"
---

# GetComponent Method (IEntity)

Gets the owning component for this entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponent() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim value As System.Object

value = instance.GetComponent()
```

### C#

```csharp
System.object GetComponent()
```

### C++/CLI

```cpp
System.Object^ GetComponent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Component that owns this entity

## VBA Syntax

See [Entity::GetComponent](ms-its:sldworksapivb6.chm::/sldworks~Entity~GetComponent.html).

## Examples

[Get Component for Selected Entity (VBA)](Get_Component_for_Selected_Entity_Example_VB.htm)
[Get Component from Feature (VBA)](Get_Component_from_Feature_Example_VB.htm)
[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## Remarks

You can use [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get the selected object in the assembly, then use the entity object representing that face or edge object to call this method.

This method works only when you get the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object directly from the assembly document or from an assembly entity that is displayed in a drawing document.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[IEntity::IGetComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IGetComponent2.html)
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.html)
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IEntity::GetSafeEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.html)
[IFaultEntity::Entity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
