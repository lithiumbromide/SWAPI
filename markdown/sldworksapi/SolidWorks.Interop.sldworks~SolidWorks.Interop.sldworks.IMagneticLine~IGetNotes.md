---
title: "IGetNotes Method (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "IGetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.html"
---

# IGetNotes Method (IMagneticLine)

Gets the notes attached to this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNotes( _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim Count As System.Integer
Dim value As Note

value = instance.IGetNotes(Count)
```

### C#

```csharp
Note IGetNotes(
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetNotes(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of notes returned by this method (see **Remarks**)

### Return Value

- In-process, unmanaged C++: Pointer to an array of [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IMagneticLine::GetNotesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine~GetNotesCount.html) to get the value of Count.

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.html)
[IMagneticLine::AddNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.html)
[IMagneticLine::RemoveNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
