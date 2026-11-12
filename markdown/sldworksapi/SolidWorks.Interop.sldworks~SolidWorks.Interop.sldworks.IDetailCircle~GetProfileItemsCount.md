---
title: "GetProfileItemsCount Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetProfileItemsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItemsCount.html"
---

# GetProfileItemsCount Method (IDetailCircle)

Gets the number of sketch segments that make up this detail circle profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileItemsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Integer

value = instance.GetProfileItemsCount()
```

### C#

```csharp
System.int GetProfileItemsCount()
```

### C++/CLI

```cpp
System.int GetProfileItemsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments that make up this detail circle profile

## VBA Syntax

See [DetailCircle::GetProfileItemsCount](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetProfileItemsCount.html).

## Remarks

Call this method before calling [IDetailCircle::IGetProfileItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~IGetProfileItems.html) to determine the size of the array.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
