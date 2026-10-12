---
title: "Select4 Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "Select4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.html"
---

# Select4 Method (IEntity)

Selects an entity and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select4(Append, Data)
```

### C#

```csharp
System.bool Select4(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select4(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the entity to the selection list, false replaces the selection list with this entity
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the selection is successful, false if not

## VBA Syntax

See [Entity::Select4](ms-its:sldworksapivb6.chm::/sldworks~Entity~Select4.html).

## Examples

[Check Interference Using IAssemblyDoc::ToolsCheckInterference2 (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)
[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

When you use this method, selection behaves differently depending on the command state of SOLIDWORKS. One case is when SOLIDWORKS is running a command that has a PropertyManager associated with a selection list box (for example, a feature creation command such as Insert Fillet). The selection behavior in this case is:

- Selecting a new entity appends it to the selection list.

- or -

- Selecting an entity that is already selected deselects the entity.

SOLIDWORKS ignores the Append argument because the selection is always appended to the selection list.

The second case is when there is no command running, which is the default state of SOLIDWORKS.

You can use this method only with [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) objects that you get from the active document. For example, if Assembly1 is the active document when you call this method, then you must get the entity directly from the Assembly1 document. You can do this using items in the selection list (for example, [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)) or you can traverse the body of an assembly component (for example, [IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html) and [IBody2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFirstFace.html)). You cannot obtain the entity from the underlying part document (for example, [IComponent2::GetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc.html) or [IBody2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFirstFace.html)).

You can use this method to select features. In Visual C++, you must first get the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) interface from the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
