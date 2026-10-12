---
title: "ResultFolder Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "ResultFolder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ResultFolder.html"
---

# ResultFolder Property (ICWFatigueStudyOptions)

Gets or sets the folder for the results of the fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
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

Results folder path name

## VBA Syntax

See [CWFatigueStudyOptions::ResultFolder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~ResultFolder.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
