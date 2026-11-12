---
title: "Active Property (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "Active"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~Active.html"
---

# Active Property (ICommandTab)

Gets or sets whether this CommandManager tab is active.

## Syntax

### Visual Basic (Declaration)

```vb
Property Active As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim value As System.Boolean

instance.Active = value

value = instance.Active
```

### C#

```csharp
System.bool Active {get; set;}
```

### C++/CLI

```cpp
property System.bool Active {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this CommandManager tab is active, false if not

## VBA Syntax

See [CommandTab::Active](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~Active.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
