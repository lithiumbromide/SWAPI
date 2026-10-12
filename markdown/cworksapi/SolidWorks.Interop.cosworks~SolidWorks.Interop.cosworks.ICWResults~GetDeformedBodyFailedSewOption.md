---
title: "GetDeformedBodyFailedSewOption Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDeformedBodyFailedSewOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedBodyFailedSewOption.html"
---

# GetDeformedBodyFailedSewOption Method (ICWResults)

Gets the option to use when a deformed body fails to sew into a solid object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDeformedBodyFailedSewOption() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim value As System.Integer

value = instance.GetDeformedBodyFailedSewOption()
```

### C#

```csharp
System.int GetDeformedBodyFailedSewOption()
```

### C++/CLI

```cpp
System.int GetDeformedBodyFailedSewOption();
```

### Return Value

Option to use when a deformed body fails to sew into a solid object as defined in [swsCreateDeformedBodyFailedSewOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyFailedSewOption_e.html)

## VBA Syntax

See [CWResults::GetDeformedBodyFailedSewOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDeformedBodyFailedSewOption.html).

## Examples

[Create Body From Deformed Shape (VBA)](Create_Body_From_Deformed_Shape_Example_VB.htm)
[Create Body From Deformed Shape (VB.NET)](Create_Body_From_Deformed_Shape_Example_VBNET.htm)
[Create Body From Deformed Shape (C#)](Create_Body_From_Deformed_Shape_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetDeformedBodyFailedSewOption.html)
[ICWResults::CreateDeformedBody2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody2.html)
[ICWResults::GetDeformedCoord Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedCoord.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
