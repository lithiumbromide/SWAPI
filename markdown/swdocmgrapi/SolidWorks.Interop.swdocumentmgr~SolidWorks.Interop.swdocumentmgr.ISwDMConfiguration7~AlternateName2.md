---
title: "AlternateName2 Property (ISwDMConfiguration7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration7"
member: "AlternateName2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~AlternateName2.html"
---

# AlternateName2 Property (ISwDMConfiguration7)

Gets or sets the user-specified name of the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlternateName2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration7
Dim value As System.String

instance.AlternateName2 = value

value = instance.AlternateName2
```

### C#

```csharp
System.string AlternateName2 {get; set;}
```

### C++/CLI

```cpp
property System.String^ AlternateName2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Alternate or user-specified name of the configuration

## VBA Syntax

See [SwDMConfiguration7::AlternateName2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration7~AlternateName2.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2005 and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

If you set [ISwDMConfiguration11::BOMPartNoSource](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.html) to anything other than [swDmBOMPartNumberSource](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmBOMPartNumberSource.html).swDmBOMPartNumber_UserSpecified, then this property is set to an empty string.

## See Also

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
