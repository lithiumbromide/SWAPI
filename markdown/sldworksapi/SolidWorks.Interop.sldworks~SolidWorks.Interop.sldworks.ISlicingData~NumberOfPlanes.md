---
title: "NumberOfPlanes Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "NumberOfPlanes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~NumberOfPlanes.html"
---

# NumberOfPlanes Property (ISlicingData)

Gets or sets the number of slicing planes.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfPlanes As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Integer

instance.NumberOfPlanes = value

value = instance.NumberOfPlanes
```

### C#

```csharp
System.int NumberOfPlanes {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfPlanes {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of slicing planes

## VBA Syntax

See [SlicingData::NumberOfPlanes](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~NumberOfPlanes.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

The number of slicing planes cannot exceed 100.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)
[ISlicingData::PlaneReferences Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
