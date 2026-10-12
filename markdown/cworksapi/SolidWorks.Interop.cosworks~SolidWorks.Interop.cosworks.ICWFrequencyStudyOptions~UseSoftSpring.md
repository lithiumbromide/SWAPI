---
title: "UseSoftSpring Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "UseSoftSpring"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseSoftSpring.html"
---

# UseSoftSpring Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::UseSoftSpring2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseSoftSpring2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.UseSoftSpring = value

value = instance.UseSoftSpring
```

### C#

```csharp
System.int UseSoftSpring {get; set;}
```

### C++/CLI

```cpp
property System.int UseSoftSpring {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use soft springs
- 0 = Do not use soft springs

## VBA Syntax

See [CWFrequencyStudyOptions::UseSoftSpring](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~UseSoftSpring.html).

## Remarks

Rigid body modes are calculated in addition to the specified number of modes.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
