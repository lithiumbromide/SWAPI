---
title: "ResultFolder Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "ResultFolder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ResultFolder.html"
---

# ResultFolder Property (ICWBucklingStudyOptions)

Gets or sets the path to the folder for storing the results of the study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
Dim value As System.String

instance.ResultFolder = value

value = instance.ResultFolder
```

### C#

```csharp
System.string ResultFolder {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResultFolder {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path for the results folder

## VBA Syntax

See [CWBucklingStudyOptions::ResultFolder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~ResultFolder.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

Make sure that the specified folder has adequate disk space for the analysis results.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
