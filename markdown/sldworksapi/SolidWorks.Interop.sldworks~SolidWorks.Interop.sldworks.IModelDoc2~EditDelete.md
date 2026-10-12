---
title: "EditDelete Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditDelete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete.html"
---

# EditDelete Method (IModelDoc2)

Deletes the selected items.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditDelete()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.EditDelete()
```

### C#

```csharp
void EditDelete()
```

### C++/CLI

```cpp
void EditDelete();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::EditDelete](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditDelete.html).

## Examples

[Undo Deleted Note and Fire Undo Post-Notify Event (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Deleted Note and Fire Undo Post-Notify Event (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Deleted Note and Fire Undo Post-Notify Event (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## Remarks

Use [IModelDocExtension::DeleteSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DeleteSelection2.html) to turn off prompting the user to confirm the deletion.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditCopy.html)
[IModelDoc2::EditCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditCut.html)
[IModelDoc2::Paste Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Paste.html)
[IAssemblyDoc::DeleteSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
