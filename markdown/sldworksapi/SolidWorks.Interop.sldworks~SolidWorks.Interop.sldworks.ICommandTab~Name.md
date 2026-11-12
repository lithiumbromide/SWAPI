---
title: "Name Property (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~Name.html"
---

# Name Property (ICommandTab)

Gets or sets the name of this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
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

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of this CommandManager tab

## VBA Syntax

See [CommandTab::Name](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~Name.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
