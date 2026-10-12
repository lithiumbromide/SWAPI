---
title: "SetEntityName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.html"
---

# SetEntityName Method (IPartDoc)

Sets the name of the entity if the entity does not have a name and the name is unique to the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityName( _
   ByVal Entity As System.Object, _
   ByVal StringValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Entity As System.Object
Dim StringValue As System.String
Dim value As System.Boolean

value = instance.SetEntityName(Entity, StringValue)
```

### C#

```csharp
System.bool SetEntityName(
   System.object Entity,
   System.string StringValue
)
```

### C++/CLI

```cpp
System.bool SetEntityName(
   System.Object^ Entity,
   System.String^ StringValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)
- `StringValue`: Name of the entity

### Return Value

True if name is set successfully, false if not

## VBA Syntax

See [PartDoc::SetEntityName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetEntityName.html).

## Examples

[Select and Rename Object (VBA)](Create_and_Rename_Objects_Example_VB.htm)
[Get Entity By Name (VBA)](Get_Entity_By_Name_Example.htm)
[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## Remarks

If the entity already has a name or the specified name is not unique to the part, then this method does not change the name and returns false.

This behavior is intended to prevent a program from accidentally renaming an entity that is referenced in some other location. For example, if an assembly contains a mate to a face on a part, then a name is automatically assigned to that face. If you were to change that name, then there is no guarantee that the mate is still valid. Therefore, when using entity names, you should first check to see if the entity is already named, and, if so, use the existing name. If no name exists for the entity, then you can name the entity.

You can explicitly delete an entity name using the [IPartDoc::DeleteEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~DeleteEntityName.html) or [IPartDoc::IDeleteEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IDeleteEntityName.html) method. You then have the option of renaming the item or using that name elsewhere. The method was provided because the action is already available in the core SOLIDWORKS Design software. However, you should recognize the possibility of reference failures as described.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.html)
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.html)
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.html)
[IPartDoc::ISetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ISetEntityName.html)
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.html)
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.html)
