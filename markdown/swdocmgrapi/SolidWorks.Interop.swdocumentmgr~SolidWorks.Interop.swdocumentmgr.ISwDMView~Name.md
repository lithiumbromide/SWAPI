---
title: "Name Property (ISwDMView)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView"
member: "Name"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~Name.html"
---

# Name Property (ISwDMView)

Gets or sets the name of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of this drawing view

## VBA Syntax

See [SwDMView::Name](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView~Name.html).

## Examples

See the [ISwDMView](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html) examples.

## See Also

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html)
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
