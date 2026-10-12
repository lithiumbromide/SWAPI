---
title: "UseLargeDisplacement Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseLargeDisplacement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeDisplacement.html"
---

# UseLargeDisplacement Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::UseLargeDisplacement2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeDisplacement2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLargeDisplacement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.UseLargeDisplacement = value

value = instance.UseLargeDisplacement
```

### C#

```csharp
System.int UseLargeDisplacement {get; set;}
```

### C++/CLI

```cpp
property System.int UseLargeDisplacement {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use large displacement formulation
- 0 = Do not use large displacement formulation

## VBA Syntax

See [CWNonLinearStudyOptions::UseLargeDisplacement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseLargeDisplacement.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
