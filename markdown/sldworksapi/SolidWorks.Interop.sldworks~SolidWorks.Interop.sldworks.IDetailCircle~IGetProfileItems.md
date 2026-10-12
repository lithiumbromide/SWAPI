---
title: "IGetProfileItems Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "IGetProfileItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetProfileItems.html"
---

# IGetProfileItems Method (IDetailCircle)

Gets the sketch segments that make up this detail circle profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProfileItems( _
   ByVal Count As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Count As System.Integer
Dim value As SketchSegment

value = instance.IGetProfileItems(Count)
```

### C#

```csharp
SketchSegment IGetProfileItems(
   System.int Count
)
```

### C++/CLI

```cpp
SketchSegment^ IGetProfileItems(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch segments that make up this detail circle profile

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) that make up this detail circle profile

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IDetailCircle::GetProfileItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~GetProfileItemsCount.html) before calling this method to determine the size of the array.

Do not modify the sketch segments returned by this method. This method only provides information about the profile geometry of the detail circle. To modify a detail circle, use [IDetailCircle::SetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~SetParameters.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number
