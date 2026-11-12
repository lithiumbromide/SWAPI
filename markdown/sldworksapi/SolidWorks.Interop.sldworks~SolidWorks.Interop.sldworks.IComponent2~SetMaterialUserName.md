---
title: "SetMaterialUserName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialUserName.html"
---

# SetMaterialUserName Method (IComponent2)

Sets the material user name for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialUserName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

- `Name`: Material user name property

### Return Value

True if the material user name was set, false if not

## VBA Syntax

See [Component2::SetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetMaterialUserName.html).

## Remarks

This material name is visible to the user.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
