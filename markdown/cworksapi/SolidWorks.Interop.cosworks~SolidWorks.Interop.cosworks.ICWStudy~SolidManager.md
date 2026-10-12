---
title: "SolidManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "SolidManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SolidManager.html"
---

# SolidManager Property (ICWStudy)

Gets the solid manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SolidManager As CWSolidManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWSolidManager

value = instance.SolidManager
```

### C#

```csharp
CWSolidManager SolidManager {get;}
```

### C++/CLI

```cpp
property CWSolidManager^ SolidManager {
   CWSolidManager^ get();
}
```

### Property Value

[Solid manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidBody.html)

## VBA Syntax

See [CWStudy::SolidManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~SolidManager.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
