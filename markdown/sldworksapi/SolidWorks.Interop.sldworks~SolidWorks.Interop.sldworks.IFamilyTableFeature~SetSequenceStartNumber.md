---
title: "SetSequenceStartNumber Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "SetSequenceStartNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetSequenceStartNumber.html"
---

# SetSequenceStartNumber Method (IFamilyTableFeature)

Sets the item start number for this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSequenceStartNumber( _
   ByVal Start As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim Start As System.Integer

instance.SetSequenceStartNumber(Start)
```

### C#

```csharp
void SetSequenceStartNumber(
   System.int Start
)
```

### C++/CLI

```cpp
void SetSequenceStartNumber(
   System.int Start
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Start`: Item start number

## VBA Syntax

See [FamilyTableFeature::SetSequenceStartNumber](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~SetSequenceStartNumber.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
