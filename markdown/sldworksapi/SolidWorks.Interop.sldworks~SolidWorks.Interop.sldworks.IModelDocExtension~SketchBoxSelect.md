---
title: "SketchBoxSelect Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SketchBoxSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchBoxSelect.html"
---

# SketchBoxSelect Method (IModelDocExtension)

Box selects all of the entities in a sketch within the specified coordinates of the selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchBoxSelect( _
   ByVal FirstPtX As System.Double, _
   ByVal FirstPtY As System.Double, _
   ByVal FirstPtZ As System.Double, _
   ByVal SecondPtX As System.Double, _
   ByVal SecondPtY As System.Double, _
   ByVal SecondPtZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FirstPtX As System.Double
Dim FirstPtY As System.Double
Dim FirstPtZ As System.Double
Dim SecondPtX As System.Double
Dim SecondPtY As System.Double
Dim SecondPtZ As System.Double
Dim value As System.Boolean

value = instance.SketchBoxSelect(FirstPtX, FirstPtY, FirstPtZ, SecondPtX, SecondPtY, SecondPtZ)
```

### C#

```csharp
System.bool SketchBoxSelect(
   System.double FirstPtX,
   System.double FirstPtY,
   System.double FirstPtZ,
   System.double SecondPtX,
   System.double SecondPtY,
   System.double SecondPtZ
)
```

### C++/CLI

```cpp
System.bool SketchBoxSelect(
   System.double FirstPtX,
   System.double FirstPtY,
   System.double FirstPtZ,
   System.double SecondPtX,
   System.double SecondPtY,
   System.double SecondPtZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstPtX`: x coordinate of the first corner of the box
- `FirstPtY`: y coordinate of the first corner of the box
- `FirstPtZ`: z coordinate of the first corner of the box
- `SecondPtX`: x coordinate of the opposite diagonal corner of the box
- `SecondPtY`: y coordinate of the opposite diagonal corner of the box
- `SecondPtZ`: z coordinate of the opposite diagonal corner of the box

### Return Value

True if the sketch entities lying in the specified coordinates are box-selected, false if not

## VBA Syntax

See [ModelDocExtension::SketchBoxSelect](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SketchBoxSelect.html).

## Examples

[Box Select a Sketch (VB.NET)](Box_Select_a_Sketch_Example_VBNET.htm)
[Box Select a Sketch (VBA)](Box_Select_a_Sketch_Example_VB.htm)
[Box Select a Sketch (C#)](Box_Select_a_Sketch_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
