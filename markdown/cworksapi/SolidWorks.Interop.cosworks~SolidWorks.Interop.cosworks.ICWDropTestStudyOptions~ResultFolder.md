---
title: "ResultFolder Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "ResultFolder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~ResultFolder.html"
---

# ResultFolder Property (ICWDropTestStudyOptions)

Gets or sets the path and name of the file for saving the results.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
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

Name of file to save results to

## VBA Syntax

See [CWDropTestStudyOptions::ResultFolder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestStudyOptions~ResultFolder.html).

## Examples

See the Examples in [ICWDropTestStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestStudyOptions.html).

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
