---
title: "GetLastUpdateStamp Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetLastUpdateStamp"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetLastUpdateStamp.html"
---

# GetLastUpdateStamp Method (ISwDMDocument)

Gets the date on which this document was last updated.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastUpdateStamp() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Integer

value = instance.GetLastUpdateStamp()
```

### C#

```csharp
System.int GetLastUpdateStamp()
```

### C++/CLI

```cpp
System.int GetLastUpdateStamp();
```

### Return Value

Date document last updated

## VBA Syntax

See [SwDMDocument::GetLastUpdateStamp](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetLastUpdateStamp.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

The update stamp is an integer representing a time stamp. The update stamp in a SOLIDWORKS document is incremented when:

- the state of the model changes (for example, you suppress or unsuppress a feature in a part or an assembly)
- the geometry changes (for example, any action that requires a rebuild)

This time stamp is not incremented for such operations as color changes, feature or configuration name changes, and so on.

This method returns 0 for non-SOLIDWORKS documents.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::CreationDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.html)
[ISwDMDocument::LastSavedBy Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.html)
[ISwDMDocument::LastSavedDate Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
