---
title: "IsReference Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IsReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsReference.html"
---

# IsReference Method (IDimension)

Gets whether the dimension is a reference dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsReference() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Boolean

value = instance.IsReference()
```

### C#

```csharp
System.bool IsReference()
```

### C++/CLI

```cpp
System.bool IsReference();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the dimension is a reference dimension, false if not

## VBA Syntax

See [Dimension::IsReference](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IsReference.html).

## Examples

[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)

## Remarks

This method returns false for dimensions in 3D sketches.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDrawingDoc::InsertRefDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)
[IDisplayDimension::IsReferenceDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsReferenceDim.html)
