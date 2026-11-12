---
title: "Select2 Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Select2.html"
---

# Select2 Method (ISketchContour)

Selects the sketch contour and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select2(Append, Data)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection to the selection list, false replaces the selection list with this selection
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if sketch contour selected, false if not

## VBA Syntax

See [SketchContour::Select2](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~Select2.html).

## Examples

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)
[Get Sketch Contours (VB.NET)](Get_Sketch_Contours_Example_VBNET.htm)
[Get Sketch Contours (C#)](Get_Sketch_Contours_Example_CSharp.htm)
[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm)

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~DeSelect.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
