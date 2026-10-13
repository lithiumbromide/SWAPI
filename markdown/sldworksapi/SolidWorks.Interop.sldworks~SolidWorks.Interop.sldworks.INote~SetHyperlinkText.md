---
title: "SetHyperlinkText Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetHyperlinkText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText.html"
---

# SetHyperlinkText Method (INote)

Sets the hyperlink in a note.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHyperlinkText( _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Text As System.String
Dim value As System.Boolean

value = instance.SetHyperlinkText(Text)
```

### C#

```csharp
System.bool SetHyperlinkText(
   System.string Text
)
```

### C++/CLI

```cpp
System.bool SetHyperlinkText(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text for hyperlink

### Return Value

True if the hyperlink is successfully set, false if not

## VBA Syntax

See [Note::SetHyperlinkText](ms-its:sldworksapivb6.chm::/sldworks~Note~SetHyperlinkText.html).

## Remarks

You can retrieve the hyperlink text using [INote::GetHyperlinkText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetHyperlinkText.html).

The input text can be a URL address or the name of a document on the local network or on your local system. You must specify the full address for a URL address, starting with the http://. You can specify a file name on your local network or system either as a full pathname or pathname relative to the current document, for example, D:\parts\drawing1.slddrw, or drawing1.slddrw.

To remove the hyperlink from a note, use this method and specify non-hyperlinked text.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetHyperlinkText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText.html)
