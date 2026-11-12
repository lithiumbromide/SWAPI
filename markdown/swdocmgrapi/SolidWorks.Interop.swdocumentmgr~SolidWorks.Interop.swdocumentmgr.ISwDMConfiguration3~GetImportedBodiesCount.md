---
title: "GetImportedBodiesCount Method (ISwDMConfiguration3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration3"
member: "GetImportedBodiesCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.html"
---

# GetImportedBodiesCount Method (ISwDMConfiguration3)

Gets the number of imported solid bodies in this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportedBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration3
Dim value As System.Integer

value = instance.GetImportedBodiesCount()
```

### C#

```csharp
System.int GetImportedBodiesCount()
```

### C++/CLI

```cpp
System.int GetImportedBodiesCount();
```

### Return Value

Number of imported solid bodies; this is a 0-based index

## VBA Syntax

See [SwDMConfiguration3::GetImportedBodiesCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration3~GetImportedBodiesCount.html).

## Remarks

This method does not include the number of imported surface bodies, if any.

Call this method before [ISwDMConfiguration3::GetImportedBody](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.html).

## See Also

[ISwDMConfiguration3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3.html)
[ISwDMConfiguration3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3_members.html)
[ISwDMConfiguration::GetBodiesCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.html)
[ISwDMConfiguration::GetBody Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP2
