---
title: "IAccessSelections Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (ILocalLinearPatternFeatureData)

Obsolete. Superseded by [ILocalLinearPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~IAccessSelections2.html).

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
Dim instance As ILocalLinearPatternFeatureData
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

See [LocalLinearPatternFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~IAccessSelections.html).

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
