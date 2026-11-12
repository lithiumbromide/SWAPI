---
title: "GetDepth Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetDepth.html"
---

# GetDepth Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::GetDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetDepth.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDepth( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetDepth(Forward)
```

### C#

```csharp
System.double GetDepth(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetDepth(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData::GetDepth](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetDepth.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
