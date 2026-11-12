---
title: "ConstantAmplitudeEventInteractionOption Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "ConstantAmplitudeEventInteractionOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ConstantAmplitudeEventInteractionOption.html"
---

# ConstantAmplitudeEventInteractionOption Property (ICWFatigueStudyOptions)

Gets or sets the interaction between constant amplitude fatigue events.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConstantAmplitudeEventInteractionOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

instance.ConstantAmplitudeEventInteractionOption = value

value = instance.ConstantAmplitudeEventInteractionOption
```

### C#

```csharp
System.int ConstantAmplitudeEventInteractionOption {get; set;}
```

### C++/CLI

```cpp
property System.int ConstantAmplitudeEventInteractionOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Interaction type as defined in [swsFatigueEventInteraction_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventInteraction_e.html) (see **Remarks**)

## VBA Syntax

See [CWFatigueStudyOptions::ConstantAmplitudeEventInteractionOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~ConstantAmplitudeEventInteractionOption.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

This property is valid only for constant amplitude fatigue studies.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::AddFatigueEventForConstantAmplitude Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~AddFatigueEventForConstantAmplitude.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
