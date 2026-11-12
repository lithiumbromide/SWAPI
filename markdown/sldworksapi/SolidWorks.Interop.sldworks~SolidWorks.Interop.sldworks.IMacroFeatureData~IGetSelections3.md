---
title: "IGetSelections3 Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetSelections3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.html"
---

# IGetSelections3 Method (IMacroFeatureData)

Gets the selected objects for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetSelections3( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Integer, _
   ByRef SelMarks As System.Integer, _
   ByRef DrViews As View, _
   ByRef ComponentXForms As MathTransform _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim ObjectTypes As System.Integer
Dim SelMarks As System.Integer
Dim DrViews As View
Dim ComponentXForms As MathTransform

instance.IGetSelections3(SelCount, Objects, ObjectTypes, SelMarks, DrViews, ComponentXForms)
```

### C#

```csharp
void IGetSelections3(
   System.int SelCount,
   out System.object Objects,
   out System.int ObjectTypes,
   out System.int SelMarks,
   out View DrViews,
   out MathTransform ComponentXForms
)
```

### C++/CLI

```cpp
void IGetSelections3(
   System.int SelCount,
   [Out] System.Object^ Objects,
   [Out] System.int ObjectTypes,
   [Out] System.int SelMarks,
   [Out] View^ DrViews,
   [Out] MathTransform^ ComponentXForms
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelCount`: Number of selected objects
- `Objects`: Array of selected objects of size SelCount
- `ObjectTypes`: Array of the selected object types as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) of size SelCount
- `SelMarks`: Array of marks associated with the selected objects of size SelCount
- `DrViews`: Array of [drawing views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) of size SelCount
- `ComponentXForms`: - in-process, unmanaged C++: Pointer to an array of [transforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) for the selections' components

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetSelectionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetSelectionCount.html) to determine the size of the arrays.

When a macro feature is inserted in-context and an entity on a different component is selected, you may need to know that component's transform.

If the assembly is the active document, then you can use [IEntity::IGetComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~IGetComponent2.html) or [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html) to get the component's transform.

However, if the part for the component is open for editing and a [macro feature is being edited](sldworksapiprogguide.chm::/Macro_Features/Edit_Definition_Function.htm), then you must use IMacroFeatureData::GetSelections3 to get the component's transform. This method returns the transform and the selection. If the selection belongs to the same part as the macro feature, then NULL is returned. See also [Macro Features and Component Transforms](sldworksapiprogguide.chm::/Macro_Features/Macro_Features_and_Component_Transforms.htm).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.html)
[IMacroFeatureData::ISetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.html)
[IMacroFeatureData::SetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
