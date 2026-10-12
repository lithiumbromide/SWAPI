---
title: "IModifyDefinition Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IModifyDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition.html"
---

# IModifyDefinition Method (IFeature)

Obsolete. Superseded by [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IModifyDefinition( _
   ByVal Data As System.Object, _
   ByVal TopDoc As ModelDoc, _
   ByVal Component As Component _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Data As System.Object
Dim TopDoc As ModelDoc
Dim Component As Component
Dim value As System.Boolean

value = instance.IModifyDefinition(Data, TopDoc, Component)
```

### C#

```csharp
System.bool IModifyDefinition(
   System.object Data,
   ModelDoc TopDoc,
   Component Component
)
```

### C++/CLI

```cpp
System.bool IModifyDefinition(
   System.Object^ Data,
   ModelDoc^ TopDoc,
   Component^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Data`:
- `TopDoc`:
- `Component`:

## VBA Syntax

See [Feature::IModifyDefinition](ms-its:sldworksapivb6.chm::/sldworks~Feature~IModifyDefinition.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
