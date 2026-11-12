---
title: "IsLightLockedToModel Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IsLightLockedToModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IsLightLockedToModel.html"
---

# IsLightLockedToModel Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IsLightLockedToModel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsLightLockedToModel.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLightLockedToModel( _
   ByVal LightId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim LightId As System.Integer
Dim value As System.Boolean

value = instance.IsLightLockedToModel(LightId)
```

### C#

```csharp
System.bool IsLightLockedToModel(
   System.int LightId
)
```

### C++/CLI

```cpp
System.bool IsLightLockedToModel(
   System.int LightId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightId`:

## VBA Syntax

See [ModelDoc::IsLightLockedToModel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IsLightLockedToModel.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
