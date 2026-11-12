---
title: "AddLightToScene Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddLightToScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightToScene.html"
---

# AddLightToScene Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddLightToScene](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddLightToScene.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLightToScene( _
   ByVal LpszNewValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim LpszNewValue As System.String
Dim value As System.Integer

value = instance.AddLightToScene(LpszNewValue)
```

### C#

```csharp
System.int AddLightToScene(
   System.string LpszNewValue
)
```

### C++/CLI

```cpp
System.int AddLightToScene(
   System.String^ LpszNewValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpszNewValue`:

## VBA Syntax

See [ModelDoc::AddLightToScene](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddLightToScene.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
