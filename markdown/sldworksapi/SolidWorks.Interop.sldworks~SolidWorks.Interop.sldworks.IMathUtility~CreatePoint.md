---
title: "CreatePoint Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "CreatePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreatePoint.html"
---

# CreatePoint Method (IMathUtility)

Creates a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePoint( _
   ByVal ArrayDataIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim ArrayDataIn As System.Object
Dim value As System.Object

value = instance.CreatePoint(ArrayDataIn)
```

### C#

```csharp
System.object CreatePoint(
   System.object ArrayDataIn
)
```

### C++/CLI

```cpp
System.Object^ CreatePoint(
   System.Object^ ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArrayDataIn`: Array of doubles representing the coordinates (x,y,z) of the point

### Return Value

Newly created [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object or null if the operation fails

## VBA Syntax

See [MathUtility::CreatePoint](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~CreatePoint.html).

## Examples

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Zoom to Region (VBA)](Zoom_to_Region_Example_VB.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::ICreatePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreatePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
