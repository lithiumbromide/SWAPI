---
title: "CreateMeasure Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateMeasure"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMeasure.html"
---

# CreateMeasure Method (IModelDocExtension)

Creates a measure tool.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMeasure() As Measure
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As Measure

value = instance.CreateMeasure()
```

### C#

```csharp
Measure CreateMeasure()
```

### C++/CLI

```cpp
Measure^ CreateMeasure();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Measure](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMeasure.html) tool

## VBA Syntax

See [ModelDocExtension::CreateMeasure](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateMeasure.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
