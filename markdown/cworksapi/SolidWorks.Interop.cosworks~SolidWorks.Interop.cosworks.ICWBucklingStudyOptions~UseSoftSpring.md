---
title: "UseSoftSpring Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "UseSoftSpring"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~UseSoftSpring.html"
---

# UseSoftSpring Property (ICWBucklingStudyOptions)

Obsolete. Superseded by [ICWBucklingStudyOptions::UseSoftSpring2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~UseSoftSpring2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

- 1 = Use soft spring to stabilize the model
- 0 = Do not use soft spring to stabilize the model

## VBA Syntax

See [CWBucklingStudyOptions::UseSoftSpring](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~UseSoftSpring.html).

## Remarks

Use this property carefully. If you set this property to 1 for checking purposes, then set more [buckling modes](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions~BucklingModes.html) and check them. Apply proper restraints for final results.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
