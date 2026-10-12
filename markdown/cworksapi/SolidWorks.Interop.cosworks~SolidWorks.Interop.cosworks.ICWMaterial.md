---
title: "ICWMaterial Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html"
---

# ICWMaterial Interface

Allows access to the material; certain materials are required for every study type.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
```

### C#

```csharp
public interface ICWMaterial
```

### C++/CLI

```cpp
public interface class ICWMaterial
```

## VBA Syntax

See [CWMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## Remarks

A number of material models are available for nonlinear studies. Material properties can be defined by selecting a material from a library or defining material properties manually.

## Accessors

[ICWBeamBody::GetBeamBodyMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody~GetBeamBodyMaterial.html)

[ICWBeamBody::GetDefaultMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody~GetDefaultMaterial.html)

[ICWCompositeShellOptions::GetPlyParameters](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetPlyParameters.html)

[ICWShell::GetDefaultMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~GetDefaultMaterial.html)

[ICWShell::GetShellMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~GetShellMaterial.html)

[ICWSolidBody::GetDefaultMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidBody~GetDefaultMaterial.html)

[ICWSolidBody::GetSolidBodyMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidBody~GetSolidBodyMaterial.html)

## See Also

[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
