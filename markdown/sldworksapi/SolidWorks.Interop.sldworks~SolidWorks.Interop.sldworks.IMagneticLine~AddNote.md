---
title: "AddNote Method (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "AddNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.html"
---

# AddNote Method (IMagneticLine)

Attaches to this magnetic line the specified note at the specified position.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddNote( _
   ByVal Note As Note, _
   ByVal Position As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim Note As Note
Dim Position As System.Double
Dim value As System.Boolean

value = instance.AddNote(Note, Position)
```

### C#

```csharp
System.bool AddNote(
   Note Note,
   System.double Position
)
```

### C++/CLI

```cpp
System.bool AddNote(
   Note^ Note,
   System.double Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Note`: [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) to attach to this magnetic line
- `Position`: 0.0 <= Attachment position on magnetic line <= 1.0; valid only if [IMagneticLine::EqualSpacing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine~EqualSpacing.html) is false

### Return Value

True if successful, false if not (see **Remarks**)

## VBA Syntax

See [MagneticLine::AddNote](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~AddNote.html).

## Examples

[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)

## Remarks

All notes attached to a magnetic line must be from the same view.

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::RemoveNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.html)
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.html)
[IMagneticLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
