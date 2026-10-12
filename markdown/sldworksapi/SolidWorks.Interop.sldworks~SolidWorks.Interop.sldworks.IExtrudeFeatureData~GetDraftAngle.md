---
title: "GetDraftAngle Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetDraftAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetDraftAngle.html"
---

# GetDraftAngle Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::GetDraftAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetDraftAngle(Forward)
```

### C#

```csharp
System.double GetDraftAngle(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetDraftAngle(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [ExtrudeFeatureData::GetDraftAngle](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetDraftAngle.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
