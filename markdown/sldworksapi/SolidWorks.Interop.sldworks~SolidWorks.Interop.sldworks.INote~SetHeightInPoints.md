---
title: "SetHeightInPoints Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetHeightInPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeightInPoints.html"
---

# SetHeightInPoints Method (INote)

Sets the height of this note in points (for example, 8, 10, 12, and so on).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetHeightInPoints( _
   ByVal HeightIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim HeightIn As System.Integer

instance.SetHeightInPoints(HeightIn)
```

### C#

```csharp
void SetHeightInPoints(
   System.int HeightIn
)
```

### C++/CLI

```cpp
void SetHeightInPoints(
   System.int HeightIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HeightIn`: Height for this note in points

## VBA Syntax

See [Note::SetHeightInPoints](ms-its:sldworksapivb6.chm::/sldworks~Note~SetHeightInPoints.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.html)
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.html)
[INote::GetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightInPoints.html)
[INote::SetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeight.html)
