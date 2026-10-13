---
title: "MultiSelect Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "MultiSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.html"
---

# MultiSelect Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::MultiSelect2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~MultiSelect2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiSelect( _
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

value = instance.MultiSelect(Objects, AppendFlag, Data)
```

### C#

```csharp
System.int MultiSelect(
   System.object Objects,
   System.bool AppendFlag,
   System.object Data
)
```

### C++/CLI

```cpp
System.int MultiSelect(
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

See [ModelDocExtension::MultiSelect](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~MultiSelect.html).

## Remarks

If this now obsolete method is used to populate a selection box in a PropertyManager page, then [IPropertyManagerPage2Handler9::OnSubmitSelection](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSubmitSelection.html) only fires when set to true and [ISelectData::Mark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData~Mark.html) is set to 0.

Use [IModelDocExtension::MultiSelect2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~MultiSelect2.html) if you need IPropertyManagerPage2Handler9::OnSubmitSelection to fire when set to true and ISelectData::Mark is set to either a 0 or non-0 value.

The [Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData~Callout.html) property of the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object is not used by this method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IModelDocSelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.html)
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
