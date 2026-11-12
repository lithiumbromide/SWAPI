---
title: "CreateDeformedBody2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreateDeformedBody2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody2.html"
---

# CreateDeformedBody2 Method (ICWResults)

Saves the deformed shape that results from running a [static](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) or [nonlinear](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDeformedBody2( _
   ByVal NCreateAs As System.Integer, _
   ByVal NAdvOption As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal SName As System.String, _
   ByVal SFolderName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NCreateAs As System.Integer
Dim NAdvOption As System.Integer
Dim NStepNumber As System.Integer
Dim SName As System.String
Dim SFolderName As System.String
Dim value As System.Integer

value = instance.CreateDeformedBody2(NCreateAs, NAdvOption, NStepNumber, SName, SFolderName)
```

### C#

```csharp
System.int CreateDeformedBody2(
   System.int NCreateAs,
   System.int NAdvOption,
   System.int NStepNumber,
   System.string SName,
   System.string SFolderName
)
```

### C++/CLI

```cpp
System.int CreateDeformedBody2(
   System.int NCreateAs,
   System.int NAdvOption,
   System.int NStepNumber,
   System.String^ SName,
   System.String^ SFolderName
)
```

### Parameters

- `NCreateAs`: Save option as defined in [swsCreateDeformedBodyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyOption_e.html)
- `NAdvOption`: Advanced save option as defined in [swsCreateDeformedBodyAdvancedOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyAdvancedOption_e.html)
- `NStepNumber`: 1 for a static study or a valid step number for a nonlinear study (see **Remarks**)
- `SName`: Name of the deformed shape to save
- `SFolderName`: Path name of folder in which to save SName

### Return Value

0 if successful, otherwise error code as defined in [swsCreateDeformedBodyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyError_e.html)

## VBA Syntax

See [CWResults::CreateDeformedBody2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreateDeformedBody2.html).

## Examples

[Create Body From Deformed Shape (VBA)](Create_Body_From_Deformed_Shape_Example_VB.htm)
[Create Body From Deformed Shape (VB.NET)](Create_Body_From_Deformed_Shape_Example_VBNET.htm)
[Create Body From Deformed Shape (C#)](Create_Body_From_Deformed_Shape_Example_CSharp.htm)

## Remarks

Deformed shapes of assembly documents are saved as multibody parts.

To populate NStepNumber for a nonlinear study, call [ICWResults::GetMaximumAvailableSteps](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMaximumAvailableSteps.html) to get the maximum number of steps in the nonlinear study.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedBodyFailedSewOption.html)
[ICWResults::SetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetDeformedBodyFailedSewOption.html)
[ICWResults::GetDeformedCoord Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedCoord.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
