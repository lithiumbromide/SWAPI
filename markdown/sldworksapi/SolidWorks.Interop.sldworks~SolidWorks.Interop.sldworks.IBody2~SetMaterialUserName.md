---
title: "SetMaterialUserName Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName.html"
---

# SetMaterialUserName Method (IBody2)

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
Dim instance As IBody2
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

See [Body2::SetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetMaterialUserName.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
