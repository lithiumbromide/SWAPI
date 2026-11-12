---
title: "GetNext Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.html"
---

# GetNext Method (INote)

Gets the next note in [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [Note::GetNext](ms-its:sldworksapivb6.chm::/sldworks~Note~GetNext.html).

## Examples

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)
[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)

## Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.html)
[IView::GetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.html)
[IView::IGetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstNote.html)
