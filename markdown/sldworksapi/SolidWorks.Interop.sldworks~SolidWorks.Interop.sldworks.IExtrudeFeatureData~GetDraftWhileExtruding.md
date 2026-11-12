---
title: "GetDraftWhileExtruding Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetDraftWhileExtruding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetDraftWhileExtruding.html"
---

# GetDraftWhileExtruding Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::GetDraftWhileExtruding](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftWhileExtruding( _
   ByVal Forward As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Boolean

value = instance.GetDraftWhileExtruding(Forward)
```

### C#

```csharp
System.bool GetDraftWhileExtruding(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.bool GetDraftWhileExtruding(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData::GetDraftWhileExtruding](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetDraftWhileExtruding.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
