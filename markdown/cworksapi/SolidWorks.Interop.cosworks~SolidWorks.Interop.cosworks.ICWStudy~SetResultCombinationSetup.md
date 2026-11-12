---
title: "SetResultCombinationSetup Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "SetResultCombinationSetup"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetResultCombinationSetup.html"
---

# SetResultCombinationSetup Method (ICWStudy)

Sets the result combination setup for this Pressure Vessel Design study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResultCombinationSetup( _
   ByVal NOption As System.Integer, _
   ByVal NItems As System.Integer, _
   ByVal MultiplicationFactors As System.Object, _
   ByVal StudyNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim NOption As System.Integer
Dim NItems As System.Integer
Dim MultiplicationFactors As System.Object
Dim StudyNames As System.Object
Dim value As System.Integer

value = instance.SetResultCombinationSetup(NOption, NItems, MultiplicationFactors, StudyNames)
```

### C#

```csharp
System.int SetResultCombinationSetup(
   System.int NOption,
   System.int NItems,
   System.object MultiplicationFactors,
   System.object StudyNames
)
```

### C++/CLI

```cpp
System.int SetResultCombinationSetup(
   System.int NOption,
   System.int NItems,
   System.Object^ MultiplicationFactors,
   System.Object^ StudyNames
)
```

### Parameters

- `NOption`: Type of result combination as defined in [swsPVResultCombinationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPVResultCombinationType_e.html)
- `NItems`: Number of elements in the MultiplicationFactors and StudyNames arrays
- `MultiplicationFactors`: Array of multiplication factors; valid only if NOption = swsPVResultCombinationType_e.swsPVResultCombinationType_Linear
- `StudyNames`: Array of names of the static studies whose results you want to combine; if NOption = swsPVResultCombinationType_e.swsPVResultCombinationType_Linear, the elements of MultiplicationFactors are coefficients of the linear combination of the static study results

### Return Value

Error as defined in [swsPVResultCombinationError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPVResultCombinationError_e.html)

## VBA Syntax

See [CWStudy::SetResultCombinationSetup](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~SetResultCombinationSetup.html).

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
