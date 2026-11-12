---
title: "ResetPresetDrawingParameters Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ResetPresetDrawingParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResetPresetDrawingParameters.html"
---

# ResetPresetDrawingParameters Method (ISldWorks)

Resets SOLIDWORKS back to its default behavior after calling [ISldWorks::PresetNewDrawingParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~PresetNewDrawingParameters.html) (i.e., display Sheet Format/Size dialog when opening a new drawing document).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResetPresetDrawingParameters()
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks

instance.ResetPresetDrawingParameters()
```

### C#

```csharp
void ResetPresetDrawingParameters()
```

### C++/CLI

```cpp
void ResetPresetDrawingParameters();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SldWorks::ResetPresetDrawingParameters](ms-its:sldworksapivb6.chm::/Sldworks~Sldworks~ResetPresetDrawingParameters.html).

## Examples

[Preset and Reset Template and Sheet Parameters for New Drawing Documents (VBA)](Preset_and_Reset_Template_and_Sheet_Parameters_for_New_Drawing_Documents_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
