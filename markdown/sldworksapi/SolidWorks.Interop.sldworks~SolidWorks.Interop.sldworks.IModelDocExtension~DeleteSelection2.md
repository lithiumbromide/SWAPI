---
title: "DeleteSelection2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteSelection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html"
---

# DeleteSelection2 Method (IModelDocExtension)

Deletes the selected items, with the option to delete absorbed features, child features, or both.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteSelection2( _
   ByVal DeleteOptions As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DeleteOptions As System.Integer
Dim value As System.Boolean

value = instance.DeleteSelection2(DeleteOptions)
```

### C#

```csharp
System.bool DeleteSelection2(
   System.int DeleteOptions
)
```

### C++/CLI

```cpp
System.bool DeleteSelection2(
   System.int DeleteOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DeleteOptions`: Options as defined in [swDeleteSelectionOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDeleteSelectionOptions_e.html)

### Return Value

True if the selected item is deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteSelection2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeleteSelection2.html).

## Examples

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)
[Delete Selected Feature (VBA)](Delete_Selected_Feature_Example_VB.htm)
[Undo Feature and Fire Undo Post-Notify Event (VBA)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Feature and Fire Undo Post Notify Event (VB.NET)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Feature and Fire Undo Post-Notify Event (C#)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## Remarks

This method does not ask the user to confirm the deletion.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IAssemblyDoc::DeleteSelections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections.html)
[IModel2::EditDelete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14.1
