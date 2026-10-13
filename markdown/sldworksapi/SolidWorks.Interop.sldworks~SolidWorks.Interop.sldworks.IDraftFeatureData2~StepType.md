---
title: "StepType Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "StepType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~StepType.html"
---

# StepType Property (IDraftFeatureData2)

Gets or sets the step type for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StepType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Short

instance.StepType = value

value = instance.StepType
```

### C#

```csharp
System.short StepType {get; set;}
```

### C++/CLI

```cpp
property System.short StepType {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Step type as defined in [swDraftStepType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftStepType_e.html)

## VBA Syntax

See [DraftFeatureData2::StepType](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~StepType.html).

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
