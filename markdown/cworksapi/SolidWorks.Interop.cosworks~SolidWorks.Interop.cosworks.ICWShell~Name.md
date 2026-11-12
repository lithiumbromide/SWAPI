---
title: "Name Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "Name"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Name.html"
---

# Name Property (ICWShell)

Gets the name of the shell.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.String

value = instance.Name
```

### C#

```csharp
System.string Name {get;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
}
```

### Property Value

Shell name

## VBA Syntax

See [CWShell::Name](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~Name.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
