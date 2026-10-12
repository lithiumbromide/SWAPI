---
title: "GetSolidBodyAt Method (ICWSolidComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidComponent"
member: "GetSolidBodyAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent~GetSolidBodyAt.html"
---

# GetSolidBodyAt Method (ICWSolidComponent)

Gets the solid body at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidBodyAt( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWSolidBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidComponent
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWSolidBody

value = instance.GetSolidBodyAt(NIndex, ErrorCode)
```

### C#

```csharp
CWSolidBody GetSolidBodyAt(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWSolidBody^ GetSolidBodyAt(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of solid body to get
- `ErrorCode`: 0 if successful, 1 if no solid body at NIndex

### Return Value

[Solid body](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidBody.html) or NULL if no solid body at NIndex

## VBA Syntax

See [CWSolidComponent::GetSolidBodyAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidComponent~GetSolidBodyAt.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## Remarks

Before calling this method, call [ICWSolidComponent::SolidBodyCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidComponent~SolidBodyCount.html) to get NIndex. Index starts at 0.

## See Also

[ICWSolidComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html)
[ICWSolidComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
