---
title: "IsReferenceDim Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IsReferenceDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsReferenceDim.html"
---

# IsReferenceDim Method (IDisplayDimension)

Gets whether this display dimension is a reference dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsReferenceDim() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.IsReferenceDim()
```

### C#

```csharp
System.bool IsReferenceDim()
```

### C++/CLI

```cpp
System.bool IsReferenceDim();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension is a reference dimension, false if not

## VBA Syntax

See [DisplayDimension::IsReferenceDim](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IsReferenceDim.html).

## Examples

[Add Reference Dimension (C#)](Add_Reference_Dimension_Example_CSharp.htm)
[Add Reference Dimension (VB.NET)](Add_Reference_Dimension_Example_VBNET.htm)
[Add Reference Dimension (VBA)](Add_Reference_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDimension::IsReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsReference.html)
[IDrawingDoc::InsertRefDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
