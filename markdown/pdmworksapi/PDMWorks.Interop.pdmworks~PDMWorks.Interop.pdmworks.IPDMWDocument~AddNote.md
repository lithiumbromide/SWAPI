---
title: "AddNote Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "AddNote"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~AddNote.html"
---

# AddNote Method (IPDMWDocument)

Adds a note to the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddNote( _
   ByVal action As System.String, _
   ByVal note As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim action As System.String
Dim note As System.String
Dim value As System.Integer

value = instance.AddNote(action, note)
```

### C#

```csharp
System.int AddNote(
   System.string action,
   System.string note
)
```

### C++/CLI

```cpp
System.int AddNote(
   System.String^ action,
   System.String^ note
)
```

### Parameters

- `action`: Action
- `note`: Note

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWDocument::AddNote](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~AddNote.html).

## Remarks

The note is added to the document history and includes the name of the current user and the time when the user added the note.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::Notes Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Notes.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
