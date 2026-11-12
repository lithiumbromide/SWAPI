---
title: "GetEDrawingsData Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetEDrawingsData"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetEDrawingsData.html"
---

# GetEDrawingsData Method (ISwDMDocument)

Obsolete as of SOLIDWORKS Document Manager API 2005 FCS. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEDrawingsData( _
   ByVal eModelFileName As System.String _
) As SwDmEDwgDataError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim eModelFileName As System.String
Dim value As SwDmEDwgDataError

value = instance.GetEDrawingsData(eModelFileName)
```

### C#

```csharp
SwDmEDwgDataError GetEDrawingsData(
   System.string eModelFileName
)
```

### C++/CLI

```cpp
SwDmEDwgDataError GetEDrawingsData(
   System.String^ eModelFileName
)
```

### Parameters

- `eModelFileName`: Filename of eDrawings file to which to save the data

### Return Value

Success or error code as defined by [SwDmEDwgDataError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmEDwgDataError.html)

## VBA Syntax

See [SwDMDocument::GetEDrawingsData](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetEDrawingsData.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
