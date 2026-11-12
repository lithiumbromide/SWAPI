---
title: "IAccessSelections Method (ISimpleHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (ISimpleHoleFeatureData)

Obsolete. Superseded by [ISimpleHoleFeatureData2::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IAccessSelections.html).

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
Dim instance As ISimpleHoleFeatureData
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

See [SimpleHoleFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData~IAccessSelections.html).

## See Also

[ISimpleHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData.html)
[ISimpleHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData_members.html)
