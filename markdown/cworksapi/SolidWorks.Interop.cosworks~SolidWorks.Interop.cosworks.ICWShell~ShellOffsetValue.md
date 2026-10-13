---
title: "ShellOffsetValue Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellOffsetValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellOffsetValue.html"
---

# ShellOffsetValue Property (ICWShell)

Gets or sets the shell offset value.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShellOffsetValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Double

instance.ShellOffsetValue = value

value = instance.ShellOffsetValue
```

### C#

```csharp
System.double ShellOffsetValue {get; set;}
```

### C++/CLI

```cpp
property System.double ShellOffsetValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

- -0.5 < offset value < 0

-or-

- 0 < offset value < 0.5 (see **Remarks**)

## VBA Syntax

See [CWShell::ShellOffsetValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellOffsetValue.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## Remarks

This property is valid only if [ICWShell::ShellOffsetOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~ShellOffsetOption.html) is set to swsShellOffsetOption_e.swsShellOffsetOption_SpecifyRatio.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
