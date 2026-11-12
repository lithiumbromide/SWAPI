---
title: "SetMaterialUserName Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "SetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~SetMaterialUserName.html"
---

# SetMaterialUserName Method (IBody)

Obsolete. Superseded by [IBody2::SetMaterialUserName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~SetMaterialUserName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialUserName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialUserName(Name)
```

### C#

```csharp
System.bool SetMaterialUserName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialUserName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [Body::SetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Body~SetMaterialUserName.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
