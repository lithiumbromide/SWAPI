---
title: "SetLightSourceName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetLightSourceName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetLightSourceName.html"
---

# SetLightSourceName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetLightSourceName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetLightSourceName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLightSourceName( _
   ByVal ID As System.Integer, _
   ByVal NewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim NewName As System.String
Dim value As System.Boolean

value = instance.SetLightSourceName(ID, NewName)
```

### C#

```csharp
System.bool SetLightSourceName(
   System.int ID,
   System.string NewName
)
```

### C++/CLI

```cpp
System.bool SetLightSourceName(
   System.int ID,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:
- `NewName`:

## VBA Syntax

See [ModelDoc::SetLightSourceName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetLightSourceName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
