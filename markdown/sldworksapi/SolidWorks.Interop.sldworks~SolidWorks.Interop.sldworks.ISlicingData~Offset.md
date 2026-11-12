---
title: "Offset Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "Offset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~Offset.html"
---

# Offset Property (ISlicingData)

Gets or sets the linear or radial spacing between slicing planes.

## Syntax

### Visual Basic (Declaration)

```vb
Property Offset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Double

instance.Offset = value

value = instance.Offset
```

### C#

```csharp
System.double Offset {get; set;}
```

### C++/CLI

```cpp
property System.double Offset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Linear spacing (meters) or radial spacing (radians) between slicing planes (see **Remarks**)

## VBA Syntax

See [SlicingData::Offset](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~Offset.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## Remarks

If [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.html) specifies:

- a planar entity, then this property specifies linear spacing between slices.
- a linear entity and a point entity, then this property specifies radial spacing between slices.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
