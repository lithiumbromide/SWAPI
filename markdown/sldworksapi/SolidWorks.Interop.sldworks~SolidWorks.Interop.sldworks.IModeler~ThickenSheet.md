---
title: "ThickenSheet Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ThickenSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ThickenSheet.html"
---

# ThickenSheet Method (IModeler)

Thickens a sheet body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ThickenSheet( _
   ByVal Sheet As Body2, _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Sheet As Body2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim value As Body2

value = instance.ThickenSheet(Sheet, Thickness, Direction)
```

### C#

```csharp
Body2 ThickenSheet(
   Body2 Sheet,
   System.double Thickness,
   System.int Direction
)
```

### C++/CLI

```cpp
Body2^ ThickenSheet(
   Body2^ Sheet,
   System.double Thickness,
   System.int Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet body that defines the profile for the temporary thickened [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Thickness`: Thickness of the temporary thickened body
- `Direction`: Direction in which to thicken the sheet body as defined in [swThickenDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThickenDirection_e.html)

### Return Value

Temporary thickened [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::ThickenSheet](ms-its:sldworksapivb6.chm::/Sldworks~Modeler~ThickenSheet.html).

## Examples

[Thicken Sheet Body (VBA)](Thicken_Sheet_Body_Example_VB.htm)

## Remarks

If you set Direction to swThickenDirection_Both, then the value set for Thickness is used in both directions.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
