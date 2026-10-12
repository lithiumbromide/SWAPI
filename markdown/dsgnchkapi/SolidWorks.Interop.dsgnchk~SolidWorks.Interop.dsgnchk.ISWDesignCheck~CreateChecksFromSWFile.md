---
title: "CreateChecksFromSWFile Method (ISWDesignCheck)"
project: "SOLIDWORKS Design Checker API Help"
interface: "ISWDesignCheck"
member: "CreateChecksFromSWFile"
kind: "method"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~CreateChecksFromSWFile.html"
---

# CreateChecksFromSWFile Method (ISWDesignCheck)

Creates checks in the Check Builder Module from an existing SOLIDWORKS document, template, or drafting standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateChecksFromSWFile( _
   ByVal bstrSWFileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWDesignCheck
Dim bstrSWFileName As System.String
Dim value As System.Integer

value = instance.CreateChecksFromSWFile(bstrSWFileName)
```

### C#

```csharp
System.int CreateChecksFromSWFile(
   System.string bstrSWFileName
)
```

### C++/CLI

```cpp
System.int CreateChecksFromSWFile(
   System.String^ bstrSWFileName
)
```

### Parameters

- `bstrSWFileName`: Full path name of an existing SOLIDWORKS document or template (**see Remarks**)

### Return Value

Error code as defined in [dsgnchkError_e](SOLIDWORKS.Interop.dsgnchk~SOLIDWORKS.Interop.dsgnchk.dsgnchkError_e.html)

## VBA Syntax

See [SWDesignCheck::CreateChecksFromSWFile](ms-its:dsgnchkapivb6.chm::/DesignCheckerLib~SWDesignCheck~CreateChecksFromSWFile.html).

## Examples

[Create Checks From Document Example (VBA)](Create_Checks_From_Document_Example_VB.htm)
[Create Checks From Document Example (VB.NET)](Create_Checks_From_Document_Example_VBNET.htm)
[Create Checks From Document Example (C#)](Create_Checks_From_Document_Example_CSharp.htm)

## Remarks

This method can build checks from any of the following types of document:

- DWG (*.dwg),
- Part (*.prt,*.sldprt)
- Assembly (*.asm,*.sldasm)
- Drawing (*.drw,*.slddrw)
- Template (*.prtdot,*.asmdot,*.drwdot)
- Drafting Standard (*.sldstd)

## See Also

[ISWDesignCheck Interface](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck.html)
[ISWDesignCheck Members](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck_members.html)
[ISWDesignCheck::CheckAgainstExistingFile Method](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~CheckAgainstExistingFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
