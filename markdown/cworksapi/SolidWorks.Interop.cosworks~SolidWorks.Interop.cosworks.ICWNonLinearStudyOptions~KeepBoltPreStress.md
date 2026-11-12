---
title: "KeepBoltPreStress Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "KeepBoltPreStress"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~KeepBoltPreStress.html"
---

# KeepBoltPreStress Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::KeepBoltPreStress2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~KeepBoltPreStress2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepBoltPreStress As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.KeepBoltPreStress = value

value = instance.KeepBoltPreStress
```

### C#

```csharp
System.int KeepBoltPreStress {get; set;}
```

### C++/CLI

```cpp
property System.int KeepBoltPreStress {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to keep bolt pre-stress, 0 to not

## VBA Syntax

See [CWNonLinearStudyOptions::KeepBoltPreStress](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~KeepBoltPreStress.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
