---
title: "ShellFace Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "ShellFace"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ShellFace.html"
---

# ShellFace Property (ICWFatigueStudyOptions)

Gets or sets the shell face on which fatigue analysis is performed.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShellFace As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

instance.ShellFace = value

value = instance.ShellFace
```

### C#

```csharp
System.int ShellFace {get; set;}
```

### C++/CLI

```cpp
property System.int ShellFace {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

[swsShellFace_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellFace_e.html).swsShellFace_Top or swsShellFace_e.swsShellFace_Bottom

## VBA Syntax

See [CWFatigueStudyOptions::ShellFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~ShellFace.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
