---
title: "GetMates Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetMates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMates.html"
---

# GetMates Method (IComponent2)

Gets the mates for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetMates()
```

### C#

```csharp
System.object GetMates()
```

### C++/CLI

```cpp
System.Object^ GetMates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of mates (either [IMate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2.html) objects or [IMateInPlace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateInPlace.html) objects)

## VBA Syntax

See [Component2::GetMates](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetMates.html).

## Examples

[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (VBA)](Get_Mates_Example_VB.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)

## Remarks

This method eliminates iterating through the list of mates, which can adversely affect performance when the list of mates is long.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
