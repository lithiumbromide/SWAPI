---
title: "GetEndCondition Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetEndCondition.html"
---

# GetEndCondition Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::GetEndCondition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndCondition( _
   ByVal Forward As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Integer

value = instance.GetEndCondition(Forward)
```

### C#

```csharp
System.int GetEndCondition(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.int GetEndCondition(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData::GetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetEndCondition.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
