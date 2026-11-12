---
title: "GetSequenceNumberIncrement Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetSequenceNumberIncrement"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetSequenceNumberIncrement.html"
---

# GetSequenceNumberIncrement Method (IFamilyTableFeature)

Gets the number with which to increment the family table items.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSequenceNumberIncrement() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.Integer

value = instance.GetSequenceNumberIncrement()
```

### C#

```csharp
System.int GetSequenceNumberIncrement()
```

### C++/CLI

```cpp
System.int GetSequenceNumberIncrement();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Item increment number

## VBA Syntax

See [FamilyTableFeature::GetSequenceNumberIncrement](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetSequenceNumberIncrement.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
