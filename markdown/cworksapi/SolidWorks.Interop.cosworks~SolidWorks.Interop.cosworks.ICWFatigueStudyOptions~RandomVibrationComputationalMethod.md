---
title: "RandomVibrationComputationalMethod Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "RandomVibrationComputationalMethod"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~RandomVibrationComputationalMethod.html"
---

# RandomVibrationComputationalMethod Property (ICWFatigueStudyOptions)

Gets or sets the random vibration computational method.

## Syntax

### Visual Basic (Declaration)

```vb
Property RandomVibrationComputationalMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

instance.RandomVibrationComputationalMethod = value

value = instance.RandomVibrationComputationalMethod
```

### C#

```csharp
System.int RandomVibrationComputationalMethod {get; set;}
```

### C++/CLI

```cpp
property System.int RandomVibrationComputationalMethod {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Random vibration computational method as defined in [swsFatigueRandomVibrationComputationalMethod_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueRandomVibrationComputationalMethod_e.html)

## VBA Syntax

See [CWFatigueStudyOptions::RandomVibrationComputationalMethod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~RandomVibrationComputationalMethod.html).

## Examples

[Create Fatigue Study for Dynamic Random Vibration Study (VBA)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VB.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (VB.NET)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_VBNET.htm)
[Create Fatigue Study for Dynamic Random Vibration Study (C#)](Create_Fatigue_Study_for_Dynamic_Random_Vibration_Study_Example_CSharp.htm)

## Remarks

This property is valid only for random vibration fatigue studies in SOLIDWORKS Simulation Premium.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForRandomVibration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForRandomVibration.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
