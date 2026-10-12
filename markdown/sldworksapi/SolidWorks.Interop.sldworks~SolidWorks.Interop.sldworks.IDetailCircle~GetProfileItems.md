---
title: "GetProfileItems Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetProfileItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems.html"
---

# GetProfileItems Method (IDetailCircle)

Gets the sketch segments that make up this detail circle profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileItems() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Object

value = instance.GetProfileItems()
```

### C#

```csharp
System.object GetProfileItems()
```

### C++/CLI

```cpp
System.Object^ GetProfileItems();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) that make up this detail circle profile

## VBA Syntax

See [DetailCircle::GetProfileItems](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetProfileItems.html).

## Remarks

Do not modify the sketch segments returned by this method. This method only provides information about the profile geometry of the detail circle. To modify a detail circle, use [IDetailCircle::SetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~SetParameters.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::IGetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetProfileItems.html)
[IDetailCircle::GetProfileItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItemsCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number
