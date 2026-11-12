---
title: "ResultFolder Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ResultFolder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ResultFolder.html"
---

# ResultFolder Property (ICWStaticStudyOptions)

Gets or sets the path name of the folder that stores the results of the study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

Path name of the results folder

## VBA Syntax

See [CWStaticStudyOptions::ResultFolder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ResultFolder.html).

## Remarks

Make sure that the adequate disk space exists where the specified folder is located for the analysis results.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
