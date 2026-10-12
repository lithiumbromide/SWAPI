---
title: "Select2 Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~Select2.html"
---

# Select2 Method (ISketchRegion)

Selects the sketch region and marks it.

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
Dim instance As ISketchRegion
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

- `Append`: True to append this selection to the selection list, false to replace the selection list with this selection
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the sketch region is selected, false if not

## VBA Syntax

See [SketchRegion::Select2](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~Select2.html).

## Examples

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
[ISketchRegion::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~DeSelect.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
