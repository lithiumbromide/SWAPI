---
title: "GetComponentCount Method (ISwDMDocument8)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument8"
member: "GetComponentCount"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetComponentCount.html"
---

# GetComponentCount Method (ISwDMDocument8)

Gets the number of components in a SOLIDWORKS assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument8
Dim value As System.Integer

value = instance.GetComponentCount()
```

### C#

```csharp
System.int GetComponentCount()
```

### C++/CLI

```cpp
System.int GetComponentCount();
```

### Return Value

Number of components in an assembly document

## VBA Syntax

See [SwDMDocument8::GetComponentCount](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument8~GetComponentCount.html).

## Remarks

This method supports SOLIDWORKS assembly documents only. A -1 is returned for all other types of SOLIDWORKS documents.

## See Also

[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.html)
[ISwDMDocument8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
