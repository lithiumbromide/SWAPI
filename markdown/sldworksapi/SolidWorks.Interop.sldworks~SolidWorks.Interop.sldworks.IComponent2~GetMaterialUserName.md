---
title: "GetMaterialUserName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialUserName.html"
---

# GetMaterialUserName Method (IComponent2)

Gets the user-visible name of the material for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialUserName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetMaterialUserName()
```

### C#

```csharp
System.string GetMaterialUserName()
```

### C++/CLI

```cpp
System.String^ GetMaterialUserName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Material user name

## VBA Syntax

See [Component2::GetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetMaterialUserName.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialIdName.html)
[IComponent2::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialIdName.html)
[IComponent2::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialUserName.html)

## Availability

SollidWorks 2001Plus FCS, Revision Number 10.0
