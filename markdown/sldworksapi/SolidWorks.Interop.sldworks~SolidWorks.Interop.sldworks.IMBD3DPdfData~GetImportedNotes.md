---
title: "GetImportedNotes Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "GetImportedNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetImportedNotes.html"
---

# GetImportedNotes Method (IMBD3DPdfData)

Gets the imported note names from the theme of this MBD3DPdfData.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportedNotes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Object

value = instance.GetImportedNotes()
```

### C#

```csharp
System.object GetImportedNotes()
```

### C++/CLI

```cpp
System.Object^ GetImportedNotes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of imported note names

## VBA Syntax

See [MBD3DPdfData::GetImportedNotes](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~GetImportedNotes.html).

## Examples

See the [IMBD3DPdfData::SetImportedNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetImportedNote.html) example.

## Remarks

Before calling this method, you need to use [IMBD3DPdfData::ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) to set the theme of this MBD3DPdfData.

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
