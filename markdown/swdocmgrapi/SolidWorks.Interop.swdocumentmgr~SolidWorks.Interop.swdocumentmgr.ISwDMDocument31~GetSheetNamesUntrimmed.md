---
title: "GetSheetNamesUntrimmed Method (ISwDMDocument31)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument31"
member: "GetSheetNamesUntrimmed"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetNamesUntrimmed.html"
---

# GetSheetNamesUntrimmed Method (ISwDMDocument31)

Gets the names of the sheets in the drawing document without removing leading or trailing whitespace characters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetNamesUntrimmed() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument31
Dim value As System.Object

value = instance.GetSheetNamesUntrimmed()
```

### C#

```csharp
System.object GetSheetNamesUntrimmed()
```

### C++/CLI

```cpp
System.Object^ GetSheetNamesUntrimmed();
```

### Return Value

Array of sheet name strings.

## VBA Syntax

See [SwDMDocument31::GetSheetNamesUntrimmed](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument31~GetSheetNamesUntrimmed.html).

## Remarks

This method only supports drawing documents saved in SOLIDWORKS 2005 SP02 and later. An empty array is returned if the names of the sheets are not found.

## See Also

[ISwDMDocument31 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31.html)
[ISwDMDocument31 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31_members.html)
[ISwDMDocument4::GetActiveSheetName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html)
[ISwDMDocument4::GetSheetCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.html)
[ISwDMDocument6::GetSheetNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.html)
[ISwDMDocument13::GetSheetFormatPath Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.html)
[GetSheetFormatPathUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetFormatPathUntrimmed.html)
[GetSheetProperties Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.html)
[GetSheetPropertiesUntrimmed Method (ISwDMDocument31)](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31~GetSheetPropertiesUntrimmed.html)

## Availability

SOLIDWORKS Document Manager API 2026 SP2
