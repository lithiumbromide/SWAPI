---
title: "ActiveStudy Property (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "ActiveStudy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ActiveStudy.html"
---

# ActiveStudy Property (ICWStudyManager)

Gets or sets the index of the active study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveStudy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim value As System.Integer

instance.ActiveStudy = value

value = instance.ActiveStudy
```

### C#

```csharp
System.int ActiveStudy {get; set;}
```

### C++/CLI

```cpp
property System.int ActiveStudy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Index of the active study

## VBA Syntax

See [CWStudyManager::ActiveStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~ActiveStudy.html).

## Examples

[Calculate Edge Weld Results (C#)](Calculate_Edge_Weld_Results_Example_CSharp.htm)
[Calculate Edge Weld Results (VB.NET)](Calculate_Edge_Weld_Results_Example_VBNET.htm)
[Calculate Edge Weld Results (VBA)](Calculate_Edge_Weld_Results_Example_VB.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudy::ActivateConfiguration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ActivateConfiguration.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
