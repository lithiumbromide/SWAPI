---
title: "SetMaterialIdName Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetMaterialIdName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName.html"
---

# SetMaterialIdName Method (IBody2)

Obsolete. Superseded by [IBody2::SetMaterialIdName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~SetMaterialIdName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialIdName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialIdName(Name)
```

### C#

```csharp
System.bool SetMaterialIdName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialIdName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [Body2::SetMaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetMaterialIdName.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
