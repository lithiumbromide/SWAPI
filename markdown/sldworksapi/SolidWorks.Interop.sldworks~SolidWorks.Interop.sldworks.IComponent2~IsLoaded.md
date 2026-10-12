---
title: "IsLoaded Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsLoaded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsLoaded.html"
---

# IsLoaded Method (IComponent2)

Gets whether a component is loaded.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLoaded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsLoaded()
```

### C#

```csharp
System.bool IsLoaded()
```

### C++/CLI

```cpp
System.bool IsLoaded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the component is loaded, false if not

## VBA Syntax

See [Component2::IsLoaded](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsLoaded.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2009 SP3, Revision Number 17.3
