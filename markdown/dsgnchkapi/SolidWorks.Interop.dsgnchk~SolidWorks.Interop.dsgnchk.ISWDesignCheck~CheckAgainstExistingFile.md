---
title: "CheckAgainstExistingFile Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "CheckAgainstExistingFile"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~CheckAgainstExistingFile.html"
---

# CheckAgainstExistingFile Method (ISWDesignCheck)

Validates an active document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CheckAgainstExistingFile()
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck

instance.CheckAgainstExistingFile()
```

### C#

```csharp
void CheckAgainstExistingFile()
```

### C++/CLI

```cpp
void CheckAgainstExistingFile();
```

## VBA Syntax

See [SWDesignCheck::CheckAgainstExistingFile](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~CheckAgainstExistingFile.html).

## Examples

[Check Against Existing File Example (VBA)](Check_Against_Existing_File_Example_VB.htm)
[Check Against Existing File Example (VB.NET)](Check_Against_Existing_File_Example_VBNET.htm)
[Check Against Existing File Example (C#)](Check_Against_Existing_File_Example_CSharp.htm)

## Remarks

This method launches a dialog from which to choose a file. After the file is selected, Check Builder launches and creates checks from it. After the checks are built, Design Checker validates the active document against the checks and displays the results on a tab in the SOLIDWORKS Task Pane.

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)
[ISWDesignCheck::CreateChecksFromSWFile Method](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~CreateChecksFromSWFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
