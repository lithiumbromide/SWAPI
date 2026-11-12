---
title: "SetBendNoteTextFormat Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetBendNoteTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetBendNoteTextFormat.html"
---

# SetBendNoteTextFormat Method (IView)

Sets the text format of all bend notes in this drawing view of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBendNoteTextFormat( _
   ByVal Format As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Format As System.String
Dim value As System.Boolean

value = instance.SetBendNoteTextFormat(Format)
```

### C#

```csharp
System.bool SetBendNoteTextFormat(
   System.string Format
)
```

### C++/CLI

```cpp
System.bool SetBendNoteTextFormat(
   System.String^ Format
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Format`: Format in which to display all bend notes in this drawing view of a sheet metal part (see **Remarks**)

### Return Value

True if format is successfully set, false if not

## VBA Syntax

See [View::SetBendNoteTextFormat](ms-its:sldworksapivb6.chm::/sldworks~View~SetBendNoteTextFormat.html).

## Remarks

Before calling this method, call [IView::GetBendNoteAttributeString](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBendNoteAttributeString.html) to specify Format.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat.html)
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
