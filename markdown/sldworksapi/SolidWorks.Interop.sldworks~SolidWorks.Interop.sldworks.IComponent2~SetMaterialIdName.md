---
title: "SetMaterialIdName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetMaterialIdName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialIdName.html"
---

# SetMaterialIdName Method (IComponent2)

Sets the material name for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialIdName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

- `Name`: Material name

### Return Value

True if the material name was set, false if not

## VBA Syntax

See [Component2::SetMaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetMaterialIdName.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialIdName.html)
[IComponent2::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialUserName.html)
[IComponent2::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
