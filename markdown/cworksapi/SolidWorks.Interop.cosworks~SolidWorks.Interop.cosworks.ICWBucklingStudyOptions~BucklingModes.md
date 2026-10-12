---
title: "BucklingModes Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "BucklingModes"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~BucklingModes.html"
---

# BucklingModes Property (ICWBucklingStudyOptions)

Gets or sets the number of buckling modes.

## Syntax

### Visual Basic (Declaration)

```vb
Property BucklingModes As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
Dim value As System.Integer

instance.BucklingModes = value

value = instance.BucklingModes
```

### C#

```csharp
System.int BucklingModes {get; set;}
```

### C++/CLI

```cpp
property System.int BucklingModes {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of buckling modes

## VBA Syntax

See [CWBucklingStudyOptions::BucklingModes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~BucklingModes.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation 2008 API SP1.0
