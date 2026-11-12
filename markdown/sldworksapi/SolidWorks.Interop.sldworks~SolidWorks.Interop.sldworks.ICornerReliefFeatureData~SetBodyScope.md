---
title: "SetBodyScope Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "SetBodyScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~SetBodyScope.html"
---

# SetBodyScope Method (ICornerReliefFeatureData)

Sets the sheet metal body to which this corner relief feature is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBodyScope( _
   ByVal SheetBody As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim SheetBody As System.Object
Dim value As System.Integer

value = instance.SetBodyScope(SheetBody)
```

### C#

```csharp
System.int SetBodyScope(
   System.object SheetBody
)
```

### C++/CLI

```cpp
System.int SetBodyScope(
   System.Object^ SheetBody
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SheetBody`: [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) sheet metal body

### Return Value

Error code as defined by [swCornerReliefError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

## VBA Syntax

See [CornerReliefFeatureData::SetBodyScope](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~SetBodyScope.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
