---
title: "GetFirstNote2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstNote2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote2.html"
---

# GetFirstNote2 Method (IView)

Gets the first note in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstNote2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstNote2()
```

### C#

```csharp
System.object GetFirstNote2()
```

### C++/CLI

```cpp
System.Object^ GetFirstNote2();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See

[View::GetFirstNote2](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstNote2.html)

.

## Examples

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)

[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)

[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)

[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)

[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)

## Remarks

This method obsoletes IView::GetFirstNote by supporting inactive sheets.

The sheet must be visible. See[ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[INote::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
