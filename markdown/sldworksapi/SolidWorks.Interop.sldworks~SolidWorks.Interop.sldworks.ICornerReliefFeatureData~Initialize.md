---
title: "Initialize Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize.html"
---

# Initialize Method (ICornerReliefFeatureData)

Initializes this corner relief feature to have specified corner relief bend type.

## Syntax

### Visual Basic (Declaration)

```vb
Function Initialize( _
   ByVal CornerType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim CornerType As System.Integer
Dim value As System.Boolean

value = instance.Initialize(CornerType)
```

### C#

```csharp
System.bool Initialize(
   System.int CornerType
)
```

### C++/CLI

```cpp
System.bool Initialize(
   System.int CornerType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerType`: Corner relief bend type as defined by [swCornerReliefBendType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html)

### Return Value

True if the corner relief feature is initialized to the specified bend type, false if not

## VBA Syntax

See [CornerReliefFeatureData::Initialize](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~Initialize.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)
[ICornerReliefFeatureData::CornerType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerType.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
