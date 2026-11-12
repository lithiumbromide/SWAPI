---
title: "Comment2 Property (ISwDMConfiguration7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration7"
member: "Comment2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Comment2.html"
---

# Comment2 Property (ISwDMConfiguration7)

Gets or sets the comment for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comment2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration7
Dim value As System.String

instance.Comment2 = value

value = instance.Comment2
```

### C#

```csharp
System.string Comment2 {get; set;}
```

### C++/CLI

```cpp
property System.String^ Comment2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Comment for the configuration

## VBA Syntax

See [SwDMConfiguration7::Comment2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration7~Comment2.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2005 and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
