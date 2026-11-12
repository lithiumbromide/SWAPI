---
title: "ActivateConfiguration Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ActivateConfiguration"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ActivateConfiguration.html"
---

# ActivateConfiguration Method (ICWStudy)

Activates the configuration of this study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ActivateConfiguration()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy

instance.ActivateConfiguration()
```

### C#

```csharp
void ActivateConfiguration()
```

### C++/CLI

```cpp
void ActivateConfiguration();
```

## VBA Syntax

See [CWStudy::ActivateConfiguration](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ActivateConfiguration.html).

## Examples

[Create Trend Tracker (VBA)](Create_Trend_Tracker_Example_VB.htm)
[Create Trend Tracker (VB.NET)](Create_Trend_Tracker_Example_VBNET.htm)
[Create Trend Tracker (C#)](Create_Trend_Tracker_Example_CSharp.htm)

## Remarks

If the model has studies that use different configurations, you must set the active study with [ICWStudyManager::ActiveStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ActiveStudy.html) after calling this method.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ConfigurationName Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ConfigurationName.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
