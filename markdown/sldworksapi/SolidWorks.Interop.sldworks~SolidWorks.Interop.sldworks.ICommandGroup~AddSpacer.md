---
title: "AddSpacer Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "AddSpacer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer.html"
---

# AddSpacer Method (ICommandGroup)

Obsolete. Superseded by [ICommandGroup::AddSpacer2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~AddSpacer2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpacer( _
   ByVal Position As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Position As System.Integer
Dim value As System.Integer

value = instance.AddSpacer(Position)
```

### C#

```csharp
System.int AddSpacer(
   System.int Position
)
```

### C++/CLI

```cpp
System.int AddSpacer(
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`:

## VBA Syntax

See [CommandGroup::AddSpacer](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~AddSpacer.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
