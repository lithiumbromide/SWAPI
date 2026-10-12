---
title: "IGetSketchRegions Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchRegions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchRegions.html"
---

# IGetSketchRegions Method (ISketch)

Gets the sketch regions in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchRegions( _
   ByVal Count As System.Integer _
) As SketchRegion
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchRegion

value = instance.IGetSketchRegions(Count)
```

### C#

```csharp
SketchRegion IGetSketchRegions(
   System.int Count
)
```

### C++/CLI

```cpp
SketchRegion^ IGetSketchRegions(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch regions

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketch::GetSketchRegionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchRegionCount.html) to get Count.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchRegions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegions.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
