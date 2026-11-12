---
title: "GetBodyScope Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "GetBodyScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetBodyScope.html"
---

# GetBodyScope Method (ICornerReliefFeatureData)

Gets the sheet metal body to which this corner relief feature is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyScope() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim value As System.Object

value = instance.GetBodyScope()
```

### C#

```csharp
System.object GetBodyScope()
```

### C++/CLI

```cpp
System.Object^ GetBodyScope();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## VBA Syntax

See [CornerReliefFeatureData::GetBodyScope](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~GetBodyScope.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
