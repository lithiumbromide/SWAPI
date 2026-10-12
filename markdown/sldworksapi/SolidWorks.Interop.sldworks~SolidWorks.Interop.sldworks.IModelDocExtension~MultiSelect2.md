---
title: "MultiSelect2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "MultiSelect2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2.html"
---

# MultiSelect2 Method (IModelDocExtension)

Selects multiple objects and returns the number of objects selected in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiSelect2( _
   ByVal Objects As System.Object, _
   ByVal AppendFlag As System.Boolean, _
   ByVal Data As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Objects As System.Object
Dim AppendFlag As System.Boolean
Dim Data As System.Object
Dim value As System.Integer

value = instance.MultiSelect2(Objects, AppendFlag, Data)
```

### C#

```csharp
System.int MultiSelect2(
   System.object Objects,
   System.bool AppendFlag,
   System.object Data
)
```

### C++/CLI

```cpp
System.int MultiSelect2(
   System.Object^ Objects,
   System.bool AppendFlag,
   System.Object^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`: Array of selectable objects:

  - can be the same type of objects (e.g., an array of faces or an array of edges) or different types of objects (e.g., an array of entities of faces and edges )
  - if an object is not selected, then it is ignored
- `AppendFlag`: True to append the objects to the selection list, false to replace the current selection list with these objects
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object, Nothing, or null

### Return Value

Number of objects selected in the model

## VBA Syntax

See [ModelDocExtension::MultiSelect2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~MultiSelect2.html).

## Examples

[Select Multiple Objects for Selection Boxes (C#)](Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm)
[Select Multiple Objects for Selection Boxes (VB.NET)](Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm)
[Select Multiple Objects for Selection Boxes (VBA)](Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm)
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)
[Multiselect Same and Different Objects (C#)](Multiselect_Same%20and_Different_Objects_Example_CSharp.htm)
[Multiselect Same and Different Objects (VB.NET)](Multiselect_Same%20and_Different_Objects_Example_VBNET.htm)
[Multiselect Same and Different Objects (VBA)](Multiselect_Same%20and_Different_Objects_Example_VB.htm)

## Remarks

| If using this method to populate... | Then... |
| --- | --- |
| A selection box in a PropertyManager page | IPropertyManagerPage2Handler9::OnSubmitSelection fires when set to true and ISelectData::Mark is set to either a 0 or a non-0 value. NOTE : IPropertyManagerPage2Handler9::OnSubmitSelection only fires when set to true and ISelectData::Mark is set to 0 if using either of the now obsolete ModelDocExtension::MultiSelect and IModelDocExtension::IMultiSelect methods. |
| Multiple selection boxes with different multiple selections in a PropertyManager page | Set: each selection box's IPropertyManagerPageSelectionbox::Mark to a different power of two; for example, 1, 2, 4, 8, etc. (Setting a selection box's mark to 0 causes all selections to appear in that selection box and the active selection box.) ISelectData::Mark and each selection box's IPropertyManagerPageSelectionbox::Mark to the same value. See the examples for details. |

**NOTE:** If an object is already selected with a mark of `x` and you attempt to select the same object again using this method with AppendFlag = true, then that object remains selected with a mark with `x`. Reselecting a previously selected object does not assign a new mark value.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)

## Availability

SoidWorks 2012 SP04, Revision Number 20.4
