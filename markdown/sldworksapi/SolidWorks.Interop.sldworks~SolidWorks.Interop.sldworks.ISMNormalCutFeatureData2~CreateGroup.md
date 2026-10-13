---
title: "CreateGroup Method (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "CreateGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CreateGroup.html"
---

# CreateGroup Method (ISMNormalCutFeatureData2)

Creates a group of connected faces to cut.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateGroup( _
   ByRef ErrCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim ErrCode As System.Integer
Dim value As System.Object

value = instance.CreateGroup(ErrCode)
```

### C#

```csharp
System.object CreateGroup(
   out System.int ErrCode
)
```

### C++/CLI

```cpp
System.Object^ CreateGroup(
   [Out] System.int ErrCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ErrCode`: Error code as defined in [swNormalCutErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutErrors_e.html)

### Return Value

[ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.html)

## VBA Syntax

See [SMNormalCutFeatureData2::CreateGroup](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~CreateGroup.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
