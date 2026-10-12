---
title: "AddFile Method (IEdmUpdateReferences)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUpdateReferences"
member: "AddFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences~AddFile.html"
---

# AddFile Method (IEdmUpdateReferences)

Adds an assembly or drawing to the batch of files for which to update file references.

## Syntax

### Visual Basic

```vb
Sub AddFile( _
   ByVal oPath As System.Object _
)
```

### C#

```csharp
void AddFile(
   System.object oPath
)
```

### C++/CLI

```cpp
void AddFile(
   System.Object^ oPath
)
```

### Parameters

- `oPath`: Full path to the file for which to update file references

## Examples

[Update References (C#)](Update_References_Example_CSharp.htm)
[Update References (VB.NET)](Update_References_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUpdateReferences Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences.html)
[IEdmUpdateReferences Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
