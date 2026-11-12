---
title: "Text Property (IStatusBarPane)"
project: "SOLIDWORKS API Help"
interface: "IStatusBarPane"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane~Text.html"
---

# Text Property (IStatusBarPane)

Gets or sets the text for this pane.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStatusBarPane
Dim value As System.String

instance.Text = value

value = instance.Text
```

### C#

```csharp
System.string Text {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Status bar pane text

## VBA Syntax

See [StatusBarPane::Text](ms-its:sldworksapivb6.chm::/sldworks~StatusBarPane~Text.html).

## See Also

[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.html)
[IStatusBarPane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
