---
title: "ResultFolderPath Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ResultFolderPath"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ResultFolderPath.html"
---

# ResultFolderPath Property (ICWNonLinearStudyOptions)

Gets or sets the path name of the folder that stores the results of this study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolderPath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.String

instance.ResultFolderPath = value

value = instance.ResultFolderPath
```

### C#

```csharp
System.string ResultFolderPath {get; set;}
```

### C++/CLI

```cpp
property System.String^ ResultFolderPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path name of the results folder

## VBA Syntax

See [CWNonLinearStudyOptions::ResultFolderPath](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ResultFolderPath.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

Make sure that the disk where the specified folder is located has adequate free disk space for the analysis results.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
