---
title: "AddCommandItem Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "AddCommandItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem.html"
---

# AddCommandItem Method (ICommandGroup)

Obsolete. Superseded by [ICommandGroup::AddComandItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~AddCommandItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCommandItem( _
   ByVal Name As System.String, _
   ByVal Position As System.Integer, _
   ByVal HintString As System.String, _
   ByVal ToolTip As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal EnableMethod As System.String, _
   ByVal UserID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Name As System.String
Dim Position As System.Integer
Dim HintString As System.String
Dim ToolTip As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim EnableMethod As System.String
Dim UserID As System.Integer
Dim value As System.Integer

value = instance.AddCommandItem(Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, UserID)
```

### C#

```csharp
System.int AddCommandItem(
   System.string Name,
   System.int Position,
   System.string HintString,
   System.string ToolTip,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string EnableMethod,
   System.int UserID
)
```

### C++/CLI

```cpp
System.int AddCommandItem(
   System.String^ Name,
   System.int Position,
   System.String^ HintString,
   System.String^ ToolTip,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ EnableMethod,
   System.int UserID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Position`:
- `HintString`:
- `ToolTip`:
- `ImageListIndex`:
- `CallbackFunction`:
- `EnableMethod`:
- `UserID`:

## VBA Syntax

See [CommandGroup::AddCommandItem](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~AddCommandItem.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
