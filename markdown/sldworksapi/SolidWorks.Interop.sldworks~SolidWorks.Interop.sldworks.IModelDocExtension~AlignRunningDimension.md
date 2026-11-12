---
title: "AlignRunningDimension Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AlignRunningDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AlignRunningDimension.html"
---

# AlignRunningDimension Method (IModelDocExtension)

Aligns the extension lines of all angular dimensions to be the same distance from the center as the baseline dimension (0⁰) in the set of angular running dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AlignRunningDimension()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.AlignRunningDimension()
```

### C#

```csharp
void AlignRunningDimension()
```

### C++/CLI

```cpp
void AlignRunningDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::AlignRunningDimension](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AlignRunningDimension.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ReJogRunningDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReJogRunningDimension.html)
[IModelDocExtension::AddAngularRunningDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddAngularRunningDim.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
