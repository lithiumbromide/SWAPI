---
title: "IAccessSelections Method (IDomeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (IDomeFeatureData)

Obsolete. Superseded by [IDomeFeatureData2::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~IAccessSelections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAccessSelections( _
   ByVal TopDoc As ModelDoc, _
   ByVal Component As Component _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData
Dim TopDoc As ModelDoc
Dim Component As Component
Dim value As System.Boolean

value = instance.IAccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool IAccessSelections(
   ModelDoc TopDoc,
   Component Component
)
```

### C++/CLI

```cpp
System.bool IAccessSelections(
   ModelDoc^ TopDoc,
   Component^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`:
- `Component`:

## VBA Syntax

See [DomeFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData~IAccessSelections.html).

## See Also

[IDomeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData.html)
[IDomeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData_members.html)
