---
title: "ShellOffsetOption Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellOffsetOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellOffsetOption.html"
---

# ShellOffsetOption Property (ICWShell)

Gets or sets the shell offset option.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShellOffsetOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Integer

instance.ShellOffsetOption = value

value = instance.ShellOffsetOption
```

### C#

```csharp
System.int ShellOffsetOption {get; set;}
```

### C++/CLI

```cpp
property System.int ShellOffsetOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Shell offset option as defined by [swsShellOffsetOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellOffsetOption_e.html)

## VBA Syntax

See [CWShell::ShellOffsetOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellOffsetOption.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::ShellOffsetValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellOffsetValue.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
