---
title: "LockLightToModel Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "LockLightToModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LockLightToModel.html"
---

# LockLightToModel Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::LockLightToModel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LockLightToModel.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function LockLightToModel( _
   ByVal LightId As System.Integer, _
   ByVal Fix As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim LightId As System.Integer
Dim Fix As System.Boolean
Dim value As System.Boolean

value = instance.LockLightToModel(LightId, Fix)
```

### C#

```csharp
System.bool LockLightToModel(
   System.int LightId,
   System.bool Fix
)
```

### C++/CLI

```cpp
System.bool LockLightToModel(
   System.int LightId,
   System.bool Fix
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightId`:
- `Fix`:

## VBA Syntax

See [ModelDoc::LockLightToModel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~LockLightToModel.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
