---
title: "IAccessSelections Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "IAccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections.html"
---

# IAccessSelections Method (IMirrorPatternFeatureData)

Obsolete. Superseded by [IMirrorPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections2.html).

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
Dim instance As IMirrorPatternFeatureData
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

See [MirrorPatternFeatureData::IAccessSelections](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~IAccessSelections.html).

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
