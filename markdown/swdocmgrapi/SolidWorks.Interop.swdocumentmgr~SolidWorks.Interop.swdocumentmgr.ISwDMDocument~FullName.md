---
title: "FullName Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "FullName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~FullName.html"
---

# FullName Property (ISwDMDocument)

Gets the full path and filename of this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FullName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.String

value = instance.FullName
```

### C#

```csharp
System.string FullName {get;}
```

### C++/CLI

```cpp
property System.String^ FullName {
   System.String^ get();
}
```

### Property Value

Full path and filename of this document

## VBA Syntax

See [SwDMDocument::FullName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~FullName.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMDocument::Title Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
