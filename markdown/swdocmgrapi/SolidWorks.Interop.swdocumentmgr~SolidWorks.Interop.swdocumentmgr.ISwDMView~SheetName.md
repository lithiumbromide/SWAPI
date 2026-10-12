---
title: "SheetName Property (ISwDMView)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView"
member: "SheetName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~SheetName.html"
---

# SheetName Property (ISwDMView)

Gets or sets the name of the sheet for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView
Dim value As System.String

instance.SheetName = value

value = instance.SheetName
```

### C#

```csharp
System.string SheetName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SheetName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of sheet

## VBA Syntax

See [SwDMView::SheetName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView~SheetName.html).

## See Also

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html)
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
