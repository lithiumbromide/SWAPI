---
title: "GetActiveSheetName Method (ISwDMDocument4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument4"
member: "GetActiveSheetName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html"
---

# GetActiveSheetName Method (ISwDMDocument4)

Gets the name of the active sheet in a SOLIDWORKS drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveSheetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument4
Dim value As System.String

value = instance.GetActiveSheetName()
```

### C#

```csharp
System.string GetActiveSheetName()
```

### C++/CLI

```cpp
System.String^ GetActiveSheetName();
```

### Return Value

Name of the active sheet

## VBA Syntax

See [SwDMDocument4::GetActiveSheetName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument4~GetActiveSheetName.html).

## Remarks

This method supports SOLIDWORKS drawing documents only. A -1 or NULL is returned for all other types of SOLIDWORKS documents.

## See Also

[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.html)
[ISwDMDocument4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4_members.html)
[ISwDMDocument4::GetSheetCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.html)
[ISwDMDocument6::GetSheetNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html)
[ISwDMDocument13::GetSheetFormatPath Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)
[ISwDMDocument13::GetSheetProperties Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
