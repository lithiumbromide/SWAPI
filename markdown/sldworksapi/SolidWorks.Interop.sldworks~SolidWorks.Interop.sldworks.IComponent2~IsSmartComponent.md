---
title: "IsSmartComponent Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsSmartComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.html"
---

# IsSmartComponent Method (IComponent2)

Gets whether this component is a Smart Component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSmartComponent() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsSmartComponent()
```

### C#

```csharp
System.bool IsSmartComponent()
```

### C++/CLI

```cpp
System.bool IsSmartComponent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a Smart Component, false if not

## Examples

[Activate Smart Features in an Assembly (C#)](Activate_Smart_Features_in_an_Assembly_Example_CSharp.htm)
[Activate Smart Features in an Assembly (VB.NET)](Activate_Smart_Features_in_an_Assembly_Example_VBNET.htm)
[Activate Smart Features in an Assembly (VBA)](Activate_Smart_Features_in_an_Assembly_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.html)
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.html)
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html)
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.html)
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
