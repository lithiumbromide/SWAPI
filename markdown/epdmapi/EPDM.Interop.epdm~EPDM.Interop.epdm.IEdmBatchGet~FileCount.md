---
title: "FileCount Property (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "FileCount"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~FileCount.html"
---

# FileCount Property (IEdmBatchGet)

Gets the number of files in this batch.

## Syntax

### Visual Basic

```vb
ReadOnly Property FileCount As System.Integer
```

### C#

```csharp
System.int FileCount {get;}
```

### C++/CLI

```cpp
property System.int FileCount {
   System.int get();
}
```

### Property Value

Number of files in this batch

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

This property is valid only after [IEdmBatchGet::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html) is called.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
