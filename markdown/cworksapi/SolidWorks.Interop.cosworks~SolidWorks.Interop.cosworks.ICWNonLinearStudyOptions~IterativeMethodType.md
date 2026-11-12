---
title: "IterativeMethodType Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "IterativeMethodType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~IterativeMethodType.html"
---

# IterativeMethodType Property (ICWNonLinearStudyOptions)

Gets or sets the type of iterative solution method.

## Syntax

### Visual Basic (Declaration)

```vb
Property IterativeMethodType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.IterativeMethodType = value

value = instance.IterativeMethodType
```

### C#

```csharp
System.int IterativeMethodType {get; set;}
```

### C++/CLI

```cpp
property System.int IterativeMethodType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of iterative solution method as defined in [swsNonLinearOptionIterativeMethodType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNonLinearOptionIterativeMethodType_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::IterativeMethodType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~IterativeMethodType.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0
