---
title: "FatigueStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "FatigueStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~FatigueStudyOptions.html"
---

# FatigueStudyOptions Property (ICWStudy)

Gets the options for this fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FatigueStudyOptions As CWFatigueStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWFatigueStudyOptions

value = instance.FatigueStudyOptions
```

### C#

```csharp
CWFatigueStudyOptions FatigueStudyOptions {get;}
```

### C++/CLI

```cpp
property CWFatigueStudyOptions^ FatigueStudyOptions {
   CWFatigueStudyOptions^ get();
}
```

### Property Value

[ICWFatigueStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueStudyOptions.html)

## VBA Syntax

See [CWStudy::FatigueStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~FatigueStudyOptions.html).

## Examples

[Create Fatigue Study (C#)](Create_Fatigue_Study_Example_CSharp.htm)
[Create Fatigue Study (VB.NET)](Create_Fatigue_Study_Example_VBNET.htm)
[Create Fatigue Study (VBA)](Create_Fatigue_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::SetFatigueResultOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetFatigueResultOptions.html)
[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
