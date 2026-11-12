---
title: "SetSolidBodyMaterial Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SetSolidBodyMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetSolidBodyMaterial.html"
---

# SetSolidBodyMaterial Method (ICWSolidBody)

Sets the material to the solid body for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSolidBodyMaterial( _
   ByVal RetVal As CWMaterial _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim RetVal As CWMaterial
Dim value As System.Integer

value = instance.SetSolidBodyMaterial(RetVal)
```

### C#

```csharp
System.int SetSolidBodyMaterial(
   CWMaterial RetVal
)
```

### C++/CLI

```cpp
System.int SetSolidBodyMaterial(
   CWMaterial^ RetVal
)
```

### Parameters

- `RetVal`: [Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

### Return Value

Error or warning as defined in [swsMaterialErrorWarning_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialErrorWarning_e.html)

## VBA Syntax

See [CWSolidBody::SetSolidBodyMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~SetSolidBodyMaterial.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWSolidBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetDefaultMaterial.html)
[ICWSolidBody::GetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetSolidBodyMaterial.html)
[ICWSolidBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial.html)
[ICWSolidBody::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
