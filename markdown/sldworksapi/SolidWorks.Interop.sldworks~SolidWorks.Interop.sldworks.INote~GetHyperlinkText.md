---
title: "GetHyperlinkText Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetHyperlinkText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText.html"
---

# GetHyperlinkText Method (INote)

Gets the hyperlink in a note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHyperlinkText() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.String

value = instance.GetHyperlinkText()
```

### C#

```csharp
System.string GetHyperlinkText()
```

### C++/CLI

```cpp
System.String^ GetHyperlinkText();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Hyperlink text

## VBA Syntax

See [Note::GetHyperlinkText](ms-its:sldworksapivb6.chm::/sldworks~Note~GetHyperlinkText.html).

## Examples

[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)

## Remarks

You can create an embedded hyperlink on a note by using [INote::SetHyperlinkText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~SetHyperlinkText.html) or by using the hyperlink button on the note creation dialog.

This command first looks for an embedded hyperlink on the note and returns the text used to take the user to that document, which can be on the internet (a URL address is returned) or on your local network or hard drive (a pathname is returned). If the pathname was specified as a relative pathname, then the full pathname is returned.

If an embedded hyperlink does not exist, the note's text is searched for a hyperlink explicitly entered as part of the note text. This could be a URL address (a text string beginning with http://) or a file address (a text string beginning with file://).

If no hyperlink is found, either embedded or explicitly entered within the note text, an empty string is returned.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::SetHyperlinkText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
