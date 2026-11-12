---
title: "SelectByID2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SelectByID2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html"
---

# SelectByID2 Method (IModelDocExtension)

Selects the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByID2( _
   ByVal Name As System.String, _
   ByVal Type As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout, _
   ByVal SelectOption As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim Type As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim SelectOption As System.Integer
Dim value As System.Boolean

value = instance.SelectByID2(Name, Type, X, Y, Z, Append, Mark, Callout, SelectOption)
```

### C#

```csharp
System.bool SelectByID2(
   System.string Name,
   System.string Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout Callout,
   System.int SelectOption
)
```

### C++/CLI

```cpp
System.bool SelectByID2(
   System.String^ Name,
   System.String^ Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout^ Callout,
   System.int SelectOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of object to select or an empty string
- `Type`: Type of object (uppercase) as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) or an empty string
- `X`: X selection location or 0
- `Y`: Y selection location or 0
- `Z`: Z selection location or 0
- `Append`:

  | If... | An, if entity is... | Then... |
  | --- | --- | --- |
  | True | Not already selected | Entity is appended to the current selection list |
  |  | Already selected | Entity is removed from the current selection list |
  | False | Not already selected | Current selection is cleared and then the entity is put on the list |
  |  | Already selected | Current selection list remains the same |
- `Mark`: Value that you want to use as a mark; this value is used by other functions that require ordered selection (see **Remarks**)
- `Callout`: Pointer to the associated [callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html)
- `SelectOption`: Selection option as defined in [swSelectOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectOption_e.html) (see **Remarks**)

### Return Value

True if item was successfully selected, false if not

## VBA Syntax

See [ModelDocExtension::SelectByID2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SelectByID2.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)
[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Add Distance Mates (VBA)](Add_Distance_Mates_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Get Selected Object (VBA)](Get_Selected_Object_Example_VB.htm)
[Insert Wrap Feature (VBA)](Insert_Wrap_Feature_Example_VB.htm)
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)
[Connect to SOLIDWORKS Session (C#)](Connect_to_SOLIDWORKS_Session_CSharp.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)
[Select Multiple Sketch Segments for Sweep Path (C#)](Select_Multiple_Paths_for_Sweep_Path_Example_CSharp.htm)
[Select Multiple Sketch Segments for Sweep Path (VB.NET)](Select_Multiple_Paths_for_Sweep_Path_Example_VBNET.htm)
[Select Multiple Sketch Segments for Sweep Path (VBA)](Select_Multiple_Paths_for_Sweep_Path_Example_VB.htm)
[Select Multiple Splines for Loft Guide Curves (C#)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_CSharp.htm)
[Select Multiple Splines for Loft Guide Curves (VB.NET)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VBNET.htm)
[Select Multiple Splines for Loft Guide Curves (VBA)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VB.htm)

## Remarks

Use this method instead of using the selection methods on the following objects:

- [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)
- [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- [IFeatureManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager.html)
- [ISketchHatch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html)
- [ISketchPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)
- [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)
- [ISketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html)

The previously listed objects' selection methods do not work well when a PropertyManager page is open or a command is running. This method, IModelDocExtension::SelectByID2, handles selection correctly regardless if a command is running.

If your application already has an object handle (for example, IFace2), use the appropriate Select method to select the item directly using its handle.

To filter the objects selected by this method, set the Type parameter. If no filtering is required, then pass an empty string for this parameter.

For example, to select an object of type swSelDIMENSIONS, use the string that appears in the comment column, "DIMENSION". The objectType might change based on your current state. For example, to select a sketch point that was created in the active sketch, specify Type as "SKETCHPOINT". However, if you do not have an active sketch, or if the point was created in a sketch other than the active sketch, or the point is the origin point, then specify Type as "EXTSKETCHPOINT".

If Type is specified, then this method returns false if it cannot find the matching object type.

The Name parameter is not intended for selection of faces, edges, and so on. This is a case-sensitive string for objects that are automatically named by SOLIDWORKS during entity creation, such as dimensions, drawing views, and so on. This method tries to find and select an object whose name matches the Name parameter; however, the match needs to be exact for this method to return true.

For example:

- If a string is passed that matches an object name but whose case does not match exactly, then this method could return false. For selection of dimensions, the Name parameter must be fully qualified.
- Specify "D1@Sketch2@Part1.SLDPRT" rather than "D1@Sketch2"; otherwise, this method could return false. If you do not know the object name, or if it is an item that is not automatically named by SOLIDWORKS, you can pass an empty string.

If you are using the Name parameter, then specify the x, y, and z coordinates in terms of the context where the item was created. For example, if you want to select a sketch point using its name (for example, "Point1") in the Name parameter, then specify X, Y, and Z in terms of the sketch where the point was created. Even if the sketch is not active, specify the X, Y, and Z values in terms of sketch space when you use the Name parameter. In certain situations, you can also pass in the x, y, and z coordinates as (0,0,0). For example, to select a feature shown in the FeatureManager design tree, you do not need to specify x, y, and z coordinates. However, to select objects such as faces or when you need a point location picked, you must specify the x, y, and z coordinates. If you are not using the Name parameter as a filter, then specify the x, y, and z coordinates in terms of model space. The coordinates are used when the object name is not provided, and the coordinates are dependent on the view state.

If you do not know the object name or the object type, pass empty strings for the Name and Type parameters. The selection routine makes the best attempt to select the correct object.

To get [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) objects by name, use [IPartDoc::GetEntityByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetEntityByName.html) or [IPartDoc::IGetEntityByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetEntityByName.html).

For SelectOption, specify swSelectOption_e.swSelectOptionDefault to indicate that the Shift key is not used during selection or specify swSelectOption_e.swSelectOptionExtensive to indicate that the Shift key is used during selection.

The [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object used to call this method must be an open and visible document. For example, you cannot use the IModelDoc2 object returned from an assembly component ([IComponent2::GetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc.html) or [IComponent2::IGetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetModelDoc.html)) unless that SOLIDWORKS component part or subassembly is an open and visible document. In this case, you can select the item using the fully qualified name (for example, "Plane4@Part1-1@Assem1").

When selecting IFace2 objects, this method uses the specified point as input to the normal user-interface selection routines to use the speed of ray tracing. As a result, if the view changes from the original recorded size or orientation, then the same IFace2 might not be selected next time. If your application has a pointer to the IFace2 object to be selected, then you can call the [IEntity::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~Select4.html) method directly. Otherwise, you can call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html). Calling either of these methods allows for tighter control over the starting point and the direction in which to search. IModelDocExtension::SelectByRay is recorded when IModelDocExtension::SelectByID2 relies on the selection coordinates and prone to failure if the model view is altered.

Use:

- Mark of 4 when selecting multiple edges or sketch segments and grouping them into one object for the path for a sweep feature. See the **Select Multiple Sketch Segments for Sweep Path** examples.
- Mark of 2 when selecting multiple edges, sketch segments, or curves and grouping them into one object for the guide curves for a loft feature. See the **Select Multiple Splines for Loft Guide Curves** examples.
- [ISelectionMgr::AddSelectionListObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObject.html) and [ISelectionMgr::AddSelectionListObjects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.html) to add objects to a selection list without preselecting the objects in the user interface.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::MultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.html)
[IModelDocExtension::IMultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.html)
[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[IFeature::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)
[IAssemblyDoc::SelectComponentsBySize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize.html)
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
