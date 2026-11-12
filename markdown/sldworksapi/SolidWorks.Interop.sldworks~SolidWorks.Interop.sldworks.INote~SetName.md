---
title: "SetName Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetName.html"
---

# SetName Method (INote)

Sets the name for this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal NameIn As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim NameIn As System.String
Dim value As System.Boolean

value = instance.SetName(NameIn)
```

### C#

```csharp
System.bool SetName(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.bool SetName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Note name

### Return Value

True if the note name is changed successfully, false if not

## VBA Syntax

See [Note::SetName](ms-its:sldworksapivb6.chm::/sldworks~Note~SetName.html).

## Examples

[Set Note Name (VBA)](Set_Note_Name_Example.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetName.html)
