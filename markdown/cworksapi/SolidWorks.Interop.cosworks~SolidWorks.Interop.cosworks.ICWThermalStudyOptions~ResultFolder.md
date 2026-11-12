---
title: "ResultFolder Property (ICWThermalStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWThermalStudyOptions"
member: "ResultFolder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions~ResultFolder.html"
---

# ResultFolder Property (ICWThermalStudyOptions)

Gets or sets the path to the folder for storing the study results.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWThermalStudyOptions
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

See [CWThermalStudyOptions::ResultFolder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWThermalStudyOptions~ResultFolder.html).

## See Also

[ICWThermalStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html)
[ICWThermalStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
