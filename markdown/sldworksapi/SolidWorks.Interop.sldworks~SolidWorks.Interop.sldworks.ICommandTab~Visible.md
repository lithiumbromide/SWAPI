---
title: "Visible Property (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~Visible.html"
---

# Visible Property (ICommandTab)

Gets or sets whether to show or hide this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
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

## VBA Syntax

See [CommandTab::Visible](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~Visible.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
