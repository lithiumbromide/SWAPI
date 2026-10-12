---
title: "SelectName Property (ISwDMComponent7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent7"
member: "SelectName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7~SelectName.html"
---

# SelectName Property (ISwDMComponent7)

Obsolete. Superseded by [ISwDMComponent11::SelectName2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~SelectName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SelectName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent7
Dim value As System.String

value = instance.SelectName
```

### C#

```csharp
System.string SelectName {get;}
```

### C++/CLI

```cpp
property System.String^ SelectName {
   System.String^ get();
}
```

### Property Value

Name to use during a selective open

## VBA Syntax

See [SwDMComponent7::SelectName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent7~SelectName.html).

## See Also

[ISwDMComponent7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7.html)
[ISwDMComponent7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7_members.html)
[ISwDMComponent7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7~Name2.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
