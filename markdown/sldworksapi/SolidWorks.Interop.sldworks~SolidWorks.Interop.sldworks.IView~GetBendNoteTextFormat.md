---
title: "GetBendNoteTextFormat Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBendNoteTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat.html"
---

# GetBendNoteTextFormat Method (IView)

Gets the text format of all bend notes in this drawing view of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendNoteTextFormat() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.GetBendNoteTextFormat()
```

### C#

```csharp
System.string GetBendNoteTextFormat()
```

### C++/CLI

```cpp
System.String^ GetBendNoteTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Format of all bend notes in this drawing view

## VBA Syntax

See [View::GetBendNoteTextFormat](ms-its:sldworksapivb6.chm::/sldworks~View~GetBendNoteTextFormat.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetBendNoteTextFormat.html)
[IView::GetBendNoteAttributeString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteAttributeString.html)
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
