---
title: "SetSequenceNumberIncrement Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "SetSequenceNumberIncrement"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetSequenceNumberIncrement.html"
---

# SetSequenceNumberIncrement Method (IFamilyTableFeature)

Sets the number with which to increment the family table items.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSequenceNumberIncrement( _
   ByVal Increment As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim Increment As System.Integer

instance.SetSequenceNumberIncrement(Increment)
```

### C#

```csharp
void SetSequenceNumberIncrement(
   System.int Increment
)
```

### C++/CLI

```cpp
void SetSequenceNumberIncrement(
   System.int Increment
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Increment`: Item increment number

## VBA Syntax

See [FamilyTableFeature::SetSequenceNumberIncrement](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~SetSequenceNumberIncrement.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
