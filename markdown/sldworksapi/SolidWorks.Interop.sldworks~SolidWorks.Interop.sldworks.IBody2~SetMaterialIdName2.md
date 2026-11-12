---
title: "SetMaterialIdName2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetMaterialIdName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html"
---

# SetMaterialIdName2 Method (IBody2)

Sets the material name for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialIdName2( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialIdName2(Name)
```

### C#

```csharp
System.bool SetMaterialIdName2(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialIdName2(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Material name

### Return Value

True if the material name is set successfully, false if not

## VBA Syntax

See [Body2::SetMaterialIdName2](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetMaterialIdName2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
