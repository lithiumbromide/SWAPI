---
title: "ThermalResults Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "ThermalResults"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalResults.html"
---

# ThermalResults Property (ICWBucklingStudyOptions)

Gets or sets the source of temperatures in this buckling study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalResults As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
Dim value As System.Integer

instance.ThermalResults = value

value = instance.ThermalResults
```

### C#

```csharp
System.int ThermalResults {get; set;}
```

### C++/CLI

```cpp
property System.int ThermalResults {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Temperature source as defined by [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html)

## VBA Syntax

See [CWBucklingStudyOptions::ThermalResults](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~ThermalResults.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
