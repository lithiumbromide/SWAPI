---
title: "SetEndCondition Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetEndCondition.html"
---

# SetEndCondition Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndCondition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndCondition( _
   ByVal Forward As System.Boolean, _
   ByVal EndCondition As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim EndCondition As System.Integer

instance.SetEndCondition(Forward, EndCondition)
```

### C#

```csharp
void SetEndCondition(
   System.bool Forward,
   System.int EndCondition
)
```

### C++/CLI

```cpp
void SetEndCondition(
   System.bool Forward,
   System.int EndCondition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `EndCondition`:

## VBA Syntax

See [ExtrudeFeatureData::SetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetEndCondition.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
