---
title: "AccessSelections Method (IDomeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData~AccessSelections.html"
---

# AccessSelections Method (IDomeFeatureData)

Obsolete. Superseded by [IDomeFeatureData2::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~AccessSelections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   System.object TopDoc,
   System.object Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.Object^ TopDoc,
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`:
- `Component`:

## VBA Syntax

See [DomeFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData~AccessSelections.html).

## See Also

[IDomeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData.html)
[IDomeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData_members.html)
