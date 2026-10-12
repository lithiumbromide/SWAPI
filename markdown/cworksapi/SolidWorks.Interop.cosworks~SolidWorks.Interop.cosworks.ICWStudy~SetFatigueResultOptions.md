---
title: "SetFatigueResultOptions Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "SetFatigueResultOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetFatigueResultOptions.html"
---

# SetFatigueResultOptions Method (ICWStudy)

Sets the result options for this fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFatigueResultOptions( _
   ByVal NFatigueCalculationsOption As System.Integer, _
   ByVal DispArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim NFatigueCalculationsOption As System.Integer
Dim DispArray As System.Object
Dim value As System.Integer

value = instance.SetFatigueResultOptions(NFatigueCalculationsOption, DispArray)
```

### C#

```csharp
System.int SetFatigueResultOptions(
   System.int NFatigueCalculationsOption,
   System.object DispArray
)
```

### C++/CLI

```cpp
System.int SetFatigueResultOptions(
   System.int NFatigueCalculationsOption,
   System.Object^ DispArray
)
```

### Parameters

- `NFatigueCalculationsOption`: Fatigue calculation option as defined in [swsFatigueCalculationsOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueCalculationsOption_e.html)
- `DispArray`: Array of vertices and reference points at which to plot damage matrix charts; only valid in variable amplitude fatigue studies

### Return Value

0 if successful, 1 if not

## VBA Syntax

See [CWStudy::SetFatigueResultOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~SetFatigueResultOptions.html).

## Examples

[Create Fatigue Study (VBA)](Create_Fatigue_Study_Example_VB.htm)
[Create Fatigue Study (VB.NET)](Create_Fatigue_Study_Example_VBNET.htm)
[Create Fatigue Study (C#)](Create_Fatigue_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::FatigueStudyOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~FatigueStudyOptions.html)
[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
