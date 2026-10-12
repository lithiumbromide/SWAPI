---
title: "GetDefaultMaterial Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "GetDefaultMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetDefaultMaterial.html"
---

# GetDefaultMaterial Method (ICWSolidBody)

Gets the CAD material of the solid body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim value As CWMaterial

value = instance.GetDefaultMaterial()
```

### C#

```csharp
CWMaterial GetDefaultMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetDefaultMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

## VBA Syntax

See [CWSolidBody::GetDefaultMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~GetDefaultMaterial.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWSolidBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial.html)
[ICWSolidBody::SetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetSolidBodyMaterial.html)
[ICWSolidBody::GetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetSolidBodyMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
