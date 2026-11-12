---
title: "GetCutListItems Method (ISwDMConfiguration16)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration16"
member: "GetCutListItems"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16~GetCutListItems.html"
---

# GetCutListItems Method (ISwDMConfiguration16)

Gets the cut-list items for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCutListItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration16
Dim value As System.Object

value = instance.GetCutListItems()
```

### C#

```csharp
System.object GetCutListItems()
```

### C++/CLI

```cpp
System.Object^ GetCutListItems();
```

### Return Value

Array of [cut-list items](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3.html)

## VBA Syntax

See [SwDMConfiguration16::GetCutListItems](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration16~GetCutListItems.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)

## Remarks

This method only works with documents saved in SOLIDWORKS 2019 or later for:

- the active configuration

- or -

- those configurations for which **Add Rebuild on Save Mark** was selected in the SOLIDWORKS ConfigurationManager before the document was saved.

## See Also

[ISwDMConfiguration16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16.html)
[ISwDMConfiguration16 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16_members.html)

## Availability

SOLIDWORKS Document Manager API 2019 SP0
