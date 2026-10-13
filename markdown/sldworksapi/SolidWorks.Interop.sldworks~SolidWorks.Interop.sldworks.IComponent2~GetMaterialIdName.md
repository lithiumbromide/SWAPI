---
title: "GetMaterialIdName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetMaterialIdName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialIdName.html"
---

# GetMaterialIdName Method (IComponent2)

Gets the material name for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialIdName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetMaterialIdName()
```

### C#

```csharp
System.string GetMaterialIdName()
```

### C++/CLI

```cpp
System.String^ GetMaterialIdName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Material name

## VBA Syntax

See [Component2::GetMaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetMaterialIdName.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialIdName.html)
[IComponent2::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialUserName.html)
[IComponent2::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
