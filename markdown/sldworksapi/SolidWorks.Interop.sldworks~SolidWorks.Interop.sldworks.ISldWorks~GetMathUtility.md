---
title: "GetMathUtility Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMathUtility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMathUtility.html"
---

# GetMathUtility Method (ISldWorks)

Gets [IMathUtility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMathUtility() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetMathUtility()
```

### C#

```csharp
System.object GetMathUtility()
```

### C++/CLI

```cpp
System.Object^ GetMathUtility();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMathUtility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility.html) or null if the operation fails

## VBA Syntax

See [SldWorks::GetMathUtility](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMathUtility.html).

## Examples

[Align Assembly Component to Assembly Origin and Planes (VBA)](Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm)
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Rotate Assembly Component on Axis (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Zoom to Region (VBA)](Zoom_to_Region_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetMathUtility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMathUtility.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
