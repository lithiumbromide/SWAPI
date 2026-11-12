---
title: "BucklingStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "BucklingStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~BucklingStudyOptions.html"
---

# BucklingStudyOptions Property (ICWStudy)

Gets the options for this buckling study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BucklingStudyOptions As CWBucklingStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWBucklingStudyOptions

value = instance.BucklingStudyOptions
```

### C#

```csharp
CWBucklingStudyOptions BucklingStudyOptions {get;}
```

### C++/CLI

```cpp
property CWBucklingStudyOptions^ BucklingStudyOptions {
   CWBucklingStudyOptions^ get();
}
```

### Property Value

[Buckling study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html)

## VBA Syntax

See [CWStudy::BucklingStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~BucklingStudyOptions.html).

## Examples

[Create Buckling Study (VBA)](Create_Buckling_Study_Example_VB.htm)
[Create Buckling Study (VB.NET)](Create_Buckling_Study_Example_VBNET.htm)
[Create Buckling Study (C#)](Create_Buckling_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
