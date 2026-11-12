---
title: "ResultFolderPath Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "ResultFolderPath"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResultFolderPath.html"
---

# ResultFolderPath Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResultFolderPath2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResultFolderPath2.html) and [ICWDynamicStudyOptions::SetResultFolderPath2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResultFolderPath2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ResultFolderPath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
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

Path to the results folder

## VBA Syntax

See [CWDynamicStudyOptions::ResultFolderPath](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~ResultFolderPath.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
