---
title: "Visible Property (IStatusBarPane)"
project: "SOLIDWORKS API Help"
interface: "IStatusBarPane"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane~Visible.html"
---

# Visible Property (IStatusBarPane)

Shows or hides this pane.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStatusBarPane
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True shows the pane, false hides it

## VBA Syntax

See [StatusBarPane::Visible](ms-its:sldworksapivb6.chm::/sldworks~StatusBarPane~Visible.html).

## See Also

[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.html)
[IStatusBarPane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
