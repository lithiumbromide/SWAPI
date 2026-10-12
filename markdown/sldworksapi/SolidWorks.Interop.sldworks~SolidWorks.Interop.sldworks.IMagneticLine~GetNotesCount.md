---
title: "GetNotesCount Method (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "GetNotesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotesCount.html"
---

# GetNotesCount Method (IMagneticLine)

Gets the number of notes attached to this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNotesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim value As System.Integer

value = instance.GetNotesCount()
```

### C#

```csharp
System.int GetNotesCount()
```

### C++/CLI

```cpp
System.int GetNotesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of attached notes

## VBA Syntax

See [MagneticLine::GetNotesCount](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~GetNotesCount.html).

## Examples

[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagnetLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.html)
[IMagnetLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
