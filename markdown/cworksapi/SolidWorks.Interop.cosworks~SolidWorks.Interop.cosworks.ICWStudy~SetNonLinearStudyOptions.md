---
title: "SetNonLinearStudyOptions Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "SetNonLinearStudyOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetNonLinearStudyOptions.html"
---

# SetNonLinearStudyOptions Method (ICWStudy)

Sets the nonlinear study options.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetNonLinearStudyOptions( _
   ByVal NonLinearOption As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim NonLinearOption As System.Object
Dim value As System.Integer

value = instance.SetNonLinearStudyOptions(NonLinearOption)
```

### C#

```csharp
System.int SetNonLinearStudyOptions(
   System.object NonLinearOption
)
```

### C++/CLI

```cpp
System.int SetNonLinearStudyOptions(
   System.Object^ NonLinearOption
)
```

### Parameters

- `NonLinearOption`: [Nonlinear study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html)

### Return Value

Error defined in [swsNonLinearStudyOptionsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearStudyOptionsError_e.html)

## VBA Syntax

See [CWStudy::SetNonLinearStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~SetNonLinearStudyOptions.html).

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::NonLinearStudyOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~NonLinearStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
