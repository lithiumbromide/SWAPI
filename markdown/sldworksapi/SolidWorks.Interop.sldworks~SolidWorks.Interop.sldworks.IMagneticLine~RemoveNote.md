---
title: "RemoveNote Method (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "RemoveNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.html"
---

# RemoveNote Method (IMagneticLine)

Detaches the specified note from this magnetic line and moves it to the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveNote( _
   ByVal Note As Note, _
   ByVal Location As MathPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim Note As Note
Dim Location As MathPoint
Dim value As System.Boolean

value = instance.RemoveNote(Note, Location)
```

### C#

```csharp
System.bool RemoveNote(
   Note Note,
   MathPoint Location
)
```

### C++/CLI

```cpp
System.bool RemoveNote(
   Note^ Note,
   MathPoint^ Location
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Note`: [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) to detach from this magnetic line
- `Location`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where to move the note specified by Note

### Return Value

True if successful, false if not

## VBA Syntax

See [MagneticLine::RemoveNote](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~RemoveNote.html).

## Examples

[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::AddNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.html)
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.html)
[IMagneticLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
