---
title: "ReverseDirection Property (ISlicingData)"
project: "SOLIDWORKS API Help"
interface: "ISlicingData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~ReverseDirection.html"
---

# ReverseDirection Property (ISlicingData)

Gets or sets whether to reverse the direction of slicing the model with respect to the initial reference plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISlicingData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of adding slices, false to not

## VBA Syntax

See [SlicingData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~SlicingData~ReverseDirection.html).

## Examples

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html) example.

## See Also

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.html)
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
