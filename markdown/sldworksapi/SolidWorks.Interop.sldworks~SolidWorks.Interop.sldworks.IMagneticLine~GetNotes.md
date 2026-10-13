---
title: "GetNotes Method (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "GetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.html"
---

# GetNotes Method (IMagneticLine)

Gets the notes attached to this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNotes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim value As System.Object

value = instance.GetNotes()
```

### C#

```csharp
System.object GetNotes()
```

### C++/CLI

```cpp
System.Object^ GetNotes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of attached [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)s

## VBA Syntax

See [MagneticLine::GetNotes](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~GetNotes.html).

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::GetNotesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotesCount.html)
[IMagneticLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.html)
[IMagneticLine::AddNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.html)
[IMagneticLine::RemoveNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
